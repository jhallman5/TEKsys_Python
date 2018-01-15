import os
import re
import matplotlib.pyplot as plt

def get_root_dir():
    return input("Enter root_dir: ")

def get_user_input():
    return input("Enter keyword: ")

def find_files():
    root_dir = get_root_dir()
    keyword = re.compile(get_user_input())

    files_found = {}
    for (dirpath, dirnames, filenames) in os.walk(root_dir):
        rel_dirpath = os.path.relpath(dirpath, root_dir)
        files_found[rel_dirpath] = 0
        for current_file in filenames:
            with open(f'{dirpath}/{current_file}') as f:
                for line in f:
                    if re.search(keyword, line):
                        files_found[rel_dirpath] += 1

    print(files_found)

    plt.bar(range(len(files_found)), list(files_found.values()), align='center', alpha=0.5)
    plt.xticks(range(len(files_found)), list(files_found.keys()))

    plt.ylabel('Files')
    plt.title('Files found which contain pharse')

    plt.show()

if __name__ == '__main__':
    find_files()
