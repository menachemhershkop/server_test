class Caeser:
    def encrypy(self,msg,offset):
        msg=list(msg.lower())
        abc= list(map(chr, range(97, 123)))
        for i,y in enumerate(msg):
            for x,z in enumerate(abc):
                if y ==z:
                    if x+offset>len(abc):
                        x-=len(abc)
                        msg[i]=abc[x+offset]
                    else:
                        msg[i] = abc[x + offset]
        print(msg)
a=Caeser()
a.encrypy("abc",49)

