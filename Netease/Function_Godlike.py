import time



def get_curTime():
    return str(int(time.time()*1000))

def str2dict(headers_str):
    res = {}
    str_list = headers_str.split("\n")   #以 换行符为分割
    # print(str_list)
    for item in str_list:  #检查每一行元素
        try:
            tmp = item.split(": ")    #以 ： 号为分隔
            if tmp[0] == "Content-Length":
                continue
            res[tmp[0]] = tmp[1]
            # print(res)
        except Exception as e:
            pass
    return res
