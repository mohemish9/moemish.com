import pandas as pd


rawPath = "/home/ec2-user/survey_project/data/raw/"
processedPath = "/home/ec2-user/survey_project/data/processed/"
interimPath = "/home/ec2-user/survey_project/data/interim/"


""" getProvince finds the province coressponding to a given ID and country in a certian DataFrame"""
def getProvince(df, countryLabel, provinceLabel, country, province, currentValue):
    cond = (df[countryLabel] == country) & (df[provinceLabel] == province)
    num = df.loc[cond , ['new_subdivision_code']]
    if not num.empty:
        return str(num.iloc[0]['new_subdivision_code'])
    return currentValue


def cleanCountry(country):
    if ": " in country:
        return country.split(": ",1)[1]
    else:
        return country

def cleanCountry2(country):
    if "/" in country:
        return country.split("/",1)[1]
    else:
        return country

data = pd.read_csv(processedPath + "GBS_provinceList.csv")
data['new_subdivision_code'] = None
data['province_e'] = data['province']
codes = pd.read_excel(processedPath + "provinceList0.1.1.xlsx", sheet_name=1)


data['province_e'] = data.apply(lambda row: cleanCountry(row['province_e']), axis=1)
data['province_e'] = data.apply(lambda row: cleanCountry2(row['province_e']), axis=1)
data['new_subdivision_code'] = data.apply(lambda row: getProvince(codes,"ISO3166_OSN", "ISO3166_2_c", row['Country name'], row['province_e'], row['new_subdivision_code'] ), axis=1)

data.to_csv(processedPath + "GBS_provinceList0.2.csv")

emp = data['new_subdivision_code'].isnull().sum() / data.shape[0]
print(emp)
