import pandas as pd


def low_price_red(s):
    if s < 10:
        color = 'red'
    else:
        color = 'black'
    return f'color:{color}'

def high_score_green(col):
    return['background-color:lime' if s==col.max() else 'background-color:white' for s in col]
# def high_score_green(col):
#     for s in col:
#         if s == col.max():
#             return 'background-color:red'
#         else:
#             return 'background-color:white'


table = pd.read_excel(r'I:\Python\books.xlsx')
table.style.applymap(low_price_red, subset=['Oct', 'Nov', 'Dec']).apply(high_score_green, subset=['Oct', 'Nov', 'Dec'])
