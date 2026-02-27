import os
import configparser

config= configparser.RawConfigParser()

# path = os.path.abspath(os.getcwd())+"\\configurations\\config.ini"

# path= os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "configurations", "config.ini"))
path= os.path.abspath(os.path.join(os.path.dirname(__file__), "../configurations/config.ini"))
config.read(path)

config.read(path)

class ReadConfig():
    @staticmethod
    def get_property(key):
        return config.get("commonInfo", key)

