from Coche import Coche, Empresa, Garage
# Instance

enterprise = Empresa('English')
print(enterprise.getInformation())
coche = Coche("Red", "Mazda", 0)
print(coche.getInfo())
audite = Garage("Red", "Mazda", 0)
audite.geAudite()