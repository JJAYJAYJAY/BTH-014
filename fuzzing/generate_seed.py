import random

# 生成一个随机的seed
seed = random.randint(0, 2**32 - 1)

# 将seed写入当前目录的txt文件
with open('random_seed.txt', 'w') as f:
    f.write(str(seed))