import json
import requests
from project_configuration import ProjectConfiguration
from project import Project 

class FoundaMl:
    def __init__(self, host, port, protocol='http'):
        self.host = host
        self.port = port
        self.protocol = protocol
    
    def getProject(self, projectId):
        url = f'{self.protocol}://{self.host}:{self.port}/projects/{projectId}'
        response = requests.get(url)
        if response.status_code == 200:
            responseData = json.loads(response.content )
            projectId = responseData['id']
            projectName = responseData['name']
            projectProblem = responseData['problem']
            projectAlgorithms = responseData['algorithms']
            projectPolicy = responseData['policy']
            projectFeaturesConfiguration = responseData['configuration']['features']
            projectLabelsConfiguration = responseData['configuration']['labels']
            projectConfiguration = ProjectConfiguration(projectFeaturesConfiguration, projectLabelsConfiguration)
            project = Project(projectId, projectName, projectProblem, projectAlgorithms, projectPolicy, projectConfiguration)
            return project
        else:
            return None
