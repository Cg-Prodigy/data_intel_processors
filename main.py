import csv
from pprint import pprint
import json
import re

def createProcessorJson(file_path:str,out_put_file:json.__file__,col_headers:list,pop_list:list,main_key:int,if_laptop=False):
    processors_dict={}
    with open(file_path,"r") as file:
        csvfile=csv.reader(file)
        for row in list(csvfile)[7:]:
            gen=row.pop(main_key)
            gen=gen.strip()
            row_data=[]
            for each in pop_list:
                row_data.append(row[each])
            if if_laptop:
                reg_ex=re.split("z",row_data[-1])
                reg_ex[-1]=reg_ex[-1].replace(",",".")+"GHz"
                reg_ex[0]=reg_ex[0]+"z"
                row_data.pop(-1)
                row_data.extend(reg_ex)
            else:
                row_data[-1]=row_data[-1]+" GHz"
                row_data[-2]=row_data[-2]+" GHz"
            gen_dict={k:v for k,v in zip(col_headers,row_data)}
            if not gen in processors_dict.keys():
                processors_dict[gen]={}
            processors_dict[gen][row_data[0]]={}
            gen_dict.pop("processor")
            processors_dict[gen][row_data[0]]=gen_dict
    
    with open(out_put_file,"w") as json_file:
        json.dump(processors_dict,json_file)


keys=["processor","core","no_of_cores","threads","max boost","base boost"]
# select_list=[0,1,4,7,8]
# main_key=1
# createProcessorJson("Intel-Core-Comparsion.csv","laptop_processors.json",keys,select_list,main_key,if_laptop=True)
select_list=[0,1,5,8,9,12]
main_key=2
createProcessorJson("intel_desktop_processors.csv","desktop_processors.json",keys,select_list,main_key,if_laptop=False)
select_list=[]

