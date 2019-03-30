from foundaml import FoundaMl 

instance = FoundaMl('127.0.0.1', 8080)
project = instance.getProject('kaggle-titanic')
project.describe()
