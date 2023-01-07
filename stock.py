class Stock:
    def __init__(self,name,code,PER,PBR,dividend):
        self.name = name
        self.code = code
        self.info = name,code,PER,PBR,dividend
        self.PER = PER
        self.PBR = PBR
        self.dividend = dividend

    def set_name(self,name):
        self.name = name

    def set_code(self,code):
        self.code = code

    def set_PER(self,PER):
        self.PER = PER

    def set_PBR(self,PBR):
        self.PBR = PBR

    def set_dividend(self,dividend):
        self.dividend = dividend

    def get_name(self):
        return self.name

    def get_code(self):
        return self.code

삼성전자 = Stock("삼성전자", "005930",15.79, 1.33, 2.83)
현대차 = Stock("현대차", "005380", 8.7, 0.35, 1.37)
LG전자 = Stock("LG전자", "066570", 317.34, 0.69, 1.37)

list = []
list.append(삼성전자.info)
list.append(현대차.info)
list.append(LG전자.info)
for i in list:
    print(i[0],i[2])