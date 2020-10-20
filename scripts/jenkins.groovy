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
     string(name: 'GRAYLOG_REVISION', defaultValue: '1', description: 'The Graylog package revision.')
   }

   environment
   {
     MOLECULE_DISTRO='generic/ubuntu2004'
     GRAYLOG_VERSION="${params.GRAYLOG_VERSION}"
     GRAYLOG_REVISION="${params.GRAYLOG_REVISION}"
     GRAYLOG_VERSION_WITH_REVISION="${GRAYLOG_VERSION}-${GRAYLOG_REVISION}"
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
          sh '''molecule destroy --scenario-name ui
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
