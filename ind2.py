# /usr/bin/env python3
# -*- coding: utf-8 -*-

# вариант - 10

if __name__ == '__main__':
    try:
        with open('ind2.txt', 'r') as f:
            lst_of_string = f.readlines()
            for i in lst_of_string:
                words = i.split()
                for word in words:
                    



    except Exception as e:
        print(e)