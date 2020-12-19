clear
cd "/home/ec2-user/survey_project/data/raw"
* for all cases including EVS longitudnal:
use WVS_Data_for_Factor_all, replace

* No EVS longitundal
* use WVSLongitudnal.dta, replace

*Insrtuctions to construct WVS Indices:
*label dir
*numlabel `r(names)', add

* select and clean all numeric variables

*local vars_ALL `ds, has(type numeric)'
*local omit Y003
*local vars: list vars_ALL - omit

*foreach var of varlist `vars' {
*  replace `var' = .  if `var' < 0
*  replace `var' = .  if `var' == .n
*}

*merge S002 and S002EVS into S002ALL
decode S002, generate(S002_STR)
decode S002EVS, generate(S002EVS_STR)
gen S002_ALL_STR = S002_STR if S002_STR != ""
replace S002_ALL_STR = S002EVS_STR if S002EVS_STR != ""
encode S002_ALL_STR, generate(S002_ALL)
drop S002_STR S002EVS_STR S002_ALL_STR

*merge X048 and X048WVS
decode X048, generate(X048_STR)
decode X048WVS, generate(X048WVS_STR)
gen X048_ALL_STR = X048_STR if X048_STR != ""
replace X048_ALL_STR = X048WVS_STR if X048WVS_STR != ""
encode X048_ALL_STR, generate(X048_ALL)
drop X048_STR X048WVS_STR X048_ALL_STR

*calculate SAMPLE_SIZE
by S001 S002_ALL S003 X048_ALL, sort: gen SAMPLE_SIZE= _N


*This code is replicated from 'Index Construction_regional.do' attached in the same file
/***************************
Cleaning Trad-Secular PCA Inputs
****************************/

*F063: Unimportance of God in Your Life
recode F063 -5/-1=.
recode F063 1=5 2=4 3=3 4=2 5=1 6=-1 7=-2 8=-3 9=-4 10=-5 /*to make it unimportance*/

*Y003: (Autonomy Index) Keep the same
*test
recode Y003 -2=2 -1=2 0=0 1=-1 2=-2


*F120: Abotion is Justifiable
recode F120 -5/-1=.
recode F120 1=-5 2=-4 3=-3 4=-2 5=-1 6=1 7=2 8=3 9=4 10=5

*G006: How not proud of nationality
recode G006 -5/-1=.
recode G006 1=-2 2=-1 3=1 2=4

*E018: Greater Respect for Authority
recode E018 -5/-1=.


/***************************
Cleaning Survival-Selfexpression PCA Inputs
****************************/

*Y002: Postmaterialism 4-Item Index
recode Y002 -5/-4=.
recode Y002 1=-1 2=0 3=1

*A008: Feeling of Happiness
recode A008 -5/-1=.
recode A008 1=2 2=1 3=-1 4=-2

*E025: Siging Political Petition
recode E025 -5/-1=.
recode E025 3=-1 2=0 1=1

*F118: Homosexulaity is Justifiable
recode F118 -5/-1=.
recode F118 1=-5 2=-4 3=-3 4=-2 5=-1 6=1 7=2 8=3 9=4 10=5

*A173: Freedom of Choice
recode A173 -5/-1=.
recode A173 1=-5 2=-4 3=-3 4=-2 5=-1 6=1 7=2 8=3 9=4 10=5

*A165: Most people can be trusted
recode A165 -5/-1=.
recode A165 1=1 2=-1


/*PCA Analysis at the National Level*/

** Aggregate Loadings at the national level: sunational
* collapse (mean) F063 Y003 F120 G006 E018 Y002 A008 E025 F118 A165 A173 , by (S001 S002_ALL S003 S009 S009A S020 S025 S026 X048_ALL)
* National-Level:
*collapse (mean) F063 Y003 F120 G006 E018 Y002 A008 E025 F118 A165 A173 , by (S001 S002 S003 S009 S020 S025 S026)


*ind Level: (General)
factor F063 Y003 F120 G006 E018 Y002 A008 E025 F118 A165, pcf factors (2)
screeplot
rotate, varimax
estat rotatecompare
loadingplot, ytitle(component 2) xtitle(component 1)

*ind Level: (No Y003)
factor F063 F120 G006 E018 Y002 A008 E025 F118 A165, pcf factors (2)
screeplot
rotate, varimax
estat rotatecompare
loadingplot, ytitle(component 2) xtitle(component 1)


*ind Level: (No F118)
factor F063 Y003 F120 G006 E018 Y002 A008 E025 A165, pcf factors (2)
screeplot
rotate, varimax
estat rotatecompare
loadingplot, ytitle(component 2) xtitle(component 1)

*ind Level: (A173)
factor F063 Y003 F120 G006 E018 Y002 A008 E025 A173 A165, pcf factors (2)
screeplot
rotate, varimax
estat rotatecompare
loadingplot, ytitle(component 2) xtitle(component 1)




*predict pc1 pc2
*rename ( pc1) (tradsec)
*drop survself
*rename ( pc2) (survself)
*scatter survself tradsec if S002 == 5 & S003 == 724, mlabel(X048_ALL)
*scatter survself tradsec if S002 == 5, mlabel(S003)

*save regional_dimensions_all.0.0.2_selectedQs.dta
