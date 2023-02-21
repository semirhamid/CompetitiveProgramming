class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.spot = [big,medium,small]

    def addCar(self, carType: int) -> bool:
        if carType == 1:
            if self.spot[0] == 0:
                return False
            else: 
                self.spot[0] -= 1
                return True
        elif carType == 2:
            if self.spot[1] == 0:
                return False
            else: 
                self.spot[1] -= 1
                return True
        else:
            if self.spot[2] == 0:
                return False
            else: 
                self.spot[2] -= 1
                return True


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)