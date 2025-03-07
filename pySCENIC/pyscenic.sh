#!/bin/bash
#$ -cwd
# error = Merged with joblog
#$ -o /u/home/s/skikuchi/project-xyang123/math168/pySCENIC/joblog/pyscenic.$JOB_ID
#$ -j y
# Edit the line below to request the appropriate runtime and memory
# (or to add any other resource) as needed:
#$ -l h_rt=20:00:00,h_data=128G
# Add multiple cores/nodes as needed:
#$ -pe shared 1

# echo job info on joblog:
echo "Job $JOB_ID started on:   " `hostname -s`
echo "Job $JOB_ID started on:   " `date `
echo " "


# load the job environment:
. /u/local/Modules/default/init/modules.sh
module load anaconda3
# To see which versions of anaconda are available use: module av anaconda
# activate an already existing conda environment (CHANGE THE NAME OF THE ENVIRONMENT):
conda activate /u/home/s/skikuchi/project-xyang123/miniconda3/envs/scenic_protocol
# in the following two lines substitute the command with the
# needed command below:
echo "running_pyscenic"

CURRENT_DIRECTORY=/u/home/s/skikuchi/project-xyang123/math168/pySCENIC/

celltype_loom=/u/home/s/skikuchi/project-xyang123/math168/alz.loom

TF="${CURRENT_DIRECTORY}/allTFs_hg38.txt"
grn_file="${CURRENT_DIRECTORY}/alz_scenic_grn.csv"

# call pyscenic
echo "pyscenic grn ${celltype_loom} ${TF} -o ${grn_file} --num_workers 20"
pyscenic grn ${celltype_loom} \
        ${TF} \
        -o ${grn_file} --num_workers 16