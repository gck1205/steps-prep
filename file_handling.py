import json
import os
import logging

logging.basicConfig(level=logging.INFO,format='%(asctime)s- %(lineno)s - %(message)s')
file_path = r"C:\Users\chaitanya.garigipati\OneDrive - Accenture\Documents\steps-prep\data_files\apple_products.csv"
wfile_path = r"C:\Users\chaitanya.garigipati\OneDrive - Accenture\Documents\steps-prep\data_files\apple_products2.csv"
jpath = r"C:\Users\chaitanya.garigipati\OneDrive - Accenture\Documents\steps-prep\data_files\sample.json"
jwpath = r"C:\Users\chaitanya.garigipati\OneDrive - Accenture\Documents\steps-prep\data_files\samplew.json"

cnt=0
try:
    #read flat file
    with open(file_path,'r') as f:
        for line in f:
            pl=line.strip()
            with open(wfile_path,'a') as wf:
                 wf.write(pl+'\n')
                 wf.flush() # clear the memory buffer
            cnt+=1
    logging.info(f"  Total lines read and written to new file: {cnt}")

#read a json file
    if os.path.exists(jpath):
        logging.info(f"Specified file path exists: {jpath}")
        with open(jpath,'r') as jf:
               data = json.load(jf)
               logging.info(f"Data from json file: {data}")
#write to a json file
    lst=[("Revansh",8,"Bangalore"),("Jiggi",5,"Hyderabad"),("Rusha",6,"Chennai")]
    dct_lst=[]
    for i in lst:
         dct_lst.append({"name":i[0],"age":i[1],"city":i[2]})
    with open(jwpath,'w') as jwf:
            json.dump(dct_lst,jwf,indent=4)

except:
    logging.error(f"Specfied file path does not exist: {file_path}")