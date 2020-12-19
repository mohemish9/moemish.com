import pandas as pd

rawPath = "/home/ec2-user/survey_project/data/raw/"
processedPath = "/home/ec2-user/survey_project/data/processed/"
interimPath = "/home/ec2-user/survey_project/data/interim/"


""" getProvince finds the province coressponding to a given ID and country in a certian DataFrame"""
def getProvince(df, countryLabel, provinceLabel, IDLabel, waveNumber, country, ID, wave,currentValue):
    if wave == waveNumber:
        cond = (df[countryLabel] == int(country)) & (df[IDLabel] == int(ID))
        num = df.loc[cond , [provinceLabel]]
        if not num.empty:
            return str(num.iloc[0][provinceLabel])
        return currentValue
    return currentValue



gbs1 = pd.read_csv(rawPath+ "GBS1.0.csv")
gbs1['province'] = None

afro05 = pd.read_csv(interimPath+"afro05_respondentsID_c.csv")
gbs1['province'] =  gbs1.apply(lambda row: getProvince(afro05, 'UN_code', 'region', 'respno',2 ,row['country_un'], row['idnumber'], int(row['region']) , row['province']), axis=1)
print("afro05 done")
del afro05

afro08 = pd.read_csv(interimPath+"afro08_respondentsID_c.csv")
gbs1['province'] =  gbs1.apply(lambda row: getProvince(afro08, 'UN_code', 'REGION', 'RESPNO',3 ,row['country_un'], row['idnumber'], int(row['region']) , row['province']), axis=1)
print("afro08 done")
del afro08

arab10 = pd.read_csv(interimPath+"arab10_respondentsID_c.csv")
gbs1['province'] =  gbs1.apply(lambda row: getProvince(arab10, 'UN_code', 'q1', 'qid',5 ,row['country_un'], row['idnumber'], int(row['region']) , row['province']), axis=1)
print("arab10 done")
del arab10

latin05 = pd.read_csv(interimPath + "latin05_respondentsID_c.csv")
gbs1['province'] =  gbs1.apply(lambda row: getProvince(latin05, 'UN_code', 'reg', 'numentre',6 ,row['country_un'], row['idnumber'], int(row['region']) , row['province']), axis=1)
print("latin05 done")
del latin05

latin10 = pd.read_csv(interimPath + "latin10_respondentsID_c.csv")
gbs1['province'] =  gbs1.apply(lambda row: getProvince(latin10, 'UN_code', 'reg', 'numentre',7 ,row['country_un'], row['idnumber'], int(row['region']) , row['province']), axis=1)
print("latin10 done")
del latin10

gbs1.to_csv(interimPath + "GBS_provinces_added_0.1.csv")

for name, group in gbs1.groupby('region'):
    emp = group['province'].isnull().sum() / group.shape[0]
    print(str(name) + ": " + str(emp))
