
import argparse
import os.path

from utilities.utils import find_base_dir, load_json

BASE_DIR=find_base_dir()
def cli():
    opt=argparse.ArgumentParser("Chatbot Parser")
    opt.add_argument('--name','-n',type=str,help='Name of the user',required=False)
    opt.parse_args()
    args=opt.parse_args()
    return  args
def main(args):
    path=os.path.join(BASE_DIR,'configs','config.json')
    print(f"Reading the confid: {path} ")
    configs=load_json(path)

    print(configs)
    pass


if __name__ == '__main__':
    args=cli()
    #print(args.name)
    # print(BASE_DIR)
    main(args)

