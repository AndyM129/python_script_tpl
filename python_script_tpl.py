#!/usr/bin/python3

import getopt
import os
import sys
import time

# =========================================== COPYRIGHT ===========================================
SCRIPT_NAME = 'python_script_tpl.py'  # 脚本名称
SCRIPT_DESC = 'Python 脚本模板，已预制常用常量、变量、方法定义，及复杂参数解析，以便快速开始核心编程。'  # 脚本名称
SCRIPT_VERSION = '0.1.0'  # 脚本版本
SCRIPT_UPDATE_TIME = '2021/12/04'  # 最近的更新时间
AUTHOR_NAME = 'MengXinxin'  # 作者
AUTHOR_EMAIL = 'andy_m129@163.com'  # 作者邮箱
README_URL = 'https://github.com/AndyM129/python_script_tpl'  # 说明文档

# =========================================== GLOBAL CONST ===========================================
TIMESTAMP = int(time.time())  # 当前时间戳，eg. 1617351251
DATE = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(TIMESTAMP))  # 当前时间，eg. 2021-04-02 16:14:11
DATE_STAMP = time.strftime('%Y%m%d%H%M%S', time.localtime(TIMESTAMP))  # 当前时间戳，eg. 20210402161411
CURRENT_PATH = os.getcwd()  # 当前所在路径
SCRIPT_DIR = os.path.dirname(__file__)  # 当前脚本的文件路径
SCRIPT_BASENAME = os.path.basename(__file__)  # 当前脚本的文件名
SCRIPT_BASENAME_WITHOUT_SUFFIX = SCRIPT_BASENAME.split('.')[0]  # 文件名（不含后缀）
SCRIPT_BASENAME_SUFFIX = SCRIPT_BASENAME.split('.')[1]  # 文件后缀

# =========================================== GLOBAL VARIABLES ===========================================
args = []
opts = {}

# =========================================== GLOBAL FUNCTIONS ===========================================

def is_debug(): return True if 'd' in opts or 'debug' in opts else False

def is_verbose(): return True if 'verbose' in opts else False

def print_debug(s=''): print('\033[1;2m%s\033[0m' % s) if is_debug() else None

def print_verbose(s=''): print('\033[1;2m%s\033[0m' % s) if is_verbose() or is_debug() else None

def print_info(s=''): print('\033[1;36m%s\033[0m' % s)

def print_success(s=''): print('\033[1;32m%s\033[0m' % s)

def print_warn(s=''): print('\033[1;33m%s\033[0m' % s)

def print_error(s=''): print('\033[1;31m%s\033[0m' % s)

def print_fatal(s=''): print('\033[1;31m%s\033[0m' % s)

# =========================================== HELP ===========================================

# 使用说明
def help():
    print_info('%s' % SCRIPT_DESC)
    print_info()
    print_info('# Usage')
    print_info('\t$ python %s [-dvh] [command] [params...] [--Option [value] [-sub_option [value]]...]...' % SCRIPT_NAME)
    print_info()
    print_info('# Global commands')
    print_info('\tauthor \t\t查看作者信息')
    print_info('\tdir \t\t查看当前命令的安装目录')
    print_info('\topen \t\t打开当前命令的安装目录')
    print_info('\tpath \t\t查看当前命令对应文件的路径')
    print_info('\tsummary \t查看简介')
    print_info('\tversion \t查看该命令的当前版本号')
    print_info('\twiki \t\t查看说明文档')
    print_info()
    print_info('# Global options')
    print_info('\t-h, --help \t查看使用说明')
    print_info('\t    --version \t查看使用说明')
    print_info('\t-v, --verbose \t启用冗余模式，并输出执行过程中详细信息')
    print_info('\t-d, --debug \t启用调试模式，并输出执行过程中调试信息')
    print_info()
    print_info('# Available commands')
    print_info()

# =========================================== PROCESS ===========================================

# 逻辑处理
def process():
    print_success('Done!')

# =========================================== MAIN ===========================================

# 主函数
def main():
    opts_tuple, args = getopt.getopt(sys.argv[1:], 'dvh', ['help', 'verbose', 'version'])
    for opt, arg in opts_tuple: opts[opt.lstrip('-')] = arg
    for key in opts: opts[key] = opts[key] if opts[key].isspace() else True

    print_debug()
    print_debug('======================== DATE ======================')
    print_debug('%s' % DATE)
    print_debug()
    print_debug('======================== GLOBAL CONST ======================')
    print_debug('TIMESTAMP = %s' % TIMESTAMP)
    print_debug('DATE = %s' % DATE)
    print_debug('DATE_STAMP = %s' % DATE_STAMP)
    print_debug('CURRENT_PATH = %s' % CURRENT_PATH)
    print_debug('SCRIPT_DIR = %s' % SCRIPT_DIR)
    print_debug('SCRIPT_BASENAME = %s' % SCRIPT_BASENAME)
    print_debug('SCRIPT_BASENAME_WITHOUT_SUFFIX = %s' % SCRIPT_BASENAME_WITHOUT_SUFFIX)
    print_debug('SCRIPT_BASENAME_SUFFIX = %s' % SCRIPT_BASENAME_SUFFIX)
    print_debug()
    print_debug('======================== COMMAND ======================')
    print_debug('python %s' % ' '.join(sys.argv))
    print_debug()
    print_debug('======================== ARGS (%s) ======================' % len(args))
    for i in range(len(args)): print_debug('args[%s] = %s' % (i, args[i]))
    print_debug()
    print_debug('======================== OPTS (%s) ======================' % len(opts))
    for key in opts: print_debug('opts[%s] = %s' % (key, opts[key]))
    print_debug()
    print_debug('==============================================')

    # 预制处理
    if len(args) > 0 and 'author' == args[0]: print_success('%s <%s>' % (AUTHOR_NAME, AUTHOR_EMAIL)); exit()
    if len(args) > 0 and 'dir' == args[0]: print_success('%s' % SCRIPT_DIR); exit()
    if len(args) > 0 and 'open' == args[0]: os.system('open %s' % SCRIPT_DIR); exit()
    if len(args) > 0 and 'path' == args[0]: print_success('%s/%s' % (SCRIPT_DIR, SCRIPT_BASENAME)); exit()
    if len(args) > 0 and 'summary' == args[0]: print_success('%s' % SCRIPT_DESC); exit()
    if len(args) > 0 and 'version' == args[0] or 'version' in opts: print_success('%s' % SCRIPT_VERSION); exit()
    if len(args) > 0 and 'wiki' == args[0]: print_success('%s' % README_URL); exit()
    if 'h' in opts or 'help' or len(args) <= 0 in opts: help(); exit()

    # 检查更新
    # check_update_if_needed $main_args && print_debug

    # 开始处理
    process()

if __name__ == '__main__': main()
