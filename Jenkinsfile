pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh 'echo "building the repo"'
                echo "Running ${env.BUILD_ID} on ${env.JENKINS_URL}"
                sh "docker build -t flaskapp:${env.BUILD_ID} ."
            }
        }

        stage('Install') {
            steps {
                sh 'echo "installing the required dependencies in requirements.txt using pip"'
                sh 'pip install -r requirements.txt --user'
            }
        }

        stage('Test') {
            steps {
                sh 'echo "executing tests using pytest"'
                sh 'pytest --html=reports/flask-test-report.html --self-contained-html test_app.py'
            }
        }

        stage('Deploy') {
            steps {
                echo 'deploying the application'
                sh 'sudo nohup python3 app.py > log.txt 2>&1 &'
            }
        }
    }

    post {
        always {
            echo 'The pipeline completed, publishing results as report'
            // publish html
            publishHTML target: [
                allowMissing: false,
                alwaysLinkToLastBuild: false,
                keepAll: true,
                reportDir: 'reports',
                reportFiles: 'flask-test-report.html',
                reportName: 'Flask Test Results'
            ]
        }
        success {
            echo 'Flask Application Up and running!!'
        }
        failure {
            echo 'Build stage failed'
            error('Stopping early…')
        }
    }
}
