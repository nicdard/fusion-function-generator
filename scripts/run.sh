#!/bin/bash

TIMESTAMP=$(date '+%s')
id=$((0))

# Build the docker image.
# docker build . -t ffg:$TIMESTAMP

IMAGE=ghcr.io/nicdard/fusion-function-generator/ffg

docker pull $IMAGE:latest
docker run -dit --mount source=ffg-$TIMESTAMP,destination=/app/vol --name ffg $IMAGE:latest /app/scripts/test.sh

