#!/bin/bash
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
# echo "--------------------------------------------------"
# echo "conda installing pytorch"
# conda install pytorch torchvision torchaudio pytorch-cuda=11.8 -c pytorch -c nvidia --yes
# echo "--------------------------------------------------"
# echo "pip installing tensorflow"
# python3 -m pip install tensorflow[and-cuda] --quiet

# echo "--------------------------------------------------"
# echo "pip installing requirements"
# python3 -m pip install -r requirements.txt --quiet

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