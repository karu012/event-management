pipeline {
    agent any 
    environment {
        DOCKERHUB_CREDENTIALS = credentials('test1') // Your Jenkins credential ID
    }
    stages {
        stage('Build Docker image') {
            steps {  
                echo "Building Docker image..."
                sh 'docker build -t karunya1203/event-planner:$BUILD_NUMBER .'
            }
        }
        stage('Login to Docker Hub') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'test1', usernameVariable: 'DOCKERHUB_USERNAME', passwordVariable: 'DOCKERHUB_PASSWORD')]) {
                    echo "Logging in to Docker Hub..."
                    sh "docker login -u $DOCKERHUB_USERNAME -p $DOCKERHUB_PASSWORD"
                }
            }
        }
        stage('Push image') {
            steps {
                echo "Pushing Docker image to Docker Hub..."
                sh 'docker push karunya1203/event-planner:$BUILD_NUMBER'
            }
        }
        stage('Deploy to Staging') {
            steps {
                // Pull the latest image from Docker Hub
                sh 'docker pull karunya1203/event-planner:$BUILD_NUMBER'

                // Stop and remove any existing containers
                sh 'docker stop event-planner-container || true'
                sh 'docker rm event-planner-container || true'

                // Run the new container with the latest image
                sh 'docker run -d --name event-planner-container -p 8080:8080 karunya1203/event-planner:$BUILD_NUMBER'
            }
        }
    }
    post {
        always {
            echo "Logging out from Docker Hub..."
            sh 'docker logout'
        }
    }
}
