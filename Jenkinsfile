pipeline {
    agent any

    environment {
        VENV_DIR = 'venv'
        SONAR_TOKEN = credentials('sonar-token')
    }

    stages {
        stage('Setup Python venv') {
            steps {
                sh '''
                python3 -m venv ${VENV_DIR}
                . ${VENV_DIR}/bin/activate
                pip install --upgrade pip
                pip install flake8 pytest
                '''
            }
        }

        stage('Lint & Unit Tests') {
            steps {
                sh '''
                . ${VENV_DIR}/bin/activate
                flake8 . --exit-zero
                pytest || true
                '''
            }
        }

        stage('SonarQube Analysis') {
            steps {
                withSonarQubeEnv('Sonar') {
                    sh '''
                    . ${VENV_DIR}/bin/activate
                    sonar-scanner
                    '''
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
