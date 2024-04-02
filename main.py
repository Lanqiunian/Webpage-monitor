import json
import threading

import requests
import time
from datetime import datetime

from PyQt6.QtGui import QTextCursor
from plyer import notification  # 引入通知功能
import webbrowser
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QTextEdit, QMessageBox, QDialog, QVBoxLayout, QLabel, QPushButton
from main_window import Ui_MainWindow  # 导入从.ui文件生成的类

config_file = "config.json"


class OutputRedirector(object):
    def __init__(self, text_widget):
        self.text_widget = text_widget

    def write(self, message):
        # 直接使用insertPlainText添加文本，手动控制新行
        self.text_widget.insertPlainText(message)
        # 确保滚动到文本末尾以便总是显示最新的日志
        self.text_widget.moveCursor(QTextCursor.MoveOperation.End)

    def flush(self):
        pass


class MyMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # 初始化UI界面


def fetch_content(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except Exception as e:
        print(f"Error fetching the webpage: {e}")
        return None


def load_config():
    with open(config_file, "r") as f:
        return json.load(f)


def save_config(url, interval):
    with open(config_file, "w") as f:
        json.dump({"url": url, "interval": interval}, f)


def check_updates(url, previous_content, log_output, timeOfChange):
    current_content = fetch_content(url)
    if current_content is None:
        return previous_content  # 如果获取内容失败，返回之前的内容

    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if previous_content is None:
        log_output(f"[{current_time}] 初始化检查...")
    elif previous_content != current_content:
        notification.notify(
            title='网页更新通知',
            message='检测到网页内容变化，请检查。',
            app_name='网页变化检测'
        )
        log_output(f"[{current_time}] 检测到内容变化！正在打开网页...")
        timeOfChange += 1
        webbrowser.open(url)
    else:
        log_output(f"[{current_time}] 内容未发生变化。")

    return current_content


def log_output(message):
    print(message)  # 使用print，现在它被重定向到 QTextEdit


import threading


class AboutDialog(QDialog):
    def __init__(self):
        super(AboutDialog, self).__init__()
        self.setWindowTitle("关于")


        layout = QVBoxLayout()

        # 添加内容到对话框
        layout.addWidget(QLabel("<p>这是一个通知监控程序，专为等待重要通知的用户设计。</p>"
                                "<p><b>开发背景:</b><br>"
                                "<p>本人考研结束后，面对等待各种成绩结果、分数线和待录取通知的焦虑期，</p>"
                                "<p>开发了这个小工具。本程序旨在实时监控相关网站的更新，</p>"
                                "<p>开一旦有更新，立即通知用户，并且使用浏览器打开网站，</p>"
                                "以便用户及时获取最新的录取信息。</p>"
                                "<p>我们理解等待的焦虑，并致力于通过实时更新减轻您的担忧。</p>"
                                "<p><i>版权所有 ©2024。</i></p>"))

        # 添加关闭按钮
        closeButton = QPushButton("关闭")
        closeButton.clicked.connect(self.close)
        layout.addWidget(closeButton)

        self.setLayout(layout)


class Monitor:
    def __init__(self):
        self.mainWindow = MyMainWindow()
        self.mainWindow.show()

        self.mainWindow.pushButton_operator.clicked.connect(self.monitor)
        self.mainWindow.actionAbout.triggered.connect(self.showAboutDialog)
        # 重定向输出到 QTextEdit
        self.TimesOfChange = 0
        sys.stdout = OutputRedirector(self.mainWindow.textEdit_log)
        self.monitoring_active = False  # 新增一个属性来控制监控状态
        self.monitor_thread = None  # 用于存储监控线程的引用
        self.setup_config()

    def showAboutDialog(self):
        print("显示关于对话框。")
        # 创建并显示“关于”对话框
        about_dialog = AboutDialog()
        about_dialog.exec()

    def monitor(self):
        if not self.monitoring_active:
            try:
                url = self.mainWindow.lineEdit_url.text()
                interval = int(self.mainWindow.lineEdit_interval.text())
                if not url or not interval:
                    log_output("URL和间隔不能为空。")
                    return
                # 更新监控状态
                self.monitoring_active = True
                # 保存配置，并启动监控线程
                save_config(url, interval)
                self.monitor_thread = threading.Thread(target=self.monitor_loop, args=(url, interval), daemon=True)
                self.monitor_thread.start()
                log_output("监控开始。")
                self.setup_config()
                self.mainWindow.label_startTime.setText(str(datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

            except ValueError:
                QMessageBox.warning(self.mainWindow, "错误", "间隔必须是一个整数。")

            except Exception as e:
                log_output("监控失败：" + str(e))

        else:
            self.monitoring_active = False  # 更新监控状态为停止
            log_output("监控停止。")
            self.setup_config()
            # 注意：这里不直接停止线程，而是通过设置标志来让线程自然退出

    def monitor_loop(self, url, interval):
        previous_content = None
        while self.monitoring_active:  # 根据监控状态决定是否继续循环
            previous_content = check_updates(url, previous_content, log_output, self.TimesOfChange)
            time.sleep(interval)

    def setup_config(self):
        try:
            config = load_config()
            self.mainWindow.lineEdit_url.setText(config["url"])
            self.mainWindow.lineEdit_interval.setText(str(config["interval"]))
            self.mainWindow.pushButton_operator.setText("停止" if self.monitoring_active else "开始")
            self.mainWindow.label_status.setText("正在监控中" if self.monitoring_active else "监控未开始")
            self.mainWindow.label_status.setStyleSheet(
                "QLabel { color : green; }" if self.monitoring_active else "QLabel { color : red; }")
            self.mainWindow.label_TimesOfChange.setText(str(self.TimesOfChange))
        except Exception as e:
            log_output("加载配置失败：" + str(e))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    monitor = Monitor()
    sys.exit(app.exec())
