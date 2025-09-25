class Filecontroler:
    def __init__(self,path:str):
        self.__path=path
        self.__file=None

    def read(self,mode='rt'):
        if self.__path is None:
            raise ValueError("path is not defined")
        if self.__file is None:
            try:
                with open(self.__path,mode) as f:

                    return f.read()
                # self.__file = open(self.__path, mode=mode)
                # data = self.__file.read()
                # self.__close()
                # return data
            except FileNotFoundError:
                print("file not found in the giving path")


    def __close(self):
        if self.__file is not None:
            self.__file.close()
            self.__file=None

    def write(self,data,mode='wt'):
        if self.__path is None:
            raise ValueError("path is not defined")
        if self.__file is None:
            try:
                with open(self.__path,mode) as f:
                    f.write(data)
                # self.__file=open(self.__path,mode=mode)
                # self.__file.write(data)
                # self.__file.close()
            except FileNotFoundError:
                print("file not found in the giving path")


if __name__=="__main__":
    file1=Filecontroler("new.txt")
    file1.write("abd")
    content=file1.read()
    # print(content)
    content=content+" abooooddo"
    print(content)
