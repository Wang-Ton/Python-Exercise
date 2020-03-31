
import tkinter.filedialog
import tkinter as tk
from tkinter import Tk, Entry
import pandas as pd
import re
import time


def selectPath():
    # 选择文件path_接收文件地址
    path_ = tkinter.filedialog.askopenfilename()

    # 通过replace函数替换绝对文件地址中的/来使文件可被程序读取
    # 注意：\\转义后为\，所以\\\\转义后为\\
    path_ = path_.replace("/", "\\\\")
    # path设置path_的值
    path.set(path_)
    # 编写tkinter界面并把函数绑定


def deal():
    file_name = file_path.get()
    data = pd.read_excel(file_name, sheet_name=None)
    First = pd.read_excel(file_name, skiprows=2)
    n = list(data)
    if len(n) > 1:
        dfs = []
        for i in n[1:]:
            df = pd.read_excel(file_name, sheet_name=i)
            dfs.append(df)
        Others = pd.concat(dfs)
        Others.columns = First.columns.values
        All = pd.concat([First, Others], ignore_index=True)
    else:
        All = First
    All['提取订单号'] = None
    if isinstance(All.iloc[All.index[-1], [0]].values[0], str):
        All.drop(All.index[-1], inplace=True)
    for x in All.index:
        if 'HJCOM' in All.at[x, '商户订单号']:
            All.at[x, '提取订单号'] = All.at[x, '商户订单号'][-18:]
        elif 'T200P'in All.at[x, '商户订单号']:
            All.at[x, '提取订单号'] = All.at[x, '商户订单号'][-18:]
        elif bool(re.search(r'\d', All.at[x, '备注'])) == True:
            All.at[x, '提取订单号'] = re.findall(r'\d+', All.at[x, '备注'])[0]
    All.set_index('序号', inplace=True)
    All.to_excel(r'd:\支付宝对账单-提取订单号.xlsx')
    print('Done')


main_box = tk.Tk()
# 变量path
path = tk.StringVar()
# 输入框，标记，按键
tk.Label(main_box, text="文件路径:").grid(row=0, column=0)
# 输入框绑定变量path
file_path = tk.Entry(main_box, textvariable=path)
file_path.grid(row=0, column=1)
tk.Button(main_box, text="文件选择", command=selectPath).grid(row=0, column=2)
tk.Button(main_box, text="启动程序", command=deal).grid(row=1, column=2)
#tk.Button(main_box, text="存储文件", command=store).grid(row=2, column=2)
main_box.mainloop()
