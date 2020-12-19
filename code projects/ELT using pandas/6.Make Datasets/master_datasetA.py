import pandas as pd

rawPath = "/home/ec2-user/survey_project/data/raw/"
processedPath = "/home/ec2-user/survey_project/data/processed/"
interimPath = "/home/ec2-user/survey_project/data/interim/"

data = pd.read_csv(processedPath + "master_longDataSet.0.0.5.csv", encoding = "ISO-8859-1")

filter = pd.isnull(data['ISO3166_2_c'])

data = data[- filter]

data.to_csv(processedPath+"master_longDataSet.0.0.6.csv")
