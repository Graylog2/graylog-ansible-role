FROM debian:buster

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
       sudo \
       systemd \
       systemd-sysv \
       build-essential \
       wget \
       libffi-dev \
       libssl-dev \
       python3-pip \
       python3-dev \
       python3-setuptools \
       python3-wheel \
       ca-certificates \
       git \
       openssh-client \
       libssl-dev \
       libffi-dev \
    && rm -rf /var/lib/apt/lists/* \
    && rm -Rf /usr/share/doc && rm -Rf /usr/share/man \
    && apt-get clean

RUN pip3 install -U pip setuptools cffi
RUN pip3 install ansible

COPY run-tests.sh run-tests.sh
