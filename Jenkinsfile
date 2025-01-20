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
                    python3 jenkins_api.py ${job_name}    
                    deactivate
                    """
                }
            }
        }
    }
}

