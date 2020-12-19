import pandas as pd

rawPath = "/home/ec2-user/survey_project/data/raw/"
processedPath = "/home/ec2-user/survey_project/data/processed/"
interimPath = "/home/ec2-user/survey_project/data/interim/"

#init miss and hit counters
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


def merge2(df):
    global data
    global americasProvinceList
    global americasData
    global provinceKey
    global hit, miss

    key = americasProvinceList
    questions = americasData.columns
    #get location
    code = key.loc[(key["pais"] == df["pais"]) & (key["prov"] == df['prov']) , 'new_subdivision_code']
    if not code.empty:
        if not (str(code.iloc[0]) == "nan" or str(code.iloc[0]) == "None"):
            code = code.unique()
            for r in range(len(code)):
                hit = hit + 1
                provinceCode = str(code[r])
                provinceInfo = provinceKey.loc[provinceKey["new_subdivision_code"] == provinceCode]
                info = provinceInfo.columns
                surveyTitle = "americas.barometer" + "_"+ str(df["wave"])
                data = data.append({'survey' : surveyTitle}, ignore_index=True)
                data.loc[data.shape[0]-1, "year"] = int(df['year'])
                for i in info:
                    if not provinceInfo[i].empty:
                        data.loc[data.shape[0]-1,i ] = provinceInfo[i].iloc[0]
                for question in questions:
                    #get row and loop over qestions
                    title = question.lower()
                    data.loc[data.shape[0]-1, title] = df[question]
    else:
        miss = miss + 1
        surveyTitle = "americas.barometer" + "_"+ str(df["wave"])
        data = data.append({'survey' : surveyTitle}, ignore_index=True)
        data.loc[data.shape[0]-1, "year"] = int(df['year'])
        prov = str(df['prov']).split(". ",1)
        coun = str(df['pais']).split(". ",1)
        if not prov[len(prov)-1] == 'nan':
            data.loc[data.shape[0]-1, "ISO3166_2_c"] = prov[len(prov)-1]
        data.loc[data.shape[0]-1, "ISO3166_OSN"] = coun[len(coun)-1]
        for question in questions:
            #get row and loop over qestions
            title = question.lower()
            data.loc[data.shape[0]-1, title] = df[question]

data = pd.read_csv(processedPath + "master_longDataSet.0.0.3.csv", encoding = "ISO-8859-1")


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
americasProvinceList = pd.read_csv(processedPath + "Americans_provinceList.0.3.csv",encoding = "ISO-8859-1" )
provinceKey = pd.read_csv(interimPath + "master_dataset.0.0.1.csv", encoding = "ISO-8859-1")

#fix codes
provinceKey["new_subdivision_code"] = provinceKey["new_subdivision_code"].astype(str)
provinceKey["new_subdivision_code"] = provinceKey.apply(lambda row: fixCode(row['new_subdivision_code']), axis=1)

americasProvinceList["new_subdivision_code"] = americasProvinceList["new_subdivision_code"].astype(str)
americasProvinceList["new_subdivision_code"] = americasProvinceList.apply(lambda row: fixCode2(row['new_subdivision_code']), axis=1)



#read  datasets

americasData = pd.read_csv(processedPath + "regional_dimensions_americas_imputed.0.0.2.csv",encoding = "ISO-8859-1")

#merge datasets

americasData.apply(merge2, axis=1)
print(miss / (miss+hit))
print(len(data.columns))
data.to_csv(processedPath+"master_longDataSet.0.0.4.csv")
