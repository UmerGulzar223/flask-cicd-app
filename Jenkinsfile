pipeline {
    agent any

    environment {
        APP_NAME = 'flask-cicd-app'
    }

    stages {
        stage('Clone') {
            steps {
                git 'https://github.com/UmerGulzar223/flask-cicd-app.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'python3 -m venv venv'
                sh './venv/bin/pip install -r requirements.txt'
            }
        }

        stage('Test') {
            steps {
                sh './venv/bin/pip install pytest'
                sh './venv/bin/pytest test_app.py'
            }
        }

        stage('Deploy') {
            steps {
                script {
                    sh 'docker build -t flask-app .'
                    sh 'docker run -d -p 5000:5000 flask-app'
                }
            }
        }
    }

    post {
        always {
            echo 'Pipeline execution completed.'
        }
        success {
            echo 'Build and test succeeded.'
        }
        failure {
            echo 'Pipeline failed.'
        }
    }
}
