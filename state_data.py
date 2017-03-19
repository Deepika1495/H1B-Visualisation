import xlrd
from collections import OrderedDict
import json
book = xlrd.open_workbook("e.xlsx")
sheet = book.sheet_by_index(0)
cacount=0;
azcount=0;
us_states = {}
lis=[]
for rx in range(sheet.nrows):
    tmp = sheet.cell_value(rowx=rx,colx=1)
    stat = sheet.cell_value(rowx=rx,colx=4)
    state = sheet.cell_value(rowx=rx,colx=10)
    job  = sheet.cell_value(rowx=rx, colx=19)
    if (stat=="H-1B" and tmp =="CERTIFIED"):
        if state in us_states.keys() :
            #if city in us_states[state]:
            # us_states[state][city]["size"] += 1 
            us_states[state]+=1   
            #us_states[state]["size"] +=1
            #else:
            #new_dict = {}
            #new_dict["name"] = city
            #new_dict["size"] = 1
            #us_states[state][city] = new_dict
        else :
            if state != '' and state!='LCA_CASE_EMPLOYER_STATE':
                us_states[state]=1
            #new_dict = {}
            #new_dict["name"] = state
            #new_dict["size"] = 1
            #us_states[state] = new_dict
            # us_states[state]={}
states = [["AK","HI"],["WA","OR","CA"],["MT","ID","WY","NV","UT","CO","AZ","NM"],["ND","SD","NE","KS","OK","TX"],["MN","IA","MO","AR","LA"],["WI","MI","IL","IN","OH","KY","TN","MS","AL"],["VT","NH","ME","MA","CT","RI","NY","PA","NJ","WV","MD","DE","VA","NC","GA","SC","FL"]]
for i in range(0,len(states)):
    ch = [{"name":key, "size": value, "order": str(j+1)} for key,value in us_states.items() if key in states[i] for j in range(0,len(states[i])) if key==states[i][j]]
    inter =[{"name":"col"+str(k+1), "order": str(k+1), "children":ch} for k in range(0,8) if i==k]
    lis.extend(inter)
us = {"name":"states_tree","children" :lis}
print (us)
#us_states.append(states)
j = json.dumps(us,indent=4)
with open('year12.json', 'w') as f:
    f.write(j)
