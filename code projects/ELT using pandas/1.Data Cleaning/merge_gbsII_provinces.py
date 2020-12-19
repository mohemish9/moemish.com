import pandas as pd

rawPath = "/home/ec2-user/survey_project/data/raw/"
processedPath = "/home/ec2-user/survey_project/data/processed/"
interimPath = "/home/ec2-user/survey_project/data/interim/"



""" getProvince finds the province coressponding to a given ID and country in a certian DataFrame"""
"""def getProvince(df, countryLabel, provinceLabel, IDLabel, waveNumber, country, ID, wave,currentValue):
    #counter variable adjust for incremental IDs and it is reset before every iteration on different wave
    global counter
    if wave == waveNumber:
        if not (wave == 2 or wave == 5):
            cond = (df[countryLabel] == int(country)) & (df[IDLabel] == int(ID))
            num = df.loc[cond , [provinceLabel]]
            if not num.empty:
                return str(num.iloc[0][provinceLabel])
            return currentValue
        else:
            cond = (df[countryLabel] == int(country)) & (counter == int(ID))
            num = df.loc[cond , [provinceLabel]]
            if not num.empty:
                print(counter)
                counter = counter + 1
                return str(num.iloc[0][provinceLabel])
            return currentValue
    return currentValue"""


""" getProvince finds the province coressponding to a given ID and country in a certian DataFrame"""
def getProvince(df, countryLabel, provinceLabel, IDLabel, waveNumber, country, ID, wave,currentValue):
    #counter variable adjust for incremental IDs and it is reset before every iteration on different wave
    global counter
    if wave == waveNumber:
        cond = (df[countryLabel] == int(country)) & (df[IDLabel] == int(ID))
        num = df.loc[cond , [provinceLabel]]
        if not num.empty:
            return str(num.iloc[0][provinceLabel])
        return currentValue
    return currentValue


gbs2 = pd.read_csv(rawPath+ "GBS2.7.csv")
gbs2['province'] = None

# fix indicies
gbs2['Fixed_ID'] = gbs2.groupby(['region', 'country_un', 'year']).country_un.cumcount() + 1


arab10_12 = pd.read_csv(interimPath+"arab11_13_respondentsID_c.csv")
gbs2['province'] =  gbs2.apply(lambda row: getProvince(arab10_12, 'UN_code', 'q1', 'qid',3 ,row['country_un'], row['idnumber'], int(row['region']) , row['province']), axis=1)
del arab10_12
print('arab12 is done')

#counter = 1
afro11_13 = pd.read_csv(interimPath+"afro11_13_respondentsID_c.csv")
#afro11_13['RESPNO'] = afro11_13['Unnamed: 0'] + 1
gbs2['province'] =  gbs2.apply(lambda row: getProvince(afro11_13, 'UN_code', 'REGION', 'RESPNO',2 ,row['country_un'], row['Fixed_ID'], int(row['region']) , row['province']), axis=1)
del afro11_13
print('afro11_13 is done')

#counter = 1
latin13 = pd.read_csv(interimPath+"latin13_respondentsID_c.csv")
gbs2['province'] =  gbs2.apply(lambda row: getProvince(latin13, 'UN_code', 'reg', 'numentre', 5 ,row['country_un'], row['Fixed_ID'], int(row['region']) , row['province']), axis=1)
print("latin13 is done")

gbs2.to_csv(processedPath + "GBSII_provinces_added_0.1.csv")

for name, group in gbs2.groupby('region'):
    emp = group['province'].isnull().sum() / group.shape[0]
    print(str(name) + ": " + str(emp))
