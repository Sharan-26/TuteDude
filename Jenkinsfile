pipeline {
    agent {
        label 'windows'
    }

    stages {

        stage('Checkout') {
            steps {
                echo 'Code checkout completed'
            }
        }

        stage('Build') {
            steps {
                bat 'echo Building on Windows Agent'
                bat 'hostname'
                bat 'whoami'
            }
        }

        stage('Test') {
            steps {
                bat 'echo Running tests'
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully!'
        }

        failure {
            echo 'Pipeline failed!'
        }
    }
}
