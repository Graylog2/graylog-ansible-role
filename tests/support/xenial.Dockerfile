FROM ubuntu:xenial

ENV container docker

VOLUME [ "/sys/fs/cgroup" ]

RUN echo 'root:root' | chpasswd

RUN apt-get -y update
RUN apt-get -y install ca-certificates=20160104ubuntu1 \
                       git='1:2.7.4-0ubuntu1' \
                       gcc='4:5.3.1-1ubuntu1' \
                       openssh-client='1:7.2p2-4ubuntu2.1' \
                       openssl=1.0.2g-1ubuntu4.5 \
                       python-pip=8.1.1-2ubuntu0.4 \
                       python-dev=2.7.11-1 \
                       libffi-dev=3.2.1-4 \
                       libssl-dev=1.0.2g-1ubuntu4.5
RUN pip install --upgrade pip \
                          setuptools \
                          ansible==2.1

COPY run-tests.sh run-tests.sh
CMD ["./run-tests.sh"]
