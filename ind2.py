# /usr/bin/env python3
# -*- coding: utf-8 -*-

# вариант - 10

import re


if __name__ == "__main__":
    lst_ok = []
    lst_not_ok = []
    try:
        with open("ind2.txt", "r") as f:
            lst_of_string = f.readlines()
            for i in lst_of_string:
                words = re.findall(r"\b\w*ie\w*\b|\b\w*ei\w*\b", i)
                for word in words:
                    if "cie" in word:
                        lst_not_ok.append(word)
                    elif "ei" in word and "cei" not in word:
                        lst_not_ok.append(word)
                    else:
                        lst_ok.append(word)
    except Exception as e:
        print(e)

    lst_ok, lst_not_ok = list(set(lst_ok)), list(set(lst_not_ok))
    print(
        f"Слова, соответствующие правилу: {lst_ok}\nДлина"
        f" списка: {len(lst_ok)}"
    )
    print(
        f"Слова, не соответствующие правилу: {lst_not_ok}\nДлина"
        f" списка: {len(lst_not_ok)}"
    )
