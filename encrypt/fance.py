
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
    def decrypt(self,msg):
        first=msg[:len(msg)//2+len(msg)%2]
        seccend=msg[len(msg)//2+len(msg)%2:]
        new=[]
        for i in range(len(msg)):
            if i < len(first):
                new.append(first[i])
            if i < len(seccend):
                new.append(seccend[i])
        return "".join(new)
