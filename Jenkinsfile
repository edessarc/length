pipeline {
    agent { label "kali-linux"}
    stages {
        stage('Build') {
            steps {
                sh 'docker build -t edessarc/length:latest .'
            }
        }
        stage('Login') {
            steps {
                sh "docker login -u edessarc -p Zlutyheets1!"
            }
        }
        stage('Push') {
            steps {
                sh "docker push edessarc/length:latest"
            }
        }
        stage('Logout') {
            steps {
                sh "docker logout"
            }
        }
    }
}
