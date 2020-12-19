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


data = pd.read_csv(processedPath + "Americans_provinceList.0.2csv.csv")
data['new_subdivision_code'] = None

codes = pd.read_excel(processedPath + "provinceList0.1.1.xlsx", sheet_name=1)

data['new_subdivision_code'] = data.apply(lambda row: getProvince(codes,"ISO3166_OSN", "ISO3166_2_c", row['pais_e'], row['prov_e'], row['new_subdivision_code'] ), axis=1)

data.to_csv(processedPath + "Americans_provinceList.0.3.csv")
