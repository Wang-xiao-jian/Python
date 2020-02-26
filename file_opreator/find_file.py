#!/usr/bin/python3

import os
import argparse as arg
import re

def _parse():
    parse = arg.ArgumentParser()
    parse.add_argument('--whole', action='store_true', default=False, help='指定完整匹配')
    parse.add_argument('--path', type=str, default='/', help='指定路径下查找')
    parse.add_argument('filename', type=str, help='查找的文件名')
    args = parse.parse_args()
    return args

def find(path, pattern):
    pwd = path
    filelist = os.listdir(path)
    for _ in filelist:
        abs = os.path.join(pwd, _)
        if re.match(pattern, _, re.I) != None:
            print(abs)
        if os.path.isdir(abs):
            find(abs, pattern)

def main():
    args = _parse()
    if not args.whole:
        args.filename = '.*' + args.filename + '.*'
    else:
        pass
        
    find(args.path, args.filename)
    
    
    

if __name__ == "__main__":
    main()