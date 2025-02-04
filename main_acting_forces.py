#GRAVITATIONAL FORCE FORMULAE
#Using Newton's Law of Gravitation formulae
#Main constants
GRAVITATIONAL_CONSTANT = 6.67430 * 10**-11
MASS_OF_EARTH = 5.972 * 10**24 #Mass of the Earth in kilograms
RADIUS_OF_EARTH = 6.731 * 10**6 #Radius of then Earth in meters

h = (float(input("What is the height of your rocket in metres: " )))
m = (float(input("What is the mass of your rocket in kilograms: ")))

#The Gravitation formulae is : Gravitational_force(Fg) = (GRAVTITATIONAL_CONSTANT * mass_of_rocket * MASS_OF_EARTH) / (RADIUS_OF_EARTH + height_of_rocket)^2

'''
num_answer = GRAVITATIONAL_CONSTANT * m * MASS_OF_EARTH
den_answer = (RADIUS_OF_EARTH + h)**2

final_answer = num_answer / den_answer
print(f"The gravitational force acting on the rocket is: {final_answer}N")
'''

final_answer = (GRAVITATIONAL_CONSTANT * m * MASS_OF_EARTH) / (RADIUS_OF_EARTH + h)**2
print(f"The gravitational gorce acting on the rocket is:{final_answer}N")

print("------------------------------------------------------------------------------------------------------")

#Thrust-force
# Based on the  joint formulaes of Newton , Hermann Oberth , Robert H. Goddard and Sergey Kororlev
# The main foormulae is: Thrust-force(N) = mass_flow_rate_of_exhaust(kg/s) * exhaust_velocity + (nozzle_exit_pressure(Pa) - ambient_pressure(Pa)) * nozzle_exit_area(m^2)
mass_flow_rate_propellant = (float(input("What is the mass flow rate of your propellant in kg/s (in decimal form): "))) #Is the mass of the propellant expelled per unit time
#exhaust_velocity = 
rocket_fuel_type = (int(input("What type of propellant is being used:\n1.Solid\n2.Liquid\n3.Space-Engine e.g Ion-Thrusters")))
if rocket_fuel_type == 1:
    solid_fuel_type = (int(input("What is your solid fuel type from the list below:\n1.Ammonium-Perchlorate\n2.Cast-Perchlorate\n3.Zinc-sulfur\n3.Composite e.g Solid-oxidizer + Binder + Metal-powder + Additive\n4.Double-base\n5.Black-powder\n6.")))