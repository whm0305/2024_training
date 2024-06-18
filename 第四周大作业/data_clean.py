import json
import os
import mysql.connector
from mysql.connector import Error

# #前置操作
# #bash
# # 1.创建并运行mysql容器 --name mysql-container：给容器命名。 -e MYSQL_ROOT_PASSWORD=my-secret-pw：设置MySQL root用户的密码。将my-secret-pw替换为自己的密码
# docker run --name whm_mysql_container -p 3307:3306 -e MYSQL_ROOT_PASSWORD=200133 -d mysql
# # 2.检查容器是否正在运行
# docker ps
# # 3.取容器的IP地址 '172.17.0.2' （4.0/4.1使用容器地址连接失败,未使用3步骤的ip地址）
# docker inspect -f '{{range.NetworkSettings.Networks}}{{.IPAddress}}{{end}}' whm_mysql_container
# # 4.0使用MySQL客户端（如mysql命令行工具）来连接到你的数据库
# mysql -h 172.17.0.2 -u root -p
# # 4.1mysql语句 为whm_database数据库设置用户主机权限（第4步连接失败的尝试）
# GRANT ALL PRIVILEGES ON whm_database.* TO 'root'@'localhost';

# # 创建并运行mysql容器，设置主机3307端口映射到容器3306上
# docker run --name whm_mysql_container -p 3307:3306 -e MYSQL_ROOT_PASSWORD=200133 -d mysql
# # 运行已存在容器
# docker start whm_mysql_container
# # 终端登录容器查看数据库（利用容器名称或ID，通过容器内部网络连接）
# docker exec -it whm_mysql_container mysql -u root -p

# 连接MySQL信息
host = 'localhost'
port = '3307'
user = 'root'
password = ''
database = 'whm_database'

# 表
TABLE_NAME = 'data_info_table'

# 读取JSON文件
with open('E:\\小米\\homework\\single-vehicle-side-example\\data_info.json', 'r') as f:
    data_info = json.load(f)

# 连接数据库
def connect_to_mysql():
    # 连接到MySQL数据库
    connection = mysql.connector.connect(
        host=host,
        port=port,
        user=user,
        password=password,
        database=database
    )
    print("MySQL Container connect successfully")
    return connection

# 创建表
def create_table(cursor,TABLE_NAME):
    # 定义SQL语句创建表结构
    create_table_sql = """
        CREATE TABLE IF NOT EXISTS {}(
        id INT AUTO_INCREMENT PRIMARY KEY,
        
        image_path VARCHAR(255) NOT NULL,
        image_timestamp BIGINT NOT NULL,
        pointcloud_path VARCHAR(255) NOT NULL,
        point_cloud_stamp BIGINT NOT NULL,
        calib_camera_intrinsic_path VARCHAR(255) NOT NULL,
        calib_lidar_to_camera_path VARCHAR(255) NOT NULL,
        label_camera_std_path VARCHAR(255) NOT NULL,
        label_lidar_std_path VARCHAR(255) NOT NULL, 
        
        image_size BIGINT,
        pointcloud_size BIGINT,
        
        calib_camera_intrinsic TEXT,
        calib_lidar_to_camera TEXT,
        label_camera_std TEXT,
        label_lidar_std TEXT
        )
        """.format(TABLE_NAME)
    cursor.execute(create_table_sql)

# 插入基础数据函数 与 二进制文件大小数据
def insert_data(cursor,data_item,TABLE_NAME):
    # 插入data_info.json信息
    Insert_sql = '''  
    INSERT INTO {} (image_path, image_timestamp, pointcloud_path, point_cloud_stamp,
    calib_camera_intrinsic_path, calib_lidar_to_camera_path,
    label_camera_std_path, label_lidar_std_path,image_size,pointcloud_size,
    calib_camera_intrinsic,calib_lidar_to_camera,label_camera_std,label_lidar_std)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) 
    '''.format(TABLE_NAME)

    # 直接获取二进制文件大小,windows系统，需要调整文件路径
    imagepath1 = data_item['image_path'].replace('/','\\')
    pointcloudpath1 = data_item['pointcloud_path'].replace('/','\\')
    imagepath = os.path.join('single-vehicle-side-example',imagepath1)
    pointcloudpath = os.path.join('single-vehicle-side-example',pointcloudpath1)
    if os.path.exists(imagepath):
        image_size = os.path.getsize(imagepath)
        #print("image路径：", imagepath)
        #print("image_size:",image_size)
    else:
        image_size = None
        #print("image路径不存在：", imagepath)
    if os.path.exists(pointcloudpath):
        pointcloud_size = os.path.getsize(pointcloudpath)
        #print("pointcloud路径：",pointcloudpath)
        #print("pointcloud_size:", pointcloud_size)
    else:
        pointcloud_size = None
        #print("pointcloud路径不存在：",pointcloudpath)

    values = (
        data_item['image_path'],
        data_item['image_timestamp'],
        data_item['pointcloud_path'],
        data_item['point_cloud_stamp'],
        data_item['calib_camera_intrinsic_path'],
        data_item['calib_lidar_to_camera_path'],
        data_item['label_camera_std_path'],
        data_item['label_lidar_std_path'],
        image_size,
        pointcloud_size,
        None,
        None,
        None,
        None
    )
    cursor.execute(Insert_sql, values)

# 更新文本数据
def update_link_data(cursor,data_item,TABLE_NAME):
    id_sql = '''
    SELECT LAST_INSERT_ID();
    '''
    cursor.execute(id_sql)
    item_id = cursor.fetchone()[0]  # fetchone()返回一个元组，只需要第一个元素
    #print("id:",item_id)
    if item_id is None:
        print("数据项中未找到'id' 键")
        return

    # 处理文件路径
    calib_camera_intrinsic_path = os.path.join('single-vehicle-side-example', data_item['calib_camera_intrinsic_path'].replace('/', '\\'))
    if os.path.exists(calib_camera_intrinsic_path):
        with open(calib_camera_intrinsic_path,'r') as file:
            content = file.read()
            # 更新文本内容的SQL语句模板
            content_column = 'calib_camera_intrinsic'
            update_text_content = f"UPDATE {TABLE_NAME} SET {content_column}=%s WHERE id=%s"
            #print(f"file Id: {item_id} saved successfully")
            cursor.execute(update_text_content,(content,item_id))

    calib_lidar_to_camera_path = os.path.join('single-vehicle-side-example', data_item['calib_lidar_to_camera_path'].replace('/', '\\'))
    if os.path.exists(calib_lidar_to_camera_path):
        with open(calib_lidar_to_camera_path,'r') as file:
            content = file.read()
            # 更新文本内容的SQL语句模板
            content_column = 'calib_lidar_to_camera'
            update_text_content = f"UPDATE {TABLE_NAME} SET {content_column}=%s WHERE id=%s"
            #print("calib_lidar_to_camera content:",content)
            cursor.execute(update_text_content,(content,item_id))
            #print(f"file Id: {item_id} saved successfully")

    label_camera_std_path = os.path.join('single-vehicle-side-example', data_item['label_camera_std_path'].replace('/', '\\'))
    if os.path.exists(label_camera_std_path):
        with open(label_camera_std_path,'r') as file:
            content = file.read()
            # 更新文本内容的SQL语句模板
            content_column = 'label_camera_std'
            update_text_content = f"UPDATE {TABLE_NAME} SET {content_column}=%s WHERE id=%s"
            #print("label_camera_std content:",content)
            cursor.execute(update_text_content,(content,item_id))
            #print(f"file Id: {item_id} saved successfully")

    label_lidar_std_path = os.path.join('single-vehicle-side-example', data_item['label_lidar_std_path'].replace('/', '\\'))
    if os.path.exists(label_lidar_std_path):
        with open(label_lidar_std_path,'r') as file:
            content = file.read()
            # 更新文本内容的SQL语句模板
            content_column = 'label_lidar_std'
            update_text_content = f"UPDATE {TABLE_NAME} SET {content_column}=%s WHERE id=%s"
            #print("label_lidar_std content:",content)
            cursor.execute(update_text_content,(content,item_id))
            print(f"file Id: {item_id} saved successfully")

# 主程序
def main():
    try:
        # 连接数据库和游标
        connection = connect_to_mysql()
        cursor = connection.cursor()

        # 创建表
        create_table(cursor,TABLE_NAME)

        # 插入和更新数据
        for data_item in data_info:
            insert_data(cursor,data_item,TABLE_NAME)
            update_link_data(cursor,data_item,TABLE_NAME)

        # 提交连接
        connection.commit()

        # 关闭连接
        cursor.close()
        connection.close()

    except mysql.connector.Error as err:
        print(f"Error while connecting MySQL: {err}")
    except Error as e:
        print(f"Error while creating table: {e}")
    finally:
        # 关闭游标和连接
        if connection.is_connected():
            connection.close()
        if cursor:
            cursor.close()

if __name__ == "__main__":
    main()
