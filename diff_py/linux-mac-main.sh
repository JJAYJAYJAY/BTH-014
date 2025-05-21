#!/bin/bash

# 环境名列表
envs=("py36" "py39" "py311")

# 输出目录
outdir="pickle_results"
mkdir -p $outdir

for env in "${envs[@]}"
do
    echo "Activating $env"
    conda activate $env

    # 获取Python版本
    pyver=$(python --version 2>&1)
    echo "Python version: $pyver"

    outfile="$outdir/result_${env}.txt"
    echo "Running compare_pickle.py in $env..."
    cover compare_pickle.py > "$outfile"

    echo "Saved output to $outfile"
    echo "-------------------------"
done

# 比较输出
echo ""
echo "Comparing outputs:"
diff $outdir/result_py36_env.txt $outdir/result_py39_env.txt || echo "py36 vs py39 differ"
diff $outdir/result_py39_env.txt $outdir/result_py311_env.txt || echo "py39 vs py311 differ"
