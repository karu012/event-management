pipeline {
    agent any
    environment {
        // Optional: DockerHub credentials if you plan to push later
        DOCKERHUB_CREDENTIALS = credentials('test1')
    }
    stages {
        stage('Build Docker image') {
            steps {
                echo "Building Docker image..."
                sh 'docker build -t event-planner-app:$BUILD_NUMBER .'
            }
        }
        stage('Optional: Login to DockerHub') {
            when {
                expression { return false } // Change to true if you want to push to DockerHub
            }
            steps {
                withCredentials([usernamePassword(credentialsId: 'test1', usernameVariable: 'DOCKERHUB_USERNAME', passwordVariable: 'DOCKERHUB_PASSWORD')]) {
                    echo "Logging in to Docker Hub..."
                    sh "docker login -u $DOCKERHUB_USERNAME -p $DOCKERHUB_PASSWORD"
                }
            }
        }
        stage('Optional: Push image to DockerHub') {
            when {
                expression { return false } // Change to true if you want to push
            }
            steps {
                echo "Pushing Docker image to Docker Hub..."
                sh 'docker push event-planner-app:$BUILD_NUMBER'
            }
        }
        stage('Deploy to Staging') {
            steps {
                echo "Deploying container..."
                
                // Stop and remove any existing containers
                sh 'docker stop event-planner-container || true'
                sh 'docker rm event-planner-container || true'

                // Run the new container
                sh 'docker run -d --name event-planner-container -p 8080:8080 event-planner-app:$BUILD_NUMBER'
            }
        }
    }
    post {
        always {
            echo "Cleaning up..."
            sh 'docker logout || true'
        }
    }
}
