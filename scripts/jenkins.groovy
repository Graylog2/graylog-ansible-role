pipeline
{
    agent none

   options
   {
      ansiColor('xterm')
      buildDiscarder logRotator(artifactDaysToKeepStr: '30', artifactNumToKeepStr: '10', daysToKeepStr: '30', numToKeepStr: '10')
      timestamps()
   }

   environment
   {
     MOLECULE_DISTRO='generic/ubuntu2004'
     GRAYLOG_VERSION=3.3.5
     GRAYLOG_VERSION_WITH_REVISION=3.3.5-1
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
          sh "molecule test --scenario-name ui"
        }
      }
   }
}
