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

conda activate scoring-env

echo "output directory"
ls /home/zhao1322/test/out/

for FILE in /home/zhao1322/test/out/*; do
    filename=$(basename "$FILE")
    filename_no_ext="${filename%.*}"
    echo "--------------------------------------------------"
    echo "SCORING ON ${filename}"
    python compare_midi.py --reference /home/zhao1322/test/eval/$filename_no_ext.mid --transcription /home/zhao1322/test/out/$filename_no_ext.mid --output /home/zhao1322/test/eval/$filename_no_ext --output /home/zhao1322/test/scores/$filename_no_ext.txt
done

echo "scoring job complete"