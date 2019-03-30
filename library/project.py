
class Project:
    def __init__(self, projectId, name, problem, algorithms, policy, configuration):
        self.projectId = projectId
        self.name = name
        self.problem = problem
        self.algorithms = algorithms
        self.policy = policy
        self.configuration = configuration

    def describe(self):
        print(f"Name: {self.name}")
        print(f"Problem: {self.problem} \n")
        print("Features:")
        for feature in self.configuration.features:
            featureName = feature['name']
            featureDescription = feature['description']
            featureType = feature['type']
            print(f"{featureName}|{featureType}|{featureDescription}")
        
        print("")
        labels = self.configuration.labels
        labelType = labels['type']
        if labelType == 'oneOf':
            print("Labels:")
            for labelName in labels['oneOf']:
                print(labelName)
        else:
            print("Label: Dynamic")
