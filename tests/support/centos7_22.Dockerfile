FROM centos:7

ENV container docker

RUN (cd /lib/systemd/system/sysinit.target.wants/; for i in *; do [ $i == systemd-tmpfiles-setup.service ] || rm -f $i; done); \
    rm -f /lib/systemd/system/multi-user.target.wants/*;\
    rm -f /etc/systemd/system/*.wants/*;\
    rm -f /lib/systemd/system/local-fs.target.wants/*; \
    rm -f /lib/systemd/system/sockets.target.wants/*udev*; \
    rm -f /lib/systemd/system/sockets.target.wants/*initctl*; \
    rm -f /lib/systemd/system/basic.target.wants/*;\
    rm -f /lib/systemd/system/anaconda.target.wants/*;

VOLUME [ "/sys/fs/cgroup" ]

RUN echo 'root:root' | chpasswd

RUN yum update -y && \
    yum install -y epel-release
RUN yum install -y ca-certificates \
                   gcc \
                   git \
                   openssl \
                   openssl-devel \
                   python2-pip \
                   python-devel \
                   libffi-devel
RUN pip install setuptools
RUN pip install ansible==2.2.1

COPY run-tests.sh run-tests.sh
