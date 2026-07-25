@Library('jenkins-shared-library') _

buildService(

    // pythonProjects: [
    //     [path: 'pyproject.toml',   name: 'pet-service']
    // ],

    dockerProjects: [
        [path: 'Dockerfile', name: 'pet-service', isPod: true],
        [path: 'database/Dockerfile', name: 'pet-database', isPod: true],
    ]
)