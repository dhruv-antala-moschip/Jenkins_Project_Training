pipeline {
    agent any
    stages {
        stage('List and Rename Jobs') {
            steps {
                script {
                   sh """    
                    python3 -m venv myvenv    
                    source myvenv/bin/activate    
                    pip install -r requirements.txt    
                    python3 build_log_info.py ${job_name}    
                    deactivate
                    """
                }
            }
        }
        stage('Send Email'){
            steps{
                emailext(
                    subject: "${env.JOB_NAME} - Build # ${env.BUILD_NUMBER}!",
                    body: "${env.JOB_NAME} - Build # ${env.BUILD_NUMBER} :\nCheck console output at ${env.BUILD_URL} to view the results.",
                    attachLog: true,
                    attachmentsPattern: 'logreport.log, requirements.txt',
                    to: 'dhruv.antala@moschip.com'
                )
            }
        
        }
    }
    post{
        always{
            archiveArtifacts artifacts:'requirements.txt,logreport.log,report.xml', fingerprint: true
            junit 'report.xml'
            
        }
    }
}

