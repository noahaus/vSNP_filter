args = commandArgs(trailingOnly=TRUE)
if (length(args)==0) {
  stop("TOO LITTLE ARGUEMENTS", call.=FALSE)
}else if (length(args)==1) {
  filename = args[1]
  cutoff = 50
}else if (length(args)==2) {
  filename = args[1]
  cutoff = args[2]
}else if (length(args)>2) {
  stop("TOO MANY ARGUMENTS", call.=FALSE)
}

full_organized_data <- read.csv(filename, header = TRUE)
filter_positions <- full_organized_data[43,2:length(full_organized_data)]


#extract rows that are below a threshold
expunge_col1 <- c()
j = 1
for(i in 1:length(filter_positions)){
  if(as.numeric(as.character(filter_positions[1,i])) <= cutoff){
    expunge_col1[j] <- i+1
    j = j + 1
  }
}

full_organized_data <- full_organized_data[,-expunge_col1]

filter_annot <- full_organized_data[44,2:length(full_organized_data)]

#extract rows that contain reference to PE + PPE family proteins
expunge_col2 <- c()
j = 1
for(i in 1:length(filter_annot)){
  if(grepl("PE family protein",as.character(filter_annot[1,i])) | grepl("PPE family protein",as.character(filter_annot[1,i])) | grepl("PE-PGRS family protein",as.character(filter_annot[1,i]))){
    expunge_col2[j] <- i+1
    j = j + 1
  }
}

full_organized_data <- full_organized_data[,-expunge_col2]

#output newly filtered csv
write.csv(full_organized_data, file="pe-ppe_filtered_out.csv")
