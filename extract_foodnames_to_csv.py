import json
import os
import csv

def extract_foodnames_to_csv(json_folder, output_csv):
    """
    遍历指定文件夹中的JSON文件，提取所有foodName字段，并保存到CSV文件中。
    """
    # 创建输出CSV文件
    with open(output_csv, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        # 写入表头
        writer.writerow(['foodName'])

        # 遍历文件夹中的所有JSON文件
        for filename in os.listdir(json_folder):
            if filename.endswith(".json"):
                file_path = os.path.join(json_folder, filename)
                print(f"正在处理文件: {filename}")

                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        data = json.load(f)

                        for item in data:
                            # 提取foodName字段
                            food_name = item.get("foodName", "")
                            if food_name:
                                # 写入CSV文件
                                writer.writerow([food_name])
                except json.JSONDecodeError as e:
                    print(f"文件 {filename} JSON解析错误: {e}")
                except Exception as e:
                    print(f"处理文件 {filename} 时发生错误: {e}")

    print(f"所有文件处理完毕，食品名称已成功导出到 {output_csv}")

# 示例调用
# 使用json_data_vision文件夹，因为这是用户最近修改的路径
json_folder_path = 'china-food-composition-data/json_data_vision'
output_csv_path = 'china-food-composition-data/food_names.csv'

if not os.path.exists(json_folder_path):
    print(f"文件夹 '{json_folder_path}' 不存在，请检查路径。")
else:
    extract_foodnames_to_csv(json_folder_path, output_csv_path)