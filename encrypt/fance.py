
class Fance:
    def encrypy(self,msg):
        msg = msg.replace(" ","")
        for i in range(len(msg)-1):
            msg[i],msg[i+1]=msg[i+1],msg[i]
a=Fance()
a.encrypy("abcde 132")
