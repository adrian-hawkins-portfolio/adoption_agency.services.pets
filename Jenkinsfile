@Library('jenkins-shared-library') _

buildService(

    pythonProjects: [
        [path: 'pyproject.toml',   name: 'pet-service']
    ],

    dockerProjects: [
        [path: 'services/pet_service/Dockerfile', name: 'pet-service', isPod: true],
        [path: 'nodes/pet_node/Dockerfile', name: 'pet-node', isPod: true],
        [path: 'database/Dockerfile', name: 'pet-database', isPod: true],
    ]
)