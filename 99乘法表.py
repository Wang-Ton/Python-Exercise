# %%
r = 1
while r <= 9:
    c = 1
    while c <= r:
        result = c*r
        print(f'{c}*{r}={result}\t', end="")
        c += 1
    r += 1
    print()


# %%
for r in range(1, 10):
    for c in range(1, r+1):
        result = c*r
        print(f'{c}*{r}={result}\t', end="")
    print()

# %%
