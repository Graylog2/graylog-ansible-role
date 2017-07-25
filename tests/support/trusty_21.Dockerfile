FROM ubuntu:trusty

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
                ansible==2.1.2

COPY run-tests.sh run-tests.sh
