# 取讀yaml的系統設置
import yaml

class config(object):
    def __init__(self):
        f = open('config.yaml', encoding='utf8')
        self.settings = yaml.load(f)
        self.account = self.settings["Account"].encode('big5')
        self.password = self.settings["Password"].encode('big5')
        self.Targets = self.settings["Targets"]
        self.WaterTarget = self.settings["WaterTarget"]

    def GetTargets(self):
        for target in self.settings["Targets"]:
            yield target["account"],target["IsSendWater"]



if __name__ == '__main__':
    a = config()
    for i,a in a.GetTargets():
        print(i,a)

