import pandas as pd
import iso3166

def getName(country):
    if not pd.isnull(country):
        return iso3166.countries.get(country).name
    return None

def getNumber(country):
    if not pd.isnull(country):
        return str(iso3166.countries.get(country).numeric)
    return None

def getProvinceCode(countryNum, provinceNum):
    if (not pd.isnull(countryNum)) and (not pd.isnull(countryNum)):
        return str(countryNum) + ('0' * (3-len(str(provinceNum)))) + str(provinceNum)
    return None

df = pd.read_csv('/home/ec2-user/survey_project/data/external/IP2LOCATION-ISO3166-2.CSV')
df['country_name'] = df['country_code'].apply(getName)
df['country_number'] = df['country_code'].apply(getNumber)
df['province_number'] = df.groupby('country_number').country_number.cumcount() + 1
df['subdivision_code'] = df.apply(lambda row : getProvinceCode(row['country_number'], row['province_number']),axis=1)
df.drop(['province_number'], axis=1)
df.rename(columns={'code':'ISO3166_code'}, inplace=True)
df = df[['country_name','country_code', 'subdivision_name' ,'ISO3166_code','country_number','subdivision_code']]
df['country_number'] = df['country_number'].astype('str')
df['subdivision_code'] = df['subdivision_code'].astype('str')
df.to_csv('/home/ec2-user/survey_project/data/processed/provinceList_WVSEVS0.0.6.csv')
