import json
n =[1,2,3,4,6]
f="f.json"
with open(f,'w') as f_obj :
    json.dump(n,f_obj)
    print("The data was written to the file")
    
