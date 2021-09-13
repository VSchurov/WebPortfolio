from flask import url_for
import re
import os


def get_file_names():
    filenames_list = []
    for root, dirs, files in os.walk("."):
        for filename in files:
            if re.match(r'.*\.html', filename):
                print(filename)
                filenames_list.append(filename)
    filenames_list.sort()
    return filenames_list


def get_file_paths():
    filepaths_list = []
    os.chdir(".")
    for root, dirs, files in os.walk(".", topdown=False):
        for name in files:
            if re.match(r'.*\.html', name):
                print(os.path.join(root, name))
                filepaths_list.append(os.path.join(root, name))
    filepaths_list.sort()
    return filepaths_list


# 'keys' - all filenames
# 'values' - all filepaths
def fill_url_dict(keys: list, values: list):
    # At first we should check does both of lists are similar by size and filled by simultaneous
    # files.
    # if keys.__len__() == values.__len__():
    #     while True:
    #         for i in range(values.__len__()):
    #             for j in range(keys.__len__()):
    #                 if keys[j] not in values[j]:
    #                     keys[j], keys[j + 1] = keys[j + 1], keys[j]
    # print(keys.__len__(), values.__len__())
    # print(keys)
    # print(values)
    return
                        # Oh my darling I hear you missed sorts for so long time


if __name__ == '__main__':
    fill_url_dict(get_file_names(), get_file_paths())
