clear
cd "/home/ec2-user/survey_project/data/raw"

* for all cases including EVS longitudnal:
use "AmericasBarometer Grand Merge 2004-2014 v3.0_FREE.dta", replace

*Insrtuctions to construct WVS Indices:

label dir
numlabel `r(names)', add

* select and clean all numeric variables
ds, has(type numeric)
foreach var of varlist `r(varlist)' {
  replace `var' = .  if `var' < 0
  replace `var' = .  if `var' == .a
  replace `var' = .  if `var' == .b
  replace `var' = .  if `var' == .c
  replace `var' = .  if `var' == .z
}


* calculate SAMPLE_SIZE
by pais wave year prov, sort: gen SAMPLE_SIZE= _N


* change direction and range of questions

* Traditional-Secular Values

* q5b : F063
recode q5b  1=-15 2=-5 3=5 4=15
replace q5b = q5b / 3

* ab1 : Y003
recode ab1 3=0 2=1 1=-1

* ab2 :Y003
recode ab2 1=1 2=-1 3=0

* ab1_plus_2 : Y003
gen ab1_plus_2 = ab1 + ab2
*recode ab1_plus_2 2=-2 3=-1 4=0 5=1 6=2

* w14a : F120
recode w14a 2=-5 1=5

* b43 : G006
recode b43 7=-6 6=-4 5=-2 4=0 3=2 2=3 1=6
replace b43 = b43 / 3

* b14 : E018
recode b14 7=-6 6=-4 5=-2 4=0 3=2 2=3 1=6
replace b14 = b14 / 6

* Materialism-Postmaterialism Values

* a4 : Y002
gen a4_n = 0
replace a4_n =-10 if a4 == 10
replace a4_n =-9 if a4 == 19
replace a4_n = -8 if a4 == 7
replace a4_n = 10 if a4==1
replace a4_n = 9 if a4 == 2
replace a4_n =8 if a4 == 3
replace a4_n = 7 if a4 == 4
replace a4_n = a4_n / 10

* soct1 : A008
recode soct1 5=-2 4=-1 3=0 2=2 1=2

* mar1 : F118
recode mar1 1=5 2=2.5 3=0 4=-2.5 5=-5 6=.

* prot6 : E025
recode prot6 2=-1 1=1

* it1 : A165
recode it1 1=3 2=1 3=-1 4=-3
replace it1 = it1 /3


pwcorr q5b ab1_plus_2 w14a b43 b14 a4_n soct1 prot6 it1


collapse (mean) q5b ab1_plus_2 w14a b43 b14 a4_n soct1 prot6 it1 SAMPLE_SIZE, by (pais wave year prov)

*cd '/home/ec2-user/survey_project/data/processed'
* save regional_dimensions_americas.0.0.0.dta

factor q5b ab1_plus_2 w14a b43 b14 a4_n soct1 prot6 it1, pcf factors (2)
screeplot
rotate, varimax
estat rotatecompare
loadingplot, ytitle(component 2) xtitle(component 1)

predict tradsec survself
*scatter survself tradsec if wave == 2008 & S003 == 724, mlabel(prov)

*cd '/home/ec2-user/survey_project/data/processed'
save regional_dimensions_americas_selectedQs.0.0.1.dta

exit
