#!/usr/bin/python3

import os
import shutil
import argparse as arg

def _parse():
    parser = arg.ArgumentParser()
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-p', '--prefix', action='store_true', default=False, help='根据前缀分类')
    group.add_argument('-s', '--suffix', action='store_true', default=True, help='根据后缀分类')
    parser.add_argument('path', type=str, help='文件夹路径')
    args = parser.parse_args()

    return args

def group(path, p_flag, s_flag):
    filelist = os.listdir(path)
    for elem in filelist:
        current_path = os.path.join(path, elem)
        if os.path.isdir(current_path):
            group(current_path, p_flag, s_flag)
            continue
        
        pos = elem.rfind('.')
        if pos == -1:
            new_dir = os.path.join(path, 'NoFeature')
        else:
            if p_flag:
                new_dir = os.path.join(path, elem[:pos])
            else:
                new_dir = os.path.join(path, elem[pos + 1:])
        
        if not os.path.exists(new_dir):
            os.mkdir(new_dir)
        shutil.move(current_path, new_dir)

def main():
    args = _parse()
    if not os.path.isdir(args.path):
        print('请输入文件夹路径')
        return
    group(args.path, args.prefix, args.suffix)

if __name__ == "__main__":
    main()