from abc import ABC,abstractmethod

class Feature_class(ABC):
    @abstractmethod
    def login(self):
        pass
    @abstractmethod
    def signin(self):
        pass


class WebApp(Feature_class):
    def login(self):
        print("this is login page")
    def signin(self):
        print("this is sigin page")
    def webapp(self):
        print("this is webapp page")


web = WebApp()

web.login()


class Car(ABC):
    @abstractmethod
    def gear(self):
        print(" The gear")

    def fuel(self):
        print("The fuel")

class Bike(Car):
        def gear(self):
          print("this is the gear")
        def fuel(self):
            print("this is the fuel")
vechile = Bike()
# vechile.gear()
vechile.fuel()


class  account(ABC):
    @abstractmethod
    def bank(self):
        pass

class withdrawingAmount(account):
    def __init__(self,creditcard,Debitcard):
        self.creditcard=creditcard
        self.Debitcard = Debitcard
    def bank(self):
        print(f"Debit card is : {self.Debitcard}")
        print(f"Credit card is :{self.creditcard}")
        
cash = withdrawingAmount("123","456")
cash.bank()