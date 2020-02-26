import os

def rename(file_dir):
    num = 0
    file_list = os.listdir(file_dir)
    for _ in file_list:
        path = os.path.join(file_dir, _)
        if os.path.isdir(path):
            rename(path)
        else :
            pos = _.rfind('.')
            new_name = str(num) + _[pos:]
            new_abs_name = os.path.join(file_dir, new_name)
            old_abs_name = os.path.join(file_dir, _)
            os.rename(old_abs_name, new_abs_name)
            num += 1
 
def main():
    file_path = input('请输入文件夹路径：')
    rename(file_path)

if __name__ == "__main__":
    main()