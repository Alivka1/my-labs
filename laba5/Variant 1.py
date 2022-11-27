class Rocket():  #Инициализатор
    def __init__(self,mass, fuel, engine):  
        self.mass = mass
        self.fuel = fuel
        self.engine = engine

    def spend_fuel(self, count):  #Метод, позволяющий израсходовать count кг топлива
        self.fuel -= count
        self.mass -= count
        if self.fuel <= 0:  
            self.fuel=0
            self.engine = False       #Двигатель останавливается, когда топливо израсходовалось 
            return False
        elif self.fuel > 0:
            self.engine = True
            return True         

    def get_fuel_level(self):
        return f'Кол-во топлива: {self.fuel}'
    def get_total_weight(self):
        return f'Масса ракеты: {self.mass}'
    def get_is_engine_running(self):
        return f'Состояние двигателя: {self.engine}'
    
def Main():
    Raketa_Baikonur = Rocket(150000, 60000, True)
    while Raketa_Baikonur.fuel > 0:                    
        Raketa_Baikonur.spend_fuel(2000)
        print(Raketa_Baikonur.get_fuel_level(), end='; ')
        print(Raketa_Baikonur.get_total_weight(), end='; ')
        print(Raketa_Baikonur.get_is_engine_running())
Main()

