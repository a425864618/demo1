import yaml


def readyaml(flidname,key=None):

    with open(flidname,encoding='utf-8') as fp:
        get_yaml=yaml.load(fp,Loader=yaml.SafeLoader)
        if key==None:
            return get_yaml
        else:
            return get_yaml[key][0]



if __name__ == '__main__':
    # a=readyaml(datayaml_payh,"registersuccess")
    pass

    # print(type(a))