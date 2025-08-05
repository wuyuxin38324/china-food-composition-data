import json
import os

def extract_foodnames_to_txt(json_folder_path, txt_file_path):
    """
    从JSON文件夹中提取foodName字段并保存到TXT文件，每行一个食品名称
    
    Args:
        json_folder_path: JSON文件夹路径
        txt_file_path: TXT文件输出路径
    """
    # 检查JSON文件夹是否存在
    if not os.path.exists(json_folder_path):
        print(f"错误: JSON文件夹 '{json_folder_path}' 不存在")
        return
    
    food_names = set()  # 使用集合避免重复
    
    try:
        # 遍历JSON文件夹中的所有文件
        for filename in os.listdir(json_folder_path):
            if filename.endswith('.json'):
                file_path = os.path.join(json_folder_path, filename)
                
                # 读取JSON文件
                with open(file_path, 'r', encoding='utf-8') as file:
                    data = json.load(file)
                    
                    # 检查数据是否是列表格式
                    if isinstance(data, list):
                        for item in data:
                            if 'foodName' in item:
                                food_names.add(item['foodName'])
                    elif isinstance(data, dict):
                        # 如果是字典格式，检查是否有foodName字段
                        if 'foodName' in data:
                            food_names.add(data['foodName'])
                        # 检查是否有包含foodName的条目列表
                        for key, value in data.items():
                            if isinstance(value, list):
                                for item in value:
                                    if 'foodName' in item:
                                        food_names.add(item['foodName'])
        
        # 将食品名称写入TXT文件
        with open(txt_file_path, 'w', encoding='utf-8') as txt_file:
            for name in sorted(food_names):  # 排序以便于查看
                txt_file.write(name + '\n')
        
        print(f"成功: 食品名称已从 '{json_folder_path}' 导出到 '{txt_file_path}'，共 {len(food_names)} 个唯一名称")
    except Exception as e:
        print(f"错误: 提取过程中发生错误 - {str(e)}")

if __name__ == "__main__":
    # 定义文件夹和文件路径
    json_folder = "json_data_vision"  # 使用json_data_vision文件夹
    txt_file = "food_names_from_json.txt"
    
    # 获取脚本所在目录
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # 构建完整的文件夹和文件路径
    json_folder_path = os.path.join(script_dir, json_folder)
    txt_file_path = os.path.join(script_dir, txt_file)
    
    # 执行提取
    extract_foodnames_to_txt(json_folder_path, txt_file_path)