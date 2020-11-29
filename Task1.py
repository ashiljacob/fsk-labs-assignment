d = [
    {
        "id" :1,
        "name": "ramesh",
        "cost":'2000'
    },
      {
        "id" :2,
        "name": "ajith",
        "cost":"5000"
    },
      {
        "id" :3,
        "name":'harish' ,
        "cost":'90000'
    },
     {
        "id" :4,
        "name":'abhishek' ,
        "cost":'55000'
    }

]

lst  = []
lst2 = []

for i in range(len(d)):
    lst.append(d[i]['name'])

lst1 = sorted(lst)

for i in lst1:
    for j in range(len(d)):
        if d[j]['name'] == i:
            lst2.append(d[j])


print("Sorted Dictionary : \n",lst2)