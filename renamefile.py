import os
import csv
import shutil


def get_department_from_path(file_path):
    # 获取文件路径中的部门名称
    parts = file_path.split(os.path.sep)
    # 假设部门名称在文件路径中的第三级目录
    department = parts[5]
    return department


def rename_files_based_on_csv(input_folder, csv_filename, output_folder):
    # 创建输出文件夹
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # 读取CSV文件内容并建立部门到新文件名的映射关系
    department_to_new_filename = {}
    with open(csv_filename, 'r', newline='', encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            filename = row[0]     # 第一列为文件名
            department = row[1]  # 第二列为部门名称
            department1 = row[2]  # 第二列为部门名称
            department2 = row[3]  # 第二列为部门名称
            department3 = row[4]  # 第二列为部门名称
            department4 = row[5]  # 第二列为部门名称
            department5 = row[6]  # 第二列为部门名称
            new_filename = row[7] # 第七列为新文件名
            pathstr = os.path.join(department1, department2, department3, department4, department5)
            department_to_new_filename[(department, filename)] = new_filename + '$' + pathstr

    # 遍历文件夹及其子文件夹中的所有文件
    for root, _, files in os.walk(input_folder):
        for file in files:
            file_path = os.path.join(root, file)
            # 获取部门名称，使用文件路径中的第三级目录名称
            department = get_department_from_path(file_path)  # 获取最后一级目录名称
            # 检查部门名称和文件名是否在CSV文件中
            if (department, file) in department_to_new_filename:
                # 获取新文件名
                records = department_to_new_filename[(department, file)]
                new_filename = records.split('$')[0]
                tmppath = records.split('$')[-1]
                # 获取目标文件夹路径
                # output_subfolder = os.path.join(output_folder, department,tmppath) 
                output_subfolder = os.path.join(output_folder,tmppath) 
                if not os.path.exists(output_subfolder):
                    os.makedirs(output_subfolder)
                # 移动并重命名文件
                new_file_path = os.path.join(output_subfolder, new_filename)
                shutil.copy2(file_path, new_file_path)
                # print(f"File '{file}' renamed to '{new_filename}' and saved to '{new_file_path}'.")

# 输入文件夹、CSV文件和输出文件夹的路径
input_folder = r"e:\users\ShiXQ01\Desktop\files"
csv_filename = r"e:\users\ShiXQ01\Downloads\knowledge_file_202403132030.csv"
output_folder = r"e:\users\ShiXQ01\Desktop\renamefiles"

# 调用函数进行文件重命名
rename_files_based_on_csv(input_folder, csv_filename, output_folder)