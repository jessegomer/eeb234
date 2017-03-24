#!/bin/bash

#### Anacapa Pipeline v1

#### Metabarcoding bioinformatics pipeline to take raw sequence data and output data analysis
#### Further description found in the README on github https://github.com/zjgold/eeb234/tree/master/eeb-177/eeb-174-final-project
#### Requires sister config file that houses paths to dependencies, inputs, and outputs

#### Author: Zachary Gold
#### contact: zack.gold@ucla.edu

#### Activate Configuration File
. /Users/zackgold/Documents/UCLA_phd/Projects/anacapa/config_file.sh

---------------------------------------
# Sequence Cleaning

#### Rename Raw Sequence Reads
#### raw sequence reads have a strange naming convention, replace this with user defined sample names for each sample
for i in ${SAMPLE_NAMES}  ;
do
	echo $i
	#grabs forward sequence files and renames them
 	sed -i '' "s/K00188/$i/g" ${FASTQ_DIK_PATH}$i"R1_001.fastq" #need to change this path
 	#grabs reverse sequence files and renames them
 	sed -i '' "s/K00188/$i/g" ${FASTQ_DIK_PATH}$i"R2_001.fastq"
done


#### Paired End reAd meRger
#### runs PEAR program on each pair of matched sequences, PEAR software works to align forward and reverse sequences with given accuracy parameters, and outputs an assigned, discarded, forward unassigned, and reverse unassigned file. 
for i in ${SAMPLE_NAMES}  ;
do
	echo $i
	${PEAR_PATH} -f ${FASTQ_DIK_PATH}$i"R1_001.fastq" -r ${FASTQ_DIK_PATH}$i"R2_001.fastq" -o ${PEAR_OUT_PATH}$i -q ${PEAR_Q} -t ${PEAR_T} -j ${PEAR_J} -y ${PEAR_Y}

done

#### make a new directory to store quality controlled reads
mkdir ${QC_FOLDER}

#### concatenates all of the paired merged reads, assembled sequences are the most important and stored in the QC folder
cat ${PEAR_OUT_PATH}*.assembled.fastq > ${QC_FOLDER}${ASSEMBLED_FASTQ}
cat ${PEAR_OUT_PATH}*.discarded.fastq > ${PEAR_OUT_PATH}${DISCARDED_FASTQ}
cat ${PEAR_OUT_PATH}*.unassembled.forward.fastq > ${PEAR_OUT_PATH}${FWRD_FASTQ}
cat ${PEAR_OUT_PATH}*.unassembled.reverse.fastq > ${PEAR_OUT_PATH}${RVRSE_FASTQ}

#### Cut Adapter
#### removes adapter sequences from the ends of the reads and filters out small sequences  (<125 bp)
module load fastx_toolkit/0.0.13.2
${CUTADAPT_PATH} -a ${FWRD_INDEX_PRIMER} -g ${RVRSE_INDEX_PRIMER} --minimum-length 125 ${QC_FOLDER}${ASSEMBLED_FASTQ} > ${CUT_FASTQ}

#### Fastaq to FASTA
#### Converts Fastq text file to to fasta text file (one text form to another to be used for input into qiime)
${FASTQ_2_FASTA} -i ${CUT_FASTQ} -o ${FASTA_ASSEMBLED} -n -Q33

#### save total number of cleaned assembled reads
grep -c ">" ${FASTA_ASSEMBLED} > ${READS_NUM}


---------------------------------------------------
#Assign Taxonomy
#### Split on primer
#### separates primers for different downstream taxonomic assignment, each primer is split into its own fasta file
${SPLIT_ON_PRIMER} -f ${FASTA_ASSEMBLED} -p ${PRIMER_LIST} -m ${SPLIT_M} -s ${SPLIT_S}

#### Pick OTUS
#### clusters sequences to representative OTUs which serve as identifiers for related sequences set by the s threshold i.e. 98% similarity
macqiime pick_otus.py -i ${FASTA_ASSEMBLED} -o ${PICK_OTU_DIR} -s ${PICK_OTU_S} -m ${CLUST_TYPE}

#### Picks a representative set of OTUs 
#### picks a representative OTU sequence for each OTU and collapses all matching sequences into a sequence count associated with each sequence, i.e. all unassigned Great white shark sequences are collapsed into 32,000 sequences assigned to OTU number 123456
macqiime pick_rep_set.py -i ${PICKED_OTUS} -f ${FASTA_ASSEMBLED} -o ${REP_SET}

#### makeblast db 
#### Make a reference database of specific sequences of interest with assigned taxonomy
#### blast is a program that compares a set of sequences to online published sequence reference database 
#### sequence database of interest is generated separately by downloading all vertebrate sequences from the NCBI website
#### makeblastdb assigns a taxonomy (i.e. Great White shark) to the sequence
#### WARNING: Very slow
 ${BLAST_DIR}bin/makeblastdb -in ${BLAST_DB_INPUT} -dbtype nucl -title ${BLAST_DB_TITLE} -out ${BLAST_DB} -taxid_map ${TAXID_MAP} -parse_seqids
 
#### next step could not be automated as of 3/23/2017 due to technical difficulties
#### open database in the MEGAN program and run least common ancestor taxonomy assignment analysis to generate reference library with assigned confidence values to each level of assigned taxonomy

#### remove low confidence assignments from Megan taxonomy
#### current threshold set at 100%
python ${UTIL_FOLDER_PATH}best_taxon_picker.py ${MEGAN_TAX} ${MEGAN_BEST_TAX} ${ASSIGNMENT_THRESHOLD}
 
#### now that there is a cleaned reference library with good taxonomic assignments

#### blast repset
#### blasts the representative set of OTU sequences against the reference library to assign accurate taxonomy to each OTU representative
#### generates a BIOM table which is essentially like a tsv file with rows as OTU IDs and columns as individual samples with number of sequences of each OTU
#### WARNING: Very slow
#### taxonomy at this step is ignored, MEGAN curated taxonomy is more accurate
${BLAST_DIR}bin/blastn -query ${REP_SET} -db ${BLAST_DB} -evalue 0.0000001 -outfmt 0 -num_alignments 20 -out ${BLASTED_REP_SET}

#### assign taxonomy to biom table
#### appends curated MEGAN taxonomy to the biom table using blast to match sequences
assign_taxonomy.py -i ${REP_SET} -r ${REF_LIB}  -t ${MEGAN_BEST_TAX} -m blast -e 0.000001 -o ${ASSIGNED_TAXONOMY}

#### Split OTU table 
#### Splits samples based on project using a user generated Map file
split_otu_table.py -i ${OTU_TABLE_RAW} -m ${MAP_TABLE}  -f ${CATEGORY_TO_SPLIT} -o ${SPLIT_DIR}


#### Collapse Samples
#### Renames Raw Sample Names to User defined site names based on user generated map file
collapse_samples.py -b ${PROJECT_1_BIOM} -m ${MAP_TABLE} --output_biom_fp ${PROJECT_1_BIOM_RENAMED} --output_mapping_fp omitted --collapse_mode sum --collapse_fields ${SAMPLE_NAME}

#### Remove Unassigned Reads 
#### Keeps OTUs with assigned taxonomy
filter_otus_from_otu_table.py -i ${PROJECT_1_BIOM_RENAMED}  -o ${PROJECT_1_BIOM_UN_REMOVED} -e ${UNASSIGNED} 

#### Biom Convert w/ Taxonomy Labels (must make a new file, will not replace a file correctly)
#### convert .biom to .tsv for python script
biom convert -i  ${PROJECT_1_BIOM_UN_REMOVED} -o ${PROJECT_1_BIOM_UN_REMOVED_TXT} --to-tsv --header-key taxonomy

#### Remove Contamination from Sequences
#### python script (works) to remove contaminated sequences
python ${UTIL_FOLDER_PATH}deconaminate.py

#### convert back to .BIOM
biom convert -i ${CLEANED_OTU_TSV}  -o ${CLEANED_OTU_BIOM} --table-type="OTU table" --to- --process-obs-metadata taxonomy

#### convert to HDF5 type for QIIME
biom convert -i ${CLEANED_OTU_BIOM} --to-hdf5 --collapsed-samples -o ${CONVERTED_BIOM}

--------------------------------------------
#### Data Analysis

#### Summarize Taxa through plots
#### generates a series of bar graphs at different taxonomic levels showing relative species abundance at each site
summarize_taxa_through_plots.py -i ${CONVERTED_BIOM} -f -o ${TAX_SUMMARY} -m ${MAP_TABLE} -p ${UTIL_FOLDER_PATH}species_parameter.txt

#### Alpha Diversity Rarefaction
####  runs an alpha rarefaction curve analysis to show 1) if sequencing depth was adequate i.e. the curve saturates at a given sequence depth and 2) compare number of species found in each sample
alpha_rarefaction.py -i ${CONVERTED_BIOM} -m ${MAP_TABLE} -o ${RARE_DATA} -p ${UTIL_FOLDER_PATH}alpha_params.txt -f -- min_rare_depth 1000

#### Beta Diversity Plot
#### generates beta-diversity plots comparing species distributions between samples
#### Additional R generated plots in separate script
jackknifed_beta_diversity.py -i ${CONVERTED_BIOM} -m ${MAP_TABLE} -o JACK_BDIV_OUT -e 1000


#### Stats analysis using permanova and permadisp
beta_diversity.py -i ${CONVERTED_BIOM} -m ${DIST_TYPE} -o ${BETA_STATS_OUT}

compare_categories.py --method permanova -i ${BETA_DATA}  -m ${MAP_TABLE} -c Habitat -o ${BETA_STATS_OUT} -n 999

compare_categories.py --method permdisp -i ${BETA_DATA}  -m ${MAP_TABLE} -c Habitat -o ${BETA_STATS_OUT} -n 999

