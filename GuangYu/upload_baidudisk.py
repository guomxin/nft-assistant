# coding: utf-8
import sys
from bypy import ByPy

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("{} <file_full_name> <date_str>".format(sys.argv[0]))
        sys.exit(1)
        
    file_full_name = sys.argv[1]
    date_str = sys.argv[2]

    bp = ByPy()
    remote_path = "GuangYu/{}".format(date_str)
    bp.mkdir(remotepath=remote_path)
    bp.upload(localpath= file_full_name, remotepath=remote_path)
