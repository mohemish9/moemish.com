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



#def merge3(key,survey, waves, country, province, F063,Y003,F120,G006,E018,Y002,A008,E025,F118,A165,tradsec,survself):
#GBS1Dimentions.apply(lambda row: merge3(GBS1ProvinceList, row["region"], GBS1waves, row["country_un"],
#                                         row["province"], row["se10"], None, row["ge1"], row["cit2"],
#                                         row["sd5"], row["imp1_2_3"], row["ee1"], row["pp8"], None ,
#                                         row["sc1"], row["tradsec"], row["survself"]), axis=1)

def merge3(df):
    global data
    global GBS1ProvinceList
    global GBS1Data
    global provinceKey
    global miss
    global hit
    GBS1waves = {2:"gbs1.Afrobarometer.3",
                 3: "gbs1.Afrobarometer.4",
                 5: "gbs1.ArabBarometer.2",
                 6: "gbs1.Latinobarometer.2005",
                 7: "gbs1.Latinobarometer.2010"}
    key = GBS1ProvinceList
    questions = GBS1Data.columns
    #get location
    code = key.loc[(key["country_un"] == df["country_un"]) & (key["province"] == df["province"]) , 'new_subdivision_code']
    if not code.empty:
        if not (str(code.iloc[0]) == "nan" or str(code.iloc[0]) == "None"):
            code = code.unique()
            for r in range(len(code)):
                provinceCode = str(code[r])
                provinceInfo = provinceKey.loc[provinceKey["new_subdivision_code"] == provinceCode]
                info = provinceInfo.columns
                survey = df["region"]
                surveyTitle = GBS1waves[survey]
                data = data.append({'survey' : surveyTitle}, ignore_index=True)
                data.loc[data.shape[0]-1, "year"] = int(df['year'])
                hit = hit + 1
                for i in info:
                    if not provinceInfo[i].empty:
                        data.loc[data.shape[0]-1,i ] = provinceInfo[i].iloc[0]
                for question in questions:
                    #get row and loop over qestions
                    title = question.lower()
                    data.loc[data.shape[0]-1, title] = df[question]
    else:
        miss = miss + 1
        survey = df["region"]
        surveyTitle = GBS1waves[survey]
        data = data.append({'survey' : surveyTitle}, ignore_index=True)
        data.loc[data.shape[0]-1, "year"] = int(df['year'])
        prov = str(df['province'])
        coun = str(df['country_un'])
        if not prov == 'nan':
            data.loc[data.shape[0]-1, "ISO3166_2_c"] = prov
        data.loc[data.shape[0]-1, "ISO3166_OSN"] = coun
        for question in questions:
            #get row and loop over qestions
            title = question.lower()
            data.loc[data.shape[0]-1, title] = df[question]

"""def merge4(df):
    global data
    global GBS2ProvinceList
    global GBS2Data
    global provinceKey
    global miss
    global hit

    GBS2waves = {2: "gbs2.Afrobarometer.5",
                 3: "gbs2.ArabBarometer.3",
                 5: "gbs2.Latinobarometer.2013"}
    key = GBS2ProvinceList
    questions = GBS2Data.columns
    #get location
    code = key.loc[(key["country_un"] == df["country_un"]) & (key["province"] == df["province"]) , 'new_subdivision_code']
    if not code.empty:
        if not (str(code.iloc[0]) == "nan" or str(code.iloc[0]) == "None"):
            provinceCode = str(code.iloc[0])
            provinceInfo = provinceKey.loc[provinceKey["new_subdivision_code"] == provinceCode]
            info = provinceInfo.columns
            survey = df["region"]
            surveyTitle = GBS2waves[survey]
            data = data.append({'survey' : surveyTitle}, ignore_index=True)
            hit = hit + 1
            for i in info:
                if not provinceInfo[i].empty:
                    data.loc[data.shape[0]-1,i ] = provinceInfo[i].iloc[0]
            for question in questions:
                #get row and loop over qestions
                title = "GBS2" + "_" + question
                data.loc[data.shape[0]-1, title] = df[question]
    else:
        miss = miss + 1"""



data = pd.read_csv(processedPath + "master_longDataSet.0.0.4.csv", encoding = "ISO-8859-1")
provinceKey = pd.read_csv(interimPath + "master_dataset.0.0.1.csv", encoding = "ISO-8859-1")


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


GBS1ProvinceList = pd.read_csv(processedPath + "GBS_provinceList0.2.csv",encoding = "ISO-8859-1" )
#GBS2ProvinceList = pd.read_csv(processedPath + "GBSII_provinceList0.2.csv",encoding = "ISO-8859-1")
#print("keys opened")
#fix codes
provinceKey["new_subdivision_code"] = provinceKey["new_subdivision_code"].astype(str)
provinceKey["new_subdivision_code"] = provinceKey.apply(lambda row: fixCode(row['new_subdivision_code']), axis=1)

GBS1ProvinceList["new_subdivision_code"] = GBS1ProvinceList["new_subdivision_code"].astype(str)
GBS1ProvinceList["new_subdivision_code"] = GBS1ProvinceList.apply(lambda row: fixCode2(row['new_subdivision_code']), axis=1)

#GBS2ProvinceList["new_subdivision_code"] = GBS2ProvinceList["new_subdivision_code"].astype(str)
#GBS2ProvinceList["new_subdivision_code"] = GBS2ProvinceList.apply(lambda row: fixCode2(row['new_subdivision_code']), axis=1)


#read  datasets

GBS1Data = pd.read_csv(processedPath + "regional_dimensions_GBS.0.0.2.csv")
#GBS2Data = pd.read_csv(processedPath + "regional_dimensions_GBSII0.0.1.csv")
#print("datasets opened")

#merge datasets

GBS1Data.apply(merge3, axis=1)
print(miss / (miss+hit))

#reset counters
#miss = 0
#hit = 0

#GBS2Data.apply(merge4, axis=1)
#print(miss / (miss+hit))



data.to_csv(processedPath+"master_longDataSet.0.0.5.csv")