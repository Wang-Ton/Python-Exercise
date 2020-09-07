from sklearn.utils import resample
from astropy.tests.runner import keyword
import requests
import bs4


def open_url(keywords):
    return res


def main():
    keywords = input("请输入关键词:")
    res = open_url(keywords)

    with open("d:\关键词.txt", "w", encoding="utf-8") as file:
        file.write(res.text)


if __name__ == "__main__":
    main()
