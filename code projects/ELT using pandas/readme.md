# File descriptions


## Stage one: Data cleaning

#### Summary
In stage one, data files are converted into CSV format for later use. In addition, province names are extracted from original survey files and attached to the GBS files.

#### Files (in order they should be executed)

#### get_gbs_provinces.py
__Description:__ Reads the original survey (Afrobaromenter 3, Afrobaromenter 4, Arab Baromometer 2, Latinobarometer 2005 and LatinBarometer 2010) data files and stores survey respondents ID, country and provinces in **interim files**.

#### get_gbsII_provinces.py
__Description:__ Reads the original survey (Afrobaromenter 5, Arab Baromometer 3, and LatinBarometer 2013) data files and stores survey respondents ID, country and provinces in **interim files**.

#### get_gbsII_F006.py
__Description:__ Reads the original survey (Afrobaromenter 5, Arab Baromometer 3, and LatinBarometer 2013) data files and stores questions of interest (those chosen to replace F006) in **interim files**.

#### clean_gbs_provinces.py
__Description:__ Reads the files from **get_gbs_provinces.py** to append country names and fixes IDs and saves them in **interim files**

#### clean_gbsII_provinces.py
__Description:__ Reads the files from **get_gbsII_provinces.py** to append country names and fixes IDs and saves them in **interim files**

#### clean_gbsII_F006.py
__Description:__ Reads the files from **get_gbsII_F006.py** to append country names and fixes IDs and saves them in **interim files**  

#### merge_gbs_provinces.py
__Description:__ Reads files from **clean_gbs_provinces.py** and merges them to the original GBS I survey data file.

#### merge_gbsII_provinces.py
__Description:__ Reads files from **clean_gbsII_provinces.py** and merges them to the original GBS I survey data file.

#### merge_gbsII_addF006.py
__Description:__ Reads files from **clean_gbsII_F006.py** and its contents merges them to the original GBS I survey data file.

***
## Stage two: Making Province List

#### Summary
Stage two constructs a list of provinces (subdivisions) of countries around the world with unified codes. Province codes are constructed using ISO3166-2 codes and they are used for merge.

#### Files (in order they should be executed)
#### province-codes.0.2.py
__Description:__ Opens provinces list, appends iso3166 country code to each country, then constructs province codes by appending a 3 digit cumulative number to the Is03166 code of the country the province belongs to.

#### province-codes.0.3.py
__Description:__ Opens the file produced by **province-codes.0.2.py** and appends Professor Fing's Country codes.

#### province-codes.0.4.py
__Description:__ Opens the file produced by **province-codes.0.3.py** and constructs province codes by appending a 3 digit cumulative number to the Is03166 code of the country the province belongs to.

***
## Stage three: Dimensions Construction

#### Summary
Stage three is composed of **STATA code** which uses principal component analysis to construct Inglehart's dimensions on a provincial level

#### Files (in order they should be executed)
#### WVSEVS_Dimensions_Construction.do
__Description:__ This file creates unified variables to hold province names and type of survey, constructs Inglehart's dimensions for WVS and EVS, aggregates values of all questions on provincial level using arithmetic mean, creates dummy variables to hold categorical values (while accounting for weight of each individual), and counts number of people who took the survey at each province.

#### WVSEVS_Dimensions_Construction_selectedQs.do
__Description:__ This file is a brief version of **WVSEVS_Dimensions_Construction.do**. It creates unified variables to hold province names and type of survey, constructs Inglehart's dimensions for WVS and EVS, aggregates values of only the questions used to construct Inglehart's dimensions on provincial level using arithmetic mean, and counts number of people who took the survey at each province.

#### Americas_Dimensions_Construction.do
__Description:__ This file constructs Inglehart's dimensions for AmericasBarometer, aggregates values of all questions on provincial level using arithmetic mean, and creates dummy variables to hold categorical values (while accounting for weight of each individual).

#### Americas_Dimensions_Construction_selectedQs.do
__Description:__  This file is a brief version of **Americas_Dimensions_Construction.do**. It  constructs Inglehart's dimensions for AmericasBarometer, aggregates values of only the questions used to construct Inglehart's dimensions on provincial level using arithmetic mean, and creates dummy variables to hold categorical values (while accounting for weight of each individual).

#### Americas_make_setB.do
__Description:__ This file opens the file produced by Americas_Dimensions_Construction.do and keeps only provinces in which at least respondents have taken the survey.

#### Americas_selectedQs_make_setB.do
__Description:__ This file opens the file produced by Americas_Dimensions_Construction_selectedQs.do and keeps only provinces in which at least respondents have taken the survey.

#### Americas_impute.r and Americas_selectedqs_impute.r
__Description:__ These files contain **R code** that uses spline regression method (na_interpolate() function from https://cran.r-project.org/web/packages/imputeTS/imputeTS.pdf) to predict missing values in of the questions used to construct Inglehart's dimensions. The first file works on the csv file produced by **Americas_make_setB.do** and the second file work on the csv file produced by **Americas_selectedQs_make_setB.do**

#### Americas_Dimensions_Construction_master_afterimputation.do
__Description:__ This file constructs Inglehart's dimensions for Americas baromenter after values of the questions have been imputed by **Americas_impute.r**

#### Americas_Dimensions_Construction_afterimputation.do
__Description:__ This file constructs Inglehart's dimensions for Americas baromenter after values of the questions have been imputed by **Americas_selectedqs_impute.r**

#### GBS_Dimensions_Construction.do
__Description:__ This file constructs Inglehart's dimensions for GBS I, aggregates values of all questions on provincial level using arithmetic mean, and creates dummy variables to hold categorical values (while accounting for weight of each individual).

#### GBS_Dimensions_Construction_selectedQs.do
__Description:__ This file is a brief version of **GBS_Dimensions_Construction.do**. It  constructs Inglehart's dimensions for GBS I, aggregates values of only the questions used to construct Inglehart's dimensions on provincial level using arithmetic mean, and creates dummy variables to hold categorical values (while accounting for weight of each individual).

#### GBSII_Dimensions_Construction.do
__Description:__ This file constructs Inglehart's dimensions for GBS II, aggregates values of all questions on provincial level using arithmetic mean, and creates dummy variables to hold categorical values (while accounting for weight of each individual).

#### GBSII_Dimensions_Construction_selectedQs.do
__Description:__ This file is a brief version of **GBSII_Dimensions_Construction.do**. It  constructs Inglehart's dimensions for GBS II, aggregates values of only the questions used to construct Inglehart's dimensions on provincial level using arithmetic mean, and creates dummy variables to hold categorical values (while accounting for weight of each individual).

****
## Stage four: Rendering reports

#### Summary
Stage five produces tables containing summaries of the data produced by stage three. This tables are used in the codebooks of the new datasets.

#### Files (in order they should be executed)

#### province_list.do
__Description:__ This file reads file produced by **WVSEVS_Dimensions_Construction.do** and produces a list of unique provinces and country names.

#### province-codes.py
__Description:__ This file reads file produced by **province_list.do** and cleans names of provinces.

#### Americas_report.py
__Description:__ This file reads file produced by **Americas_Dimensions_Construction_afterimputation.do** and produces tables containing titles of the questions, a list of waves, list of countries and how many provinces each country includes, list of provinces that doesn't have enough data to construct Inglehart's dimensions, and a list of unique provinces and country names.

#### GBS_report.py (optional)
__Description:__ This file reads file produced by **GBS_Dimensions_Construction_selectedQs.do** and produces tables containing titles of the questions, a list of waves, list of countries and how many provinces each country includes, and a list of provinces that doesn't have enough data to construct Inglehart's dimensions

#### GBS_provincelist.py
__Description:__ This file reads file produced by **GBS_Dimensions_Construction_selectedQs.do** and produces a list of unique provinces and country names.

#### GBSII_report.py (optional)
__Description:__ This file reads file produced by **GBSII_Dimensions_Construction_selectedQs.do** and produces tables containing titles of the questions, a list of waves, list of countries and how many provinces each country includes, and a list of provinces that doesn't have enough data to construct Inglehart's dimensions

#### GBSII_provincelist.py
__Description:__ This file reads file produced by **GBSII_Dimensions_Construction_selectedQs.do** produces a list of unique provinces and country names.

****
## Stage five: Convert province codes

#### Summary
Stage five constructs a list containing the unique names of country and province codes, the ones produced by stage four, and matches = them with the new province codes constructed in stage two.

#### Files (in order they should be executed)
#### WVSEVS_add_newProvinceCodes.py (optional)
__Description:__ Note that the list of province names matched with the new province codes was created manually, so this code doesn't produce any new files.

#### Americas_make_newProvinceCodes.py
__Description:__ This file opens the files produced by **Americas_report.py** and **province-codes.0.4.py** to match the province list produced by the first to the new codes produced by the latter.

#### GBS_make_newProvinceCodes.py
__Description:__ This file opens the files produced by **GBS_provincelist.py** and **province-codes.0.4.py** to match the province list produced by the first to the new codes produced by the latter. **Note:** the final file produced by this code is edited manually to add province codes for provinces that where encoded using different names from the standard ISO 3166-2. Save output files before rerunning this code.

#### GBSII_make_newProvinceCodes.py
__Description:__ This file opens the files produced by **GBSII_provincelist.py** and **province-codes.0.4.py** to match the province list produced by the first to the new codes produced by the latter. **Note:** the final file produced by this code is edited manually to add province codes for provinces that where encoded using different names from the standard ISO 3166-2. Save output files before rerunning this code.

****
## Stage six: Making Datasets

#### Summary
Stage six merges the files from stage three into 2 files, one containing the files that includes all questions (master dataset) and the other contains files that includes Inglehart's dimensions and the questions used to construct them.

#### Files (in order they should be executed)
#### selectedQs_dataset.py
__Description:__ This file merges the files produced by stage three that contains the selected questions and the Inglehart dimensions. The merge is done by using the files created in stage five to match the old names from the original survey  Each file in the row holds all the records of a province. Each column after the province name and code holds the values of a give question. Names of questions are put into the following format : *QuestionsName* _ *SurveyName* _ *WaveNumber*  

#### selectedQs_longDataset.py
__Description:__ This file merges the files produced by stage three that contains the selected questions and the Inglehart dimensions in a long format. The merge is done by using the files created in stage five to match the old names from the original survey. Columns of the long dataset contain the values of one question from across all surveys

#### master_longDataSet_columns.py
__Description:__ This file creates the columns of the master dataset. Each column, after the province name and code, holds the values of a give question. Names of questions are put into the following format : *SurveyName* _ *QuestionsName* . Moreover, it adds a column called *survey* which stores the name of the survey and the wave.

#### master_longDataset_wvsevs.py
__Description:__ This file open the WVS-EVS files produced in stage three which contains all the questions. It adds the new province code of each province and then adds and merges the values with the file from **master_longDataSet_columns.py** in a long format.

#### master_longDataset_gbs.py
__Description:__ This file open the GBS I and GBS II files produced in stage three which contains all the questions. It adds the new province code of each province and then adds and merges the values with the file from **master_longDataset_wvsevs.py** in a long format.

#### master_longDataset_americas.py
__Description:__ This file open the Americas files produced in stage three which contains all the questions. It adds the new province code of each province and then adds and merges the values with the file from **master_longDataset_gbs.py** in a long format.

#### drop_empty_columns.py
__Description:__ This file open opens the file produced by **master_longDataset_americas.py** and drops columns that are completely empty.

#### master_dataset_columns.py (optional)
__Description:__ This file merges the files produced by stage three that contains all the questions. The merge is done by using the files created in stage five to match the old names from the original survey  Each file in the row holds all the records of a province. Each column after the province name and code holds the values of a give question. Names of questions are put into the following format : *SurveyName* _ *QuestionsName*

#### master_dataset_wvsevs.py (optional)
__Description:__ This file open the WVS-EVS files produced in stage three which contains all the questions. It merges the values with the file from **master_datataSet_columns.py** in a long format.

#### master_dataset_gbs.py (optional)
__Description:__ This file open the GBS I and GBS II files produced in stage three which contains all the questions. It merges the values with the file from **master_dataset_wvsevs.py** in a long format.

#### master_dataset_americas.py (optional)
__Description:__ This file open the Americas files produced in stage three which contains all the questions. It merges the values with the file from **master_dataset_gbs.py** in a long format.

***

## Stage seven: Create Database

#### Summary
In stage seven, Mongo database is initialized, and the datasets from stage six are uploaded to Mongo Server.

#### Files (in order they should be executed)
#### create_database.js
The code in this file initialize the Database on mongo server, creates two collections (one for master dataset and another for selected questions) and then uploads **selectedQs_dataset.0.0.2.csv** and **master_longDataSet.0.0.6.csv** into these collections respectively.

#### selectedQs.sql
This file contains the code to create a SQL Database and table for the selected questions. .
