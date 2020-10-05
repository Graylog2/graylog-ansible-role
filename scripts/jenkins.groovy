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
      stage('Install and Validate')
      {
        agent
        {
          label 'linux'
        }
        steps
        {
          sh "MOLECULE_DISTRO='generic/ubuntu2004'; molecule test --scenario-name ui"
        }
      }
   }
}
