from configparser import ConfigParser

class ConfigHandler:
    def __init__(self,config):
        self.config=config

    def read_ini(self,section="test"):
        parser=ConfigParser()
        parser.read(self.config)
        host=parser.get(section,"host")
        username = parser.get(section, "username")
        password = parser.get(section, "password")
        return host,username,password

    def read_cfg(self,section="Training data"):
        parser = ConfigParser()
        parser.read(self.config)
        # host=parser.get(None,"host")
        valid=parser.get(section, "valid")
        return valid






# configurer=ConfigParser()
#
# configurer.read("./abc.ini")
#
# environment=configurer.get('ENV','prod')#string
#
# print(environment)
# configurer.getint()#int
# configurer.getfloat()#float
# configurer.getboolean()#boolean

CONF=ConfigHandler("./config/test.ini")
print(CONF.read_ini())