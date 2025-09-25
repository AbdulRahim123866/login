class FileController:
    def _init_(self, path: str):
        self.__path = path
        self.__file = None

    def read(self):
        self.get_file("rt")
        data = self.__file.read()
        self.__close()
        return data

    def get_file(self, mode: str = "rt"):
        if self.__path is None:
            raise ValueError("path is not defined")
        if self.__file is None:
            try:
                self.__file = open(self.__path, mode=mode)
            except FileNotFoundError:
                print("file not found in the giving path")

    def __close(self):
        if self.__file is not None:
            self.__file.close()
            self.__file = None

    def write(self, data):
        self.get_file("wt")
        if data is not None:
            self.__file.write(data)
            self.__close()


class FileControllerWithoutPath:
    def _init_(self):
        self.__file = None

    def read(self, path):
        self.get_file(path, "rt")
        data = self.__file.read()
        self.__close()
        return data

    def get_file(self, path, mode: str = "rt"):
        if path is None:
            raise ValueError("path is not defined")
        if self.__file is None:
            try:
                self.__file = open(path, mode=mode)
            except FileNotFoundError:
                print("file not found in the giving path")

    def __close(self):
        if self.__file is not None:
            self.__file.close()
            self.__file = None

    def write(self, data, path):
        self.get_file(path, "wt")
        if data is not None:
            self.__file.write(data)
            self.__close()


if __name__ == "__main__":
    file1 = FileController("new.txt")
    print(file1.read())
    file1.write("hi again")
    file11 = FileController("test.txt")
    print(file11.read())

    fileControllerWithoutPath = FileControllerWithoutPath()
    print(fileControllerWithoutPath.read("new.txt"))
    print(fileControllerWithoutPath.read("test.txt"))
