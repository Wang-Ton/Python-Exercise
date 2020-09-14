import requests


def open_url(keywords, page=1):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0", "cookie": "newFunctionMaskVisible=false; thw=cn; hng=CN%7Czh-CN%7CCNY%7C156; enc=WytxQMul2h1rGpZRPuzagpTNt6nemy7boHKhEmn35wxtOYNzEBp9s6ElklJSPs%2BNOuvQmmMBS0zq0mm5LPE0fQ%3D%3D; xlly_s=1; t=4e41d7a9e773d7f4e3bd3c6f3f2c93c2; sgcookie=E100%2FZeN65oZ6bplHargf7S1dKFgxJ6McExiuOjDBNQKERV9rycAgaOBMxakcStzE2sXKgYJZ1nrqOX6yro3Pi4lOw%3D%3D; cookie2=188924a70578fb8240d58d5a48bef4d3; _tb_token_=e788f38b48597; _samesite_flag_=true; mt=ci=0_0; tracknick=; cna=5gFBDqubswsCAd8VsuVDCPsF; v=0; _m_h5_tk=7abd42aeb1353d94eeb57404f7c943bb_1599887287986; _m_h5_tk_enc=80637ea34eac661ff24ace1dc7fa4204; alitrackid=www.taobao.com; lastalitrackid=www.taobao.com; JSESSIONID=6A1C704F71E3059B21666933EA3CE68D; tfstk=co-CBwgsKWVIusuzYpMNa0o1aps5ZO2fF21HdetJOP-uhsvCi6qVG622r7QxEO1..; l=eBEda49IORfOKaLyBOfwnurza77tsIRAguPzaNbMiOCP9F1p55RRWZyLxYY9CnGVh68kR3P4acHBBeYBqIv4n5U62j-lasDmn; isg=BLOzZxaD6AbCNqTF8zrAGbUEQrfd6EeqPniMJGVQClIJZNMG7bkp-hH2GpSKRJ-i"}

    payload = {'q': keywords, 'sort': 'sale-desc', 's': str((page-1) * 44)}
    url = "https://s.taobao.com/search"
    res = requests.get(url, params=payload, headers=headers)
    return res


def main():
    keywords = input("请输入关键词:")
    page=3
    for each in range(page):
        res = open_url(keywords,each+1)

    with open(r"d:\销售数据.txt", "w", encoding="utf-8") as file:
        file.write(res.text)


if __name__ == "__main__":
    main()
