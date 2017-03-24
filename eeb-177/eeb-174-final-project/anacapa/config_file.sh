#### Configuration File for Anacapa Pipeline
#### Created March 2017 by Zack Gold for EEB 234
#### Last Modified 03/23/2017


#### Instructions
#### Step 1: Replace all file paths to match those on your computer
#### Step 2: Run Anacapa Pipeline

#### Directory with Scripts and Files needed for Anacapa Pipeline
UTIL_FOLDER_PATH="/Users/zackgold/Documents/UCLA_phd/Projects/anacapa/utilites/"

#### Sample Names to Replace Raw Sequencing Names
SAMPLE_NAMES="RWZG001_S12_L002_ RWZG001_S12_L002_ RWZG002_S26_L002_ RWZG002_S26_L002_ RWZG003_S27_L002_ RWZG003_S27_L002_"

#### Directory of Raw Fastq files from Sequencer
FASTQ_DIK_PATH="/Users/zackgold/Documents/UCLA_phd/Projects/anacapa/dummy/"

#### Input Directory with user generated/downloaded NCBI Taxids, Primer file, QIIME Mapping File, and Unassigned Reference Library Database
INPUT_FOLDER=:"/Users/zackgold/Documents/UCLA_phd/Projects/anacapa/input/"

#### For Storing Quality Controlled and PEAR'd fastq
QC_FOLDER="/Users/zackgold/Documents/UCLA_phd/Projects/anacapa/qc/"

#### Config for PEAR program
PEAR_PATH="pear "
PEAR_OUT_PATH="/Users/zackgold/Documents/UCLA_phd/Projects/anacapa/dummy/PEAR/"
PEAR_Q="30"
PEAR_T="100"
PEAR_J="10"
PEAR_Y="4G"

#### Config for Assembling PEAR Outputs
ASSEMBLED_FASTQ="moorea_assembled.fastq"
DISCARDED_FASTQ="moorea_discarded.fastq"
FWRD_FASTQ="moorea_unassembled_forward.fastq"
RVRSE_FASTQ="moorea_unassembled_reverse.fastq"


#### Config for Cutadapt program
CUTADAPT_PATH="/Users/zackgold/.local/bin/cutadapt"
FWRD_INDEX_PRIMER="TCGTCGGCAGCGTCAGATGTGTATAAGAGACAGGT"
RVRSE_INDEX_PRIMER="GTCTCGTGGGCTCGGAGATGTGTATAAGAGACAG"
CUT_FASTQ="/Users/zackgold/Documents/UCLA_phd/Projects/anacapa/qc/moorea_assembled_cut.fastq"

#### Config to convert fastq to fasta file
FASTQ_2_FASTA="/Users/zackgold/.local/bin_2/fastq_to_fasta"
FASTA_ASSEMBLED="/Users/zackgold/Documents/UCLA_phd/Projects/anacapa/qc/moorea_assembled_cut.fasta"

#### Config to print number of assembled reads 
READS_NUM="/Users/zackgold/Documents/UCLA_phd/Projects/anacapa/qc/moorea_assembled_cut_reads.txt"

#### Config to Split on Primer (must be done even if only 1 primer sequenced)
SPLIT_ON_PRIMER="/Users/zackgold/Documents/UCLA_phd/Projects/anacapa/utilites/Split_on_Primer.py"
PRIMER_LIST="/Users/zackgold/Documents/UCLA_phd/Projects/anacapa/input/PANEL_5_PRIMERS.txt"
SPLIT_M="8"
SPLIT_S="5"

#### Config for Pick OTU in Qiime
PICK_OTU_DIR="/Users/zackgold/Documents/UCLA_phd/Projects/anacapa/qiime/otu_98_swarm"
PICK_OTU_S="0.98"
CLUST_TYPE="swarm"

#### Config for Pick Rep Set
PICKED_OTUS="/Users/zackgold/Documents/UCLA_phd/Projects/anacapa/qiime/otu_98_swarm/MiFishUFR_no_n_otus.txt"
REP_SET="/Users/zackgold/Documents/UCLA_phd/Projects/anacapa/qiime/repset_98.fasta"

#### Config for Make BLAST Database
BLAST_DIR="/Users/zackgold/.local/bin/ncbi-blast-2.6.0+/"
BLAST_DB_INPUT="/Users/zackgold/Documents/UCLA_phd/Projects/anacapa/input/blast_databases/sequence.fasta-4.txt"
BLAST_DB_TITLE="MiFish_Universal_12s"
BLAST_DB="/Users/zackgold/Documents/UCLA_phd/Projects/anacapa/input/blast_databases/MiFish_Universal/12S"
TAXID_MAP="/Users/zackgold/Documents/UCLA_phd/Projects/anacapa/input/ncbi_accessions_taxonomy_dump/nucl_gb.accession2taxid"

#### Config for best_taxon_picker.py
MEGAN_TAX="/Users/zackgold/Documents/UCLA_phd/Projects/anacapa/input/mifish_rep_set_localsonly20-taxonomy.txt"
MEGAN_BEST_TAX="/Users/zackgold/Documents/UCLA_phd/Projects/anacapa/input/mifish_rep_set_localsonly20-taxonomy_best_taxonomy.txt"
ASSIGNMENT_THRESHOLD="100"

#### Config for Blast Rep Set 
BLASTED_REP_SET="/Users/zackgold/Documents/UCLA_phd/Projects/anacapa/qiime/BLAST_repset_99.txt"

#### Config for Assigning Taxonomy

ASSIGNED_TAXONOMY="/Users/zackgold/Documents/UCLA_phd/Projects/anacapa/qiime/assigned_taxonomy/"
REF_LIB="/Users/zackgold/Documents/UCLA_phd/Projects/anacapa/input/blast_databases/MiFish_Universal/12S/Mifish_40k_no_n_nr.fasta"

#### Config for Splitting OTU Table based on project
OTU_TABLE_RAW="/Users/zackgold/Documents/UCLA_phd/Projects/anacapa/qiime/assigned_taxonomy/mifish_megan_otu_table.biom"
MAP_TABLE="/Users/zackgold/Documents/UCLA_phd/Projects/anacapa/input/moorea_1_seq_map.txt"
CATEGORY_TO_SPLIT="Project"
SPLIT_DIR="/Users/zackgold/Documents/UCLA_phd/Projects/anacapa/qiime/per_project_otu_tables"

#### Config for Collapse Samples
PROJECT_1_BIOM="/Users/zackgold/Documents/UCLA_phd/Projects/anacapa/qiime/per_project_otu_tables/otu_table_mc2_w_tax__Project_Moorea__.biom"
PROJECT_1_BIOM_RENAMED="/Users/zackgold/Documents/UCLA_phd/Projects/anacapa/qiime/per_project_otu_tables/otu_table_mc2_w_tax__Project_Moorea__renamed.biom"
SAMPLE_NAME="Sample_name"

#### Config for Filter out Unassigned Reads
PROJECT_1_BIOM_UN_REMOVED="/Users/zackgold/Documents/UCLA_phd/Projects/anacapa/qiime/per_project_otu_tables/otu_table_mc2_w_tax__Project_Moorea__renamed_unassigned_removed.biom"
UNASSIGNED="/Users/zackgold/Documents/UCLA_phd/Projects/anacapa/qiime/per_project_otu_tables/unassigned.txt"

#### Config for decontaminate.py
PROJECT_1_BIOM_UN_REMOVED_TXT="/Users/zackgold/Documents/UCLA_phd/Projects/anacapa/qiime/per_project_otu_tables/otu_table_mc2_w_tax__Project_Moorea_r_unr.txt"
OTU_TABLE_TXT="'otu_table_mc2_w_tax__Project_Moorea_r_unr.txt'"
LABEL_OTU="'#OTU ID'"
LABEL_TAX="'taxonomy'"
CONTROL_1="'pcrblank'"
CONTROL_2="'negcontrol1'"
CONTROLS_ALL="config['CONTROL_1'],config['CONTROL_2']"
### just add more controls if you have more blanks and make sure to include them all in controlls_all
CLEANED_OTU="'cleaned_otu_table.csv'"
CLEANED_OTU_TSV="cleaned_otu_table.csv"
CLEANED_OTU_BIOM="/Users/paulbarber/Desktop/zjg_folder/201609_ZG/gz/pick_otu/moorea_mifish/per_project_otu_tables/otu_table_mc2_w_tax__Project_Moorea_r_unr_controls_removed.biom"
CONVERTED_BIOM="/Users/paulbarber/Desktop/zjg_folder/201609_ZG/gz/pick_otu/moorea_mifish/per_project_otu_tables/otu_table_mc2_w_tax__Project_Moorea_r_unr_controls_removed_converted.biom"


########## Config for Data Analysis

#### Config for Summarize taxa through plots
TAX_SUMMARY="/Users/zacharygold/Documents/UCLAPhD/Projects/Moorea/Sequences/taxa_summary"

#### Config for Alpha diversity Rarefaction
RARE_DATA="moorare"
REP_SET_TRE="/Users/zacharygold/Documents/UCLAPhD/Projects/Moorea/Dropbox/201609_ZG/MiFish/otu_default/rep_set.tre"

#### Config for Betadiversity Rarefaction
JACK_BDIV_OUT="jack_bdiv_even1000"

#### Config for Beta Diversity Statistics
DIST_TYPE="dist_bray_curtis,abund_jaccard,binary_dist_jaccard"
BETA_STATS_OUT="beta_div/"
BETA_DATA="/Users/zacharygold/Documents/UCLAPhD/Projects/Moorea/Sequences/beta_div/weighted_unifrac_otu_table_mc2_w_tax__Project_Moorea__cleaned.txt"
