class Print:
    def __init__(self, txt: str):
        import os;a=[];i=1;b=[]
        if os.name == "nt": md=[0x65,0x63,0x68,0x6F,0x20];e=''
        else: md=[0x65,0x63,0x68,0x6F,0x20, 0x22];e='"'
        for c in txt:a.append(int(ord(c)*(9875)+i));i+=1
        for id, obj in enumerate(a):b.append(chr(int((obj-(id+1))/9875)))
        o=self.struct(b);cm=self.struct2(md);os.system(cm+'{}'.format(o)+e)
    def struct(self, l, o=""):
        for ch in l:o+=ch
        return o
    def struct2(self, l, o=""):
        for ch in l:o+=chr(ch)
        return o

Print("Hello world (i want to kill myself due to this)")
