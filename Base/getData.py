import os

import yaml


class GetData:
    def read_yaml(self,filname):
        # ss = []
        with open('../data/'+filname,"r",encoding="utf-8") as f:
            return yaml.safe_load(f)
        #     for i in data.values():
        #         ss.append(tuple(i.values()))
        # return ss
ss = GetData()
data = ss.read_yaml('login_right.yaml')
s2 = []
for i in data.values():
    s2.append(tuple(i.values()))
print(s2)