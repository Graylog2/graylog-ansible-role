# Testing

If you'd like to run the Molecule tests, you'll need a few things installed:

- [Vagrant](https://www.vagrantup.com/docs/installation)
- [Molecule](https://molecule.readthedocs.io/en/latest/installation.html)
- [testinfra](https://testinfra.readthedocs.io/en/latest/)

Note that this is ONLY required if you want to run the test harness. You don't need any of this to run the playbook. This is a special setup that allows you to test the Ansible playbook against disposable VMs.

## Install Notes

Setting up Molecule requires installing a number tools for the VM environment.

Install Virtualenv, Molecule, and testinfra

    sudo apt-get update
    sudo apt-get install -y python3-pip libssl-dev python3-virtualenv
    virtualenv venv
    source venv/bin/activate
    python3 -m pip install "molecule[lint]"
    pip3 install testinfra

Install Vagrant

    sudo wget -nv https://releases.hashicorp.com/vagrant/2.2.9/vagrant_2.2.9_x86_64.deb
    sudo dpkg -i vagrant_2.2.9_x86_64.deb
    vagrant --version
    pip3 install python-vagrant molecule-vagrant

Test that Vagrant works

    vagrant init generic/ubuntu1804
    vagrant up
    vagrant ssh
    vagrant halt

Test that Molecule works

    git clone https://github.com/Graylog2/graylog-ansible-role.git
    cd graylog-ansible-role
    molecule create
    molecule converge
    molecule login
    systemctl status graylog-server
    exit
    molecule destroy

#### Commands

To spin up a test VM:

    export MOLECULE_DISTRO='generic/ubuntu2004'
    export GRAYLOG_VERSION=4.2.0
    export GRAYLOG_REVISION=3
    molecule create

To run the Ansible playbook:

    molecule converge

To run the smoke tests:

    molecule verify

To login to the VM:

    molecule login

To destroy the VM:

    molecule destroy

To test against other distros, you can also set the MOLECULE_DISTRO environment variable to one of these:

    export MOLECULE_DISTRO='geerlingguy/centos8'
    export MOLECULE_DISTRO='debian/jessie64'
    export MOLECULE_DISTRO='debian/stretch64'
    export MOLECULE_DISTRO='debian/buster64'
    export MOLECULE_DISTRO='generic/ubuntu1604'
    export MOLECULE_DISTRO='generic/ubuntu1804'
    export MOLECULE_DISTRO='generic/ubuntu2004'
