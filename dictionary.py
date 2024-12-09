info={
    "age": 19,
    "vill": "kolaberia",
    "is adult": True,
    "sub":["c","python"],
     "topics": ("dictionary","sets"),
    2.6:7.7
}
print(info)
print(info["age"])
print(info[2.6])
info["age"]=18
print(info)
print(info.keys())
print(info.get("qwerty"))
for key,value in info.items():
    print(key,"->",value);