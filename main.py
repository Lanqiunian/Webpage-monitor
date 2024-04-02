import requests
import time
from datetime import datetime
from plyer import notification  # 引入通知功能
import webbrowser

def fetch_content(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except Exception as e:
        print(f"Error fetching the webpage: {e}")
        return None

def check_updates(url, previous_content):
    current_content = fetch_content(url)
    if current_content is None:
        return previous_content  # 如果获取内容失败，返回之前的内容

    # 获取当前时间
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if previous_content is None:
        print(f"[{current_time}] 初始化检查...")
    elif previous_content != current_content:
        notification.notify(
            title='网页更新通知',
            message='检测到网页内容变化，请检查。',
            app_name='网页变化检测'
        )
        print(f"[{current_time}] 检测到内容变化！正在打开网页...")
        webbrowser.open(url)  # 使用默认浏览器打开网页
    else:
        print(f"[{current_time}] 内容未发生变化。")

    return current_content

def main():
    url = input("请输入要检测的网址：")
    interval = int(input("请输入检测间隔（秒）："))
    previous_content = None

    # 循环检查直到用户中断
    while True:
        previous_content = check_updates(url, previous_content)
        time.sleep(interval)  # 等待时间（秒），根据需要调整

if __name__ == "__main__":
    main()
