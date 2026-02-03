#!/usr/bin/bash
DOCKER_FILE=$(realpath $(dirname $0))/Dockerfile
sudo docker build -f $DOCKER_FILE -t local:wf-engine-fedora .
