---
title: "in_class_exercise_8-zjg"
author: "ZJG"
date: "March 1, 2017"
output: md_document
---

## Reading in Data files
```{r}
cocoli_dat <- read.table("~/Desktop/eeb234/eeb-177/classwork/feb-21/cocoli.txt", header = TRUE)
sizes_94<-cocoli_dat$dbh1
names(sizes_94)<- cocoli_dat$tag
sizes_94["000009"]
sizes_94[c("000009","000099")]
sizes_97<-cocoli_dat$dbh2

r_gr1<- (sizes_97-sizes_94)/sizes_94/3

cocoli_dat$rgr1<-r_gr1

```

```{r}
#bar graph made with barplot()


#boxplot - make with boxplot()

#scatter plot - make with plot()

#histogram make with hist()

#hist(sizes_94, xlab = "DBH (mm)", main="Distribution of Tree Sizes in Cocoli (1994)")

plot(x=sizes_94, y= sizes_97, main = "97 vs 94 Sizes", xlab = "Size 94", ylab = 'Size 97', pch =19,col='blue', log = 'xy')

```

```{r}
library(dplyr)
cocoli_dat
# is identical to pipe in terminal
#cocoli_dat %>% filter(sizes_94 > 0) %>% arrange(-dbh1) %>% select(spcode)

cocoli_dat %>% filter(sizes_94 > 0) %>% group_by(spcode) %>% summarize(mean_dbh_1994 = mean(dbh1))
```


