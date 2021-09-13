from flask import url_for
import re
import os

url_dict = {

}

import os

os.chdir(".")
for root, dirs, files in os.walk(".", topdown = False):
   for name in files:
      print(os.path.join(root, name))
   for name in dirs:
      print(os.path.join(root, name))

# folder_paths = []
# for entry_name in os.listdir('.'):
#     entry_path = os.path.join('.', entry_name)
#     if os.path.isdir(entry_path):
#         folder_paths.append(entry_path)
#
# file_paths = []
# for file_name in os.listdir('.'):
#     file_path = os.path.join('.', file_name)
#     if os.path.isfile(file_path):
#         file_paths.append(file_path)
#
# print(folder_paths)
#
# print(file_paths)

