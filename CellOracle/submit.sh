#!/bin/bash
#$ -cwd
# error = Merged with joblog
#$ -o /u/home/s/skikuchi/project-xyang123/math168/CellOracle/joblog/CellOracle.$JOB_ID
#$ -j y
# Edit the line below to request the appropriate runtime and memory
# (or to add any other resource) as needed:
#$ -l h_rt=24:00:00,h_data=32G
# Add multiple cores/nodes as needed:
#$ -pe shared 1

# ex. qsub submit.sh

# echo job info on joblog:
echo "Job $JOB_ID started on:   " `hostname -s`
echo "Job $JOB_ID started on:   " `date `
echo " "


# load the job environment:
. /u/local/Modules/default/init/modules.sh
module load anaconda3
module load R
# To see which versions of anaconda are available use: module av anaconda
# activate an already existing conda environment (CHANGE THE NAME OF THE ENVIRONMENT):
conda activate /u/project/xyang123/skikuchi/miniconda3/envs/CellOracle
python "buildGRN.py"
# echo job info on joblog:
echo "Job $JOB_ID.$SGE_TASK_ID ended on:   " `hostname -s`
echo "Job $JOB_ID.$SGE_TASK_ID ended on:   " `date `
echo " "
### anaconda_python_submit.sh STOP ###