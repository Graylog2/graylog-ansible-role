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
RUN yum install -y ca-certificates-2015.2.6 \
                   gcc-4.8.5 \
                   git-1.8.3.1 \
                   openssl-1.0.1e \
                   openssl-devel-1.0.1e \
                   python2-pip-8.1.2 \
                   python-devel-2.7.5 \
                   libffi-devel-3.0.13
RUN pip install --upgrade pip setuptools
RUN pip install ansible==2.1

COPY run-tests.sh run-tests.sh
