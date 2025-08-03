import json
import sqlite3
import os

def process_json_to_db_as_text(json_folder, db_file):
    """
    遍历指定文件夹中的JSON文件，将所有数据作为TEXT类型导入SQLite数据库。
    """
    # 连接到SQLite数据库，如果文件不存在则自动创建
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    # 创建数据表
    # 将所有字段都定义为TEXT类型
    cursor.execute("DROP TABLE IF EXISTS foods")
    create_table_sql = """
    CREATE TABLE foods (
        foodCode TEXT,
        foodName TEXT,
        edible TEXT,
        water TEXT,
        energyKCal TEXT,
        energyKJ TEXT,
        protein TEXT,
        fat TEXT,
        CHO TEXT,
        dietaryFiber TEXT,
        cholesterol TEXT,
        ash TEXT,
        vitaminA TEXT,
        carotene TEXT,
        retinol TEXT,
        thiamin TEXT,
        riboflavin TEXT,
        niacin TEXT,
        vitaminC TEXT,
        vitaminETotal TEXT,
        vitaminE1 TEXT,
        vitaminE2 TEXT,
        vitaminE3 TEXT,
        Ca TEXT,
        P TEXT,
        K TEXT,
        Na TEXT,
        Mg TEXT,
        Fe TEXT,
        Zn TEXT,
        Se TEXT,
        Cu TEXT,
        Mn TEXT,
        remark TEXT,
        type TEXT
    );
    """
    cursor.execute(create_table_sql)
    print("数据表 'foods' 创建成功，所有字段均为TEXT类型。")

    # 遍历文件夹中的所有JSON文件
    for filename in os.listdir(json_folder):
        if filename.endswith(".json"):
            file_path = os.path.join(json_folder, filename)
            file_type = os.path.splitext(filename)[0]  # 使用文件名作为 type 字段的值

            print(f"正在处理文件: {filename}")

            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    data = json.load(f)

                    for item in data:
                        # 准备插入的SQL语句
                        insert_sql = """
                        INSERT INTO foods VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
                        """

                        # 按照数据库字段顺序准备数据
                        # 使用str()确保所有值都被转换为字符串
                        values = (
                            str(item.get("foodCode", '')),
                            str(item.get("foodName", '')),
                            str(item.get("edible", '')),
                            str(item.get("water", '')),
                            str(item.get("energyKCal", '')),
                            str(item.get("energyKJ", '')),
                            str(item.get("protein", '')),
                            str(item.get("fat", '')),
                            str(item.get("CHO", '')),
                            str(item.get("dietaryFiber", '')),
                            str(item.get("cholesterol", '')),
                            str(item.get("ash", '')),
                            str(item.get("vitaminA", '')),
                            str(item.get("carotene", '')),
                            str(item.get("retinol", '')),
                            str(item.get("thiamin", '')),
                            str(item.get("riboflavin", '')),
                            str(item.get("niacin", '')),
                            str(item.get("vitaminC", '')),
                            str(item.get("vitaminETotal", '')),
                            str(item.get("vitaminE1", '')),
                            str(item.get("vitaminE2", '')),
                            str(item.get("vitaminE3", '')),
                            str(item.get("Ca", '')),
                            str(item.get("P", '')),
                            str(item.get("K", '')),
                            str(item.get("Na", '')),
                            str(item.get("Mg", '')),
                            str(item.get("Fe", '')),
                            str(item.get("Zn", '')),
                            str(item.get("Se", '')),
                            str(item.get("Cu", '')),
                            str(item.get("Mn", '')),
                            str(item.get("remark", '')),
                            file_type  # 新增的 type 字段
                        )
                        
                        cursor.execute(insert_sql, values)

            except json.JSONDecodeError as e:
                print(f"文件 {filename} JSON解析错误: {e}")
            except Exception as e:
                print(f"处理文件 {filename} 时发生错误: {e}")

    # 提交更改并关闭连接
    conn.commit()
    conn.close()
    print("所有文件处理完毕，数据已成功导入数据库。")

# 示例调用
# 假设你的所有JSON文件都放在一个名为 'json_files' 的文件夹里
json_folder_path = 'china-food-composition-data/json_data_vision'  
database_file_path = 'china-food-composition-data/food_data.db'

if not os.path.exists(json_folder_path):
    print(f"文件夹 '{json_folder_path}' 不存在，请创建并放入JSON文件。")
else:
    process_json_to_db_as_text(json_folder_path, database_file_path)