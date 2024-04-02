# /usr/bin/env python3
# -*- coding: utf-8 -*-

# вариант - 10

if __name__ == "__main__":
    lst_of_int = [str(i) for i in range(10, 100)]
    try:
        with open("ind1.txt", "r") as f:
            lst_of_lines = f.readlines()
            for i in lst_of_lines:
                words = i.split()
                flag = list(filter(lambda x: x in lst_of_int, words))
                if not flag:
                    print(i[:-1])
    except Exception:
        print("There is no file with that name")
