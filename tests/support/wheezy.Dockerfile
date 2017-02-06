FROM debian:wheezy

RUN apt-get -y update
RUN apt-get -y install ca-certificates \
                       git' \
                       openssh-client \
                       python-pip \
                       python-dev \
                       libffi-dev
RUN pip install ansible==2.1

COPY run-tests.sh run-tests.sh
CMD ["./run-tests.sh"]
