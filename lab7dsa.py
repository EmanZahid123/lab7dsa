
class Stack:
    def __init__(self):
        self.list=[]

    def push(self,val):
        self.list.append(val)
    def pop(self):
        p=self.list.pop()
        return p
    def is_empty(self):
        if len(self.list)==0:
            return True
        return False
class CityData:
    def __init__(self,name,concount,con):
        self.name=name
        self.concount=concount
        self.con=con
        self.seen=False
        self.pred=-1
    def get_city(self):
        return self.name
    def get_seen(self):
        return self.seen
    def set_seen(self):
        self.seen=True
    def set_pred(self,cc):
        self.pred=cc
    def get_outcon(self):
        return self.con
def route(file,sc,des):
    f=open(file,"r")
    r=f.readline()
    city=[]
    for i in range(int(r)):
        r1=f.readline()
        r1=r1.replace(",","")
        r1=r1.split()

        concount=int(r1[2])

        con=[]
        for i in range(concount):
            con.append(int(r1[2+(i+1)]))
        cd=CityData(r1[1],concount,con)
        city.append(cd)
    stack=Stack()
    stcity=""
    for i in range(len(city)):
        if sc==city[i].get_city():
            stcity=sc
            city[i].seen=True
            stack.push(i)
    if stcity=="":
        return f"{sc} is not a valid city. Please re-enter options,"
    while not stack.is_empty():
        cc=stack.pop()
        dcity=""
        for i in range(len(city)):
            if des==city[i].get_city():
                dcity=des
                if cc==i:
                    pred=city[cc].pred
                    s=[]
                    s.append(des)
                    while pred !=-1:
                        s.append(city[pred].get_city())
                        pred=city[pred].pred

                    s.reverse()
                    s=" -> ".join(s)

                    return f"path is {s}"
                else:
                    con=city[cc].get_outcon()
                    for i in range(len(con)):
                        x=con[i]
                        if city[x].get_seen()==False:
                            city[x].set_seen()
                            city[x].set_pred(cc)
                            stack.push(x)
        if dcity=="":
            return f"{des} is not a valid city. Please re-enter options,"
    if stack.is_empty():
        return f"path not found from {sc} to {des},Please re-enter options,"

def main():
    file=input("Enter file name ")
    sc=input("Enter starting city ")
    des=input("Enter destination ")
    print(route(file,sc,des))
main()




