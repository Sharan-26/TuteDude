pipeline {
    agent any

    stages {
        stage('Hello') {
            steps {
                echo 'Hello from Jenkins!'
            }
        }

        stage('System Info') {
            steps {
                sh 'hostname'
                sh 'whoami'
                sh 'pwd'
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully!'
        }
    }
}
