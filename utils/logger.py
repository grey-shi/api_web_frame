import logging, time
import os
from os.path import exists

class Log(object):
    # 定义一个名为Log的类，用于自定义日志记录器。
    def __init__(self, log_path):
        self.log_name = os.path.join(log_path, f'{time.strftime("%Y-%m-%d")}.log')
        self.log_path = log_path
        # 这是类的初始化方法，接收一个log_path参数，用于设置日志文件的路径。在初始化时，会根据当前日期生成一个日志文件名。

    def __printconsole(self, level, message):
        # 创建一个日志记录器,并设置日志级别为INFO。
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)

        # os.makedirs 功能: 递归地创建目录。如果目标路径中的任何中间目录不存在，os.makedirs会自动创建这些中间目录。
        # os.mldir不会 递归地创建目录
        if not os.path.exists(self.log_path):
            os.makedirs(self.log_path)

        file_handler = logging.FileHandler(self.log_name, 'a+', encoding='utf-8')
        file_handler.setLevel(logging.INFO)

        # 创建一个用于输出到控制台的处理器(StreamHandler)，设置日志级别为INFO。
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)

        # 创建格式化器并将其添加到处理器, 定义日志输出格式，包括日期、日志名称、日志级别和日志信息。
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)

        # 将处理器添加到日志记录器
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

        # 记录一条日志,根据日志级别记录相应的日志信息。
        if level == 'info':
            logger.info(message)
        elif level == 'debug':
            logger.debug(message)
        elif level == 'warning':
            logger.warning(message)
        elif level == 'error':
            logger.error(message)

        # 移除处理器，以防止重复输出。
        logger.removeHandler(console_handler)
        logger.removeHandler(file_handler)

        # 关闭文件处理器。
        file_handler.close()

    # 这些方法分别是对外暴露的记录不同日志级别信息的接口。它们实际上调用了__printconsole()方法来进行日志记录。
    def debug(self, message):
        self.__printconsole('debug', message)

    def info(self, message):
        self.__printconsole('info', message)

    def warning(self, message):
        self.__printconsole('warning', message)

    def error(self, message):
        self.__printconsole('error', message)