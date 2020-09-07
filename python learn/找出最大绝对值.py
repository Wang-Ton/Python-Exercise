x = [1, 2, 3, 4, 5, -6, -7, -8, -9]
'''
max_number = abs(max(x))
min_number = abs(min(x))
max_abs_number = max(max_number, min_number)
for i in x:
    if abs(i) == max_abs_number:
        print(i)
'''
maxes = max(x, key=abs)
maxes = max(x, key=lambda y: pow(y, 2))
print(maxes)
# %%
