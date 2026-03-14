from vehicle import vehicle
class car(vehicle) :
    def __init__(self, n):
        super().__init__(n)
    def work(self):
        print("car runs on road with "+str(self.tyres)+" tyres")
class truck(vehicle):
    def __init__(self, n):
        super().__init__(n)
    def work(self):
        print("truck runs on road with "+str(self.tyres)+" tyres")
