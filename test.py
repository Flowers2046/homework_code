import pandas as pd

def print_csv_info(file_path):
    # 尝试使用 ISO-8859-1 编码打开文件
    try:
        df = pd.read_csv(file_path, encoding='ISO-8859-1')
    except UnicodeDecodeError:
        # 如果 ISO-8859-1 失败，尝试 utf-16
        df = pd.read_csv(file_path, encoding='utf-16')

    # 打印前10行
    print("前10行数据：")
    print(df.head(10))

    # 打印数据概览
    print("\n数据概览：")
    print(df.info())

    # 打印每列的基本统计信息
    print("\n每列的统计信息：")
    print(df.describe())

    # 打印每列的缺失值数量
    print("\n每列的缺失值数量：")
    print(df.isnull().sum())


if __name__ == '__main__':
    # 示例：使用文件路径调用该函数
    file_path = '/Users/yang/PycharmProjects/AgentScope/ReKT/data/ASSIST09/skill_builder_data_corrected_collapsed.csv'  # 请替换为实际文件路径
    print_csv_info(file_path)