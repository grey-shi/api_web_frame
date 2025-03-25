import os
import yaml
from common.logger import Log

consult_path = os.path.dirname(__file__)
parent_path = os.path.dirname(consult_path)
log = Log()


def write_yaml(data):
    # 写入：追加
    with open(parent_path+"/extract.yaml", encoding="utf-8", mode="a+") as f:
        yaml.dump(data, stream=f, allow_unicode=True)


def read_yaml(key):
    # 读取
    with open(parent_path+"/extract.yaml", encoding="utf-8", mode="r") as f:
        value = yaml.load(f, yaml.FullLoader)
        log.info(value[key])
        return value[key]


def clear_yaml():
    # 清空
    with open(parent_path+"/extract.yaml", encoding="utf-8", mode="w") as f:
        f.truncate()


def read_yaml_testcase(yamlpath):
    # 读取
    with open(parent_path+'\\'+yamlpath, encoding="utf-8", mode="r") as f:
        value = yaml.load(f, yaml.FullLoader)
        return value
