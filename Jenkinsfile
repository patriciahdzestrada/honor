pipeline {
    agent any

    environment {
        DEMO_TOKEN = credentials('demo-token')
        APP_ENV = 'dev'
        DOCKER_IMAGE = 'mi-etl_ratings'
    }

    stage('Checkout') {
        steps {
            checkout scm
        }
    }    
/*
    stages {
        stage('Install Dependencies') {
            steps {
                bat '"C:\\Users\\mauri\\AppData\\Local\\Programs\\Python\\Python313\\python.exe" -m pip install --upgrade pip'
                bat '"C:\\Users\\mauri\\AppData\\Local\\Programs\\Python\\Python313\\python.exe" -m pip install -r requirements.txt'
            }
        }
*/
        stage('Test') {
            steps {
                bat '"C:\\Users\\mauri\\AppData\\Local\\Programs\\Python\\Python313\\Scripts\\pytest.exe"'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat '"C:\\Users\\mauri\\AppData\\Local\\Programs\\DockerDesktop\\resources\\bin\\docker.exe" build -t %DOCKER_IMAGE% .'
            }
        }

        stage('Run ETL in Docker') {
            steps {
                bat '"C:\\Users\\mauri\\AppData\\Local\\Programs\\DockerDesktop\\resources\\bin\\docker.exe" run --rm %DOCKER_IMAGE%'
            }
        }


/*
        stage('Run ETL') {
            steps {
                bat '"C:\\Users\\mauri\\AppData\\Local\\Programs\\Python\\Python313\\python.exe" src\\etl_ratings.py'
            }
        }
*/
        stage('Archive Artifact') {
            steps {
                archiveArtifacts artifacts: 'data/resultado_promedios.csv', fingerprint: true
            }
        }
    }

    post {
        success {
            echo 'Pipeline ejecutado correctamente'
        }

        failure {
            echo 'Pipeline fallo. Revisar los logs.'
        }
    }
}