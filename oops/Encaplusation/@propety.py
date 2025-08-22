class peron:
    def __init__(self):
        self.__name=""
    @property
    def dataAcee(self):
        return self.__name
    @dataAcee.setter
    def dataAcee(self,val):
        self.__name=val
p=peron()
p.dataAcee='suneel'
res=p.dataAcee
print(res)