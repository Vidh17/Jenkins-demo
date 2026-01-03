pipeline {
    agent any

    environment {
        APP_DIR     = "/home/ubuntu/flask-app"
        VENV_DIR    = "venv"
        FLASK_PORT  = "5000"
        FLASK_EC2   = "ubuntu@13.215.201.183"   // Target EC2 (Flask server)
    }

    stages {

        stage('Clone Repository') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/Vidh17/Jenkins-demo.git'
            }
        }

        stage('Install Dependencies (Jenkins Test)') {
            steps {
                sh '''
                python3 -m venv venv
                . venv/bin/activate
                pip install --upgrade pip
                pip install -r requirements.txt
                '''
            }
        }

        stage('Run Basic Test') {
            steps {
                sh '''
                . venv/bin/activate
                python -c "import flask; print('Flask OK')"
                '''
            }
        }

        stage('Deploy to Flask EC2') {
            steps {
                sh '''
                # Ensure app directory exists on target EC2
                ssh -o StrictHostKeyChecking=no ${FLASK_EC2} "mkdir -p ${APP_DIR}"

                # Copy application files (excluding venv)
                scp -o StrictHostKeyChecking=no -r \
                    app.py requirements.txt dev_flask.sh templates \
                    ${FLASK_EC2}:${APP_DIR}

                # Setup virtualenv, install deps, restart app
                ssh -o StrictHostKeyChecking=no ${FLASK_EC2} "
                    cd ${APP_DIR} &&
                    rm -rf venv &&
                    python3 -m venv venv &&
                    . venv/bin/activate &&
                    pip install --upgrade pip &&
                    pip install -r requirements.txt &&
                    chmod +x dev_flask.sh &&
                    ./dev_flask.sh restart
                "
                '''
            }
        }
    }
}

