# %%
import pandas as pd


def Score_validation(row):
    try:
        assert 0 < row.Score < 100
    except:
        print(f'#{row.ID}\t is worng as {row.Score}')


def Score_check(row):
    if row.Score > 100:
        print(f'#{row.ID}\t is worng as {row.Score}')


score = pd.read_excel(r'I:\Python\join查询.xlsx', sheet_name='Score')
#  score.apply(Score_validation,axis=1)
score.apply(Score_check, axis=1)
print('Finished')
# %%
