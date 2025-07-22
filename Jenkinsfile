pipeline {
    agent any

    stages {
        stage('Clone') {
            steps {
                git 'https://github.com/yourusername/flask-cicd-app.git'
            }
        }

        stage('SonarQube Analysis') {
            steps {
                withSonarQubeEnv('Sonar') {
                    sh 'sonar-scanner'
                }
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
                sh './venv/bin/pytest test_app.py'
            }
        }

        stage('Docker Build & Deploy') {
            steps {
                sh '''
                docker rm -f flask-app || true
                docker build --no-cache -t flask-app .
                docker run -d -p 5000:5000 --name flask-app flask-app
                '''
            }
        }
    }

    post {
        success {
            echo '🎉 CI/CD pipeline completed with SonarQube + Docker'
        }
        failure {
            echo '❌ Build failed. Check SonarQube or Test reports.'
        }
    }
}
