# /qompassai/radar/container-vars.mk
# -----------------------------------
# Copyright (C) 2025 Qompass AI, All rights reserved

CONTAINER_MLFLOW_TRACKING_INCLUDE_FILES =\
    docker/configs/aws-config\
    docker/configs/build.pip.conf\
    docker/requirements/linux-$(DETECTED_ARCH)-py3.11-mlflow-tracking-requirements.txt\
    docker/shellscripts/entrypoint-mlflow-tracking.m4\
    docker/shellscripts/fix-permissions.m4\
    docker/shellscripts/parse-uri.m4\
    docker/shellscripts/wait-for-it.sh
CONTAINER_NGINX_INCLUDE_FILES =\
    docker/configs/nginx.conf\
    docker/shellscripts/entrypoint-nginx.m4\
    docker/shellscripts/parse-uri.m4\
    docker/shellscripts/wait-for-it.sh

CONTAINER_PYTORCH_CPU_INCLUDE_FILES =\
    docker/configs/aws-config\
    docker/configs/build.pip.conf\
    docker/requirements/linux-$(DETECTED_ARCH)-py3.11-pytorch-cpu-requirements.txt\
    docker/shellscripts/entrypoint-worker.m4\
    docker/shellscripts/fix-permissions.m4\
    docker/shellscripts/parse-uri.m4\
    docker/shellscripts/wait-for-it.sh\
    $(CODE_PACKAGING_FILES)\
    $(CODE_SRC_FILES)

CONTAINER_PYTORCH_GPU_INCLUDE_FILES =\
    docker/configs/aws-config\
    docker/configs/build.pip.conf\
    docker/requirements/linux-amd64-py3.11-pytorch-gpu-requirements.txt\
    docker/shellscripts/entrypoint-worker.m4\
    docker/shellscripts/fix-permissions.m4\
    docker/shellscripts/parse-uri.m4\
    docker/shellscripts/wait-for-it.sh\
    $(CODE_PACKAGING_FILES)\
    $(CODE_SRC_FILES)

CONTAINER_RESTAPI_INCLUDE_FILES =\
    docker/configs/aws-config\
    docker/configs/build.pip.conf\
    docker/configs/gunicorn.restapi.conf.py\
    docker/requirements/linux-$(DETECTED_ARCH)-py3.11-restapi-requirements.txt\
    docker/shellscripts/entrypoint-restapi.m4\
    docker/shellscripts/fix-permissions.m4\
    docker/shellscripts/parse-uri.m4\
    docker/shellscripts/wait-for-it.sh\
    wsgi.py\
    $(CODE_PACKAGING_FILES)\
    $(CODE_SRC_FILES)

CONTAINER_TENSORFLOW2_CPU_INCLUDE_FILES =\
    docker/configs/aws-config\
    docker/configs/build.pip.conf\
    docker/requirements/linux-$(DETECTED_ARCH)-py3.11-tensorflow2-cpu-requirements.txt\
    docker/shellscripts/entrypoint-worker.m4\
    docker/shellscripts/fix-permissions.m4\
    docker/shellscripts/parse-uri.m4\
    docker/shellscripts/wait-for-it.sh\
    $(CODE_PACKAGING_FILES)\
    $(CODE_SRC_FILES)

CONTAINER_TENSORFLOW2_GPU_INCLUDE_FILES =\
    docker/configs/aws-config\
    docker/configs/build.pip.conf\
    docker/requirements/linux-amd64-py3.11-tensorflow2-gpu-requirements.txt\
    docker/shellscripts/entrypoint-worker.m4\
    docker/shellscripts/fix-permissions.m4\
    docker/shellscripts/parse-uri.m4\
    docker/shellscripts/wait-for-it.sh\
    $(CODE_PACKAGING_FILES)\
    $(CODE_SRC_FILES)
