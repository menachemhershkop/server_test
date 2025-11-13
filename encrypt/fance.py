
class Fance:
    def encrypy(self,msg):
        msg = list(msg.replace(" ",""))
        for i in range(len(msg)):
            if i %2 ==0:
                msg[i],msg[i+1]=msg[i+1],msg[i]

        return "".join(msg)

