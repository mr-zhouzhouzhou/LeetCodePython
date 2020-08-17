from numba.dictobject import new_dict
import json



with open("tw.json","w") as f:
      json.dump(new_dict,f)
      print("加载入文件完成...")