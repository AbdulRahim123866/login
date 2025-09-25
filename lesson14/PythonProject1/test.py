

class FileController:
    def __init__(self,path:str):
        self.__path=path
        self.__file=None
    def read(self):
        if self.__path is None:
            raise ValueError("path is not defined")
        if self.__file is None:
            try:
                self.__file = open(self.__path)
            except FileNotFoundError:
                print("file not found in the given path")
        return self.__file.read()


    def close(self):
        if self.__file is not None:
            self.__file.close()

    def write(self,data):
        if self.__file is None:
            if self.__path is None:
                raise ValueError("path is not defined")
            try:
                self.__file = open(self.__path)
            except FileNotFoundError:
                print("file not found in the given path")


        return self.__file.read()