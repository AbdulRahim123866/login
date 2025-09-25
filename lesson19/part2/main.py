import logging
from sqlite3.dbapi2 import Timestamp

#log level
#5-critical
#4-error
#3-warning
#2-info
#1-debug
#انت بتقدر تشوف نوع الللوج والنوع اللي تحته بالليلف فالرقم واحد بشوف الكل وهكذا

#log format:
#Timestamp, line, function, file - message



logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(lineno)d - %(module)s- %(filename)s - %(message)s',
                    filename="log.log",
                    filemode="w"
                    )


logger=logging.getLogger("BikeLogger")
handler=logging.FileHandler(filename="test.log",mode="w")
formatter=logging.Formatter('%(asctime)s - %(levelname)s - %(lineno)d - %(module)s- %(filename)s - %(message)s ')
handler.setFormatter(formatter)
logger.setLevel("DEBUG")
logger.addHandler(handler)
logger.info("hello world")


def main():
    while True:
        try:
            x=int(input("Enter a number: "))
            logger.info(f"you enterd {x}")
            logger.error("invalid input")
            logger.warning("invalid input")
            logger.info("invalid input")
            logger.critical("invalid input")
            logger.debug("invalid input")
            return x
        except ValueError:
            logging.error("invalid input")
            logging.warning("invalid input")
            logging.info("invalid input")
            logging.critical("invalid input")
            logging.debug("invalid input")
            continue


if __name__=="__main__":
    main()



class ImmutableClass:
    def __init__(self,age):
        self.age=age

    def increase_age(self):
        x=copy(self)
        x.age+=1
        return x