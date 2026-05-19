class Money:
    def __init__(self, amount = int, currency = "VND"):
        self.__amount = amount
        self.__currency = currency
    
    def __str__(self):
        return f"{self.__amount} {self.__currency}"
    
    def __eq__(self, other):
        if self.__currency != other.__currency:
            return False
        return self.__amount == other.__amount