
## Stage three: Dimensions Construction

#### Summary
Stage three is composed of **STATA code** which uses principal component analysis to construct Inglehart's dimensions on a provincial level
***
#### Files (in order they should be executed)
#### WVSEVS_Dimensions_Construction.do
__Description:__ This file creates unified variables to hold province names and type of survey, constructs Inglehart's dimensions for WVS and EVS, aggregates values of all questions on provincial level using arithmetic mean, creates dummy variables to hold categorical values (while accounting for weight of each individual), and counts number of people who took the survey at each province.

__Input files:__ WVS_Data_for_Factor_all.dta

__Output files:__ regional_dimensions_all.0.0.2.dta
***

#### WVSEVS_Dimensions_Construction_selectedQs.do
__Description:__ This file is a brief version of **WVSEVS_Dimensions_Construction.do**. It creates unified variables to hold province names and type of survey, constructs Inglehart's dimensions for WVS and EVS, aggregates values of only the questions used to construct Inglehart's dimensions on provincial level using arithmetic mean, and counts number of people who took the survey at each province.

__Input files:__ WVS_Data_for_Factor_all.dta

__Output files:__ regional_dimensions_all.0.0.2_selectedQs.dta
***
#### Americas_Dimensions_Construction.do
__Description:__ This file constructs Inglehart's dimensions for AmericasBarometer, aggregates values of all questions on provincial level using arithmetic mean, and creates dummy variables to hold categorical values (while accounting for weight of each individual).

__Input files:__ AmericasBarometer Grand Merge 2004-2014 v3.0_FREE.dta

__Output files:__ regional_dimensions_americas.0.0.3.dta
***
#### Americas_Dimensions_Construction_selectedQs.do
__Description:__  This file is a brief version of **Americas_Dimensions_Construction.do**. It  constructs Inglehart's dimensions for AmericasBarometer, aggregates values of only the questions used to construct Inglehart's dimensions on provincial level using arithmetic mean, and creates dummy variables to hold categorical values (while accounting for weight of each individual).

__Input files:__ AmericasBarometer Grand Merge 2004-2014 v3.0_FREE.dta

__Output files:__ regional_dimensions_americas_selectedQs.0.0.1.dta
***
#### Americas_make_setB.do
__Description:__ This file opens the file produced by Americas_Dimensions_Construction.do and keeps only provinces in which at least respondents have taken the survey.

__Input files:__ regional_dimensions_americas.0.0.3.dta

__Output files:__ regional_dimensions_americas.0.0.4.dta, regional_dimensions_americas.0.0.4.csv
***
#### Americas_selectedQs_make_setB.do
__Description:__ This file opens the file produced by Americas_Dimensions_Construction_selectedQs.do and keeps only provinces in which at least respondents have taken the survey.

__Input files:__ regional_dimensions_americas_selectedQs.0.0.1.dta

__Output files:__ regional_dimensions_americas_selectedQs.0.0.2.dta, regional_dimensions_americas_selectedQs.0.0.2.csv
***
#### Americas_impute.r and Americas_selectedqs_impute.r
__Description:__ These files contain **R code** that uses spline regression method (na_interpolate() function from https://cran.r-project.org/web/packages/imputeTS/imputeTS.pdf) to predict missing values in of the questions used to construct Inglehart's dimensions. The first file works on the csv file produced by **Americas_make_setB.do** and the second file work on the csv file produced by **Americas_selectedQs_make_setB.do**

__Input files:__ regional_dimensions_americas.0.0.3.csv and regional_dimensions_americas_selectedQs.0.0.2.csv respectively

__Output files:__ regional_dimensions_americas_imputed.0.0.1.csv and regional_dimensions_americas_selectedQs_imputed.0.0.2.csv respectively
***
#### Americas_Dimensions_Construction_master_afterimputation.do
__Description:__ This file constructs Inglehart's dimensions for Americas baromenter after values of the questions have been imputed by **Americas_impute.r**

__Input files:__ regional_dimensions_americas_imputed.0.0.1.csv

__Output files:__ regional_dimensions_americas_imputed.0.0.2.csv
***

#### Americas_Dimensions_Construction_afterimputation.do
__Description:__ This file constructs Inglehart's dimensions for Americas baromenter after values of the questions have been imputed by **Americas_selectedqs_impute.r**

__Input files:__ regional_dimensions_americas_selectedQs_imputed.0.0.1.dta

__Output files:__ regional_dimensions_americas_selectedQs_imputed.0.0.2.dta

***
#### GBS_Dimensions_Construction.do
__Description:__ This file constructs Inglehart's dimensions for GBS I, aggregates values of all questions on provincial level using arithmetic mean, and creates dummy variables to hold categorical values (while accounting for weight of each individual).

__Input files:__ GBS_provinces_added_0.2.dta  (same file as GBS_provinces_added_0.1.csv after respondents with unknow locations where dropped)

__Output files:__ regional_dimensions_GBS.0.0.2.dta
***
#### GBS_Dimensions_Construction_selectedQs.do
__Description:__ This file is a brief version of **GBS_Dimensions_Construction.do**. It  constructs Inglehart's dimensions for GBS I, aggregates values of only the questions used to construct Inglehart's dimensions on provincial level using arithmetic mean, and creates dummy variables to hold categorical values (while accounting for weight of each individual).

__Input files:__ GBS_provinces_added_0.2.dta  (same file as GBS_provinces_added_0.1.csv after respondents with unknow locations where dropped)

__Output files:__ regional_dimensions_GBS_selectedQs.0.0.3.dta
***
#### GBSII_Dimensions_Construction.do
__Description:__ This file constructs Inglehart's dimensions for GBS II, aggregates values of all questions on provincial level using arithmetic mean, and creates dummy variables to hold categorical values (while accounting for weight of each individual).

__Input files:__ GBSII_provinces_added_0.3.dta  (same file as GBSII_provinces_added_0.2.csv after respondents with unknow locations where dropped)

__Output files:__ regional_dimensions_GBSII0.0.1.dta
***
#### GBSII_Dimensions_Construction_selectedQs.do
__Description:__ This file is a brief version of **GBSII_Dimensions_Construction.do**. It  constructs Inglehart's dimensions for GBS II, aggregates values of only the questions used to construct Inglehart's dimensions on provincial level using arithmetic mean, and creates dummy variables to hold categorical values (while accounting for weight of each individual).

__Input files:__ GBSII_provinces_added_0.3.dta (same file as GBSII_provinces_added_0.2.csv after respondents with unknow locations where dropped)

__Output files:__ regional_dimensions_GBSII_selectedqs.0.0.1.dta

