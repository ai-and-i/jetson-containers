#---
# name: tabbyapi
# group: llm
# config: config.py
# depends: [exllama:dev]
# requires: '>=36.2.0'
#---
ARG BASE_IMAGE
FROM ${BASE_IMAGE}

ARG TABBYAPI_BRANCH

COPY build.sh /tmp/tabbyAPI/build.sh

RUN /tmp/tabbyAPI/build.sh

WORKDIR /opt/tabbyAPI
CMD ["python3", "main.py"]