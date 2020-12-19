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
by region	country	country_un	year province, sort: gen SAMPLE_SIZE= _N




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




collapse (mean) f006_customized gov5 imp1_2_3 ee1 pp6 sc1 SAMPLE_SIZE, by (region	country	country_un	year province)


* save regional_dimensions_GBSII_selectedQs.0.0.0.dta

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


save regional_dimensions_GBSII_selectedqs.0.0.1.dta, replace

exit
