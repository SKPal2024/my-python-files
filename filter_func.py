friends=[
    ("a",16),
    ("b",19),
    ("c",32),
    ("d",18)
]
vote=lambda data:data[1]>17
x=list(filter(vote,friends))
for i in x:
    print(i)