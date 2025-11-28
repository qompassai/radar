#!/bin/bash

echo ""
echo "------------- ENV variables --------------------"
echo "DOCKER_NO_CACHE=${DOCKER_NO_CACHE}"
echo "DOCKER_BUILD_TARGET=${DOCKER_BUILD_TARGET}"
echo "DOCKER_BUILDKIT_VALUE=${DOCKER_BUILDKIT_VALUE}"
echo "IMAGE_TAG=${IMAGE_TAG}"
echo ""
prefix=${PROJECT_PREFIX}
echo ""
echo "Building ${prefix}/${PROJECT_COMPONENT}"
echo "=========================================="
echo ""
DOCKERFILE="docker/Dockerfile.${PROJECT_COMPONENT}"
BUILD_CONTEXT="."
BUILD_ARGS="${DOCKER_BUILD_ARGS}"
IMAGE_NAME="${prefix}/${PROJECT_COMPONENT}"
CREATED_DATE="$(date -u +%Y-%m-%dT%H:%M:%SZ)"
REVISION="$(git log -1 --pretty=%H)"
if [[ -e ${DOCKERFILE} ]]; then
  DOCKER_BUILDKIT=${DOCKER_BUILDKIT_VALUE} \
    docker build ${DOCKER_NO_CACHE} \
    --tag ${IMAGE_NAME}:${IMAGE_TAG} \
    -f ${DOCKERFILE} \
    --target ${DOCKER_BUILD_TARGET} \
    --label "maintainer=Qompass AI, Matt A. Porter <map@qompass.ai>" \
    --label "org.opencontainers.image.title=${PROJECT_COMPONENT}" \
    --label "org.opencontainers.image.description=Provides the ${PROJECT_COMPONENT} microservice within the Radar architecture." \
    --label "org.opencontainers.image.authors=maintainer=Qompass AI, Matt A. Porter <map@qompass.ai>" \
    --label "org.opencontainers.image.vendor=Qompass AI" \
    --label "org.opencontainers.image.url=https://github.com/qompassai/radar" \
    --label "org.opencontainers.image.source=https://github.com/qompassai/radar" \
    --label "org.opencontainers.image.documentation=https://pages.nist.gov/radar" \
    --label "org.opencontainers.image.version=dev" \
    --label "org.opencontainers.image.created=${CREATED_DATE}" \
    --label "org.opencontainers.image.revision=${REVISION}" \
    --label "org.opencontainers.image.licenses=Q-CDA 1.0" \
    ${BUILD_ARGS} \
    ${BUILD_CONTEXT} ||
    exit 1
fi
