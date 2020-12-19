import pandas as pd

def getProvinceCode(countryNum, provinceNum):
    if (not pd.isnull(countryNum)) and (not pd.isnull(countryNum)):
        return str(countryNum)[0:4] + ('0' * (3-len(str(provinceNum)))) + str(provinceNum)
    return None


df = pd.read_csv('/home/ec2-user/survey_project/data/interim/provinceList0.0.7.csv')
df['province_number'] = df.groupby('country_number').country_number.cumcount() + 1
df['subdivision_ID'] = df.apply(lambda row : getProvinceCode(row['ID'], row['province_number']),axis=1)
df.drop('province_number', axis=1)
print(df)
df.to_csv('/home/ec2-user/survey_project/data/processed/provinceList_WVSEVS0.0.9.csv')
