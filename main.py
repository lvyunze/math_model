import os
import shutil
import pandas as pd
file_path = r"E:\数据挖掘\数学建模\2021MCM_ProblemC_Files\2021MCM_ProblemC_Files"
target_path = r'E:\数据挖掘\数学建模\数据'
id_path = r'E:\数据挖掘\数学建模\2021MCM_ProblemC_ Images_by_GlobalID.xlsx'
label_path = r'E:\数据挖掘\数学建模\2021MCMProblemC_DataSet.xlsx'


def read_name():
    name = os.listdir(file_path)
    return name


def get_file_name_list():
    name = read_name()
    _name_list = [each_name[:each_name.find('.')] for each_name in name]
    return _name_list


def get_name_id():
    data = pd.read_excel(id_path)
    file_name = list(data["FileName"])
    file_id = [each_id[each_id.find('{')+1:-1] for each_id in list(data["GlobalID"])]
    data_list = list(zip(file_name, file_id))
    data_dict = {
        data[0]: data[1] for data in data_list
    }
    return data_dict


def get_label():
    data = pd.read_excel(label_path)
    file_id = [each_id[each_id.find('{')+1:-1] for each_id in list(data["GlobalID"])]
    file_label = list(data["Lab Status"])
    data_list = list(zip(file_id, file_label))
    data_dict = {
        data[0]: data[1] for data in data_list
    }
    return data_dict


def copy_file():
    name_id = get_name_id()
    id_label = get_label()
    name_label = {}
    print(len(name_id), len(id_label))
    for name, data_id in name_id.items():
        name_label[name] = id_label[data_id]
    for data_name, data_label in name_label.items():
        source = file_path + '\\' + data_name
        target = target_path + '\\' + data_label + '\\' + data_name
        shutil.copy(source, target)
    print(len(name_label))



# name_list = get_file_name_list()
# print(len(name_list))
#
# get_name_id()
# # get_label()
copy_file()