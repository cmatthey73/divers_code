import math

class kreis:
    def __init__(self, r):
        self.radius = r
           
    def get_umfang(self):
        return 2*self.radius * math.pi

    def get_flaeche(self):
        return self.radius**2 * math.pi 
    
    def print(self):
        print("Kreis mit Radius "+str(self.radius)+" : \n"+"- Umfang = "+str(self.get_umfang())+"\n"+"- Flaeche = "+str(self.get_flaeche()))

class zylinder:
    def __init__(self, r, h):
        self.radius = r
        self.hohe = h
    
    def volumen(self):
        return self.radius * self.hohe
    
    def print(self):
        print("Zylinder mit Radius "+str(self.radius)+" und Höhe "+str(self.hohe)+" : \n"+"- Volumen = "+str(self.volumen()))

kreis(10).print()
zylinder(10,50).print()

