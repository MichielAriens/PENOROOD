rawData = read.csv(file = file.choose(), header = TRUE,dec = ",", sep = ";")
data = t(rawData)
write.table(data,file = file.choose(),sep=";")