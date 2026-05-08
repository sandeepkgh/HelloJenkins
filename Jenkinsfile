pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out code from repository...'
                checkout scm
            }
        }
        
        stage('Setup') {
            steps {
                echo 'Setting up Python environment...'
                sh 'python3 --version'
            }
        }
        
        stage('Run Hello World') {
            steps {
                echo 'Running Hello World Python script...'
                sh 'python3 hello_world.py'
            }
        }
        
        stage('Test') {
            steps {
                echo 'Running basic tests...'
                sh 'python3 -m py_compile hello_world.py'
                echo 'Python syntax validation passed!'
            }
        }
    }
    
    post {
        always {
            echo 'Pipeline execution completed!'
        }
        success {
            echo '✓ Pipeline completed successfully!'
        }
        failure {
            echo '✗ Pipeline failed!'
        }
    }
}
