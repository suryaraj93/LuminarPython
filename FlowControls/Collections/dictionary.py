employee={"name":"arun","id":100,"salary":500000}
for k,v in employee.items():
    print(k,",",v)
employee["exp"]=2
print(employee)
print("name" in employee)