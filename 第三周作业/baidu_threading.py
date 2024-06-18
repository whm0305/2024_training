import requests
import threading

# 锁 用于同步写入文件
lock = threading.Lock()
def fetch_and_save_html(url, file_path):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    try:
        response = requests.get(url, headers=headers) # request获取网页内容
        response.raise_for_status()  # 检查 HTTP 响应的状态码，并在状态码表示错误时引发一个 HTTPError 异常
        # 使用锁来确保文件写入时的线程安全
        with lock:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(response.text)
        print(f"HTML from {url} has been saved to {file_path}")
    except requests.RequestException as e:
        print(f"Error fetching the page {url}: {e}")
# 创建一个线程列表
threads = []
# 爬取多个页面
urls = ['https://www.baidu.com', 'https://hectorstatic.baidu.com']  # URL列表
file_paths = ['baidu_homepage1.html', 'baidu_homepage2.html']  # 对应的文件路径列表

# 为每个URL和文件路径创建一个线程
for url, file_path in zip(urls, file_paths):
    t = threading.Thread(target=fetch_and_save_html, args=(url, file_path))
    threads.append(t)
    t.start()

# 等待所有线程完成
for t in threads:
    t.join()

print("All threads have finished.")


# 此爬取方式少了很多数据内容，仅保留了部分数据格式
# # 获取下载链接的内容
# content = requests.get('https://baidu.com').content
# # 以二进制写方式打开新命名压缩包example.zip，把下载内容写入
# open("E:\\小米\\python_code\\baidu.html","wb").write(content)
# print("baidu data has been downloaded")