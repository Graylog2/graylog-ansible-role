pipeline
{
   agent none

   options
   {
      ansiColor('xterm')
      buildDiscarder logRotator(artifactDaysToKeepStr: '30', artifactNumToKeepStr: '10', daysToKeepStr: '30', numToKeepStr: '10')
      timestamps()
   }

   parameters
   {
     string(name: 'GRAYLOG_VERSION', defaultValue: '', description: 'The Graylog version you want tested (3.3.6, 4.0.0, etc).')
     string(name: 'GRAYLOG_REVISION', defaultValue: '1', description: 'The Graylog package revision. (1, 2, 2.beta.2, etc.)')
   }

   environment
   {
     MOLECULE_DISTRO='generic/ubuntu2004'
     GRAYLOG_VERSION="${params.GRAYLOG_VERSION}"
     GRAYLOG_REVISION="${params.GRAYLOG_REVISION}"
     PIP_DISABLE_PIP_VERSION_CHECK=1
   }

   stages
   {
      stage('Install and Validate')
      {
        agent
        {
          label 'linux'
        }
        steps
        {
          sh '''#!/bin/bash
                python3 -m venv venv
                source venv/bin/activate
                python3 -m pip install -U pip
                pip3 install -r requirements.txt
                molecule destroy --scenario-name ui
                molecule create --scenario-name ui
                molecule converge --scenario-name ui
                molecule verify --scenario-name ui
             '''
        }
        post
        {
          always
          {
            sh 'molecule destroy --scenario-name ui'
            cleanWs()
          }
        }
      }
    }
}
