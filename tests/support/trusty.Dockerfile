FROM ubuntu:trusty

RUN apt-get -y update
RUN apt-get -y install ca-certificates=20160104ubuntu0.14.04.1 \
                       git='1:1.9.1-1ubuntu0.3' \
                       gcc='4:4.8.2-1ubuntu6' \
                       openssh-client='1:6.6p1-2ubuntu2.8' \
                       openssl=1.0.1f-1ubuntu2.21 \
                       python-pip=1.5.4-1ubuntu4 \
                       python-dev=2.7.5-5ubuntu3 \
                       libffi-dev='3.1~rc1+r3.0.13-12ubuntu0.1' \
                       libssl-dev=1.0.1f-1ubuntu2.21
RUN pip install --upgrade pip \
                          setuptools \
                          ansible==2.1

COPY run-tests.sh run-tests.sh
CMD ["./run-tests.sh"]
