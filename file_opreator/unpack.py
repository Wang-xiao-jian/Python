#!/usr/bin/python3

import argparse as arg
import os
import shutil

parser = arg.ArgumentParser('support bztar, gztar, xztar, tar, zip unpack format')
parser.add_argument('--dest-path', '-d', type=str, default='./', help='指定解压后的文件路径')
parser.add_argument('unpackfile', type=str, help='解压文件')
args = parser.parse_args()

formats = (
    'tar',
    '.tar.gz',
    '.tar.bz2',
    '.tar.xz',
    '.zip'
)

def main():
    if os.path.isdir(args.unpackfile):
        files = os.listdir(args.unpackfile)
        for file in files:
            if file.endswith(formats):
                if args.dest_path:
                    if not os.path.exists(args.dest_path):
                        os.mkdir(args.dest_path)
                    shutil.unpack_archive(file, args.dest_path)
                else:
                    shutil.unpack_archive(file)
    else:
        if args.dest_path:
            if not os.path.exists(args.dest_path):
                os.mkdir(args.dest_path)
            shutil.unpack_archive(args.unpackfile, args.dest_path)
        else:
            shutil.unpack_archive(args.unpackfile)

if __name__ == "__main__":
    main()