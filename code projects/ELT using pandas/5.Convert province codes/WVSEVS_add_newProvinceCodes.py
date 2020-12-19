import pandas as pd


# NOTE: don't run code since this wvs and evs were converted by members of the lab

rawPath = "/home/ec2-user/survey_project/data/raw/"
processedPath = "/home/ec2-user/survey_project/data/processed/"
interimPath = "/home/ec2-user/survey_project/data/interim/"


""" getProvince finds the province coressponding to a given ID and country in a certian DataFrame"""
def getProvince(df, countryLabel, provinceLabel, country, province, currentValue):
    cond = (df[countryLabel] == country) & ((df[provinceLabel] == province) | (df["Region"] == province))
    num = df.loc[cond , ['new_subdivision_code']]
    if not num.empty:
        return str(num.iloc[0]['new_subdivision_code'])
    return currentValue




data = pd.read_csv(processedPath + "regional_dimensions_all.0.0.2.csv")
data['new_subdivision_code'] = None

codes = pd.read_excel(processedPath + "merged_WVSEVS.xlsx")

data['new_subdivision_code'] = data.apply(lambda row: getProvince(codes,"S003", "X048_ALL", row['S003'], row['X048_ALL'], row['new_subdivision_code'] ), axis=1)

#data.to_csv(processedPath + "regional_dimensions_all.0.0.3.csv")

#data[['S003', 'X048_ALL', 'new_subdivision_code']].to_csv(processedPath + "regional_dimensions_all.test.csv")

emp = data['new_subdivision_code'].isnull().sum() / data.shape[0]
print(emp)
