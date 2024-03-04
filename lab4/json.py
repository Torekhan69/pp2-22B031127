import json

with open(r"C:\Users\Torekhan\Desktop\Git\py_repo\tsis4\sample-data.json") as s:
    data = json.load(s)

print("""Interface Status
================================================================================
DN                                                 Description           Speed    MTU  
-------------------------------------------------- --------------------  ------  ------""")
for i in data["imdata"]:
    print(i["l1PhysIf"]["attributes"]["dn"]+" "*30
    +i["l1PhysIf"]["attributes"]["speed"]+" "*3
    +i["l1PhysIf"]["attributes"]["mtu"])
