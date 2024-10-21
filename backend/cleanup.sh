#!/bin/bash
#SBATCH -A standby
#SBATCH --nodes=1
#SBATCH --gpus-per-node=1

# rm ./*
echo "running cleanup"
# rm /home/zhao1322x/test/out/*