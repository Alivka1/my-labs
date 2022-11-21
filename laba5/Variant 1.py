class Rocket():                                #Инициализатор
    def __init__(self,mass, fuel, engine):  
        self.mass = mass
        self.fuel = fuel
        engine = engine

class Baikonur(Rocket):
    def __init__(self):
        super().__init__(8000, 3500, True)
        if self.fuel == 0:              #Проверяет, есть ли топливо в изначально заданных параметрах
            self.engine = False
        else:
            self.engine = True

    def spend_fuel(self, count):            #Метод, позволяющий израсходовать count кг топлива
        self.fuel = (int(self.fuel) - int(count))
        self.mass = (int(self.mass) - int(count))
        if (int(self.fuel) - int(count)) <= 0:
            self.engine = False
        if self.fuel > 0:
            return True 
        else:
            return False

    def get_fuel_level(self):
        return self.fuel
    def get_total_weight(self):
        return self.mass
    def get_is_engine_running(self):
        return self.engine
    
class Main(Rocket):
    def __init__(self):
        super().__init__(int(input()), int(input()), True)
        if self.fuel == 0:
            self.engine = False
        else:
            self.engine = True
        step = int(input())   #Количество топлива, которое расходуется каждую секунду
        while self.engine == True:#Пока двигатель работает, топливо расходуется
            self.fuel = self.fuel - step
            self.mass = self.mass - step
            if self.fuel - step < 0:    
            	self.engine = False #Двигатель останавливается, когда топливо израсходовалось 
            print(self.mass, self.fuel, self.engine) #Каждый этап выводятся параметры ракеты

M = Main()
print(M.mass,'\n')
R = Baikonur()
print(R.spend_fuel(3500))
print(R.get_fuel_level())
print(R.get_total_weight())
print(R.get_is_engine_running())

