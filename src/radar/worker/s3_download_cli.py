import argparse
import logging
import logging.config
from typing import Union

import boto3
from radar.sdk.utilities.logging import (
    attach_stdout_stream_handler,
    configure_structlog,
)

from radar.worker.s3_download import s3_download


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="""
        Download file(s) from S3 to a directory.
        """
    )

    parser.add_argument(
        "-e",
        "--endpoint-url",
        help="""
        URL of an S3 endpoint to connect to
        """,
        required=True,
    )

    parser.add_argument(
        "-d",
        "--dest-dir",
        help="""
        The directory to download to.  Default: "%(default)s"
        """,
        default=".",
    )

    parser.add_argument(
        "-c",
        "--clear",
        help="""
        Clear the destination directory
        """,
        action="store_true",
    )

    parser.add_argument(
        "-p",
        "--preserve-paths",
        help="""
        Treat keys as paths and create that directory structure in the
        filesystem.  If not given, any key structure is flattened: directory
        structure is ignored, and filename path components (the last path
        component) are used to name the files created in the destination
        directory.
        """,
        action="store_true",
    )

    parser.add_argument(
        "-l",
        "--log-level",
        help="""
        Set the logging level.  "all" is a special setting which causes logging
        from all modules to display at the debug level, in addition to this
        application.  This can result in a lot of logging noise.
        Default: %(default)s
        """,
        choices=["all", "debug", "info", "warning", "error", "critical"],
        default="info",
    )

    parser.add_argument(
        "s3_uri",
        help="""
        S3 URI(s) to download from
        """,
        nargs="+",
    )

    return parser.parse_args()


def _setup_logging(log_level: Union[int, str] = logging.INFO) -> None:
    """
    Set up logging.

    Args:
        log_level: The logging level to use.  May be one of the integer log
            level constants or names recognized by the logging module, or
            "all".
    """
    if isinstance(log_level, str):
        log_level = log_level.upper()

    configure_structlog()

    if log_level == "ALL":
        log = logging.getLogger()
        log.setLevel(logging.DEBUG)
    else:
        log = logging.getLogger("radar")
        log.setLevel(log_level)

    attach_stdout_stream_handler(False, log)


def main() -> None:
    args = parse_args()
    _setup_logging(args.log_level)

    s3 = boto3.client("s3", endpoint_url=args.endpoint_url)

    s3_download(s3, args.dest_dir, args.clear, args.preserve_paths, *args.s3_uri)


if __name__ == "__main__":
    main()
