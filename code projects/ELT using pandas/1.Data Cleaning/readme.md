## Stage one: Data cleaning

#### Summary
In stage one, data files are converted into CSV format for later use. In addition, province names are extracted from original survey files and attached to the GBS files.

***

#### Files (in order they should be executed)

#### get_gbs_provinces.py
__Description:__ Reads the original survey (Afrobaromenter 3, Afrobaromenter 4, Arab Baromometer 2, Latinobarometer 2005 and LatinBarometer 2010) data files and stores survey respondents ID, country and provinces in **interim files**.

__Input files:__  afro_merged_r3_data.sav, afro_merged_r4_data.sav, ABII_English.dta, Latinobarometro_2005_datos_eng_v2014_06_27.dta, Latinobarometro_2010_datos_eng_v2014_06_27.dta

__Output files:__ afro05_respondentsID.csv, afro08_respondentsID.csv, arab10_respondentsID.csv, latin05_respondentsID.csv, latin10_respondentsID.csv
***
#### get_gbsII_provinces.py
__Description:__ Reads the original survey (Afrobaromenter 5, Arab Baromometer 3, and LatinBarometer 2013) data files and stores survey respondents ID, country and provinces in **interim files**.
***
__Input files:__ afro_merged-round-5-data-34-countries-2011-2013-last-update-july-2015.sav, Latinobarometro2013Eng.dta, ABIII_English.csv

__Output files:__ afro11_13_respondentsID, latin13_respondentsID arab10_12_respondentsID.csv

***
#### get_gbsII_F006.py
__Description:__ Reads the original survey (Afrobaromenter 5, Arab Baromometer 3, and LatinBarometer 2013) data files and stores questions of interest (those chosen to replace F006) in **interim files**.

__Input files:__ afro_merged-round-5-data-34-countries-2011-2013-last-update-july-2015.sav, Latinobarometro2013Eng.dta, ABIII_English.dta

__Output files:__ afro11_13_F006.csv, latin13_F006.csv, arab10_12_F006.csv
***
#### clean_gbs_provinces.py
__Description:__ Reads the files from **get_gbs_provinces.py** to append country names and fixes IDs and saves them in **interim files**

__Input files:__ afro05_respondentsID.csv, afro08_respondentsID.csv, arab10_respondentsID.csv, latin05_respondentsID.csv, latin10_respondentsID.csv

__Output files:__ afro05_respondentsID_c.csv, afro08_respondentsID_c.csv, arab10_respondentsID_c.csv, latin05_respondentsID_c.csv, latin10_respondentsID_c.csv
***
#### clean_gbsII_provinces.py
__Description:__ Reads the files from **get_gbsII_provinces.py** to append country names and fixes IDs and saves them in **interim files**

__Input files:__ arab10_12_respondentsID.csv, afro11_13_respondentsID.csv, latin13_respondentsID.csv

__Output files:__ arab11_13_respondentsID_c.csv, afro11_13_respondentsID_c.csv, latin13_respondentsID_c.csv
***
#### clean_gbsII_F006.py
__Description:__ Reads the files from **get_gbsII_F006.py** to append country names and fixes IDs and saves them in **interim files**  

__Input files:__ arab10_12_F006.csv, afro11_13_F006.csv, latin13_F006.csv

__Output files:__ arab10_12_F006_c.csv, afro11_13_F006_c.csv, latin13_F006_c.csv
***
#### merge_gbs_provinces.py
__Description:__ Reads files from **clean_gbs_provinces.py** and merges them to the original GBS I survey data file.

__Input files:__ afro05_respondentsID_c.csv, afro08_respondentsID_c.csv, arab10_respondentsID_c.csv, latin05_respondentsID_c.csv, latin10_respondentsID_c.csv

__Output files:__ GBS_provinces_added_0.1.csv
***
#### merge_gbsII_provinces.py
__Description:__ Reads files from **clean_gbsII_provinces.py** and merges them to the original GBS I survey data file.

__Input files:__ arab11_13_respondentsID_c.csv, afro11_13_respondentsID_c.csv, latin13_respondentsID_c.csv

__Output files:__ GBSII_provinces_added_0.1.csv
***

#### merge_gbsII_addF006.py
__Description:__ Reads files from **clean_gbsII_F006.py** and its contents merges them to the original GBS I survey data file.

__Input files:__ arab10_12_F006.csv, afro11_13_F006.csv, latin13_F006.csv

__Output files:__ GBSII_provinces_added_0.2.csv

