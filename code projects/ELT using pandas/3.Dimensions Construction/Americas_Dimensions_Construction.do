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

* dummy variables for idiomaq q1 tamano (ed_can or ed_usa) ocup4a

* idiomaq
gen idiomaq_Spanish = .
*replace idiomaq_Spanish = 0 if idiomaq != 1
gen idiomaq_English = .
*replace idiomaq_English = 0 if idiomaq != 2
gen idiomaq_Portuguese = .
*replace idiomaq_Portuguese = 0 if idiomaq != 3
gen idiomaq_Dutch = .
*replace idiomaq_Dutch = 0 if idiomaq != 12
gen idiomaq_Creole = .
*replace idiomaq_Creole = 0 if idiomaq != 14
gen idiomaq_Indigenous = .
*replace idiomaq_Indigenous = 0 if idiomaq != 102
gen idiomaq_Quichua = .
*replace idiomaq_Quichua = 0 if idiomaq != 902
gen idiomaq_Quechua = .
*replace idiomaq_Quechua = 0 if idiomaq != 1002
gen idiomaq_Aymara = .
*replace idiomaq_Aymara = 0 if idiomaq != 1003
gen idiomaq_Guarani_Yopara = .
*replace idiomaq_Guarani_Yopara = 0 if idiomaq != 1202
gen idiomaq_Spanish_and_Guarani = .
*replace idiomaq_Spanish_and_Guarani = 0 if idiomaq != 1203
gen idiomaq_Spanish_Guarani = .
*replace idiomaq_Spanish_Guarani = 0 if idiomaq != 1204
gen idiomaq_Indigenous_Sranan_tongo = .
*replace idiomaq_Indigenous_Sranan_tongo= 0 if idiomaq != 2713
gen idiomaq_Indigenous_French = .
*replace idiomaq_Indigenous_French= 0 if idiomaq != 4101

* q1
gen q1_male = .
*replace q1_male= 0 if q1 != 1
gen q1_female = .
*replace q1_female= 0 if q1 != 2

* tamano
gen tamano_1 = .
*replace tamano_1= 0 if tamano != 1
gen tamano_2 = .
*replace tamano_2= 0 if tamano != 2
gen tamano_3 = .
*replace tamano_3= 0 if tamano != 3
gen tamano_4 = .
*replace tamano_4= 0 if tamano != 4
gen tamano_5 = .
*replace tamano_5 = 0 if tamano != 5

* ed_usa
gen ed_usa_1 = .
*replace ed_usa_1= 0 if ed_usa != 1
gen ed_usa_2 = .
*replace ed_usa_2= 0 if ed_usa != 2
gen ed_usa_3 = .
*replace ed_usa_3= 0 if ed_usa != 3
gen ed_usa_4 = .
*replace ed_usa_4= 0 if ed_usa != 4
gen ed_usa_5 = .
*replace ed_usa_5= 0 if ed_usa != 5
gen ed_usa_6 = .
*replace ed_usa_6= 0 if ed_usa != 6

* ocup4a
gen ocup4a_1 = .
*replace ocup4a_1 = 0 if ocup4a != 1
gen ocup4a_2 = .
*replace ocup4a_2 = 0 if ocup4a != 2
gen ocup4a_3 = .
*replace ocup4a_3 = 0 if ocup4a != 3
gen ocup4a_4 = .
*replace ocup4a_4 = 0 if ocup4a != 4
gen ocup4a_5 = .
*replace ocup4a_5 = 0 if ocup4a != 5
gen ocup4a_6 = .
*replace ocup4a_6 = 0 if ocup4a != 6
gen ocup4a_7 = .
*replace ocup4a_7 = 0 if ocup4a != 7



svyset idnum [pweight = weight1500]
levelsof wave, local(regions)
foreach r of local regions{
  levelsof pais if wave == `r', local(countries)
  foreach c of local countries{
    levelsof prov if wave == `r' & pais == `c', local(provinces)
    foreach l of local provinces {
      display "province " `l'
      capture noisily {
        svy, subpop(if prov == `l' & wave == `r' & pais == `c' ): tab idiomaq
        matrix values = e(Prop)
        replace idiomaq_Spanish = values[1,1] if prov == `l' & wave == `r' & pais == `c'
        replace idiomaq_English = values[2,1] if prov == `l' & wave == `r' & pais == `c'
        replace idiomaq_Portuguese = values[3,1] if prov == `l' & wave == `r' & pais == `c'
        replace idiomaq_Dutch = values[4,1] if prov == `l' & wave == `r' & pais == `c'
        replace idiomaq_Creole = values[5,1] if prov == `l' & wave == `r' & pais == `c'
        replace idiomaq_Indigenous = values[6,1] if prov == `l' & wave == `r' & pais == `c'
        replace idiomaq_Quichua = values[7,1] if prov == `l' & wave == `r' & pais == `c'
        replace idiomaq_Quechua = values[8,1] if prov == `l' & wave == `r' & pais == `c'
        replace idiomaq_Aymara = values[9,1] if prov == `l' & wave == `r' & pais == `c'
        replace idiomaq_Guarani_Yopara = values[10,1] if prov == `l' & wave == `r' & pais == `c'
        replace idiomaq_Spanish_and_Guarani = values[11,1] if prov == `l' & wave == `r' & pais == `c'
        replace idiomaq_Spanish_Guarani = values[12,1] if prov == `l' & wave == `r' & pais == `c'
        replace idiomaq_Indigenous_Sranan_tongo = values[13,1] if prov == `l' & wave == `r' & pais == `c'
        replace idiomaq_Indigenous_French = values[14,1] if prov == `l' & wave == `r' & pais == `c'

      }

      capture noisily {
        svy, subpop(if prov == `l' & wave == `r' & pais == `c' ): tab q1
        matrix values = e(Prop)
        replace q1_male = values[1,1] if prov == `l' & wave == `r' & pais == `c'
        replace q1_female = values[2,1] if prov == `l' & wave == `r' & pais == `c'

      }

      capture noisily {
        svy, subpop(if prov == `l' & wave == `r' & pais == `c' ): tab tamano
        matrix values = e(Prop)
        replace tamano_1 = values[1,1] if prov == `l' & wave == `r' & pais == `c'
        replace tamano_2 = values[2,1] if prov == `l' & wave == `r' & pais == `c'
        replace tamano_3 = values[3,1] if prov == `l' & wave == `r' & pais == `c'
        replace tamano_4 = values[4,1] if prov == `l' & wave == `r' & pais == `c'
        replace tamano_5 = values[5,1] if prov == `l' & wave == `r' & pais == `c'

      }

      capture noisily {
        svy, subpop(if prov == `l' & wave == `r' & pais == `c'): tab ed_usa
        matrix values = e(Prop)
        replace ed_usa_1 = values[1,1] if prov == `l' & wave == `r' & pais == `c'
        replace ed_usa_2 = values[2,1] if prov == `l' & wave == `r' & pais == `c'
        replace ed_usa_3 = values[3,1] if prov == `l' & wave == `r' & pais == `c'
        replace ed_usa_4 = values[4,1] if prov == `l' & wave == `r' & pais == `c'
        replace ed_usa_5 = values[5,1] if prov == `l' & wave == `r' & pais == `c'
        replace ed_usa_6 = values[6,1] if prov == `l' & wave == `r' & pais == `c'
      }

      capture noisily {
        svy, subpop(if prov == `l' & wave == `r' & pais == `c'): tab ocup4a
        matrix values = e(Prop)
        replace ocup4a_1 = values[1,1] if prov == `l' & wave == `r' & pais == `c'
        replace ocup4a_2 = values[2,1] if prov == `l' & wave == `r' & pais == `c'
        replace ocup4a_3 = values[3,1] if prov == `l' & wave == `r' & pais == `c'
        replace ocup4a_4 = values[4,1] if prov == `l' & wave == `r' & pais == `c'
        replace ocup4a_5 = values[5,1] if prov == `l' & wave == `r' & pais == `c'
        replace ocup4a_6 = values[6,1] if prov == `l' & wave == `r' & pais == `c'
        replace ocup4a_7 = values[7,1] if prov == `l' & wave == `r' & pais == `c'
      }
    }
  }
}



* change direction and range of questions

* Traditional-Secular Values

* q5b
recode q5b  1=-15 2=-5 3=5 4=15
replace q5b = q5b / 3

* ab1
recode ab1 3=2 2=3 1=1

* ab2
recode ab2 1=3 2=1 3=2

* ab1_plus_2
gen ab1_plus_2 = ab1 + ab2
recode ab1_plus_2 2=-2 3=-1 4=0 5=1 6=2

* w14a
recode w14a 2=-5 1=5

* b43
recode b43 7=-6 6=-4 5=-2 4=0 3=2 2=3 1=6
replace b43 = b43 / 3

* b14
recode b14 7=-6 6=-4 5=-2 4=0 3=2 2=3 1=6
replace b14 = b14 / 6

* Materialism-Postmaterialism Values

* a4
recode a4 10 = -1 1=1
replace a4 = 0 if a4 != 1 & a4 != -1

* soct1
recode soct1 5=-1 4=-1 3=0 2=2 1=2

* colideol4b
* recode colideol4b 1=-5 2=-4 3=-3 4=-1 5=0 6=1 7=2 8=3 9=4 10=5

* prot6
recode prot6 2=-1 1=1

* it1
recode it1 1=3 2=1 3=-1 4=-3
replace it1 = it1 /3


pwcorr q5b ab1_plus_2 w14a b43 b14 a4 soct1 prot6 it1


ds, has(type numeric)
local vars_ALL `r(varlist)'
local omit pais wave year prov
local vars: list vars_ALL - omit
collapse (mean) `vars', by (pais wave year prov)

*cd '/home/ec2-user/survey_project/data/processed'
* save regional_dimensions_americas.0.0.0.dta

factor q5b ab1_plus_2 w14a b43 b14 a4 soct1 prot6 it1, pcf factors (2)
screeplot
rotate, varimax
estat rotatecompare
loadingplot, ytitle(component 2) xtitle(component 1)


predict tradsec survself
* rename ( pc1) (tradsec)
* rename ( pc2) (survself)
* scatter survself tradsec if wave == 2008 & S003 == 724, mlabel(prov)

*cd '/home/ec2-user/survey_project/data/processed'
save regional_dimensions_americas.0.0.3.dta

outsheet using regional_dimensions_americas.0.0.3.csv,comma

exit
