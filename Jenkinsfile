@Library('jenkins-shared-library') _

buildPythonAndDocker(

    pythonProjects: [
        [path: 'pyproject.toml',   name: 'pet-service']
    ],

    dockerProjects: [
        [path: 'Dockerfile',   name: 'pet-service'],
        [path: 'database/Dockerfile',   name: 'pet-database'],
    ]
)