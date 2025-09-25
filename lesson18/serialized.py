import json


with open("test.json") as file:
    config =json.load(file)

print(config)
print(type(config))


with open("test.json","wt") as file:
    json.dump([1,5,3],file)

config=json.dumps(obj=[1,5,3])
# config=json.loads(obj={1,5,3})

print(config)        # "[1, 5, 3]"
print(type(config))  # <class 'str'>

# ______________________________________________________________________

# from PIL import Image
#
# img=Image.open("logo.png")
# img.show()
# print(img.size, img.mode)

import yaml

with open("test.yaml") as file:
    config=yaml.load(file,Loader=yaml.Loader)

print(config)


def load_json(path:str)->dict:
    try:
        result=eval(f"{path.split(".")[-1]}.load(path)")
        # result=json.load(path)
        return result
    except json.JSONDecodeError as e:
        raise e
    except FileNotFoundError as e:
        raise e
    except IOError as e:
        raise e
    except:
        raise

