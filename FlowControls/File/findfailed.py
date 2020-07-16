f1=open("C:/Users/user/PycharmProjects/LuminarPython/FlowControls/File/students")
f2=open("C:/Users/user/PycharmProjects/LuminarPython/FlowControls/File/passed")
f3=open("failed.txt","w")
def readdata(fref):
    st=set()
    for data in fref:
        data=data.rstrip("\n")
        st.add(data)
    return st
st1=readdata(f1)
st2=readdata(f2)
print(st1)
print(st2)
fail=st1-st2
print(fail)
for data in fail:
    f3.write(data+"\n")
