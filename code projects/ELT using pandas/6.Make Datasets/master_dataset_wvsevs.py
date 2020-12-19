import pandas as pd

rawPath = "/home/ec2-user/survey_project/data/raw/"
processedPath = "/home/ec2-user/survey_project/data/processed/"
interimPath = "/home/ec2-user/survey_project/data/interim/"

#miss and hit counter
miss = 0
hit = 0

#define helper functions

def fixCode(code):
    if (str(code) != "nan") and (str(code) != "None") and len(str(code)) < 6:
        dif = 6 - len(str(code))
        return ("0" * dif) + str(code)
    else:
        return code

def fixCode2(code):
    if "." in code:
        code = code.split(".",1)[0]
    if (str(code) != "nan") and len(str(code)) < 6:
        dif = 6 - len(str(code))
        return ("0" * dif) + str(code)
    else:
        return code


def merge1(df):
    global data
    global wvsEvsProvinceList
    global wvsEvsData
    global miss
    global hit

    key = wvsEvsProvinceList
    questions = wvsEvsData.columns
    #get location
    code = key.loc[(key["S003"] == df["S003"]) & (key["X048_ALL"] == df["X048_ALL"]) , 'new_subdivision_code']
    if not code.empty:
        if not (str(code.iloc[0]) == "nan" and str(code.iloc[0]) == "None"):
            provinceCode = str(code.iloc[0])
            hit = hit + 1
            for question in questions:
                #get row and loop over qestions
                survey = df["S001"]
                wave = df["S002_ALL"]
                title = question + "." + survey[-3:] + "."+ wave[0]
                data.loc[data['new_subdivision_code'] == provinceCode, title] = df[question]
    else:
        miss = miss + 1

data = pd.read_csv(processedPath + "master_dataset.0.0.2.csv", encoding = "ISO-8859-1")


surveys = {"wvs":[1,2,3,4,5,6],
            "evs":[1,2,3,4],
            "americas.barometer": [2004,2006,2008,2010,2012,2014],
            "gbs1.Afrobarometer": [3,4],
            "gbs2.Afrobarometer":[5],
            "gbs1.ArabBarometer": [2],
            "gbs2.ArabBarometer": [3],
            "gbs1.Latinobarometer": [2005,2010],
            "gbs2.Latinobarometer": [2013]}


#read province list keys
wvsEvsProvinceList = pd.read_csv(processedPath + "merged_WVSEVS0.3.csv",encoding = "ISO-8859-1")


#fix codes
data["new_subdivision_code"] = data["new_subdivision_code"].astype(str)
data["new_subdivision_code"] = data.apply(lambda row: fixCode(row['new_subdivision_code']), axis=1)

wvsEvsProvinceList["new_subdivision_code"] = wvsEvsProvinceList["new_subdivision_code"].astype(str)
wvsEvsProvinceList["new_subdivision_code"] = wvsEvsProvinceList.apply(lambda row: fixCode(row['new_subdivision_code']), axis=1)


#read datasets
wvsEvsData = pd.read_csv(processedPath + "regional_dimensions_all.0.0.3.csv")


#merge datasets
wvsEvsData.apply(merge1,axis=1)


data.to_csv(processedPath+ "master_dataset.0.0.3.csv")


print(miss / (miss+hit))
