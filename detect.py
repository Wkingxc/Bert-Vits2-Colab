import os
import shutil

# 定义源目录和目标目录
src_dir = './Data/EX1/models/'
dst_dir = '/content/gdrive/MyDrive/models/'

# 获取源目录中的所有文件
files = os.listdir(src_dir)

# 将文件按类别（G、D、WD）分组
g_files = [file for file in files if file.startswith('G_')]
d_files = [file for file in files if file.startswith('D_')]
wd_files = [file for file in files if file.startswith('WD_')]

# 对每个类别的文件列表进行排序，以找到最新的文件（即数字最大的文件）
latest_g_file = max(g_files, key=lambda file: int(file.split('_')[1].split('.')[0]))
latest_d_file = max(d_files, key=lambda file: int(file.split('_')[1].split('.')[0]))
latest_wd_file = max(wd_files, key=lambda file: int(file.split('_')[1].split('.')[0]))

# 将最新的文件复制到目标目录
shutil.copy(os.path.join(src_dir, latest_g_file), dst_dir)
shutil.copy(os.path.join(src_dir, latest_d_file), dst_dir)
shutil.copy(os.path.join(src_dir, latest_wd_file), dst_dir)