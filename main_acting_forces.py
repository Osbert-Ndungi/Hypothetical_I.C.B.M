#GRAVITATIONAL FORCE FORMULAE
#Using Newron's Law of Gravitation formulae
#Main constants
GRAVITATIONAL_CONSTANT = 6.674 * 10**-11
MASS_OF_EARTH = 5.972 * 10**24 #Mass of the Earth in kilograms
RADIUS_OF_EARTH = 6.731 * 10**6 #Radius of then Earth in meters

h = (int(input("What is the height of your rocket in metres: " )))
m = (int(input("What is the mass of your rocket in kilograms: ")))

#The Gravitation formulae is : Gravitational_force(Fg) = (GRAVTITATIONAL_CONSTANT * mass_of_rocket * MASS_OF_EARTH) / (RADIUS_OF_EARTH + height_of_rocket)^2


num_answer = GRAVITATIONAL_CONSTANT * m * MASS_OF_EARTH
den_answer = (RADIUS_OF_EARTH + h)**2

final_answer = num_answer / den_answer
print(f"The gravitational force acting on the rocket is: {final_answer}N")

#final_answer = (GRAVITATIONAL_CONSTANT * m * MASS_OF_EARTH) / (RADIUS_OF_EARTH + h)**2
#print(f"The gravitational gorce acting on the rocket is:{final_answer}")
