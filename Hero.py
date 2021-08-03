class Hero:
    def __init__(self,name):
        self.HealthPool=[1,100,200,300,400,500]
        self.AttackpowerPool=[0,10,20,30,40,50]
        self.armorpool=[1,2,3,4,5]
        self.__name=name
        self.__exp=0
        self.__level=0
        
    def showifo(self):
        print("{} \n\tLevel : {}\n\tHealth : {}\n\tattackpower : {} \n\tArmor : {}".format(
                 self.__name,
                 self.__level,
                 self.__Health,
                 self.__AttackPower, 
                 self.__armor
        )
    ) 

    @property
    def HealthPool(self):
        pass
    
    @property
    def AttackPowerPool(self):
        pass

    @property    
    def armorPool(self):
        pass

    @property
    def Levelup (self):
        pass

    @property
    def Gain_exp(self):
        pass

    @HealthPool.setter
    def HealthPool(self,input):
        self.__HealthPool=input

    @AttackPowerPool.setter
    def AttackPowerPool(self,input):
        self.__AttackPowerPool=input

    @armorPool.setter
    def armorPool(self,input):
        self.__armorPool=input

    @Gain_exp.setter
    def Gain_exp(self,input):
        self.__exp += input
        if(self.__exp >= 100):
            self.Levelup=self.__exp//100
            self.__exp %= 100

    @Levelup.setter
    def Levelup(self,input):
        self.__level += input
        self.__Health = self.__HealthPool[self.__level]
        self.__AttackPower= self.__AttackPowerPool[self.__level]
        self.__armor=self.__armorPool[self.__level]

class HeroInteligent(Hero):
    def __init__(self, name):
        super().__init__(name)
        self.HealthPool=[0,50,100,150,200,350]
        self.AttackPowerPool=[0,20,40,80,100]
        self.armorPool=[1,2,4,6,8,10]
        self.Levelup=1


class HeroStrength(Hero):
    def __init__(self, name):
        super().__init__(name)
        self.HealthPool=[1,200,400,600,800]
        self.AttackPowerPool=[0,20,40,60,80,100]
        self.armorPool=[1,1.5,2,2.5,3]
        self.Levelup=1
