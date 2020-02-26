import pandas as pd


def low_price_red(s):
    color = 'red' if s < 10 else 'black'
    return f'color:{color}'

# def low_price_red(s):
#     if s < 10:
#         color = 'red'
#     else:
#         color = 'black'
#     return f'color:{color}'


# def high_score_green(col):
#     return['background-color:lime' if s==col.max() else 'background-color:white' for s in col]

def high_score_green(col):
    evens = []
    for s in col:
        if s == col.max():
            evens.append('background-color:lime')
        else:
            evens.append('background-color:white')
    return evens


table = pd.read_excel(r'I:\Python\books.xlsx')
table.style.applymap(low_price_red, subset=['Oct', 'Nov', 'Dec']).apply(
    high_score_green, subset=['Oct', 'Nov', 'Dec'])
