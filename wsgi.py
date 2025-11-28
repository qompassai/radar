# /qompassai/radar/wsgi.py
# -----------------------------------
# Copyright (C) 2025 Qompass AI, All rights reserved
import os

from radar.restapi import create_app
from radar.sdk.utilities.logging import (
    attach_stdout_stream_handler,
    configure_structlog,
    set_logging_level,
)

attach_stdout_stream_handler(
    True if os.getenv("RADAR_RESTAPI_LOG_AS_JSON") else False,
)
set_logging_level(os.getenv("RADAR_RESTAPI_LOG_LEVEL", default="INFO"))
configure_structlog()
app = create_app(env=os.getenv("RADAR_RESTAPI_ENV"))
