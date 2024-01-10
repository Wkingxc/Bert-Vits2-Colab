import os
import re
import argparse

def download_from_gdrive(original_link):
    # 提取文件 ID
    file_id = re.search(r'/d/(.*?)/view', original_link).group(1)
    
    # 创建 gdown 可以识别的链接
    gdown_link = f'https://drive.google.com/uc?id={file_id}'
    
    # 使用 gdown 命令下载文件
    os.system(f'gdown {gdown_link}')
    # print(gdown_link)

# 创建解析器并添加参数
parser = argparse.ArgumentParser()
parser.add_argument('-u', '--url', type=str, required=True, help='需要下载的谷歌文件分享链接')
args = parser.parse_args()

download_from_gdrive(args.url)