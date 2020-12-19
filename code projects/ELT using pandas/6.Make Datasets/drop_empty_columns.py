import pandas as pd

rawPath = "/home/ec2-user/survey_project/data/raw/"
processedPath = "/home/ec2-user/survey_project/data/processed/"
interimPath = "/home/ec2-user/survey_project/data/interim/"

data = pd.read_csv(processedPath + "master_longDataSet.0.0.5.csv", index_col=[0], encoding = "ISO-8859-1")
questions = data.columns
print(data.shape)
data= data.loc[:, ~data.columns.str.match('Unnamed')]
print(data.shape)
for q in questions:
    data = data.dropna(how='all', axis=1)


data= data.loc[:, ~data.columns.str.match('Unnamed')]
print(data.shape)

data.to_csv(processedPath+ "master_longDataSet.0.0.6.csv")
