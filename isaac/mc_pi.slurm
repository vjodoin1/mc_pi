#!/bin/bash

#SBATCH --job-name=mcpi

#SBATCH --output=mcpi.out

#SBATCH -A ACF-UTK0011

#SBATCH --ntasks=1

#SBATCH --cpus-per-task=8

#SBATCH --time=00:05:00

#SBATCH --mem=4G



module load Python/3.9.10-gcc

source mcpi-venv/bin/activate

python mc_pi.py --n 100000000

% To run, use 'sbatch mc_pi.slurm'
