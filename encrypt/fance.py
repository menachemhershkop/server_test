
class Fence:
    def encrypy(self,msg):
        msg = msg.replace(" ","")
        double=[]
        odd=[]
        for i in range(len(msg)):
            if i %2 ==0:
                double.append(msg[i])
            else:
                odd.append(msg[i])
        return "".join(double+odd)
a=Fence()
print(a.encrypy("1234"))
