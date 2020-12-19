import pandas as pd
#from tqdm import tqdm

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

count = 0
def merge1(df):
    global data
    global wvsEvsProvinceList
    global wvsEvsData
    global provinceKey
    global miss
    global hit
    global count
    count = count +1
    print(count)
    key = wvsEvsProvinceList
    questions = wvsEvsData.columns

    #get location
    code = key.loc[(key["S003"] == df["S003"]) & (key["X048_ALL"] == df["X048_ALL"]) , 'new_subdivision_code']
    if not code.empty:
        if not (str(code.iloc[0]) == "nan" or str(code.iloc[0]) == "None"):
            code = code.unique()
            for r in range(len(code)):
                provinceCode = str(code[r])
                provinceInfo = provinceKey.loc[provinceKey["new_subdivision_code"] == provinceCode]
                info = provinceInfo.columns
                hit = hit + 1
                survey = df["S001"]
                wave = df["S002_ALL"]
                surveyTitle = survey[-3:] + "_"+ wave[0]
                data = data.append({'survey' : surveyTitle}, ignore_index=True)
                data.loc[data.shape[0]-1, "year"] = int(df['S020'][:4])
                for i in info:
                    if not provinceInfo[i].empty:
                        data.loc[data.shape[0]-1,i] = provinceInfo[i].iloc[0]
                for question in questions:
                    #get row and loop over qestions
                    title = question.lower()
                    data.loc[data.shape[0]-1, title] = df[question]
    else:
        miss = miss + 1
        survey = df["S001"]
        wave = df["S002_ALL"]
        surveyTitle = survey[-3:] + "_"+ wave[0]
        data = data.append({'survey' : surveyTitle}, ignore_index=True)
        data.loc[data.shape[0]-1, "year"] = int(df['S020'][:4])
        prov = str(df['X048_ALL']).split(". ",1)
        coun = str(df['S003']).split(". ",1)
        if not prov[len(prov)-1] == 'nan':
            data.loc[data.shape[0]-1, "ISO3166_2_c"] = prov[len(prov)-1]
        data.loc[data.shape[0]-1, "ISO3166_OSN"] = coun[len(coun)-1]
        for question in questions:
            #get row and loop over qestions
            title = question.lower()
            data.loc[data.shape[0]-1, title] = df[question]

data = pd.read_csv(processedPath + "master_longDataSet.0.0.2.csv")


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
provinceKey = pd.read_csv(interimPath + "master_dataset.0.0.1.csv", encoding = "ISO-8859-1")


#fix codes
provinceKey["new_subdivision_code"] = provinceKey["new_subdivision_code"].astype(str)
provinceKey["new_subdivision_code"] = provinceKey.apply(lambda row: fixCode(row['new_subdivision_code']), axis=1)

wvsEvsProvinceList["new_subdivision_code"] = wvsEvsProvinceList["new_subdivision_code"].astype(str)
wvsEvsProvinceList["new_subdivision_code"] = wvsEvsProvinceList.apply(lambda row: fixCode(row['new_subdivision_code']), axis=1)


#read datasets
wvsEvsData = pd.read_csv(processedPath + "regional_dimensions_all.0.0.3.csv")

print(data.shape)
#merge datasets
wvsEvsData.apply(merge1,axis=1)
print(data.shape)

data.to_csv(processedPath+ "master_longDataSet.0.0.3.csv")
#data = data.drop("Unnamed: 5",axis=1)

print(miss / (miss+hit))
