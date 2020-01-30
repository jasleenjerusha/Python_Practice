class Planet:

    shape = 'round'

    def __init__(self,name,radius,gravity,system):
        self.name = name
        self.radius = radius
        self.gravity = gravity
        self.system = system

    def orbit(self):
        return f'{self.name} is orbiting in the {self.system}'

    @classmethod
    def common(cls):
        return f'all planets are {cls.shape} duw to gravity'

    @staticmethod
    def spin(speed = '2000 miles per hour'):
        return f'the planets spin at {speed}'   

earth = Planet('Earth',200000,5.5,'solar system')
print(f'Name is : {earth.name}')
print(f'Radius is : {earth.radius}')
print(f'Gravity is : {earth.gravity}')
print(f'System is : {earth.system}')
print(earth.orbit())

planet_new = Planet('Jupiter',400000,6.5,'solar system')
print(f'Name is : {planet_new.name}')
print(f'Radius is : {planet_new.radius}')
print(f'Gravity is : {planet_new.gravity}')
print(f'System is : {planet_new.system}')
print(planet_new.orbit())

print(Planet.shape)
print(planet_new.shape)

print(Planet.common())
print(Planet.spin('at a very high speed'))