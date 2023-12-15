# TODO здесь писать код
import json
from typing import Any


def read_from_file(file_name) -> dict:
    with open(file_name, 'r') as file:
        res = json.load(file)
    return dict(res)


def find_key(struct: Any, key: str) -> Any:
    """ поиск заданного ключа key в структуре struct"""
    if key in struct:
        return struct[key]
    else:
        for sub in struct.values():
            if isinstance(sub, dict):
                res = find_key(sub, key)
                if isinstance(res, (list, tuple, set)):
                    for item in res:
                        if isinstance(item, dict):
                            result = find_key(item, key)
                            if result:
                                break
                    else:
                        result = None
                    if result is not None:
                        res = result
                if res:
                    break
        else:
            res = None
    return res


def comparison(dict_1: dict, dict_2: dict) -> dict:
    global diff_list

    changes = dict()
    for key in diff_list:
        value_old = find_key(dict_1, key)
        value_new = find_key(dict_2, key)
        if value_old != value_new:
            changes[key] = value_new
    return changes


def save_to_file(value: dict) -> None:
    with open('result.json', 'w') as file:
        json.dump(value, file, indent=4)


diff_list = ["services", "staff", "datetime", "attendance"]

res_old = read_from_file('json_old.json')
print(res_old)
res_new = read_from_file('json_new.json')
print(res_new)

result = comparison(res_old, res_new)
print(result)
save_to_file(result)
