import argparse
import yaml

def update_config_file(bert_processes, emo_processes, train_processes):
    # 读取config.yml文件
    with open('config.yml', 'r') as file:
        config_data = yaml.safe_load(file)
    
    # 读取../config.yml文件
    with open('../../config.yml', 'r') as file:
        config_data2 = yaml.safe_load(file)

    config_data = json.loads(json.dumps(data).replace('false', 'False').replace('true', 'True'))
    config_data2 = json.loads(json.dumps(data).replace('false', 'False').replace('true', 'True'))

    # 更新相应字段的值
    config_data['bert_gen']['num_processes'] = bert_processes
    config_data['emo_gen']['num_processes'] = emo_processes
    config_data['train_ms']['num_processes'] = train_processes
    config_data2['bert_gen']['num_processes'] = bert_processes
    config_data2['emo_gen']['num_processes'] = emo_processes
    config_data2['train_ms']['num_processes'] = train_processes

    config_data = json.loads(json.dumps(data).replace('False', 'false').replace('True', 'true'))
    config_data2 = json.loads(json.dumps(data).replace('False', 'false').replace('True', 'true'))
    # 将更新后的数据写回文件
    with open('config.yml', 'w') as file:
        yaml.dump(config_data, file)
    # 将更新后的数据写回文件
    with open('../../config.yml', 'w') as file:
        yaml.dump(config_data2, file)

    print("config.yml文件已成功更新。")
    print("根目录config.yml文件已成功更新。")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Update config.yml with specified processes.")
    parser.add_argument("-b", type=int, default=2, help="Number of processes for bert_gen.")
    parser.add_argument("-e", type=int, default=2, help="Number of processes for emo_gen.")
    parser.add_argument("-t", type=int, default=2, help="Number of processes for train_ms.")
    args = parser.parse_args()
    update_config_file(args.b, args.e, args.t)
