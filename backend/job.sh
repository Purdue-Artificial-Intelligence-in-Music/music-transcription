#!/bin/bash
#SBATCH -A standby
#SBATCH --nodes=1
#SBATCH --gpus-per-node=1

echo "--------------------------------------------------"
echo "loading modules"
source /etc/profile.d/modules.sh

module --force purge

module load anaconda
module load ffmpeg

echo "--------------------------------------------------"
echo "creating conda environment"
conda env create -f environment.yml -n testing-env

conda activate testing-env

for FILE in /home/zhao1322/test/test-files/*; do
    filename=$(basename "$FILE")
    filename_no_ext="${filename%.*}"
    echo "--------------------------------------------------"
    echo "TESTING ON ${filename}"
    python main.py -i /home/zhao1322/test/test-files/$filename -o /home/zhao1322/test/out/$filename_no_ext.mid
done

echo "--------------------------------------------------"
echo "cleaning up environment"
cd ..

conda deactivate
conda env remove -n testing-env --yes
conda clean --all --yes