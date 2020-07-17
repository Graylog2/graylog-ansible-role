FROM ubuntu:xenial

ENV container docker

RUN echo 'root:root' | chpasswd

RUN apt-get -y update
RUN apt-get -y install ca-certificates \
                       git \
                       gcc \
                       openssh-client \
                       openssl \
                       python-pip \
                       python-dev \
                       libffi-dev \
                       libssl-dev
RUN pip install setuptools \
                ansible==2.5

COPY run-tests.sh run-tests.sh
