# !/bin/bash

# 启用 bash 的错误追踪和变量展开调试
set -e
set -o pipefail

# 设置环境名
envs=("py311")
os_name="$(uname | tr '[:upper:]' '[:lower:]')"
# 设置输出目录
outdir="test_results"


for env in "${envs[@]}"; do
    echo "Activating $env"
    # 激活 Conda 环境（注意 source 和 conda.sh 的位置可能因安装方式不同而异）
    source "$(conda info --base)/etc/profile.d/conda.sh"
    conda activate "$env"
    pip install pytest coverage
    echo "Running compare_pickle.py in $env..."
    coverage run -m pytest ./black_test/ ./fuzzing/ ./white_test/ ./boundary_value_test/ > "$outdir/result_${os_name}_${env}.txt"

    echo "Saved output to $outdir/result_${env}.txt"
    echo "-------------------------"
done

echo
