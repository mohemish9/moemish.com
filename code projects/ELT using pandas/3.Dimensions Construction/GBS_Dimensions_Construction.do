clear
cd "/home/ec2-user/survey_project/data/processed"

use "GBS_provinces_added_0.2.dta", replace

*Insrtuctions to construct WVS Indices:
label dir
numlabel `r(names)', add

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

* dummy variables for se1 se3 se6 se8 se28

* se1
gen se1_male = .
*replace se1_male= 0 if se1 != 1
gen se1_female = .
*replace se1_female= 0 if se1 != 2

* se3
gen se3_1 = .
*replace se3_1= 0 if se3 != 1
gen se3_2 = .
*replace se3_2= 0 if se3 != 2
gen se3_3 = .
*replace se3_3= 0 if se3 != 3
gen se3_4 = .
*replace se3_4= 0 if se3 != 4
gen se3_5 = .
*replace se3_5= 0 if se3 != 5

* se6
gen se6_1 = .
*replace se6_1= 0 if se6 != 1
gen se6_2 = .
*replace se6_2= 0 if se6 != 2
gen se6_3 = .
*replace se6_3= 0 if se6 != 3
gen se6_4 = .
*replace se6_4= 0 if se6 != 4
gen se6_5 = .
*replace se6_5= 0 if se6 != 5

* se8
gen se8_unemployed = .
*replace se8_unemployed= 0 if se8 != 1
gen se8_employed = .
*replace se8_employed= 0 if se8 != 2


* se28
gen se28_rural = .
*replace se28_rural = 0 if se28 != 1
gen se28_urban = .
*replace se28_urban= 0 if se28 != 2

gen province2 = subinstr(province," ",".",.)
replace province2 = subinstr(province2,"-",":",.)
replace province2 = subinstr(province2,"/",":",.)

svyset idnumber [pweight = wt]
levelsof region, local(regions)
foreach r of local regions{
  levelsof country_un if region == `r', local(countries)
  foreach c of local countries{
    levelsof province2 if region == `r' & country_un == `c', local(provinces)
    foreach l of local provinces {
      display "province " "`l'"
      capture noisily {
        svy, subpop(if province2 == "`l'" & region == `r' & country_un == `c' ): tab se1
        matrix values = e(Prop)
        replace se1_male = values[1,1] if province2 == "`l'" & region == `r' & country_un == `c'
        replace se1_female = values[2,1] if province2 == "`l'" & region == `r' & country_un == `c'
      }

      capture noisily {
        svy, subpop(if province2 == "`l'" & region == `r' & country_un == `c' ): tab se3
        matrix values = e(Prop)
        replace se3_1 = values[1,1] if province2 == "`l'" & region == `r' & country_un == `c'
        replace se3_2 = values[2,1] if province2 == "`l'" & region == `r' & country_un == `c'
        replace se3_3 = values[3,1] if province2 == "`l'" & region == `r' & country_un == `c'
        replace se3_4 = values[4,1] if province2 == "`l'" & region == `r' & country_un == `c'
        replace se3_5 = values[5,1] if province2 == "`l'" & region == `r' & country_un == `c'

      }

      capture noisily {
        svy, subpop(if province2 == "`l'" & region == `r' & country_un == `c' ): tab se6
        matrix values = e(Prop)
        replace se6_1 = values[1,1] if province2 == "`l'" & region == `r' & country_un == `c'
        replace se6_2 = values[2,1] if province2 == "`l'" & region == `r' & country_un == `c'
        replace se6_3 = values[3,1] if province2 == "`l'" & region == `r' & country_un == `c'
        replace se6_4 = values[4,1] if province2 == "`l'" & region == `r' & country_un == `c'
        replace se6_5 = values[5,1] if province2 == "`l'" & region == `r' & country_un == `c'
      }

      capture noisily {
        svy, subpop(if province2 == "`l'" & region == `r' & country_un == `c'): tab se8
        matrix values = e(Prop)
        replace se8_unemployed = values[1,1] if province2 == "`l'" & region == `r' & country_un == `c'
        replace se8_employed = values[2,1] if province2 == "`l'" & region == `r' & country_un == `c'
      }

      capture noisily {
        svy, subpop(if province2 == "`l'" & region == `r' & country_un == `c'): tab se28
        matrix values = e(Prop)
        replace se28_rural = values[1,1] if province2 == "`l'" & region == `r' & country_un == `c'
        replace se28_urban = values[2,1] if province2 == "`l'" & region == `r' & country_un == `c'

      }
    }
  }
}

drop province2
* change direction and range of questions

* Traditional-Secular Values

* se10
recode se10 3=-5 2=-5 1=5


* ge1
recode ge1 1=-15 2=-5 3=5 4=15
replace ge1 = ge1/3

* cit2
recode cit2 4=-6 3=-2 2=2 1=6
replace cit2 = cit2 / 3

* sd5
recode sd5 4=-3 3=-1 2=1 1=3
replace sd5 = sd5 / 3

* Materialism-Postmaterialism Values

* imp1
recode imp1 1=2 2=1
replace imp1 = 0 if imp1 != 2 & imp1 != 1

* imp2
recode imp2 1=2 2=1
replace imp2 = 0 if imp2 != 2 & imp2 != 1

* imp3
recode imp3 1=2 2=1
replace imp3 = 0 if imp3 != 2 & imp3 != 1

* imp1_2_3
gen imp1_2_3 = imp1 + imp2 + imp3
replace imp1_2_3 = imp1_2_3 - 3
replace imp1_2_3 = imp1_2_3 / 3

* ee1
recode ee1 1=-2 2=-1 3=0 4=1 5=2

* pp8
recode pp8 1=-1 2=0 3=1

* sc1
recode sc1 1=-1 2=1

pwcorr sd5 imp1_2_3 ee1 pp8 sc1 if region == 2
pwcorr sd5 imp1_2_3 ee1 pp8 if region == 3
pwcorr se10 ge1 sd5 ee1 sc1 if region == 5
pwcorr se10 cit2 sd5 ee1 sc1 if region == 6
pwcorr se10 sd5 ee1 sc1 if region == 7

ds, has(type numeric)
local vars_ALL `r(varlist)'
local omit region	country	country_un	year province
local vars: list vars_ALL - omit
collapse (mean) `vars', by (region	country	country_un	year province)


* save regional_dimensions_GBS_selectedQs.0.0.0.dta

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


save regional_dimensions_GBS.0.0.2.dta, replace

exit
