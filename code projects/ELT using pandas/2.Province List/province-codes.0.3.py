import pandas as pd
import iso3166



def getName(country):
    if not pd.isnull(country):
        try:
            return iso3166.countries.get(country).numeric
        except:
            print( country + " not found")
            return None
    return None

df = pd.read_csv('/home/ec2-user/survey_project/data/external/new_country_code.csv')
df['country_code'] = df['country'].apply(getName)
df['country_code'] = df['country_code'].astype('str')

#df.to_csv('/home/ec2-user/survey_project/data/processed/provinceList0.0.7.csv')

def getID(country):
    num = df.loc[df['country_code'] == country, 'ID']
    if not num.empty:
        return str(num.iloc[0])
    return None

data = pd.read_csv('/home/ec2-user/survey_project/data/processed/provinceList_WVSEVS0.0.6.csv')
data['ID'] = data.apply(lambda row: getID(row['country_number']), axis = 1)
data.to_csv('/home/ec2-user/survey_project/data/interim/provinceList0.0.7.csv')
