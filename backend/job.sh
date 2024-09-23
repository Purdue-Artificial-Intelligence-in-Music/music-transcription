#!/bin/bash
echo "--------------------------------------------------"
echo "loading modules"
source /etc/profile.d/modules.sh

module --force purge

module load anaconda
module load ffmpeg

echo "--------------------------------------------------"
echo "creating conda environment"
conda create -n test310 python=3.10 --yes

conda activate test310
echo "--------------------------------------------------"
echo "conda installing pytorch"
conda install pytorch torchvision torchaudio pytorch-cuda=11.8 -c pytorch -c nvidia --yes
echo "--------------------------------------------------"
echo "pip installing tensorflow"
python3 -m pip install tensorflow[and-cuda] --quiet

echo "--------------------------------------------------"
echo "pip installing requirements"
python3 -m pip install -r requirements.txt --quiet

for FILE in /home/zhao1322/test/test-files/*; do
    filename=$(basename "$FILE")
    filename_no_ext="${filename%.*}"
    echo "--------------------------------------------------"
    echo "TESTING ON ${filename}"
    python main.py -i /home/zhao1322/test/test-files/$filename -o /home/zhao1322/test/out/$filename_no_ext.mid
done
conda deactivate
conda env remove -n test310 --yes
conda clean --all --yes