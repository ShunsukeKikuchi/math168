#!/bin/bash
#$ -cwd
# error = Merged with joblog
#$ -o /u/home/s/skikuchi/project-xyang123/math168/SCING/joblog/supercell.$JOB_ID
#$ -j y
# Edit the line below to request the appropriate runtime and memory
# (or to add any other resource) as needed:
#$ -l h_rt=24:00:00,h_data=64G
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
conda activate /u/project/xyang123/skikuchi/miniconda3/envs/scing

# in the following two lines substitute the command with the
# needed command below:
echo "python supercell.py"


python /u/home/s/skikuchi/project-xyang123/math168/SCING/Python_Codes/supercell.py

# echo job info on joblog:
echo "Job $JOB_ID ended on:   " `hostname -s`
echo "Job $JOB_ID ended on:   " `date `
echo " "
### anaconda_python_submit.sh STOP ###