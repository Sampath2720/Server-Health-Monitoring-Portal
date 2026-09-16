pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                echo 'Checking out source code...'
            }
        }

        stage('Pytest') {
            steps {
                sh '''
                python3 -m venv venv
                . venv/bin/activate
                pip install -r requirements.txt
                pytest -v
                '''
            }
        }

        stage('Flake8') {
            steps {
                sh '''
                . venv/bin/activate
                flake8 app.py
                '''
            }
        }

        stage('Build') {
            steps {
                sh 'docker build -t server-health:v1 .'
            }
        }

        stage('Deploy') {
            steps {
                sh '''
                docker stop server-health || true
                docker rm server-health || true

                docker run -d \
                --name server-health \
                -p 7010:7010 \
                server-health:v1
                '''
            }
        }

    }
}
