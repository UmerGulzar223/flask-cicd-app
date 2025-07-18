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
                    sh '''
                    echo "🧹 Cleaning old container..."
                    docker ps --format '{{.ID}} {{.Ports}}' | grep '0.0.0.0:5000' | awk '{print $1}' | xargs -r docker stop
                    docker rm -f flask-app || true

                    echo "⚙️  Building fresh image (no cache)..."
                    docker build --no-cache -t flask-app .

                    echo "🚀 Deploying new container..."
                    docker run -d -p 5000:5000 --name flask-app flask-app
                    '''
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
