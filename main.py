# 这是一个示例 Python 脚本。
import tushare as ts
import efinance as ef
# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。


def print_hi(name):
    # 在下面的代码行中使用断点来调试脚本。
    #print(f'Hi, {name}')  # 按 Ctrl+F8 切换断点。
    ts.set_token('0dcb8f7b64a48754e1730bca9afd10a521ac690ae97af7484bc66e72')
    pro = ts.pro_api()
    df = pro.daily(ts_code='301059.SZ', trade_date='20220107')
    print(df)

def efi():
    stock_code = '301059'
    frequency = 5
    #dd = ef.stock.get_quote_history(stock_code)
    dd = ef.stock.get_quote_history(stock_code, klt=frequency)
    print(dd)

# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    print_hi('PyCharm')
    efi()

# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助
