pipeline
{
   agent none

   options
   {
      ansiColor('xterm')
      buildDiscarder logRotator(artifactDaysToKeepStr: '30', artifactNumToKeepStr: '10', daysToKeepStr: '30', numToKeepStr: '10')
      timestamps()
   }

   stages
   {
      stage('Install and Validate - Ubuntu 20.04')
      {
        agent
        {
          label 'linux'
        }
        environment
        {
          MOLECULE_DISTRO='generic/ubuntu2004'
          GRAYLOG_VERSION="4.2.0"
          GRAYLOG_REVISION="3"
          PIP_DISABLE_PIP_VERSION_CHECK=1
        }
        steps
        {
          sh '''#!/bin/bash
                python3 -m venv venv
                source venv/bin/activate
                python3 -m pip install -U pip
                pip3 install -r requirements.txt
                molecule destroy
                molecule create
                molecule converge
                molecule verify
             '''
        }
        post
        {
          always
          {
            sh '''#!/bin/bash
                  source venv/bin/activate
                  molecule destroy
               '''
            cleanWs()
          }
        }
      }
      stage('Install and Validate - Centos 8')
      {
        agent
        {
          label 'linux'
        }
        environment
        {
          MOLECULE_DISTRO='geerlingguy/centos8'
          GRAYLOG_VERSION="4.2.0"
          GRAYLOG_REVISION="3"
          PIP_DISABLE_PIP_VERSION_CHECK=1
        }
        steps
        {
          sh '''#!/bin/bash
                python3 -m venv venv
                source venv/bin/activate
                python3 -m pip install -U pip
                pip3 install -r requirements.txt
                molecule destroy
                molecule create
                molecule converge
                molecule verify
             '''
        }
        post
        {
          always
          {
            sh '''#!/bin/bash
                  source venv/bin/activate
                  molecule destroy
               '''
            cleanWs()
          }
        }
      }
    }
}
