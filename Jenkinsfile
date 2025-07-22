pipeline {
    agent any

    environment {
        SONAR_TOKEN = credentials('sonar-token') // Jenkins secret text
    }

    stages {
        stage('Install Dependencies') {
            steps {
                sh 'pip install flake8 pytest'
            }
        }

        stage('Lint & Unit Tests') {
            steps {
                sh 'flake8 . --exit-zero'
                sh 'pytest || true'
            }
        }

        stage('SonarQube Analysis') {
            steps {
                withSonarQubeEnv('MySonarQube') {
                    sh 'sonar-scanner'
                }
            }
        }

        stage('Docker Build') {
            steps {
                sh 'docker build -t flask-cicd-app .'
            }
        }

        stage('Deploy via Docker Compose') {
            steps {
                sh 'docker-compose down || true'
                sh 'docker-compose up -d --build'
            }
        }
    }
}
