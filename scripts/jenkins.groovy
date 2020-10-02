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
              sh "MOLECULE_DISTRO='generic/ubuntu2004'; molecule test"
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
              sh "MOLECULE_DISTRO='generic/ubuntu1804'; molecule test"
            }
          }
          stage('Ubuntu 16.04')
          {
            agent
            {
              label 'linux'
            }
            steps
            {
              sh "MOLECULE_DISTRO='generic/ubuntu1604'; molecule test"
            }
          }
          stage('Debian Buster')
          {
            agent
            {
              label 'linux'
            }
            steps
            {
              sh "export MOLECULE_DISTRO='debian/buster64'; molecule test"
            }
          }
          stage('Debian Stretch')
          {
            agent
            {
              label 'linux'
            }
            steps
            {
              sh "export MOLECULE_DISTRO='debian/stretch64'; molecule test"
            }
          }
          stage('Debian Jessie')
          {
            agent
            {
              label 'linux'
            }
            steps
            {
              sh "export MOLECULE_DISTRO='debian/stretch64'; molecule test"
            }
          }
          stage('Debian Jessie')
          {
            agent
            {
              label 'linux'
            }
            steps
            {
              sh "export MOLECULE_DISTRO='debian/jessie64'; molecule test"
            }
          }
          stage('CentOS 8')
          {
            agent
            {
              label 'linux'
            }
            steps
            {
              sh "export MOLECULE_DISTRO='centos/8'; molecule test"
            }
          }
          stage('CentOS 7')
          {
            agent
            {
              label 'linux'
            }
            steps
            {
              sh "export MOLECULE_DISTRO='centos/7'; molecule test"
            }
          }
        }
      }
   }
}
