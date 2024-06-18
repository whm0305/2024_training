import zipfile
import requests
import zipfile

#获取下载链接的内容
content = requests.get('https://bj.bcebos.com/apollo-air/v2-2022-01-08/'
                       'single-vehicle-side-example_16011558474489856.zip?'
                       'authorization=bce-auth-v1%2F62ff93831d5840338d0fcc9585430b3a%'
                       '2F2024-06-11T14%3A22%3A32Z%2F604800%2F%2F64ab5f606c97675dc2e71'
                       '7515f33ebcd7ca66a6534874584509b4e35bad89539').content
#以二进制写方式打开新命名压缩包example.zip，把下载内容写入
open("E:\\小米\\homework\\example.zip","wb").write(content)
print("ZIP文件下载完成")
# 打开zip文件
with zipfile.ZipFile("E:\\小米\\homework\\example.zip", 'r') as zip_ref:
    # 解压文件到指定目录
    zip_ref.extractall("E:\\小米\\homework\\")
print("ZIP文件解压完成")
