

from argparse import ArgumentParser

def main(args):#2 steps and extended
    #cpath=input("Enter the path to the logs: ")
    #lpath=input("Enter the path to the logs:")
    #url=input("Enter the path to the logs:")
    pass

def validate_cli(args):
    # logical validation of the values
    assert args.config.endswith('.json'), f"Argument 'config' must point to a JSON file"
    return args

# def sorted(lst):
#     assert isinstance(lst,list),"steps12 must be a list"
#     sorte=lst.copy()
#     sorte.sort()
#     return sorte


def cli():
    ops=ArgumentParser("Cody")
    ops.add_argument('-l','--logs',type=str.upper,default='./logs',help="path to the logs directory")
    ops.add_argument('-c','--config',type=str,default='./logs',help="path to the config file. JSON Formate")

    # ops.add_argument('-c','--config',type=bool,required=True,help="path to the config file.JSON format")
    # ops.add_argument('-s','--steps',type=int,nargs='+',required=True,help="path to the config file.JSON format")#nargs هي عدد المتغيرات
    # ops.add_argument('-s1','--steps12',type=int,nargs='+',required=True,help="path to the config file.JSON format",action=sorter)#nargs هي عدد المتغيرات
    # ops.add_argument('-b','--bole',action="store_true",required=True,help="path to the config file.JSON format")


    args=ops.parse_args()
    return validate_cli(args)











if __name__ == '__main__':
    args=cli()
    # print(args.config)
    # print(args.steps)
    # print(args.bole)
    #
    # print(type(args.bole))
    # print(type(args.steps))
    # print(type(args.steps12))
    # print(args.logs)
    #
    # print(type(args.logs))

    main(args)
