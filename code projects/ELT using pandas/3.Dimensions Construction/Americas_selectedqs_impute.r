library(imputeTS)

data <- read.csv('regional_dimensions_americas_selectedQs.0.0.2.csv')
groups <- unique(data[c('pais', 'prov')])
questions <-  c('q5b','ab1_plus_2','w14a','b43','b14','a4','soct1','prot6', 'it1','tradsec','survself')

data.imputed <- data[0,]
for (row in 1:nrow(groups))
{
  data.selected <- data[which(data$pais == groups$pais[row] & data$prov == groups$prov[row]),]
  #print(data.selected)
  for (q in questions)
  {
    if(sum(!is.na(data.selected[,q])) > 1)
    {
      data.selected[,q] <- na.interpolation(data.selected[,q],option ="spline")
    }
  }
  data.imputed <- rbind(data.imputed,data.selected)
}

write.csv(data.imputed, "regional_dimensions_americas_selectedQs_imputed.0.0.1.csv")
