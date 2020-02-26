def count_words(file_name,words):
    d=dict.fromkeys(words,0)

    f=open(file_name,'r',encoding ='utf-8')
    for s in f.readlines():
        for name in d:
            d[name]=d[name]+s.count(name)
    f.close()
    return d
    