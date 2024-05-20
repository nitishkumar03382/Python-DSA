import os
from os import walk
import random
cwd = os.getcwd()
res = []

for (dir_path, dir_names, file_names) in walk(cwd):
    # print(dir_names)
    if '.git' not in dir_path:
        res.extend(file_names)
aaj_ka_ques = random.choices(res, k = 2)
print("Aaj ye question karna hai: ", aaj_ka_ques )
