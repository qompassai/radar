"""
A CLI tool used to start up a worker process for running jobs.
"""

import logging
import os
import sys

import rq.cli

from radar.sdk.utilities.logging import (
    attach_stdout_stream_handler,
    set_logging_level,
)

_REQUIRED_ENV = {
    "MLFLOW_S3_ENDPOINT_URL",
    "RADAR_API",
    "RADAR_WORKER_USERNAME",
    "RADAR_WORKER_PASSWORD",
}


def _setup_logging() -> None:
    attach_stdout_stream_handler(
        True if os.getenv("RADAR_RQ_WORKER_LOG_AS_JSON") else False,
    )
    set_logging_level(os.getenv("RADAR_RQ_WORKER_LOG_LEVEL", default="INFO"))


def main() -> int:
    _setup_logging()
    log = logging.getLogger("radar-worker")
    exit_status = 0

    # We know what functions will be executed through rq and what they
    # require, so we may as well check that before starting up the worker.
    # Better to error out as early as possible.
    unset_vars = _REQUIRED_ENV - os.environ.keys()
    if unset_vars:
        exit_status = 1
        log.fatal("Environment variables must be set: %s", ", ".join(unset_vars))
    else:
        # Disabling standalone mode means the worker function can return a
        # value to this script, exceptions will propagate to us, etc. (as
        # opposed to being intercepted and handled by click).  As a wrapper
        # that seems appropriate, although I don't think the worker function
        # is written to return anything, and we presently don't need to
        # specially handle any of the exceptions.
        rq.cli.worker(standalone_mode=False)

    return exit_status


if __name__ == "__main__":
    sys.exit(main())
