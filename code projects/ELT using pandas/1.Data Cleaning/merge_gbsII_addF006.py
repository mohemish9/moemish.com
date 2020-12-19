import pandas as pd

rawPath = "/home/ec2-user/survey_project/data/raw/"
processedPath = "/home/ec2-user/survey_project/data/processed/"
interimPath = "/home/ec2-user/survey_project/data/interim/"



""" getProvince finds the province coressponding to a given ID and country in a certian DataFrame"""
def getValue(df, countryLabel, valueLabel, IDLabel, waveNumber, country, ID, wave,currentValue):
    #counter variable adjust for incremental IDs and it is reset before every iteration on different wave
    global counter
    if wave == waveNumber:
        cond = (df[countryLabel] == int(country)) & (df[IDLabel] == int(ID))
        num = df.loc[cond , [valueLabel]]
        if not num.empty:
            return str(num.iloc[0][valueLabel])
        return currentValue
    return currentValue



gbs2 = pd.read_csv(processedPath+ "GBSII_provinces_added_0.1.csv")
gbs2['F006_customized'] = None

arab10_12 = pd.read_csv(interimPath+"arab10_12_F006_c.csv")
gbs2['F006_customized'] =  gbs2.apply(lambda row: getValue(arab10_12, 'UN_code', 'q6101', 'qid',3 ,row['country_un'], row['idnumber'], int(row['region']) , row['F006_customized']), axis=1)
del arab10_12
print('arab12 is done')

counter = 1
afro11_13 = pd.read_csv(interimPath+"afro11_13_F006_c.csv")
afro11_13['RESPNO'] = afro11_13['RESPNO'].astype('int')  
gbs2['F006_customized'] =  gbs2.apply(lambda row: getValue(afro11_13, 'UN_code', 'Q98B', 'RESPNO', 2 ,row['country_un'], row['Fixed_ID'], int(row['region']) , row['F006_customized']), axis=1)
del afro11_13
print('afro11_13 is done')

counter = 1
latin13 = pd.read_csv(interimPath+"latin13_F006_c.csv")
gbs2['F006_customized'] =  gbs2.apply(lambda row: getValue(latin13, 'UN_code', 'S14_A', 'numentre', 5 ,row['country_un'], row['Fixed_ID'], int(row['region']) , row['F006_customized']), axis=1)
print("latin13 is done")

gbs2.to_csv(processedPath + "GBSII_provinces_added_0.2.csv")

for name, group in gbs2.groupby('region'):
    emp = group['F006_customized'].isnull().sum() / group.shape[0]
    print(str(name) + ": " + str(emp))
