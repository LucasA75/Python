class Currency(object):
    def __init__(self,name,symbol,factor):
        self.name = name
        self.symbol = symbol
        self.factor = factor

    def convert_amount_to_base_currency(self,aNunber):
        return aNunber * self.factor
    def convert_amount_from_base_currency(self,aNunber):
        return aNunber / self.factor
    def __repr__(self):
        return self.name

class Money(object):
    def __init__(self,amount,currency):
        self.amount = amount
        self.currency = currency

    def base_currency_amount(self):
        return self.currency.convert_amount_to_base_currency(self.amount)

    def __add__(self,anAmount0fmoney):
        amount = self.base_currency_amount() + anAmount0fmoney.base_currency_amount()
        amount = self.currency.convert_amount_from_base_currency(amount)
        return Money(amount, self.currency)

    def __sub__(self,anAmount0fmoney):
        amount = self.base_currency_amount() - anAmount0fmoney.base_currency_amount()
        amount = self.currency.convert_amount_from_base_currency(amount)
        return Money(amount, self.currency)

    def __mul__(self, aNunber):
        return Money(self.amount * aNunber, self.currency)

    def __truediv__(self, aNunber):
        return Money(self.amount / aNunber, self.currency)


    def __repr__(self):
        return "{} {} ".format(self.currency.symbol, self.amount)


dolar = Currency("Dolar", "U$S",1)
pesos = Currency("pesos (Arg)", "$", 1/40)

one_dolar = Money(1,dolar)
one_peso = Money(1,pesos)