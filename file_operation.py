import os
import shutil

def write_to_file(file_path,content):
    with open(file_path,"w") as file:
        file.write(content)
        print(f"Content are written to {file_path}")

def append_to_file(file_path,content):
    with open(file_path,"a") as file:
        file.write(content)
        print(f"Content are appended to {file_path}")

def readfile(file_path,mode ="all"):
    with open(file_path,"r") as file:
        if mode =="all":
            return file.read()
        elif mode =="line":
            return file.readline()
        elif mode == "lines":
            return file.readlines()
        else:
            raise ValueError("Invalid mode. use 'all','line', 'lines' ")
        
def rename_file(source,target):
    os.rename(source,target)
    print(f"File renamed from {source} to {target}")


def delete_file(file_path):
    if os.path.exists(file_path):
        os.remove(file_path)
        print(f"File {file_path} deleted")
    else:
        print(f" File {file_path} does not exist")


def create_directory(dir_path):
    os.mkdir(dir_path)
    print("Directory {dir_path} created")


def check_directory_exists(dir_path):
    return os.path.exists(dir_path)



def rename_directory (source, target):
    os.rename (source, target)
    print(f"Directory renamed from {source} to {target}")


def remove_directory(dir_path, force=False):
    if force:
        shutil.rmtree(dir_path)
    else:
        os.rmdir(dir_path)
        # only removes if empty
        print(f"Directory {dir_path} removed")


def get_current_working_directory():
    return os.getcwd()