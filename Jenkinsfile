pipeline {
    agent any
    tools {
        dockerTool 'Docker'
    }
    environment {
        AWS_REGION = 'eu-west-3'
        ECR_REGISTRY = '329599629502.dkr.ecr.eu-west-3.amazonaws.com'
        IMAGE_NAME = "loanaproval" 
        COMPONENT_NAME = 'LoanApproval'
        SONAR_TOKEN = '39cc334a0a13dc54d616ab48a6949fae534f6b15'
        SONAR_HOST = 'http://192.168.0.147:9000'
    }
    stages {
        stage('Checkout') {
            steps {
                checkout scmGit(
                    branches: [[name: '*/main']],
                    extensions: [],
                    userRemoteConfigs: [[credentialsId: 'ser3elah', url: 'https://github.com/projet-fintech/Loan-Approval.git']]
                )
            }
        }

        stage('Prepare Environment') {
            steps {
                script {
                    sh """
                        python3 -m venv venv
                        . venv/bin/activate
                        pip install -r requirements.txt
                    """
                }
            }
        }

        stage('Run Unit Tests') {
            steps {
                script {
                     sh '''
            . venv/bin/activate
            pip install -r requirements.txt
            pip install pytest 
            cd LoanPridiction  // Correction du chemin
            pytest test_app.py -v
                '''
                }
            }
        }

        stage('SonarQube Analysis') {
            steps {
                script {
                    withSonarQubeEnv('sonarqube') {
                        sh """
                            sonar-scanner \
                                -Dsonar.projectKey=${COMPONENT_NAME}-project \
                                -Dsonar.sources=. \
                                -Dsonar.host.url=${env.SONAR_HOST} \
                                -Dsonar.login=${env.SONAR_TOKEN}
                        """
                    }
                }
            }
        }

        /*stage('Build Docker Image') {
            steps {
                script {
                    def localImageName = "${IMAGE_NAME}:${BUILD_NUMBER}"
                    sh "docker build -t ${localImageName} ."
                }
            }
        }
*/
        /*stage('Push to ECR') {
            steps {
                script {
                    withCredentials([aws(credentialsId: 'aws-credentials')]) {
                        def awsCredentials = "-e AWS_ACCESS_KEY_ID=${AWS_ACCESS_KEY_ID} -e AWS_SECRET_ACCESS_KEY=${AWS_SECRET_ACCESS_KEY}"
                        
                        docker.image('amazon/aws-cli').inside("--entrypoint='' ${awsCredentials}") {
                            sh """
                                aws ecr get-login-password --region ${AWS_REGION} > ecr_password.txt
                            """
                        }
                        
                        // Login à ECR
                        sh "cat ecr_password.txt | docker login --username AWS --password-stdin ${ECR_REGISTRY}"
                        sh "rm ecr_password.txt"
                        
                        // Tag et push des images
                        def localImageName = "${IMAGE_NAME}:${BUILD_NUMBER}"
                        def ecrImageLatest = "${ECR_REGISTRY}/${IMAGE_NAME}:latest"
                        def ecrImageVersioned = "${ECR_REGISTRY}/${IMAGE_NAME}:${BUILD_NUMBER}"
                        
                        sh """
                            docker tag ${localImageName} ${ecrImageLatest}
                            docker tag ${localImageName} ${ecrImageVersioned}
                            docker push ${ecrImageLatest}
                            docker push ${ecrImageVersioned}
                        """
                    }
                }
            }
        }*/

        stage('Cleanup') {
            steps {
                script {
                    sh """
                        docker rmi ${IMAGE_NAME}:${BUILD_NUMBER} || true
                        docker rmi ${ECR_REGISTRY}/${IMAGE_NAME}:${BUILD_NUMBER} || true
                        docker rmi ${ECR_REGISTRY}/${IMAGE_NAME}:latest || true
                    """
                }
            }
        }
    }
    post {
        failure {
            echo 'Pipeline failed! Cleaning up...'
            sh 'rm -f ecr_password.txt || true'
        }
        success {
            echo 'Pipeline succeeded! Image pushed to ECR.'
        }
        always {
            cleanWs()
        }
    }
}