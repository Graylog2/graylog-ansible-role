FROM debian:wheezy

RUN apt-get -y update
RUN apt-get -y install ca-certificates='20130119+deb7u1' \
                       git='1:1.7.10.4-1+wheezy3' \
                       openssh-client='1:6.0p1-4+deb7u6' \
                       python-pip=1.1-3 \
                       python-dev=2.7.3-4+deb7u1 \
                       libffi-dev=3.0.10-3
RUN pip install ansible==2.1

COPY run-tests.sh run-tests.sh
CMD ["./run-tests.sh"]
