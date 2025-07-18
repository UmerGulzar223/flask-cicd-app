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
                    // Stop any container using port 5000
                    sh '''
                    CONTAINER_ID=$(docker ps --filter "publish=5000" --format "{{.ID}}")
                    if [ ! -z "$CONTAINER_ID" ]; then
                    docker stop $CONTAINER_ID
                    docker rm $CONTAINER_ID
                    fi
                    '''

                    // Now run the container
                    sh 'docker run -d -p 5000:5000 --name flask-app flask-app'
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
