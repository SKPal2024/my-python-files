store=[
    ("shirt",10),
    ("pant",12),
    ("hat",4)
]
to_inr=lambda data: (data[0],data[1]*83)
inr_store=list(map(to_inr,store))
for i in inr_store:
    print(i)
