import configparser, os
class Config:
    def __init__(self):
        self.cfg = configparser.ConfigParser()
        if os.environ.get('production') is not None:
            if os.environ['production']=='true':
                self.production = True
                self.cfg.read('./config/production.ini')
            else:
                self.production = False
                self.cfg.read('./config/development.ini')
        else:
            self.production = False
            self.cfg.read('./config/development.ini')
    def get(self,name,key):
        if self.production:
            return self.cfg.get(name, key, vars=os.environ)
        else:
            return self.cfg.get(name, key)
        