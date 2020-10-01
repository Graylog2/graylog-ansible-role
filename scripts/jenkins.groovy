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
        parallel
        {
          stage('Ubuntu 20.04')
          {
            agent
            {
              label 'linux'
            }
            steps
            {
              sh 'molecule test'
            }
          }
          stage('Ubuntu 18.04')
          {
            agent
            {
              label 'linux'
            }
            steps
            {
              sh 'molecule test'
            }
          }
        }
      }
   }
}
