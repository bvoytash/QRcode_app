pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                script {
                    if (isUnix()) {
                        sh '''
                            python3 -m venv .venv
                            source .venv/bin/activate
                            python3 -m pip install --upgrade pip
                            pip3 install -r requirements.txt
                        '''
                    } else {
                        bat '''
                            python -m venv .venv
                            call .venv\\Scripts\\activate.bat
                            python -m pip install --upgrade pip
                            pip install -r requirements.txt
                        '''
                    }
                }
            }
        }

        stage('Test') {
            steps {
                script {
                    if (isUnix()) {
                        sh '''
                            source .venv/bin/activate
                            python3 test.py
                        '''
                    } else {
                        bat '''
                            call .venv\\Scripts\\activate.bat
                            python test.py
                        '''
                    }
                }
            }
        }

        stage('Deploy to Render') {
            steps {
                script {
                    withCredentials([
                        string(credentialsId: 'RENDER_API_KEY_3', variable: 'RENDER_API_KEY_3'),
                        string(credentialsId: 'RENDER_DEPLOY_HOOK_3', variable: 'RENDER_DEPLOY_HOOK_3')
                    ]) {
                        if (isUnix()) {
                            sh """
                                curl -X POST https://api.render.com/v1/services/${env.RENDER_DEPLOY_HOOK_3}/deploys \
                                -H "Authorization: Bearer ${env.RENDER_API_KEY_3}" \
                                -H "Content-Type: application/json" \
                                -d "{}"
                            """
                        } else {
                            bat """
                                curl -X POST https://api.render.com/v1/services/${env.RENDER_DEPLOY_HOOK_3}/deploys ^
                                -H "Authorization: Bearer ${env.RENDER_API_KEY_3}" ^
                                -H "Content-Type: application/json" ^
                                -d "{}"
                            """
                        }
                    }
                }
            }
        }
    }

    post {
        always {
            cleanWs()
        }
    }
}
