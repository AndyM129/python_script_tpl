#!/usr/bin/python3

import functools
import inspect
import os
import sys
import time
import argparse
import textwrap
from colorama import *


# =========================================== COPYRIGHT ===========================================
SCRIPT_NAME = 'python_script_class_tpl.py'
SCRIPT_DESC = 'Python 脚本模板，已预制常用常量、变量、方法定义，及复杂参数解析，以便快速开始核心编程。'
SCRIPT_VERSION = '1.0.0'
SCRIPT_UPDATETIME = '2025/04/15'
AUTHER_NAME = 'Andy Meng'
AUTHER_EMAIL = 'andy_m129@163.com'
AUTHOR_URL = 'https://juejin.cn/user/2875978147966855'
README_URL = 'https://github.com/AndyM129'
SCRIPT_UPDATE_LOG = '''
### 2025/04/15: v1.0.0
* 更新为面向对象的脚本模板

### 2022/10/30: v0.1.0
* 完成脚本模板的搭建
'''


# =========================================== GLOBAL CONST ===========================================
TIMESTAMP = int(time.time())  # 当前时间戳，eg. 1617351251
DATE_TIME = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(TIMESTAMP))  # 当前时间，eg. 2021-04-02 16:14:11
DATE_STAMP = time.strftime('%Y%m%d%H%M%S', time.localtime(TIMESTAMP))  # 当前时间戳，eg. 20210402161411
CURRENT_PATH = os.getcwd()  # 当前所在路径
CURRENT_SCRIPT_FILE = __file__  # 当前脚本文件路径
CURRENT_SCRIPT_DIR = os.path.dirname(CURRENT_SCRIPT_FILE)  # 当前的文件目录
CURRENT_SCRIPT_BASENAME = os.path.basename(CURRENT_SCRIPT_FILE)  # 当前脚本的文件名
CURRENT_SCRIPT_BASENAME_TITLE = '.'.join(CURRENT_SCRIPT_BASENAME.split('.')[0:-1])  # 文件名（不含后缀）
CURRENT_SCRIPT_BASENAME_EXT = CURRENT_SCRIPT_BASENAME.split('.')[-1]  # 文件后缀


# =========================================== Decorator ===========================================

# 装饰器：打印函数调试信息
def print_debug_func_info(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        stack = inspect.stack()  # 获取当前调用栈
        caller_frame = stack[1]  # 获取装饰器调用的上一层（即方法定义的位置）
        filename = os.path.basename(caller_frame.filename)
        lineno = caller_frame.lineno  # 获取行号
        instance = args[0]  # 获取当前实例
        cls_name = type(instance).__name__ if args else "UnknownClass"  # 获取类名
        method_name = func.__name__  # 获取方法名
        bound = inspect.signature(func).bind(*args, **kwargs)  # 获取参数信息
        bound.apply_defaults()

        instance.print_debug(f"[FUNC] {filename}:{lineno} - {cls_name}.{method_name}() - {bound.arguments}")  # 打印调试信息
        return func(*args, **kwargs)  # 调用原函数
    return wrapper

# =========================================== Script Class ===========================================


class Script:

    # 构造方法，初始化属性
    def __init__(self):
        self.parse_arguments()

    # 定义常用方法
    def debug_time(self): time_str = (time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))); return f'[{time_str}] ' if self.args.debug else ''
    def print_noset(self, string='', end='\n'): print(self.debug_time() + string, end=end)
    def print_debug(self, string='', end='\n'): print(f'{Fore.LIGHTBLACK_EX}{Style.BRIGHT}{self.debug_time() + string}{Style.RESET_ALL}', end=end) if self.args.debug else None
    def print_verbose(self, string='', end='\n'): print(f'{Fore.WHITE}{self.debug_time() + string}{Style.RESET_ALL}', end=end) if self.args.verbose else None
    def print_info(self, string='', end='\n'): print(f'{Fore.LIGHTCYAN_EX}{self.debug_time() + string}{Style.RESET_ALL}', end=end)
    def print_warning(self, string='', end='\n'): print(f'{Fore.LIGHTYELLOW_EX}{self.debug_time() + string}{Style.RESET_ALL}', end=end)
    def print_success(self, string='', end='\n'): print(f'{Fore.LIGHTGREEN_EX}{self.debug_time() + string}{Style.RESET_ALL}', end=end)
    def print_error(self, string='', end='\n'): print(f'{Fore.LIGHTRED_EX}{self.debug_time() + string}{Style.RESET_ALL}', end=end)
    def print_fatal(self, string='', end='\n', code=1): print(f'{Fore.LIGHTRED_EX}{self.debug_time() + Style.BRIGHT}{string}{Style.RESET_ALL}', end=end); sys.exit(code) if code != 0 else None
    def os_system(self, command, auto_exit=True): self.print_debug(f'$ {command}'); res = os.system(command); self.parser.exit() if res != 0 and auto_exit else None; return res  # 执行Shell 并打印命令、结果
    def arg_help_zh(self, string=''): return f'{Fore.LIGHTBLACK_EX}{Style.BRIGHT} （{string}）{Style.RESET_ALL}' if len(string) > 0 else ''
    def arg_help(self, en='', zh=''): return f'{en} {Fore.LIGHTBLACK_EX}{Style.BRIGHT}（{zh}）{Style.RESET_ALL}' if len(zh) > 0 else f'{en}'

    # 测试日志打印
    @print_debug_func_info
    def print_tests(self):
        self.print_noset(f' Log 示例 '.center(120, '='))
        self.print_debug(f'[debug] This is {SCRIPT_NAME} ({SCRIPT_VERSION})')
        self.print_verbose(f'[verbose] This is {SCRIPT_NAME} ({SCRIPT_VERSION})')
        self.print_info(f'[info] This is {SCRIPT_NAME} ({SCRIPT_VERSION})')
        self.print_warning(f'[warning] This is {SCRIPT_NAME} ({SCRIPT_VERSION})')
        self.print_success(f'[success] This is {SCRIPT_NAME} ({SCRIPT_VERSION})')
        self.print_error(f'[error] This is {SCRIPT_NAME} ({SCRIPT_VERSION})')
        self.print_fatal(f'[fatal] This is {SCRIPT_NAME} ({SCRIPT_VERSION})', code=0)
        self.os_system(f'pwd')
        self.print_debug()

    # 解析命令行参数
    def parse_arguments(self):
        self.parser = argparse.ArgumentParser(
            formatter_class=argparse.RawDescriptionHelpFormatter,
            prog=SCRIPT_NAME,
            prefix_chars='-+',
            description=textwrap.dedent(f'''
                {Fore.LIGHTCYAN_EX}
                脚本名称：{SCRIPT_NAME}
                功能简介：{SCRIPT_DESC}
                当前版本：{SCRIPT_VERSION}
                最近更新：{SCRIPT_UPDATETIME}
                作    者：{AUTHER_NAME} <{AUTHER_EMAIL}> ({AUTHOR_URL})
                说明文档：{README_URL}
                {Style.RESET_ALL}
            '''),
            epilog=textwrap.dedent(f'''
            examples：
                # 查看使用说明
                $ python {SCRIPT_NAME} -h

                # 查看脚本版本
                $ python {SCRIPT_NAME} -V

                # 自定义方法的示例
                $ python {SCRIPT_NAME} --hi
            ''')
        )  # 可通过`parser.print_help()`手动打印使用说明
        self.parser.add_argument('-d', '--debug', dest='debug', action='store_true', help=self.arg_help(en=f'show debug log', zh='显示调试信息'))
        
        # 日志模式：互斥参数，若指定 `required=True` 表示在互斥组中至少有一个参数是需要的
        pgroup_logs = self.parser.add_mutually_exclusive_group()
        pgroup_logs.add_argument('-q', '--quiet', dest='quiet', action='store_true', help=self.arg_help(en='do not print any output except for warnings and errors', zh='仅显示异常和警告信息'))
        pgroup_logs.add_argument('-v', '--verbose', dest='verbose', action='store_true', help=self.arg_help(en='provide additional status output', zh='显示详细信息'))
        
        # 执行的功能：互斥参数
        pgroup_cmds = self.parser.add_mutually_exclusive_group()
        pgroup_cmds.add_argument('-V', '--version', action='version', version=self.arg_help(en=f'{SCRIPT_NAME} {SCRIPT_VERSION}'))
        pgroup_cmds.add_argument('--print_tests', dest='print_tests', action='store_true', help=self.arg_help(en=f'print tests', zh='测试日志打印'))
        pgroup_cmds.add_argument('--hi', dest='hi', action='store_true', help=self.arg_help(en=f'custom func example', zh='自定义方法的示例'))
        self.args = self.parser.parse_args()

        self.print_debug(f' GLOBAL CONST '.center(120, '='))
        self.print_debug(f'TIMESTAMP = {TIMESTAMP}')
        self.print_debug(f'DATE_TIME = {DATE_TIME}')
        self.print_debug(f'DATE_STAMP = {DATE_STAMP}')
        self.print_debug(f'CURRENT_PATH = {CURRENT_PATH}')
        self.print_debug(f'CURRENT_SCRIPT_FILE = {CURRENT_SCRIPT_FILE}')
        self.print_debug(f'CURRENT_SCRIPT_DIR = {CURRENT_SCRIPT_DIR}')
        self.print_debug(f'CURRENT_SCRIPT_BASENAME = {CURRENT_SCRIPT_BASENAME}')
        self.print_debug(f'CURRENT_SCRIPT_BASENAME_TITLE = {CURRENT_SCRIPT_BASENAME_TITLE}')
        self.print_debug(f'CURRENT_SCRIPT_BASENAME_EXT = {CURRENT_SCRIPT_BASENAME_EXT}')
        self.print_debug()
        self.print_debug(f' COMMAND '.center(120, '='))
        self.print_debug('python %s' % ' '.join(sys.argv))
        self.print_debug()
        self.print_debug(f' ARGS '.center(120, '='))
        for key, value in vars(self.args).items():
            self.print_debug(f'args.{key} = {value}')
        self.print_debug()

    # 方法示例
    @print_debug_func_info
    def hi(self):
        self.print_info('Hi~ 这是一个方法示例')

    # 开始执行
    def run(self):
        if self.args.print_tests:
            self.print_tests()
        elif self.args.hi:
            self.hi()
        else:
            self.parser.print_help()


# =========================================== __main__ ===========================================

if __name__ == '__main__':
    Script().run()
