#!/bin/bash
#$ -cwd
# error = Merged with joblog
#$ -o /u/home/s/skikuchi/project-xyang123/math168/SCING/joblog/buildnet.$JOB_ID
#$ -j y
# Edit the line below to request the appropriate runtime and memory
# (or to add any other resource) as needed:
#$ -l h_rt=3:00:00,h_data=16G
# Add multiple cores/nodes as needed:
#$ -pe shared 1


# qsub -t 1-100 /u/home/s/skikuchi/project-xyang123/math168/SCING/Python_Codes/buildnet.sh
# echo job info on joblog:
echo "Job $JOB_ID.$SGE_TASK_ID started on:   " `hostname -s`
echo "Job $JOB_ID.$SGE_TASK_ID started on:   " `date `
echo " "


# load the job environment:
. /u/local/Modules/default/init/modules.sh
module load anaconda3
# activate an already existing conda environment (CHANGE THE NAME OF THE ENVIRONMENT):
conda activate /u/project/xyang123/skikuchi/miniconda3/envs/scing

# in the following two lines substitute the command with the
# needed command below:
echo "python buildnet.py $SGE_TASK_ID "
# call python code with -out only if second arguments is given:

python /u/home/s/skikuchi/project-xyang123/math168/SCING/Python_Codes/buildnet.py "$SGE_TASK_ID"
sleep 5m

# echo job info on joblog:
echo "Job $JOB_ID.$SGE_TASK_ID ended on:   " `hostname -s`
echo "Job $JOB_ID.$SGE_TASK_ID ended on:   " `date `
echo " "
