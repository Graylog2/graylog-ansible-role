FROM debian:jessie

RUN apt-get -y update
RUN apt-get -y install ca-certificates \
                       git \
                       openssh-client \
                       libssl-dev \
                       python-pip \
                       python-dev \
                       libffi-dev
RUN pip install -U pip cffi
RUN pip install -U setuptools==44.1.1
RUN pip install ansible==2.5

COPY run-tests.sh run-tests.sh
