class Caesar:
    def encrypy(self,msg,offset):
        msg=list(msg.lower())
        abc= list(map(chr, range(97, 123)))
        for i,y in enumerate(msg):
            for x,z in enumerate(abc):
                if y ==z:
                    if x+offset>len(abc):
                        x=(x+offset)%25
                        msg[i]=abc[x]
                    else:
                        msg[i] = abc[x + offset]
        return "".join(msg)
    def decrypt(self,msg,offset):
        msg = list(msg.lower())
        abc = list(map(chr, range(97, 123)))
        for i,y in enumerate(msg):
            for x,z in enumerate(abc):
                if y ==z:
                    if x-offset<0:
                        x=(x+offset)%25
                        msg[i]=abc[x]
                    else:
                        msg[i] = abc[x - offset]
        return "".join(msg)
