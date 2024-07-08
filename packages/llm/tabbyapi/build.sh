#!/usr/bin/env bash
set -ex

echo "Building tabbyapi"

git clone --branch=${TABBYAPI_BRANCH} --depth=1 https://github.com/theroyallab/tabbyAPI.git /opt/tabbyAPI

cd /opt/tabbyAPI
pip install .
