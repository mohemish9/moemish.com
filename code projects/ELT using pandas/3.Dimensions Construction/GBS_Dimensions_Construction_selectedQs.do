clear
cd "/home/ec2-user/survey_project/data/processed"

use "GBS_provinces_added_0.2.dta", replace

*Insrtuctions to construct WVS Indices:
*label dir
*numlabel `r(names)', add

* select and clean all numeric variables
ds, has(type numeric)
foreach var of varlist `r(varlist)' {
  replace `var' = .  if `var' == -1
  replace `var' = .  if `var' == 7
  replace `var' = .  if `var' == 8
  replace `var' = .  if `var' == 9
  replace `var' = .  if `var' == 0
}
replace region = 7 if region == .


* calculate SAMPLE_SIZE
by region	country	country_un	year province, sort: gen SAMPLE_SIZE= _N


* change direction and range of questions

* Traditional-Secular Values

* se10 : F063
recode se10 3=-5 2=-5 1=5

* ge1: F121
recode ge1 1=-15 2=-5 3=5 4=15
replace ge1 = ge1/3

* cit2: G006
recode cit2 4=-6 3=-2 2=2 1=6
replace cit2 = cit2 / 3

* sd5 : E018
recode sd5 4=-3 3=-1 2=1 1=3
replace sd5 = sd5 / 3

* Materialism-Postmaterialism Values

* imp1: Y002
recode imp1 1=2 2=1
replace imp1 = 0 if imp1 != 2 & imp1 != 1 & imp1 != .

* imp2 : Y002
recode imp2 1=2 2=1
replace imp2 = 0 if imp2 != 2 & imp2 != 1 & imp2 != .

* imp3 : Y002
recode imp3 1=2 2=1
replace imp3 = 0 if imp3 != 2 & imp3 != 1 & imp3 != .

* imp1_2_3 : Y002
gen imp1_2_3 = imp1 + imp2 + imp3
replace imp1_2_3 = imp1_2_3 - 3
replace imp1_2_3 = imp1_2_3 / 3



* ee1: A008
recode ee1 1=-2 2=-1 3=0 4=1 5=2

* pp8: E025
recode pp8 1=-1 2=0 3=1

*qg4: A173
recode qg4 1=-15 2=-5 3=5 4=15
replace qg4 = qg4/3

* sc1: A165
recode sc1 1=-1 2=1

pwcorr sd5 imp1_2_3 ee1 pp8 sc1 qg4 if region == 2
pwcorr sd5 imp1_2_3 ee1 pp8 qg4 if region == 3
pwcorr se10 ge1 sd5 ee1 sc1 if region == 5
pwcorr se10 cit2 sd5 ee1 sc1 qg4 if region == 6
pwcorr se10 sd5 ee1 sc1 qg4 if region == 7


collapse (mean) se10 ge1 cit2 sd5 imp1_2_3 ee1 pp8 sc1 SAMPLE_SIZE, by (region	country	country_un	year province)


*save regional_dimensions_GBS_selectedQs.0.0.0.dta,replace

*factor sd5 imp1_2_3 ee1 pp8 sc1 if region == 2, pcf factors (2)
*screeplot
*rotate, varimax
*estat rotatecompare
*loadingplot, ytitle(component 2) xtitle(component 1)

*predict tradsec2 survself2 if region == 2

factor sd5 imp1_2_3 ee1 pp8 if region == 3, pcf factors (2)
screeplot
rotate, varimax
estat rotatecompare
loadingplot, ytitle(component 2) xtitle(component 1)

predict tradsec3 survself3 if region == 3


factor se10 ge1 sd5 ee1 sc1 if region == 5, pcf factors (2)
screeplot
rotate, varimax
estat rotatecompare
loadingplot, ytitle(component 2) xtitle(component 1)

predict tradsec5 survself5 if region == 5

factor se10 cit2 sd5 ee1 sc1 if region == 6, pcf factors (2)
screeplot
rotate, varimax
estat rotatecompare
loadingplot, ytitle(component 2) xtitle(component 1)

predict tradsec6 survself6 if region == 6


factor se10 sd5 ee1 sc1 if region == 7, pcf factors (2)
screeplot
rotate, varimax
estat rotatecompare
loadingplot, ytitle(component 2) xtitle(component 1)

predict tradsec7 survself7 if region == 7


*gen tradsec = tradsec2 if region == 2
gen tradsec = tradsec3 if region ==3
replace tradsec = tradsec3 if region ==3
replace tradsec = tradsec5 if region ==5
replace tradsec = tradsec6 if region == 6
replace tradsec = tradsec7 if region == 7

*gen survself = survself2 if region == 2
gen survself = survself3 if region ==3
replace survself = survself3 if region ==3
replace survself = survself5 if region ==5
replace survself = survself6 if region ==6
replace survself = survself7 if region ==7

*drop survself2 survself3 survself5 survself6 survself7 tradsec2 tradsec3 tradsec5 tradsec6 tradsec7
drop  survself3 survself5 survself6 survself7  tradsec3 tradsec5 tradsec6 tradsec7


*cd '/home/ec2-user/survey_project/data/processed'
*save regional_dimensions_GBS_selectedQs.0.0.3.dta, replace

exit
