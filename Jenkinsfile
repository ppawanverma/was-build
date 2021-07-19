pipeline {
  environment {
    registry = "ppawanverma/jdemo"
    registryCredential = 'dockerhubcred-jdemo'
  }
  agent any
  stages {
    stage('Building image') {
      steps{
        script {
          docker.build registry + ":$BUILD_NUMBER"
        }
      }
    }
  }
}
