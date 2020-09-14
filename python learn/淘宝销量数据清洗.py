import re
import json


def get_space_end(level):
    return '  ' * level + "-"


def get_space_expand(level):
    return '  ' * level + "+"


def find_keys(targets, level):
    keys = iter(targets)
    for each in keys:
        if type(targets[each]) is not dict:
            print(get_space_end(level) + each)
        else:
            next_level = level + 1
            print(get_space_expand(level)+each)
            find_keys(targets[each], next_level)


def main():
    with open(r"d:/销售数据.txt", 'r', encoding='utf-8') as file1:
        g_page_config = re.search(r"g_page_config = (.*?);\n ", file1.read())
        # with open(r"d:/g_page_config.txt", 'w', encoding="utf-8") as file2:
        #     file2.write(g_page_config.group(1))
        page_config_json = json.loads(g_page_config.group(1))
        find_keys(page_config_json, 1)


if __name__ == "__main__":
    main()
