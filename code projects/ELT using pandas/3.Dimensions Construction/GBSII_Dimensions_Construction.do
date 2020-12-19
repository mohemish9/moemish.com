clear
cd "/home/ec2-user/survey_project/data/processed"

use "GBSII_provinces_added_0.3.dta", replace

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



* calculate SAMPLE_SIZE
by region	country	country_un year province, sort: gen SAMPLE_SIZE= _N

* add dummy variables
* se1
gen se1_male = .
*replace se1_male= 0 if se1 != 1 & se1 != .
gen se1_female = .
*replace se1_female= 0 if se1 != 2 & se1 != .


* se3
gen se3_1 = .
*replace se3_1= 0 if se3 != 1 & se3 != .
gen se3_2 = .
*replace se3_2= 0 if se3 != 2 & se3 != .
gen se3_3 = .
*replace se3_3= 0 if se3 != 3 & se3 != .
gen se3_4 = .
*replace se3_4= 0 if se3 != 4 & se3 != .
gen se3_5 = .
*replace se3_5= 0 if se3 != 5 & se3 != .

* se7
gen se7_1 = .
*replace se7_1= 0 if se7 != 1
gen se7_2 = .
*replace se7_2= 0 if se7 != 2
gen se7_3 = .
*replace se7_3= 0 if se7 != 3
gen se7_4 = .
*replace se7_4= 0 if se7 != 4
gen se7_5 = .
*replace se7_5= 0 if se7 != 5

* se9
gen se9_unemployed = .
*replace se9_unemployed= 0 if se9 != 1 & se9 != .
gen se9_employed = .
*replace se9_employed= 0 if se9 != 2 & se9 != .

* se13
gen se13_rural = .
*replace se13_rural = 0 if se13 != 1 & se13 != .
gen se13_semi_urban = .
*replace se13_semi_urban = 0 if se13 != 1.5 & se13 != .
gen se13_urban = .
*replace se13_urban= 0 if se13 != 2 & se13 != .

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
      display "province" "`l'"
      capture{
        svy, subpop(if province2 == "`l'" & region == `r' & country_un == `c' ): tab se1
        matrix values = e(Prop)
        replace se1_male = values[1,1] if province2 == "`l'" & region == `r' & country_un == `c'
        replace se1_female = values[2,1] if province2 == "`l'" & region == `r' & country_un == `c'
      }

      capture{
        svy, subpop(if province2 == "`l'" & region == `r' & country_un == `c' ): tab se3
        matrix values = e(Prop)
        replace se3_1 = values[1,1] if province2 == "`l'" & region == `r' & country_un == `c'
        replace se3_2 = values[2,1] if province2 == "`l'" & region == `r' & country_un == `c'
        replace se3_3 = values[3,1] if province2 == "`l'" & region == `r' & country_un == `c'
        replace se3_4 = values[4,1] if province2 == "`l'" & region == `r' & country_un == `c'
        replace se3_5 = values[5,1] if province2 == "`l'" & region == `r' & country_un == `c'
      }

      capture{
        svy, subpop(if province2 == "`l'" & region == `r' & country_un == `c' ): tab se7
        matrix values = e(Prop)
        replace se7_1 = values[1,1] if province2 == "`l'" & region == `r' & country_un == `c'
        replace se7_2 = values[2,1] if province2 == "`l'" & region == `r' & country_un == `c'
        replace se7_3 = values[3,1] if province2 == "`l'" & region == `r' & country_un == `c'
        replace se7_4 = values[4,1] if province2 == "`l'" & region == `r' & country_un == `c'
        replace se7_5 = values[5,1] if province2 == "`l'" & region == `r' & country_un == `c'
      }

      capture{
        svy, subpop(if province2 == "`l'" & region == `r' & country_un == `c'): tab se9
        matrix values = e(Prop)
        replace se9_unemployed = values[1,1] if province2 == "`l'" & region == `r' & country_un == `c'
        replace se9_employed = values[2,1] if province2 == "`l'" & region == `r' & country_un == `c'
      }

      capture{
        svy, subpop(if province2 == "`l'" & region == `r' & country_un == `c'): tab se13
        matrix values = e(Prop)
        replace se13_rural = values[1,1] if province2 == "`l'" & region == `r' & country_un == `c'
        replace se13_semi_urban = values[2,1] if province2 == "`l'" & region == `r' & country_un == `c'
        replace se13_urban = values[3,1] if province2 == "`l'" & region == `r' & country_un == `c'
      }
    }
  }
}

drop province2
* change direction and range of questions

* Traditional-Secular Values

* f006_customized
recode f006_customized 1=15 2=5 3=-5 4=-15 if region ==2
replace f006_customized = f006_customized / 3 if region ==2
recode f006_customized 1=-5 2=-2.5 3=0 4=2.5 5=5 if region == 3
recode f006_customized 1=-15 2=-5 3=5 4=15 if region == 3
replace f006_customized = f006_customized / 3 if region ==5

* gov5
recode gov5 2=-1 1=1

* Materialism-Postmaterialism Values

* imp1
recode imp1 1=2 2=1
replace imp1 = 0 if imp1 != 1 & imp1 != 2 & imp1 != .

* imp2
recode imp2 1=2 2=1
replace imp2 = 0 if imp2 != 1 & imp2 != 2 & imp2 != .

*imp3
recode imp3 1=2 2=1
replace imp3 =0 if imp3 != 1 & imp3 != 3 & imp3 != .

* imp1_2_3
gen imp1_2_3 = imp1 + imp2 + imp3
recode imp1_2_3 0=-3 1=-2 2=-1 3=0 4=1 5=2 6=3
replace imp1_2_3 = imp1_2_3 / 3

* ee1
recode ee1 1=-2 2=-1 3=0 4=1 5=2

*pp6
recode pp6 1=-1 2=0 3=1

*sc1
recode sc1 1=-1 2=1


pwcorr f006_customized gov5 imp1_2_3 ee1 pp6 sc1 if region ==2
pwcorr f006_customized gov5 imp1_2_3 ee1 pp6 sc1 if region ==3
pwcorr f006_customized gov5 imp1_2_3 ee1 pp6 sc1 if region ==5


ds, has(type numeric)
local vars_ALL `r(varlist)'
local omit region	country	country_un	year province
local vars: list vars_ALL - omit
collapse (mean) `vars', by (region	country	country_un	year province)


factor f006_customized gov5 imp1_2_3 ee1 pp6 sc1 if region == 2, pcf factors (2)
screeplot
rotate, varimax
estat rotatecompare
loadingplot, ytitle(component 2) xtitle(component 1)
predict tradsec2 survself2 if region ==2

factor f006_customized gov5 ee1 pp6 sc1 if region ==3, pcf factors (2)
screeplot
rotate, varimax
estat rotatecompare
loadingplot, ytitle(component 2) xtitle(component 1)
predict tradsec3 survself3 if region ==3

factor f006_customized gov5 ee1 pp6 sc1 if region ==5, pcf factors (2)
screeplot
rotate, varimax
estat rotatecompare
loadingplot, ytitle(component 2) xtitle(component 1)

predict tradsec5 survself5 if region ==5
* rename ( pc1) (tradsec)
* rename ( pc2) (survself)
* scatter survself tradsec if wave == 2008 & S003 == 724, mlabel(prov)

gen tradsec = tradsec2 if region ==2
replace tradsec = tradsec3 if region ==3
replace tradsec = tradsec5 if region ==5

gen survself = survself2 if region ==2
replace survself = survself3 if region ==3
replace survself = survself5 if region ==5

drop survself2 survself3 survself5 tradsec2 tradsec3 tradsec5


save regional_dimensions_GBSII0.0.1.dta, replace


exit
