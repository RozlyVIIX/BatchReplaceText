# -*- coding:utf-8 -*-

# import package
import os
import sys
import shutil
import re


# init
def do_init(text_list, file_list):
    for file_name in file_list:
        old_file = file_name
        new_file = file_name + '.new'
        bak_file = file_name + '.bak'

        check_file(old_file)
        back_up_file(old_file, bak_file)

        print("==========" + old_file + "==========")
        handle_file(old_file, new_file, text_list)


# back up resource
def back_up_file(old_file, bak_file):
    bak_file_path = './backup'
    bak_file = bak_file_path + '/' + bak_file
    if os.path.exists(old_file):
        if os.path.exists(bak_file_path):
            shutil.copyfile(old_file, bak_file)
        else:
            os.mkdir(bak_file_path)
            shutil.copyfile(old_file, bak_file)
    else:
        print("please check if it exists." + old_file)
        exit()


# check file
def check_file(path):
    if not (os.path.exists(path) and os.path.getsize(path)):
        print("please check file : " + path)
        exit()


# check file content
def check_content(path):
    if len(path) % 2 != 0:
        print("please check: " + path)
        exit()


# get file content
def get_file_content(path):
    with open(path, mode="r", encoding="utf-8") as content_file:
        content_list = content_file.read().splitlines()
        return content_list


# handle file
def handle_file(old_file, new_file, content_list):
    i = 0
    while i < len(content_list):
        num = 0
        old_str = content_list[i]
        new_str = content_list[i + 1]
        print("old_str: " + old_str)
        print("new_str: " + new_str)

        # read and create files
        f = open(old_file, mode="r", encoding="utf-8")
        f_new = open(new_file, mode="w", encoding="utf-8")

        # Loop through the file contents by line
        for line in f:
            if re.search(old_str, line, re.I):
                num += len(re.findall(old_str, line, re.I))
                line = re.sub(old_str, new_str, line, flags=re.I)
            f_new.write(line)
        print(old_str + " replaced %s times\n" % num)
        i = i + 2
        f.close()
        f_new.close()

        # rename for file
        os.remove(old_file)
        os.rename(new_file, old_file)  # open.txt.new modified into  open.txt


if __name__ == "__main__":
    # parameter declarations
    arg = []
    arg = sys.argv

    # parameter assignment
    list_file = arg[1]
    text_file = arg[2]

    check_file(text_file)
    check_file(list_file)
    check_content(text_file)
    tf = get_file_content(text_file)
    lf = get_file_content(list_file)
    do_init(tf, lf)

    print("==========success!==========")
