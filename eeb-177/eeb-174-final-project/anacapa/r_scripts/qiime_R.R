# R script to implement Qiime in R for data analysis and plotting

library("qiimer", lib.loc="/Library/Frameworks/R.framework/Versions/3.3/Resources/library")
library(reshape2)
library(ggplot2)
library(ggrepel)
library(vegan)
library(wesanderson) # I just want to give a shout out to karthik for being a true legend and fellow Wes Anderson afficiando, as well as to Gaurav for sharing with me this amazing package. Truly life altering

# Read in cleaned biom table
biom_table <- read_qiime_otu_table("/Users/zackgold/Documents/UCLA_phd/Projects/anacapa/qiime/assigned_taxonomy/mifish_no_tax_otu_table_mm_filtered__Project_Moorea__renamed.txt")
#biom_table

#Read in mapping file
mor_map <- read_qiime_mapping_file("/Users/zackgold/Documents/UCLA_phd/Projects/anacapa/input/moorea_1_seq_map__Project_Moorea__updated_again.txt")
head(mor_map)

# Create data frame from biom_table
data <- biom_table$counts

# Transpose data frame to R usable format
dataT <- t(data)
dataT <- as.data.frame(dataT)

# Map metadata to mapper data frame
mapper <- data.frame(mor_map$Habitat, mor_map$SampleID)
#append metadata to dataT 
colnames(dataT)[0] <- "mor_map.SampleID"
dataT_lab <- dataT
dataT_lab$mor_map.SampleID <- biom_table$sample_ids
dataT_lab <- left_join(dataT_lab, mapper, by = "mor_map.SampleID")


# Calculate Bray Curtis Similarity Distance
bray_dist_dataT<-vegdist(dataT, method = "bray")

# Plot Bray Curtis Distance Map
melted_bray <- melt(as.matrix(bray_dist_dataT))
pal <- wes_palette("Zissou", 100, type = "continuous")
ggplot(data = melted_bray, aes(x=Var1, y=Var2, fill=value)) + geom_tile() + labs(x= 'Moorea Sites', y= 'Moorea Sites') + scale_fill_gradient(low="white", high= pal[1], guide=guide_legend(title="Dissimilarity")) + ggtitle('Bray Curtis Similarity Heat Map') + theme(plot.title = element_text(hjust = 0.5))+ theme(axis.text.x = element_text(size=5, angle=45))


#  Bray Curtis NMDS Plot
## Create Distance Data Frame
gr.habitat <- dataT_lab$mor_map.Habitat
col.gr <- wes_palette(name = "Darjeeling2")
grp <- dataT_lab$mor_map.Habitat
test<-cmdscale(bray_dist_dataT)

data.scores_1 <- as.data.frame(scores(test))  #Using the scores function from vegan to extract the site scores and convert to a data.frame
data.scores_1$site <- rownames(data.scores_1)  # create a column of site names, from the rownames of data.scores
head(data.scores_1) 
data.scores_1$grp <- grp  #  add the grp variable created earlier
head(data.scores_1)  #look at the data

#### Calculate Shape Around Points
grp.backreef <- data.scores_1[data.scores_1$grp == "Backreef", ][chull(data.scores_1[data.scores_1$grp == "Backreef", c("Dim1", "Dim2")]), ]  
grp.fourreef <- data.scores_1[data.scores_1$grp == "Forereef", ][chull(data.scores_1[data.scores_1$grp == "Forereef", c("Dim1", "Dim2")]), ]  
grp.lab <- data.scores_1[data.scores_1$grp == "Lab", ][chull(data.scores_1[data.scores_1$grp == "Lab", c("Dim1", "Dim2")]), ] 
grp.pelagic <- data.scores_1[data.scores_1$grp == "Pelagic", ][chull(data.scores_1[data.scores_1$grp == "Pelagic", c("Dim1", "Dim2")]), ] 
grp.backflow <- data.scores_1[data.scores_1$grp == "Backreef_flow", ][chull(data.scores_1[data.scores_1$grp == "Backreef_flow", c("Dim1", "Dim2")]), ] 

hull.data <- rbind(grp.backreef, grp.fourreef,grp.lab,grp.pelagic,grp.backflow)  #combine grp.a and grp.b
hull.data

#### Plot Bray Curtis NMDS
col.gr <- wes_palette(name = "Moonrise3")
ggplot() + 
  geom_polygon(data=hull.data,aes(x=Dim1,y=Dim2,fill=grp,group=grp),alpha=0.30) + scale_fill_manual(values=col.gr, guide=guide_legend(title = "Habitat"), labels=c("Backreef", "High Flow Backreef", "Forereef", "Lab", "Pelagic")) +
  geom_point(data=data.scores_1,aes(x=Dim1,y=Dim2, colour = grp ),size=2) + scale_colour_manual(values=col.gr, guide=guide_legend(title = "Habitat"), labels=c("Backreef", "High Flow Backreef", "Forereef","Lab","Pelagic")) +# add the point markers
  geom_text_repel(data=data.scores_1,aes(x=Dim1,y=Dim2,label=site),size=2.5, nudge_y = 0.01,box.padding = unit(0.25, "lines"),point.padding = unit(.1, "lines")) +  # add the site labels
  theme_bw() + ggtitle('Bray Curtis NMDS') + theme(plot.title = element_text(hjust = 0.5))


#Jaccard Similarity 
# Calculate Jaccard Similarity Distance
jaccard_dist_dataT<-vegdist(dataT, method = "jaccard")

# Plot Jaccard Distance Map
melted_jaccard <- melt(as.matrix(jaccard_dist_dataT))
pal <- wes_palette("Zissou", 100, type = "continuous")
ggplot(data = melted_jaccard, aes(x=Var1, y=Var2, fill=value)) + geom_tile() + labs(x= 'Moorea Sites', y= 'Moorea Sites') + scale_fill_gradient(low="white", high= pal[1], guide=guide_legend(title="Dissimilarity")) + ggtitle('Bray Curtis Similarity Heat Map') + theme(plot.title = element_text(hjust = 0.5))+ theme(axis.text.x = element_text(size=5, angle=45))


#  Jaccard NMDS Plot
## Create Distance Data Frame
gr.habitat <- dataT_lab$mor_map.Habitat
col.gr <- wes_palette(name = "Darjeeling2")
grp <- dataT_lab$mor_map.Habitat
jaccard<-cmdscale(jaccard_dist_dataT)

data.scores <- as.data.frame(scores(jaccard))  #Using the scores function from vegan to extract the site scores and convert to a data.frame
data.scores$site <- rownames(data.scores)  # create a column of site names, from the rownames of data.scores
head(data.scores) 
data.scores$grp <- grp  #  add the grp variable created earlier
head(data.scores)  #look at the data

#### Calculate Shape Around Points
grp.backreef_j <- data.scores[data.scores$grp == "Backreef", ][chull(data.scores[data.scores$grp == "Backreef", c("Dim1", "Dim2")]), ]  
grp.fourreef_j <- data.scores[data.scores$grp == "Forereef", ][chull(data.scores[data.scores$grp == "Forereef", c("Dim1", "Dim2")]), ]  
grp.lab_j <- data.scores[data.scores$grp == "Lab", ][chull(data.scores[data.scores$grp == "Lab", c("Dim1", "Dim2")]), ] 
grp.pelagic_j <- data.scores[data.scores$grp == "Pelagic", ][chull(data.scores[data.scores$grp == "Pelagic", c("Dim1", "Dim2")]), ] 
grp.backflow_j <- data.scores[data.scores$grp == "Backreef_flow", ][chull(data.scores[data.scores$grp == "Backreef_flow", c("Dim1", "Dim2")]), ] 

hull.data_j <- rbind(grp.backreef_j, grp.fourreef_j,grp.lab_j,grp.pelagic_j,grp.backflow_j)  #combine grp.a and grp.b

# Plot Jaccard NMDS Plot
col.gr <- wes_palette(name = "Moonrise3")
ggplot() + 
  geom_polygon(data=hull.data_j,aes(x=Dim1,y=Dim2,fill=grp,group=grp),alpha=0.30) + scale_fill_manual(values=col.gr, guide=guide_legend(title = "Habitat"), labels=c("Backreef", "High Flow Backreef", "Forereef", "Lab", "Pelagic")) +
  geom_point(data=data.scores,aes(x=Dim1,y=Dim2, colour = grp ),size=2) + scale_colour_manual(values=col.gr, guide=guide_legend(title = "Habitat"), labels=c("Backreef", "High Flow Backreef", "Forereef","Lab","Pelagic")) +# add the point markers
  geom_text_repel(data=data.scores,aes(x=Dim1,y=Dim2,label=site),size=2, nudge_y = 0.01,box.padding = unit(0.2, "lines"),point.padding = unit(.1, "lines")) +  # add the site labels
  theme_bw() + ggtitle('Jaccard NMDS') + theme(plot.title = element_text(hjust = 0.5))
