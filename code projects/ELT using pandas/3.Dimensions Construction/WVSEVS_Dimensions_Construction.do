clear
cd "/home/ec2-user/survey_project/data/raw"
* for all cases including EVS longitudnal:
use WVS_Data_for_Factor_all, replace

* No EVS longitundal
* use WVSLongitudnal.dta, replace

*Insrtuctions to construct WVS Indices:
label dir
numlabel `r(names)', add

* select and clean all numeric variables
ds, has(type numeric)
foreach var of varlist `r(varlist)' {
  replace `var' = .  if `var' < 0
  replace `var' = .  if `var' == .n
}

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


/******************
creating dummy variables for X003R X049 x049a X025 X025CSWVS X051 X047
********************/


*X003R
gen X003R_15_24 = .
*replace X003R_15_24 = 0 if X003R != 1
gen X003R_25_34 = .
*replace X003R_25_34 = 0 if X003R != 2
gen X003R_35_44 = .
*replace X003R_35_44 = 0 if X003R != 3
gen X003R_45_54 = .
*replace X003R_45_54 = 0 if X003R != 4
gen X003R_55_64 = .
*replace X003R_55_64 = 0 if X003R != 5
gen X003R_65_above = .
*replace X003R_65_above = 0 if X003R != 6

*x049a
gen X049a_1 = .
*replace X049a_1 = 0 if x049a != 1
gen X049a_2 = .
*replace X049a_2 = 0 if x049a != 2
gen X049a_3 = .
*replace X049a_3 = 0 if x049a != 3
gen X049a_4 = .
*replace X049a_4 = 0 if x049a != 4
gen X049a_5 = .
*replace X049a_5 = 0 if x049a != 5

*X049
gen X049_1 = .
*replace X049_1 = 0 if X049 != 1
gen X049_2 = .
*replace X049_2 = 0 if X049 != 2
gen X049_3 = .
*replace X049_3 = 0 if X049 != 3
gen X049_4 = .
*replace X049_4 = 0 if X049 != 4
gen X049_5 = .
*replace X049_5 = 0 if X049 != 5
gen X049_6 = .
*replace X049_6 = 0 if X049 != 6
gen X049_7 = .
*replace X049_7 = 0 if X049 != 7
gen X049_8 = .
*replace X049_8 = 0 if X049 != 8

*X025
gen X025_1 = .
*replace X025_1 = 0 if X025 != 1
gen X025_2 = .
*replace X025_2 = 0 if X025 != 2
gen X025_3 = .
*replace X025_3 = 0 if X025 != 3
gen X025_4 = .
*replace X025_4 = 0 if X025 != 4
gen X025_5 = .
*replace X025_5 = 0 if X025 != 5
gen X025_6 = .
*replace X025_6 = 0 if X025 != 6
gen X025_7 = .
*replace X025_7 = 0 if X025 != 7
gen X025_8 = .
*replace X025_8 = 0 if X025 != 8

*X041
gen X041_0 = .
*replace X041_0 = 0 if X041 != 0
gen X041_1 = .
*replace X041_1 = 0 if X041 != 1

svyset S007_01 [pweight = S017]
levelsof S001, local(surveys)
foreach s of local surveys{
  levelsof S002_ALL if S001 == `s', local(regions)
  foreach r of local regions{
    levelsof S003A if S002_ALL == `r' & S001 == `s', local(countries)
    foreach c of local countries{
      levelsof X048_ALL if S002_ALL == `r' & S003A == `c' & S001 == `s', local(provinces)
      foreach l of local provinces {
        display "province " "`l'"
        capture noisily{
          svy, subpop(if X048_ALL == `l' & S002_ALL == `r' & S003A == `c' & S001 == `s' ): tab X003R
          matrix values = e(Prop)
          replace X003R_15_24 = values[1,1] if X048_ALL == `l' & S002_ALL == `r' & S003A == `c' & S001 == `s'
          replace X003R_25_34 = values[2,1] if X048_ALL == `l' & S002_ALL == `r' & S003A == `c' & S001 == `s'
          replace X003R_35_44 = values[3,1] if X048_ALL == `l' & S002_ALL == `r' & S003A == `c' & S001 == `s'
          replace X003R_45_54 = values[4,1] if X048_ALL == `l' & S002_ALL == `r' & S003A == `c' & S001 == `s'
          replace X003R_55_64 = values[5,1] if X048_ALL == `l' & S002_ALL == `r' & S003A == `c' & S001 == `s'
          replace X003R_65_above = values[6,1] if X048_ALL == `l' & S002_ALL == `r' & S003A == `c' & S001 == `s'
        }

        capture noisily{
          svy, subpop(if X048_ALL == `l' & S002_ALL == `r' & S003A == `c' & S001 == `s'): tab x049a
          matrix values = e(Prop)
          replace X049a_1 = values[1,1] if X048_ALL == `l' & S002_ALL == `r' & S003A == `c' & S001 == `s'
          replace X049a_2 = values[2,1] if X048_ALL == `l' & S002_ALL == `r' & S003A == `c' & S001 == `s'
          replace X049a_3 = values[3,1] if X048_ALL == `l' & S002_ALL == `r' & S003A == `c' & S001 == `s'
          replace X049a_4 = values[4,1] if X048_ALL == `l' & S002_ALL == `r' & S003A == `c' & S001 == `s'
          replace X049a_5 = values[5,1] if X048_ALL == `l' & S002_ALL == `r' & S003A == `c' & S001 == `s'
        }

        capture noisily{
          svy, subpop(if X048_ALL == `l' & S002_ALL == `r' & S003A == `c' & S001 == `s' ): tab X049
          matrix values = e(Prop)
          replace X049_1 = values[1,1] if X048_ALL == `l' & S002_ALL == `r' & S003A == `c' & S001 == `s'
          replace X049_2 = values[2,1] if X048_ALL == `l' & S002_ALL == `r' & S003A == `c' & S001 == `s'
          replace X049_3 = values[3,1] if X048_ALL == `l' & S002_ALL == `r' & S003A == `c' & S001 == `s'
          replace X049_4 = values[4,1] if X048_ALL == `l' & S002_ALL == `r' & S003A == `c' & S001 == `s'
          replace X049_5 = values[5,1] if X048_ALL == `l' & S002_ALL == `r' & S003A == `c' & S001 == `s'
          replace X049_6 = values[6,1] if X048_ALL == `l' & S002_ALL == `r' & S003A == `c' & S001 == `s'
          replace X049_7 = values[7,1] if X048_ALL == `l' & S002_ALL == `r' & S003A == `c' & S001 == `s'
          replace X049_8 = values[8,1] if X048_ALL == `l' & S002_ALL == `r' & S003A == `c' & S001 == `s'
        }

        capture noisily{
          svy, subpop(if X048_ALL == `l' & S002_ALL == `r' & S003A == `c' & S001 == `s'): tab X025
          matrix values = e(Prop)
          replace X025_1 = values[1,1] if X048_ALL == `l' & S002_ALL == `r' & S003A == `c' & S001 == `s'
          replace X025_2 = values[2,1] if X048_ALL == `l' & S002_ALL == `r' & S003A == `c' & S001 == `s'
          replace X025_3 = values[3,1] if X048_ALL == `l' & S002_ALL == `r' & S003A == `c' & S001 == `s'
          replace X025_4 = values[4,1] if X048_ALL == `l' & S002_ALL == `r' & S003A == `c' & S001 == `s'
          replace X025_5 = values[5,1] if X048_ALL == `l' & S002_ALL == `r' & S003A == `c' & S001 == `s'
          replace X025_6 = values[6,1] if X048_ALL == `l' & S002_ALL == `r' & S003A == `c' & S001 == `s'
          replace X025_7 = values[7,1] if X048_ALL == `l' & S002_ALL == `r' & S003A == `c' & S001 == `s'
          replace X025_8 = values[8,1] if X048_ALL == `l' & S002_ALL == `r' & S003A == `c' & S001 == `s'
        }

        capture noisily{
          svy, subpop(if X048_ALL == `l' & S002_ALL == `r' & S003A == `c' & S001 == `s'): tab X041
          matrix values = e(Prop)
          replace X041_0 = values[1,1] if X048_ALL == `l' & S002_ALL == `r' & S003A == `c' & S001 == `s'
          replace X041_1 = values[2,1] if X048_ALL == `l' & S002_ALL == `r' & S003A == `c' & S001 == `s'
        }
      }
    }
  }
}

*This code is replicated from 'Index Construction_regional.do' attached in the same file
/***************************
Cleaning Trad-Secular PCA Inputs
****************************/

*F063: Unimportance of God in Your Life
*recode F063 -5/-1=.
recode F063 1=5 2=4 3=3 4=2 5=1 6=-1 7=-2 8=-3 9=-4 10=-5 /*to make it unimportance*/

*Y003: (Autonomy Index) Keep the same

*F120: Abotion is Justifiable
*recode F120 -5/-1=.
recode F120 1=-5 2=-4 3=-3 4=-2 5=-1 6=1 7=2 8=3 9=4 10=5

*G006: How not proud of nationality
*recode G006 -5/-1=.
recode G006 1=-2 2=-1 3=1 2=4

*E018: Greater Respect for Authority
*recode E018 -5/-1=.


/***************************
Cleaning Survival-Selfexpression PCA Inputs
****************************/

*Y002: Postmaterialism 4-Item Index
*recode Y002 -5/-4=.
recode Y002 1=-1 2=0 3=1

*A008: Feeling of Happiness
*recode A008 -5/-1=.
recode A008 1=2 2=1 3=-1 4=-2

*E025: Siging Political Petition
*recode E025 -5/-1=.
recode E025 3=-1 2=0 1=1

*F118: Homosexulaity is Justifiable
*recode F118 -5/-1=.
recode F118 1=-5 2=-4 3=-3 4=-2 5=-1 6=1 7=2 8=3 9=4 10=5

*A165: Most people can be trusted
*recode A165 -5/-1=.
recode A165 1=1 2=-1


/*PCA Analysis*/
pwcorr F063 Y003 F120 G006 E018 Y002 A008 E025 F118 A165

**Aggregate Loadings at the national level:
ds, has(type numeric)
local vars_ALL `r(varlist)'
local omit S001 S002_ALL S003 S009 S009A S020 S025 S026 X048_ALL
local vars: list vars_ALL - omit
collapse (mean) `vars', by (S001 S002_ALL S003 S009 S009A S020 S025 S026 X048_ALL)
factor F063 Y003 F120 G006 E018 Y002 A008 E025 F118 A165, pcf factors (2)
screeplot
rotate, varimax
estat rotatecompare
loadingplot, ytitle(component 2) xtitle(component 1)

predict pc1 pc2
rename ( pc1) (tradsec)
drop survself
rename ( pc2) (survself)
scatter survself tradsec if S002 == 5 & S003 == 724, mlabel(X048WVS)

save regional_dimensions_all.0.0.2.dta
