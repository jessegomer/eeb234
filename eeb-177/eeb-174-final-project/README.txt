Zack Gold EEB 234 Final Project

eDNA Bioinformatics Pipeline- Anacapa

The Anacapa pipeline has two scripts the rlibrary_builder and anacapa.

rlibrary_builder generates a reference library for your target primer of interest. For example, using MiFish Universal 12s primers we will generate a complete reference library of NCBI species that can be targeted by this 12s primer. WARNING: this script requires a lot of computing time. Recommended to run on a large server or cluster. 

The anacapa script takes raw sequence files and runs the full bioinformatics pipeline providing an output of analyzed data.
