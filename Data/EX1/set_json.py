import json
import argparse

# 创建解析器并添加参数
parser = argparse.ArgumentParser()
parser.add_argument('-b', '--batch_size', type=int, default=4, help='Batch size to set')
parser.add_argument('-e', '--epochs', type=int, default=100 , help='Epochs to set')
args = parser.parse_args()

# 读取json文件为字符串
with open('config.json', 'r') as file:
    data = json.load(file)

# 修改batch_size的值
data['train']['batch_size'] = args.batch_size
data['train']['epochs'] = args.epochs

# 将修改后的数据写回文件
with open('config.json', 'w') as file:
    json.dump(data, file, indent=2)