pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "swiggy_cicd"
        DOCKER_COMPOSE_FILE = "compose.yml"
    }

    stages {
        stage('Checkout Code') {
            steps {
                echo "📦 Pulling code from Git..."
                checkout scm
            }
        }

        stage('Remove previous docker image') {
            steps {
                echo "🐳 Removing previous Docker image..."
                sh 'docker compose down'
            }
        }

        stage('Build Docker Image') {
            steps {
                echo "🐳 Building Docker image..."
                sh 'docker compose build'
            }
        }

        stage('Run Django Container') {
            steps {
                echo "🚀 Starting container..."
                sh 'docker compose up -d'
            }
        }

        stage('Run Migrations') {
            steps {
                echo "🔄 Applying database migrations..."
                sh 'docker compose exec django python manage.py migrate --noinput'
            }
        }

        stage('Post Actions') {
            steps {
                echo "✅ Deployment complete!"
            }
        }
    }

    post {
        failure {
            echo "❌ Build failed."
        }
        success {
            echo "✅ Build succeeded."
        }
    }
}
