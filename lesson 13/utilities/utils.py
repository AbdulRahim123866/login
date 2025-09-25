import json
import os.path


def load_json(path:str)->dict:
    try:
        with open(path,'rt') as file:
            result= json.load(file)
    except FileNotFoundError as e:
        print(f"File not found: {path}")
        raise e
    except json.JSONDecodeError as e:
        print(f"Error decoding json: {path}")
        raise e
    except IOError as e:
        print(f"Error reading file: {path}")
        raise e
    except Exception as e:
        print(f"Unknown error: {e}")
        raise e
    return result

def find_base_dir():
    base=os.path.dirname(os.path.dirname(__file__))
    return base

if __name__=="__main__":
    print(find_base_dir())