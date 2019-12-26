import yaml, os


class GetData:

    def get_yml_data(self, name):
        """
        返回yaml文件数据
        :param name: 需要读取文件名字
        :return:
        """
        # 打开文件
        # with open("./data" + os.sep + name, "r", encoding="utf-8") as f:
        with open("./data/"+name, "r", encoding="utf-8") as f:
            # 加载文件
            s4 = []
            data = yaml.safe_load(f)
            for i in data.values():
                s4.append(tuple(i.values()))
        return s4

# s3 = GetData()
# cc = s3.get_yml_data('login.yml')
# print(cc)
# s4 = []
# for i in cc.values():
#     s4.append(tuple(i.values()))
# print(s4)


