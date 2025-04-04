# GRAVITATIONAL FORCE FORMULAE
# Using Newton's Law of Gravitation formulae
# Main constants
import math

GRAVITATIONAL_CONSTANT = 6.67430 * 10**-11
MASS_OF_EARTH = 5.972 * 10**24  # Mass of the Earth in kilograms
RADIUS_OF_EARTH = 6.731 * 10**6  # Radius of then Earth in meters
GRAVITATIONAL_ACCELERATION = 9.81 #This is in m/s**2
SEA_LEVEL_AIR_DENSITY= 1.224 #This is an approximate in kg/m3
SEA_LEVEL_STD_TEMP = 288.15 #This is in Kelvin
TEMP_LAPSE_RATE = 0.0065 #This is in Kelvin per meter(K/m)
MOLAR_MASS_EARTH_AIR = 0.028965 #This is in kilogram/mol (kg/mol)
GAS_CONSTANT = 8.314 #This is in Joules per mol per Kelvin

rocket_height = float(input("What is the height of your rocket in metres: "))
initial_rocket_mass = float(input("What is the mass of your rocket in kilograms: "))
#rocket_latitude = float(input("What are the latitude co-ordinates of your launch site in DMS(degrees , minutes , seconds)"))
# rocket_latitude_direction = float(input("What is the direction of your longitude:\n1.North\n2.South)"))
# rocket_longitude = float(input("What are the longitude co-ordinates of your launch site in DMS(degrees , minutes , seconds)"))
# rocket_longitude_direction = float(input("What is the direction of your longitude:\n1.North\n2.South"))
# The Gravitation formulae is : Gravitational_force(Fg) = (GRAVTITATIONAL_CONSTANT * mass_of_rocket * MASS_OF_EARTH) / (RADIUS_OF_EARTH + height_of_rocket)^2

final_answer = (GRAVITATIONAL_CONSTANT * initial_rocket_mass * MASS_OF_EARTH) / (RADIUS_OF_EARTH + rocket_height) ** 2
print(f"The gravitational force acting on the rocket is:{final_answer}N")

print(
    "------------------------------------------------------------------------------------------------------"
)

# Thrust-force
# Based on the  joint formulaes of Newton , Hermann Oberth , Robert H. Goddard and Sergey Kororlev
# The main formulae is: Thrust-force(N) = mass_flow_rate_of_exhaust(kg/s) * exhaust_velocity + (nozzle_exit_pressure(Pa) - ambient_pressure(Pa)) * nozzle_exit_area(m^2)
# mass_flow_rate_propellant = (int(input("What is the mass flow rate of your propellant in kg/s: "))) #Is the mass of the propellant expelled per unit time
# Mass flow rate can be calculated multiplying the density of the propellant with the surface area of the propellant and its average burn rate
#specific impulse (Isp) this is the thrust per unit weight flow rate of propellant in seconds
#Exhaust velocity can be found using two different formulas for ease I used the simple formula of exhaust velocity =  specific impulse (in seconds) * gravitational acceleartion(in m/s**2)  


# Rocket / Tsiolkovsky equation
# It can be used to measure the change in velocity of a rocket in motion during fuel consumption
# Change in velocity = Exhaust_velocity * ln(Initial_mass / Final_mass)
# The mass of the fuel can be idenfied directly or calculated using density of propellant * surface area of propellant * length or height



average_burning_surface_area = float(
    input(
        "What is your average burning surface area in square meters-This is the area of the cylinder that contains the propellant\n"
    )
)
rocket_fuel_type = int(
    input(
        "\nWhat type of propellant is being used:\n1.Solid\n2.Liquid\n3.Space-Engine e.g Ion-Thrusters\n"
    )
)

if rocket_fuel_type == 1:
    solid_fuel_type = int(
        input(
            "What is your solid fuel type from the list below:\n1.Ammonium-Perchlorate\n2.Potassium-perchlorate\n3.Zinc-sulfur\n3.Composite e.g Solid-oxidizer + Binder + Metal-powder + Additive\n4.Double-base\n5.Black-powder\n"
        )
    )

    if solid_fuel_type == 1:
        ammonium_perchlorate_burn_rate = (
            0.03  # This is an average of between 0.01 to 0.05 m/s
        )
        ammonium_perchlorate_density = 1800  # This is in kg/m3
        ammonium_perchlorate_mfr = (
            ammonium_perchlorate_burn_rate
            * average_burning_surface_area
            * ammonium_perchlorate_density
        )  # This is the average mass flow rate of Ammonium-perchlorate in kg/s
        print(
            f"Your ammonium-perchlorate mass flow rate is {ammonium_perchlorate_mfr}kg/s"
        )
        ammonium_perchlorate_isp = 220 #This is an average of between 180 to 260 seconds
        ammonium_perchlorate_exhaust_velocity = ammonium_perchlorate_isp * GRAVITATIONAL_ACCELERATION
        print(f"Your exhaust velocity is {ammonium_perchlorate_exhaust_velocity}s")
        thrust_force = ammonium_perchlorate_mfr * ammonium_perchlorate_exhaust_velocity
        print(f"Your approximate thrust is {thrust_force}Newtons")
        mass_of_propellant = (float(input("What is the mass of your fuel/propellant in kilograms?\n")))
        final_rocket_mass = initial_rocket_mass - mass_of_propellant  
        change_in_mass = initial_rocket_mass / final_rocket_mass
        change_in_velocity = ammonium_perchlorate_exhaust_velocity * math.log(change_in_mass) 
        print(f"Your change in velocity is {change_in_velocity}")
        rocket_altitude = float(input("What is the altitude of your rocket in meters ?\n"))
        #For this equation i asked the user to input their altitude but this can be done using an altimeter
        ground_velocity = float(input("What is your ground velocity in m/s ?\n"))
        wind_velocity = float(input("What is your wind velocity in m/s ?\n"))
        wind_direction = int(input("Is your rocket flying ;\n1.Against the wind(Opposite to the rocket)\n2.In the same direction"))
        if wind_direction == 1:
            air_relative_velocity = ground_velocity + wind_velocity
            print(f"Your Actual air relative velocity is {air_relative_velocity}m/s")
            centripetal_force = (initial_rocket_mass * (air_relative_velocity **2)) / (rocket_height + rocket_altitude + RADIUS_OF_EARTH)
            print(f"Your centripetal force is {centripetal_force}Newtons")
            #To find the centripetal force = (Mass of the rocket (kg) * air_relative velocity ** 2 ) / radius of the earth + height of rocket
        elif wind_direction == 2:
            air_relative_velocity = ground_velocity - wind_velocity
            print(f"Your Actual air relative velocity is {air_relative_velocity}m/s")
            #The drag coefficient of your rocket can be deteermined before hand by running various tests like wind tunnel testing , CFD , flight testing and empirical estimation
            #It is usually between 0.1 to 1.5
            drag_coefficient = int(input("What is your drag coefficient ?\n"))
            #The formulae for drag is Drag = 0.5 * drag_coefficient * air_density * cross_sec_area * air_relative_-velocity^2
            
            inner_den = SEA_LEVEL_STD_TEMP + (TEMP_LAPSE_RATE * rocket_altitude) #This is the denominator inside the brackets of the air density formulae
            inner_full = SEA_LEVEL_STD_TEMP / inner_den #This is everything inside the bracket of the air density formulae
            outer_power = (GRAVITATIONAL_ACCELERATION * MOLAR_MASS_EARTH_AIR) / (GAS_CONSTANT * TEMP_LAPSE_RATE) #This is everything in the power form for the air density formulae
            inner_power = inner_full * outer_power #This is when everything in the bracket is multiplied by the the full power in the air density formulae
            air_density = SEA_LEVEL_AIR_DENSITY * inner_power
            print(f"The air density is {air_density}kg/m3")
            rocket_cross_sectional_area = float(input("What is the cross-sectional area of your rocket in meters-squared ?\n"))
            drag_force = 0.5 * drag_coefficient * air_density * rocket_cross_sectional_area * (air_relative_velocity ** 2)
            print(f"Your approximate drag is {drag_force}Newtons")
            centripetal_force = (initial_rocket_mass * (ground_velocity **2)) / (rocket_height + rocket_altitude + RADIUS_OF_EARTH)
            print(f"{centripetal_force}Newtons")
            rocket_fins = int(input("Does your rocket have aerodynamic fins ?\n1.Yes\n2.No\n"))
            
            if rocket_fins == 1:
                lift_coefficient = int(input("What is your coefficient of lift"))
                wing_area = float(input("What is your reference/wing area in meters-squared ?\n"))
                lift_force = 0.5 * lift_coefficient * air_density * wing_area * (air_relative_velocity ** 2)
                print (f"Your approximate lift force if {lift_force}")
            elif rocket_fins == 2:
                lift_force = 0 #Your rocket does not generate lift without aerodynamic fins
                print(f"Your rocket {lift_force}Newtons")

    elif solid_fuel_type == 2:
        potassium_perchlorate_burn_rate = (
            0.016  # This is an average of between 0.002 to 0.03 m/s
        )
        potassium_perchlorate_density = 2520  # This is in kg/m3
        potassium_perchlorate_mfr = (
            potassium_perchlorate_burn_rate
            * average_burning_surface_area
            * potassium_perchlorate_density
        )
        print(
            f"Your potassium-perchlorate mass flow rate is {potassium_perchlorate_mfr}kg/s"
        )
        potassium_perchlorate_isp = 187.5 #This is an average of between 165 to 210 seconds
        potassium_perchlorate_exhaust_velocity = potassium_perchlorate_isp * GRAVITATIONAL_ACCELERATION
        print(f"Your exhaust velocity is {potassium_perchlorate_exhaust_velocity}s")
        thrust_force = potassium_perchlorate_mfr * potassium_perchlorate_exhaust_velocity
        print(f"Your approximate thrust is {thrust_force}Newtons") 
        mass_of_propellant = (float(input("What is the mass of your fuel/propellant in kilograms?\n")))
        final_rocket_mass = initial_rocket_mass - mass_of_propellant  
        change_in_mass = initial_rocket_mass / final_rocket_mass
        change_in_velocity = potassium_perchlorate_exhaust_velocity * math.log(change_in_mass) 
        print(f"Your change in velocity is {change_in_velocity}")
        rocket_altitude = float(input("What is the altitude of your rocket in meters ?\n"))
        #For this equation i asked the user to input their altitude but this can be done using an altimeter
        ground_velocity = float(input("What is your ground velocity in m/s ?\n"))
        wind_velocity = float(input("What is your wind velocity in m/s ?\n"))
        wind_direction = int(input("Is your rocket flying ;\n1.Against the wind(Opposite to the rocket)\n2.In the same direction"))
        if wind_direction == 1:
            air_relative_velocity = ground_velocity + wind_velocity
            print(f"Your Actual air relative velocity is {air_relative_velocity}m/s")
            centripetal_force = (initial_rocket_mass * (air_relative_velocity **2)) / (rocket_altitude + rocket_height + RADIUS_OF_EARTH)
            print(f"Your centripetal force is {centripetal_force}Newtons")
        elif wind_direction == 2:
            air_relative_velocity = ground_velocity - wind_velocity
            print(f"Your Actual air relative velocity is {air_relative_velocity}m/s")
            #The drag coefficient of your rocket can be deteermined before hand by running various tests like wind tunnel testing , CFD , flight testing and empirical estimation
            #It is usually between 0.1 to 1.5
            drag_coefficient = int(input("What is your drag coefficient ?\n"))
            #The formulae for drag is Drag = 0.5 * drag_coefficient * air_density * cross_sec_area * air_relative_-velocity^2
            
            inner_den = SEA_LEVEL_STD_TEMP + (TEMP_LAPSE_RATE * rocket_altitude) #This is the denominator inside the brackets of the air density formulae
            inner_full = SEA_LEVEL_STD_TEMP / inner_den #This is everything inside the bracket of the air density formulae
            outer_power = (GRAVITATIONAL_ACCELERATION * MOLAR_MASS_EARTH_AIR) / (GAS_CONSTANT * TEMP_LAPSE_RATE) #This is everything in the power form for the air density formulae
            inner_power = inner_full * outer_power #This is when everything in the bracket is multiplied by the the full power in the air density formulae
            air_density = SEA_LEVEL_AIR_DENSITY * inner_power
            print(f"The air density is {air_density}kg/m3")
            rocket_cross_sectional_area = float(input("What is the cross-*sectional area of your rocket in meters-squared ?\n"))
            drag_force = 0.5 * drag_coefficient * air_density * rocket_cross_sectional_area * (air_relative_velocity ** 2)
            print(f"Your approximate drag is {drag_force}Newtons")
            centripetal_force = (initial_rocket_mass * (ground_velocity **2)) / (rocket_altitude + rocket_height + RADIUS_OF_EARTH)
            print(f"{centripetal_force}Newtons")
            rocket_fins = int(input("Does your rocket have aerodynamic fins ?\n1.Yes\n2.No\n"))
            
            if rocket_fins == 1:
                lift_coefficient = int(input("What is your coefficient of lift"))
                wing_area = float(input("What is your reference/wing area in meters-squared ?\n"))
                lift_force = 0.5 * lift_coefficient * air_density * wing_area * (air_relative_velocity ** 2)
                print (f"Your approximate lift force if {lift_force}")
            elif rocket_fins == 2:
                lift_force = 0 #Your rocket does not generate lift without aerodynamic fins
                print(f"Your rocket {lift_force}Newtons")

    elif solid_fuel_type == 3:
        zinc_sulfur_burn_rate = 0.3  # This is an average of between 0.1 to 0.5 m/s
        zinc_sulfur_density = 2250  # This is an average of between 2000 to 2500 kg/m3
        zinc_sulfur_mfr = (
            zinc_sulfur_burn_rate * average_burning_surface_area * zinc_sulfur_density
        )
        print(f"Your zinc-sulfur mass flow rate is {zinc_sulfur_mfr}kg/s")
        zinc_sulfur_isp = 160 #This is an average of between 150 - 170 s
        zinc_sulfur_exhaust_velocity = zinc_sulfur_isp * GRAVITATIONAL_ACCELERATION
        print(f"Your exhaust velocity is {zinc_sulfur_exhaust_velocity}s")
        thrust_force = zinc_sulfur_mfr * zinc_sulfur_exhaust_velocity #This is your approx thrust in Newtons
        print(f"Your approximate thrust is {thrust_force}Newtons")
        mass_of_propellant = (float(input("What is the mass of your fuel/propellant in kilograms?\n")))
        final_rocket_mass = initial_rocket_mass - mass_of_propellant  
        change_in_mass = initial_rocket_mass / final_rocket_mass
        change_in_velocity = zinc_sulfur_exhaust_velocity * math.log(change_in_mass) 
        print(f"Your change in velocity is {change_in_velocity}")
        rocket_altitude = float(input("What is the altitude of your rocket in meters ?\n"))
        #For this equation i asked the user to input their altitude but this can be done using an altimeter
        ground_velocity = float(input("What is your ground velocity in m/s ?\n"))
        wind_velocity = float(input("What is your wind velocity in m/s ?\n"))
        wind_direction = int(input("Is your rocket flying ;\n1.Against the wind(Opposite to the rocket)\n2.In the same direction"))
        if wind_direction == 1:
            air_relative_velocity = ground_velocity + wind_velocity
            print(f"Your Actual air relative velocity is {air_relative_velocity}m/s")
            centripetal_force = (initial_rocket_mass * (ground_velocity **2)) / (rocket_height + rocket_altitude + RADIUS_OF_EARTH)
            print(f"Your centripetal force is {centripetal_force}Newtons")
        elif wind_direction == 2:
            air_relative_velocity = ground_velocity - wind_velocity
            print(f"Your Actual air relative velocity is {air_relative_velocity}m/s")
            #The drag coefficient of your rocket can be deteermined before hand by running various tests like wind tunnel testing , CFD , flight testing and empirical estimation
            #It is usually between 0.1 to 1.5
            drag_coefficient = int(input("What is your drag coefficient ?\n"))
            #The formulae for drag is Drag = 0.5 * drag_coefficient * air_density * cross_sec_area * air_relative_-velocity^2
            
            inner_den = SEA_LEVEL_STD_TEMP + (TEMP_LAPSE_RATE * rocket_altitude) #This is the denominator inside the brackets of the air density formulae
            inner_full = SEA_LEVEL_STD_TEMP / inner_den #This is everything inside the bracket of the air density formulae
            outer_power = (GRAVITATIONAL_ACCELERATION * MOLAR_MASS_EARTH_AIR) / (GAS_CONSTANT * TEMP_LAPSE_RATE) #This is everything in the power form for the air density formulae
            inner_power = inner_full * outer_power #This is when everything in the bracket is multiplied by the the full power in the air density formulae
            air_density = SEA_LEVEL_AIR_DENSITY * inner_power
            print(f"The air density is {air_density}kg/m3")
            rocket_cross_sectional_area = float(input("What is the cross-sectional area of your rocket in meters-squared ?\n"))
            drag_force = 0.5 * drag_coefficient * air_density * rocket_cross_sectional_area * (air_relative_velocity ** 2)
            print(f"Your approximate drag is {drag_force}Newtons")
            centripetal_force = (initial_rocket_mass * (ground_velocity **2)) / (rocket_altitude + rocket_height + RADIUS_OF_EARTH)
            print(f"{centripetal_force}Newtons")
            rocket_fins = int(input("Does your rocket have aerodynamic fins ?\n1.Yes\n2.No\n"))
            
            if rocket_fins == 1:
                lift_coefficient = int(input("What is your coefficient of lift"))
                wing_area = float(input("What is your reference/wing area in meters-squared ?\n"))
                lift_force = 0.5 * lift_coefficient * air_density * wing_area * (air_relative_velocity ** 2)
                print (f"Your approximate lift force if {lift_force}")
            elif rocket_fins == 2:
                lift_force = 0 #Your rocket does not generate lift without aerodynamic fins
                print(f"Your rocket {lift_force}Newtons")


    elif solid_fuel_type == 4:
        composite_burn_rate = 1.35  # This is an average of between 0.2 to 2.5 m/s
        composite_density = 1800  # This is an average of between 1700 to 1900 kg/m3
        composite_mfr = (
            composite_burn_rate * average_burning_surface_area * composite_density
        )
        print(f"Your composite mass flow rate is {composite_mfr}kg/s")
       

    elif solid_fuel_type == 5:
        double_base_burn_rate = (
            0.015  # This is an average of between 0.005 and 0.025 m/s
        )
        double_base_density = 1650  # This is an average of between 1600 to 1700 kg/m3
        double_base_mfr = (
            double_base_burn_rate * average_burning_surface_area * double_base_density
        )
        print(f"Your double-base mass flow rate is {double_base_mfr}kg/s")
        double_base_isp = 240 #This is an average of between 230 to 250 seconds
        double_base_exhaust_velocity = double_base_isp * GRAVITATIONAL_ACCELERATION
        print(f"Your exhaust velocity is {double_base_exhaust_velocity}s")
        thrust_force = double_base_mfr * double_base_exhaust_velocity
        print(f"Your approximate thrust is {thrust_force}Newtons")
        mass_of_propellant = (float(input("What is the mass of your fuel/propellant in kilograms?\n")))
        final_rocket_mass = initial_rocket_mass - mass_of_propellant  
        change_in_mass = initial_rocket_mass / final_rocket_mass
        change_in_velocity = double_base_exhaust_velocity * math.log(change_in_mass) 
        print(f"Your change in velocity is {change_in_velocity}")
        rocket_altitude = float(input("What is the altitude of your rocket in meters ?\n"))
        #For this equation i asked the user to input their altitude but this can be done using an altimeter
        ground_velocity = float(input("What is your ground velocity in m/s ?\n"))
        wind_velocity = float(input("What is your wind velocity in m/s ?\n"))
        wind_direction = int(input("Is your rocket flying ;\n1.Against the wind(Opposite to the rocket)\n2.In the same direction"))
        if wind_direction == 1:
            air_relative_velocity = ground_velocity + wind_velocity
            print(f"Your Actual air relative velocity is {air_relative_velocity}m/s")
            centripetal_force = (initial_rocket_mass * (air_relative_velocity **2)) / (rocket_altitude + rocket_height + RADIUS_OF_EARTH)
            print(f"Your centripetal force is {centripetal_force}Newtons")
        elif wind_direction == 2:
            air_relative_velocity = ground_velocity - wind_velocity
            print(f"Your Actual air relative velocity is {air_relative_velocity}m/s")
            #The drag coefficient of your rocket can be deteermined before hand by running various tests like wind tunnel testing , CFD , flight testing and empirical estimation
            #It is usually between 0.1 to 1.5
            drag_coefficient = int(input("What is your drag coefficient ?\n"))
            #The formulae for drag is Drag = 0.5 * drag_coefficient * air_density * cross_sec_area * air_relative_-velocity^2
            
            inner_den = SEA_LEVEL_STD_TEMP + (TEMP_LAPSE_RATE * rocket_altitude) #This is the denominator inside the brackets of the air density formulae
            inner_full = SEA_LEVEL_STD_TEMP / inner_den #This is everything inside the bracket of the air density formulae
            outer_power = (GRAVITATIONAL_ACCELERATION * MOLAR_MASS_EARTH_AIR) / (GAS_CONSTANT * TEMP_LAPSE_RATE) #This is everything in the power form for the air density formulae
            inner_power = inner_full * outer_power #This is when everything in the bracket is multiplied by the the full power in the air density formulae
            air_density = SEA_LEVEL_AIR_DENSITY * inner_power
            print(f"The air density is {air_density}kg/m3")
            rocket_cross_sectional_area = float(input("What is the cross-sectional area of your rocket in meters-squared ?\n"))
            drag_force = 0.5 * drag_coefficient * air_density * rocket_cross_sectional_area * (air_relative_velocity ** 2)
            print(f"Your approximate drag is {drag_force}Newtons")
            centripetal_force = (initial_rocket_mass * (ground_velocity **2)) / ( rocket_height + rocket_altitude + RADIUS_OF_EARTH)
            print(f"{centripetal_force}Newtons")
            rocket_fins = int(input("Does your rocket have aerodynamic fins ?\n1.Yes\n2.No\n"))
            
            if rocket_fins == 1:
                lift_coefficient = int(input("What is your coefficient of lift"))
                wing_area = float(input("What is your reference/wing area in meters-squared ?\n"))
                lift_force = 0.5 * lift_coefficient * air_density * wing_area * (air_relative_velocity ** 2)
                print (f"Your approximate lift force if {lift_force}")
            elif rocket_fins == 2:
                lift_force = 0 #Your rocket does not generate lift without aerodynamic fins
                print(f"Your rocket {lift_force}Newtons")

    elif solid_fuel_type == 6:
        black_powder_burn_rate = 0.35  # This is an average of between 0.1 to 0.6 m/s
        black_powder_density = 1750  # This is in kg/m3
        black_powder_mfr = (
            black_powder_burn_rate * average_burning_surface_area * black_powder_density
        )
        print(f"Your black powder mass flow rate is {black_powder_mfr}kg/s")
        black_powder_isp = 90 #This is an average of between 80 to 100 second
        black_powder_exhaust_velocity = black_powder_isp * GRAVITATIONAL_ACCELERATION
        print(f"Your exhaust velocity is {black_powder_exhaust_velocity}s")
        thrust_force = black_powder_mfr * black_powder_exhaust_velocity
        print(f"Your thrust is {thrust_force}Newtons")
        mass_of_propellant = (float(input("What is the mass of your fuel/propellant in kilograms?\n")))
        final_rocket_mass = initial_rocket_mass - mass_of_propellant  
        change_in_mass = initial_rocket_mass / final_rocket_mass
        change_in_velocity = black_powder_exhaust_velocity * math.log(change_in_mass) 
        print(f"Your change in velocity is {change_in_velocity}")
        rocket_altitude = float(input("What is the altitude of your rocket in meters ?\n"))
        #For this equation i asked the user to input their altitude but this can be done using an altimeter
        ground_velocity = float(input("What is your ground velocity in m/s ?\n"))
        wind_velocity = float(input("What is your wind velocity in m/s ?\n"))
        wind_direction = int(input("Is your rocket flying ;\n1.Against the wind(Opposite to the rocket)\n2.In the same direction"))
        if wind_direction == 1:
            air_relative_velocity = ground_velocity + wind_velocity
            print(f"Your Actual air relative velocity is {air_relative_velocity}m/s")
            centripetal_force = (initial_rocket_mass * (air_relative_velocity **2)) / (rocket_height + rocket_altitude + RADIUS_OF_EARTH)
            print(f"Your centripetal force is {centripetal_force}Newtons")
        elif wind_direction == 2:
            air_relative_velocity = ground_velocity - wind_velocity
            print(f"Your Actual air relative velocity is {air_relative_velocity}m/s")
            #The drag coefficient of your rocket can be deteermined before hand by running various tests like wind tunnel testing , CFD , flight testing and empirical estimation
            #It is usually between 0.1 to 1.5
            drag_coefficient = int(input("What is your drag coefficient ?\n"))
            #The formulae for drag is Drag = 0.5 * drag_coefficient * air_density * cross_sec_area * air_relative_-velocity^2
            
            inner_den = SEA_LEVEL_STD_TEMP + (TEMP_LAPSE_RATE * rocket_altitude) #This is the denominator inside the brackets of the air density formulae
            inner_full = SEA_LEVEL_STD_TEMP / inner_den #This is everything inside the bracket of the air density formulae
            outer_power = (GRAVITATIONAL_ACCELERATION * MOLAR_MASS_EARTH_AIR) / (GAS_CONSTANT * TEMP_LAPSE_RATE) #This is everything in the power form for the air density formulae
            inner_power = inner_full * outer_power #This is when everything in the bracket is multiplied by the the full power in the air density formulae
            air_density = SEA_LEVEL_AIR_DENSITY * inner_power
            print(f"The air density is {air_density}kg/m3")
            rocket_cross_sectional_area = float(input("What is the cross-sectional area of your rocket in meters-squared ?\n"))
            drag_force = 0.5 * drag_coefficient * air_density * rocket_cross_sectional_area * (air_relative_velocity ** 2)
            print(f"Your approximate drag is {drag_force}Newtons")
            centripetal_force = (initial_rocket_mass * (ground_velocity **2)) / (rocket_height + rocket_altitude + RADIUS_OF_EARTH)
            print(f"{centripetal_force}Newtons")
            rocket_fins = int(input("Does your rocket have aerodynamic fins ?\n1.Yes\n2.No\n"))
            
            if rocket_fins == 1:
                lift_coefficient = int(input("What is your coefficient of lift"))
                wing_area = float(input("What is your reference/wing area in meters-squared ?\n"))
                lift_force = 0.5 * lift_coefficient * air_density * wing_area * (air_relative_velocity ** 2)
                print (f"Your approximate lift force if {lift_force}")
            elif rocket_fins == 2:
                lift_force = 0 #Your rocket does not generate lift without aerodynamic fins
                print(f"Your rocket {lift_force}Newtons")


elif rocket_fuel_type == 2:
    liquid_fuel_type = int(
        input(
            "What is your liquid fuel type from the list below:\n1.Liquid hydrogen(LH2)\n2.Liquid Oxygen\n3.Hydrogen-Peroxide\n4.Petroleum-fuel\n5.Liquid-Methane\n6.Liquid-BioLPG\n"
        )
    )
    if liquid_fuel_type == 1:
        liquid_hydrogen_burn_rate = 2.4  # This is an average of between 1.8 to 3.0 m/s
        liquid_hydrogen_density = 70.85  # This is in kg/m3
        liquid_hydrogen_mfr = (
            liquid_hydrogen_burn_rate
            * average_burning_surface_area
            * liquid_hydrogen_density
        )
        print(f"Your liquid hydrogen mass flow rate is {liquid_hydrogen_mfr}kg/s")
        liquid_hydrogen_isp = 455 #This is an average of between 450 and 460 seconds
        liquid_hydrogen_exhaust_velocity = liquid_hydrogen_isp * GRAVITATIONAL_ACCELERATION
        print(f"Your exhaust velocity is {liquid_hydrogen_exhaust_velocity}s")
        thrust_force = liquid_hydrogen_exhaust_velocity * liquid_hydrogen_mfr
        print(f"Your approximate thrust is {thrust_force}Newtons")
        mass_of_propellant = (float(input("What is the mass of your fuel/propellant in kilograms?\n")))
        final_rocket_mass = initial_rocket_mass - mass_of_propellant  
        change_in_mass = initial_rocket_mass / final_rocket_mass
        change_in_velocity = liquid_hydrogen_exhaust_velocity * math.log(change_in_mass) 
        print(f"Your change in velocity is {change_in_velocity}")
        rocket_altitude = float(input("What is the altitude of your rocket in meters ?\n"))
        #For this equation i asked the user to input their altitude but this can be done using an altimeter
        ground_velocity = float(input("What is your ground velocity in m/s ?\n"))
        wind_velocity = float(input("What is your wind velocity in m/s ?\n"))
        wind_direction = int(input("Is your rocket flying ;\n1.Against the wind(Opposite to the rocket)\n2.In the same direction"))
        if wind_direction == 1:
            air_relative_velocity = ground_velocity + wind_velocity
            print(f"Your Actual air relative velocity is {air_relative_velocity}m/s")
            centripetal_force = (initial_rocket_mass * (air_relative_velocity **2)) / (rocket_height + rocket_altitude + RADIUS_OF_EARTH)
            print(f"Your centripetal force is {centripetal_force}Newtons")
        elif wind_direction == 2:
            air_relative_velocity = ground_velocity - wind_velocity
            print(f"Your Actual air relative velocity is {air_relative_velocity}m/s")
            #The drag coefficient of your rocket can be deteermined before hand by running various tests like wind tunnel testing , CFD , flight testing and empirical estimation
            #It is usually between 0.1 to 1.5
            drag_coefficient = int(input("What is your drag coefficient ?\n"))
            #The formulae for drag is Drag = 0.5 * drag_coefficient * air_density * cross_sec_area * air_relative_-velocity^2
            
            inner_den = SEA_LEVEL_STD_TEMP + (TEMP_LAPSE_RATE * rocket_altitude) #This is the denominator inside the brackets of the air density formulae
            inner_full = SEA_LEVEL_STD_TEMP / inner_den #This is everything inside the bracket of the air density formulae
            outer_power = (GRAVITATIONAL_ACCELERATION * MOLAR_MASS_EARTH_AIR) / (GAS_CONSTANT * TEMP_LAPSE_RATE) #This is everything in the power form for the air density formulae
            inner_power = inner_full * outer_power #This is when everything in the bracket is multiplied by the the full power in the air density formulae
            air_density = SEA_LEVEL_AIR_DENSITY * inner_power
            print(f"The air density is {air_density}kg/m3")
            rocket_cross_sectional_area = float(input("What is the cross-sectional area of your rocket in meters-squared ?\n"))
            drag_force = 0.5 * drag_coefficient * air_density * rocket_cross_sectional_area * (air_relative_velocity ** 2)
            print(f"Your approximate drag is {drag_force}Newtons")
            centripetal_force = (initial_rocket_mass * (ground_velocity **2)) / (rocket_height + rocket_altitude + RADIUS_OF_EARTH)
            print(f"{centripetal_force}Newtons")
            rocket_fins = int(input("Does your rocket have aerodynamic fins ?\n1.Yes\n2.No\n"))
            
            if rocket_fins == 1:
                lift_coefficient = int(input("What is your coefficient of lift"))
                wing_area = float(input("What is your reference/wing area in meters-squared ?\n"))
                lift_force = 0.5 * lift_coefficient * air_density * wing_area * (air_relative_velocity ** 2)
                print (f"Your approximate lift force if {lift_force}")
            elif rocket_fins == 2:
                lift_force = 0 #Your rocket does not generate lift without aerodynamic fins
                print(f"Your rocket {lift_force}Newtons")

    elif liquid_fuel_type == 2:
        liquid_oxygen_burn_rate = 30  # Heavily depends on different factors like the type of fuel its mixed with , pressure and the combustion chamber design but it falls between the range of 10m/s to 50m/s
        liquid_oxygen_density = 1141  # This is in kg/m3
        liquid_oxygen_mfr = (
            liquid_oxygen_burn_rate
            * average_burning_surface_area
            * liquid_oxygen_density
        )
        print(f"Your liquid oxygen mass flow rate is {liquid_oxygen_mfr}kg/s")
        liquid_oxygen_isp = 288
        liquid_oxygen_exhaust_velocity = liquid_oxygen_isp * GRAVITATIONAL_ACCELERATION 
        print(f"Your exhaust velocity is {liquid_oxygen_exhaust_velocity}s")
        thrust_force = liquid_oxygen_mfr * liquid_oxygen_exhaust_velocity
        print(f"Your approximate thrust is {thrust_force}Newtons")
        mass_of_propellant = (float(input("What is the mass of your fuel/propellant in kilograms?\n")))
        final_rocket_mass = initial_rocket_mass - mass_of_propellant  
        change_in_mass = initial_rocket_mass / final_rocket_mass
        change_in_velocity = liquid_oxygen_exhaust_velocity * math.log(change_in_mass) 
        print(f"Your change in velocity is {change_in_velocity}")
        rocket_altitude = float(input("What is the altitude of your rocket in meters ?\n"))
        #For this equation i asked the user to input their altitude but this can be done using an altimeter
        ground_velocity = float(input("What is your ground velocity in m/s ?\n"))
        wind_velocity = float(input("What is your wind velocity in m/s ?\n"))
        wind_direction = int(input("Is your rocket flying ;\n1.Against the wind(Opposite to the rocket)\n2.In the same direction"))
        if wind_direction == 1:
            air_relative_velocity = ground_velocity + wind_velocity
            print(f"Your Actual air relative velocity is {air_relative_velocity}m/s")
            centripetal_force = (initial_rocket_mass * (air_relative_velocity **2)) / (rocket_height + rocket_altitude + RADIUS_OF_EARTH)
            print(f"Your centripetal force is {centripetal_force}Newtons")
        elif wind_direction == 2:
            air_relative_velocity = ground_velocity - wind_velocity
            print(f"Your Actual air relative velocity is {air_relative_velocity}m/s")
            #The drag coefficient of your rocket can be deteermined before hand by running various tests like wind tunnel testing , CFD , flight testing and empirical estimation
            #It is usually between 0.1 to 1.5
            drag_coefficient = int(input("What is your drag coefficient ?\n"))
            #The formulae for drag is Drag = 0.5 * drag_coefficient * air_density * cross_sec_area * air_relative_-velocity^2
            
            inner_den = SEA_LEVEL_STD_TEMP + (TEMP_LAPSE_RATE * rocket_altitude) #This is the denominator inside the brackets of the air density formulae
            inner_full = SEA_LEVEL_STD_TEMP / inner_den #This is everything inside the bracket of the air density formulae
            outer_power = (GRAVITATIONAL_ACCELERATION * MOLAR_MASS_EARTH_AIR) / (GAS_CONSTANT * TEMP_LAPSE_RATE) #This is everything in the power form for the air density formulae
            inner_power = inner_full * outer_power #This is when everything in the bracket is multiplied by the the full power in the air density formulae
            air_density = SEA_LEVEL_AIR_DENSITY * inner_power
            print(f"The air density is {air_density}kg/m3")
            rocket_cross_sectional_area = float(input("What is the cross-sectional area of your rocket in meters-squared ?\n"))
            drag_force = 0.5 * drag_coefficient * air_density * rocket_cross_sectional_area * (air_relative_velocity ** 2)
            print(f"Your approximate drag is {drag_force}Newtons")
            centripetal_force = (initial_rocket_mass * (ground_velocity **2)) / (rocket_height + rocket_altitude + RADIUS_OF_EARTH)
            print(f"Your centripetal force is {centripetal_force}Newtons")
            rocket_fins = int(input("Does your rocket have aerodynamic fins ?\n1.Yes\n2.No\n"))
            
            if rocket_fins == 1:
                lift_coefficient = int(input("What is your coefficient of lift"))
                wing_area = float(input("What is your reference/wing area in meters-squared ?\n"))
                lift_force = 0.5 * lift_coefficient * air_density * wing_area * (air_relative_velocity ** 2)
                print (f"Your approximate lift force if {lift_force}")
            elif rocket_fins == 2:
                lift_force = 0 #Your rocket does not generate lift without aerodynamic fins
                print(f"Your rocket {lift_force}Newtons")

    elif liquid_fuel_type == 3:
        hydrogen_peroxide_burn_rate = (
            0.3  # This is an average of between 0.2 to 0.4 m/s
        )
        hydrogen_peroxide_density = 1450  # This is in kg/m3
        hydrogen_peroxide_mfr = (
            hydrogen_peroxide_burn_rate
            * average_burning_surface_area
            * hydrogen_peroxide_density
        )
        print(f"Your Hydrogen-peroxide mass flow rate is {hydrogen_peroxide_mfr}kg/s")
        hydrogen_peroxide_isp = 150 #This is an average of between 140 to 160 seconds
        hydrogen_peroxide_exhaust_velocity = hydrogen_peroxide_isp * GRAVITATIONAL_ACCELERATION 
        print(f"Your exhaust velocity is {hydrogen_peroxide_exhaust_velocity}s")
        thrust_force = hydrogen_peroxide_exhaust_velocity * hydrogen_peroxide_mfr
        print(f"Your approximate thrust is {thrust_force}Newtons")
        mass_of_propellant = (float(input("What is the mass of your fuel/propellant in kilograms?\n")))
        final_rocket_mass = initial_rocket_mass - mass_of_propellant  
        change_in_mass = initial_rocket_mass / final_rocket_mass
        change_in_velocity = hydrogen_peroxide_exhaust_velocity * math.log(change_in_mass) 
        print(f"Your change in velocity is {change_in_velocity}")
        rocket_altitude = float(input("What is the altitude of your rocket in meters ?\n"))
        #For this equation i asked the user to input their altitude but this can be done using an altimeter
        ground_velocity = float(input("What is your ground velocity in m/s ?\n"))
        wind_velocity = float(input("What is your wind velocity in m/s ?\n"))
        wind_direction = int(input("Is your rocket flying ;\n1.Against the wind(Opposite to the rocket)\n2.In the same direction"))
        if wind_direction == 1:
            air_relative_velocity = ground_velocity + wind_velocity
            print(f"Your Actual air relative velocity is {air_relative_velocity}m/s")
            centripetal_force = (initial_rocket_mass * (air_relative_velocity **2)) / (rocket_height + rocket_altitude + RADIUS_OF_EARTH)
            print(f"Your centripetal force is {centripetal_force}Newtons")
        elif wind_direction == 2:
            air_relative_velocity = ground_velocity - wind_velocity
            print(f"Your Actual air relative velocity is {air_relative_velocity}m/s")
            #The drag coefficient of your rocket can be deteermined before hand by running various tests like wind tunnel testing , CFD , flight testing and empirical estimation
            #It is usually between 0.1 to 1.5
            drag_coefficient = int(input("What is your drag coefficient ?\n"))
            #The formulae for drag is Drag = 0.5 * drag_coefficient * air_density * cross_sec_area * air_relative_-velocity^2
            
            inner_den = SEA_LEVEL_STD_TEMP + (TEMP_LAPSE_RATE * rocket_altitude) #This is the denominator inside the brackets of the air density formulae
            inner_full = SEA_LEVEL_STD_TEMP / inner_den #This is everything inside the bracket of the air density formulae
            outer_power = (GRAVITATIONAL_ACCELERATION * MOLAR_MASS_EARTH_AIR) / (GAS_CONSTANT * TEMP_LAPSE_RATE) #This is everything in the power form for the air density formulae
            inner_power = inner_full * outer_power #This is when everything in the bracket is multiplied by the the full power in the air density formulae
            air_density = SEA_LEVEL_AIR_DENSITY * inner_power
            print(f"The air density is {air_density}kg/m3")
            rocket_cross_sectional_area = float(input("What is the cross-sectional area of your rocket in meters-squared ?\n"))
            drag_force = 0.5 * drag_coefficient * air_density * rocket_cross_sectional_area * (air_relative_velocity ** 2)
            print(f"Your approximate drag is {drag_force}Newtons")
            centripetal_force = (initial_rocket_mass * (ground_velocity **2)) / (rocket_altitude + rocket_height + RADIUS_OF_EARTH)
            print(f"Your centripetal force is {centripetal_force}Newtons")
            rocket_fins = int(input("Does your rocket have aerodynamic fins ?\n1.Yes\n2.No\n"))
            
            if rocket_fins == 1:
                lift_coefficient = int(input("What is your coefficient of lift"))
                wing_area = float(input("What is your reference/wing area in meters-squared ?\n"))
                lift_force = 0.5 * lift_coefficient * air_density * wing_area * (air_relative_velocity ** 2)
                print (f"Your approximate lift force if {lift_force}")
            elif rocket_fins == 2:
                lift_force = 0 #Your rocket does not generate lift without aerodynamic fins
                print(f"Your rocket {lift_force}Newtons")

    elif liquid_fuel_type == 4:
        petroleum_fuel_burn_rate = 0.7  # This is an average of between 0.4 to 1.0 m/s
        petroleum_fuel_density = 825  # This is an average of between 800 to 850 kg/m3
        petroleum_fuel_mfr = (
            petroleum_fuel_burn_rate
            * average_burning_surface_area
            * petroleum_fuel_density
        )
        print(f"Your petroleum fuel mass flow rate is {petroleum_fuel_mfr}kg/s")
        petroleum_fuel_isp = 275 #This is an average of between 260 to 290 seconds
        petroleum_fuel_exhaust_velocity = petroleum_fuel_isp * GRAVITATIONAL_ACCELERATION
        print(f"Your exhaust velocity is {petroleum_fuel_exhaust_velocity}s")
        thrust_force = petroleum_fuel_exhaust_velocity * petroleum_fuel_mfr
        print(f"Your approximate thrus is {thrust_force}Newtons")
        mass_of_propellant = (float(input("What is the mass of your fuel/propellant in kilograms?\n")))
        final_rocket_mass = initial_rocket_mass - mass_of_propellant  
        change_in_mass = initial_rocket_mass / final_rocket_mass
        change_in_velocity = petroleum_fuel_exhaust_velocity * math.log(change_in_mass) 
        print(f"Your change in velocity is {change_in_velocity}")
        rocket_altitude = float(input("What is the altitude of your rocket in meters ?\n"))
        #For this equation i asked the user to input their altitude but this can be done using an altimeter
        ground_velocity = float(input("What is your ground velocity in m/s ?\n"))
        wind_velocity = float(input("What is your wind velocity in m/s ?\n"))
        wind_direction = int(input("Is your rocket flying ;\n1.Against the wind(Opposite to the rocket)\n2.In the same direction"))
        if wind_direction == 1:
            air_relative_velocity = ground_velocity + wind_velocity
            print(f"Your Actual air relative velocity is {air_relative_velocity}m/s")
            centripetal_force = (initial_rocket_mass * (air_relative_velocity **2)) / (rocket_height + rocket_altitude + RADIUS_OF_EARTH)
            print(f"Your centripetal force is {centripetal_force}Newtons")
        elif wind_direction == 2:
            air_relative_velocity = ground_velocity - wind_velocity
            print(f"Your Actual air relative velocity is {air_relative_velocity}m/s")
            #The drag coefficient of your rocket can be deteermined before hand by running various tests like wind tunnel testing , CFD , flight testing and empirical estimation
            #It is usually between 0.1 to 1.5
            drag_coefficient = int(input("What is your drag coefficient ?\n"))
            #The formulae for drag is Drag = 0.5 * drag_coefficient * air_density * cross_sec_area * air_relative_-velocity^2
            
            inner_den = SEA_LEVEL_STD_TEMP + (TEMP_LAPSE_RATE * rocket_altitude) #This is the denominator inside the brackets of the air density formulae
            inner_full = SEA_LEVEL_STD_TEMP / inner_den #This is everything inside the bracket of the air density formulae
            outer_power = (GRAVITATIONAL_ACCELERATION * MOLAR_MASS_EARTH_AIR) / (GAS_CONSTANT * TEMP_LAPSE_RATE) #This is everything in the power form for the air density formulae
            inner_power = inner_full * outer_power #This is when everything in the bracket is multiplied by the the full power in the air density formulae
            air_density = SEA_LEVEL_AIR_DENSITY * inner_power
            print(f"The air density is {air_density}kg/m3")
            rocket_cross_sectional_area = float(input("What is the cross-sectional area of your rocket in meters-squared ?\n"))
            drag_force = 0.5 * drag_coefficient * air_density * rocket_cross_sectional_area * (air_relative_velocity ** 2)
            print(f"Your approximate drag is {drag_force}Newtons")
            centripetal_force = (initial_rocket_mass * (ground_velocity **2)) / (rocket_height + rocket_altitude + RADIUS_OF_EARTH)
            print(f"Your centripetal force is {centripetal_force}Newtons")
            rocket_fins = int(input("Does your rocket have aerodynamic fins ?\n1.Yes\n2.No\n"))
            
            if rocket_fins == 1:
                lift_coefficient = int(input("What is your coefficient of lift"))
                wing_area = float(input("What is your reference/wing area in meters-squared ?\n"))
                lift_force = 0.5 * lift_coefficient * air_density * wing_area * (air_relative_velocity ** 2)
                print (f"Your approximate lift force if {lift_force}")
            elif rocket_fins == 2:
                lift_force = 0 #Your rocket does not generate lift without aerodynamic fins
                print(f"Your rocket {lift_force}Newtons")

    elif liquid_fuel_type == 5:
        liquid_methane_burn_rate = 2.6  # This is an average of between 2.2 to 3.0m/s
        liquid_methane_density = 422  # This is in kg/m3
        liquid_methane_mfr = (
            liquid_methane_burn_rate
            * average_burning_surface_area
            * liquid_methane_density
        )
        print(f"Your liquid methane mass flow rate is {liquid_methane_mfr}kg/s")
        liquid_methane_isp = 360 #This is an average of between 350 to 370 seconds
        liquid_methane_exhaust_velocity =liquid_methane_isp * GRAVITATIONAL_ACCELERATION
        print(f"Your exhaust velocity is {liquid_methane_exhaust_velocity}s")
        thrust_force = liquid_methane_exhaust_velocity * liquid_methane_mfr
        print(f"Your approximate thrust is {thrust_force}Newtons")
        mass_of_propellant = (float(input("What is the mass of your fuel/propellant in kilograms?\n")))
        final_rocket_mass = initial_rocket_mass - mass_of_propellant  
        change_in_mass = initial_rocket_mass / final_rocket_mass
        change_in_velocity = liquid_methane_exhaust_velocity * math.log(change_in_mass) 
        print(f"Your change in velocity is {change_in_velocity}")
        rocket_altitude = float(input("What is the altitude of your rocket in meters ?\n"))
        #For this equation i asked the user to input their altitude but this can be done using an altimeter
        ground_velocity = float(input("What is your ground velocity in m/s ?\n"))
        wind_velocity = float(input("What is your wind velocity in m/s ?\n"))
        wind_direction = int(input("Is your rocket flying ;\n1.Against the wind(Opposite to the rocket)\n2.In the same direction"))
        if wind_direction == 1:
            air_relative_velocity = ground_velocity + wind_velocity
            print(f"Your Actual air relative velocity is {air_relative_velocity}m/s")
            centripetal_force = (initial_rocket_mass * (air_relative_velocity **2)) / (rocket_height + rocket_altitude + RADIUS_OF_EARTH)
            print(f"Your centripetal force is {centripetal_force}Newtons")
        elif wind_direction == 2:
            air_relative_velocity = ground_velocity - wind_velocity
            print(f"Your Actual air relative velocity is {air_relative_velocity}m/s")
            #The drag coefficient of your rocket can be deteermined before hand by running various tests like wind tunnel testing , CFD , flight testing and empirical estimation
            #It is usually between 0.1 to 1.5
            drag_coefficient = int(input("What is your drag coefficient ?\n"))
            #The formulae for drag is Drag = 0.5 * drag_coefficient * air_density * cross_sec_area * air_relative_-velocity^2
            
            inner_den = SEA_LEVEL_STD_TEMP + (TEMP_LAPSE_RATE * rocket_altitude) #This is the denominator inside the brackets of the air density formulae
            inner_full = SEA_LEVEL_STD_TEMP / inner_den #This is everything inside the bracket of the air density formulae
            outer_power = (GRAVITATIONAL_ACCELERATION * MOLAR_MASS_EARTH_AIR) / (GAS_CONSTANT * TEMP_LAPSE_RATE) #This is everything in the power form for the air density formulae
            inner_power = inner_full * outer_power #This is when everything in the bracket is multiplied by the the full power in the air density formulae
            air_density = SEA_LEVEL_AIR_DENSITY * inner_power
            print(f"The air density is {air_density}kg/m3")
            rocket_cross_sectional_area = float(input("What is the cross-sectional area of your rocket in meters-squared ?\n"))
            drag_force = 0.5 * drag_coefficient * air_density * rocket_cross_sectional_area * (air_relative_velocity ** 2)
            print(f"Your approximate drag is {drag_force}Newtons")
            centripetal_force = (initial_rocket_mass * (ground_velocity **2)) / (rocket_height + rocket_altitude + RADIUS_OF_EARTH)
            print(f"Your centripetal force is {centripetal_force}Newtons")
            rocket_fins = int(input("Does your rocket have aerodynamic fins ?\n1.Yes\n2.No\n"))
            
            if rocket_fins == 1:
                lift_coefficient = int(input("What is your coefficient of lift"))
                wing_area = float(input("What is your reference/wing area in meters-squared ?\n"))
                lift_force = 0.5 * lift_coefficient * air_density * wing_area * (air_relative_velocity ** 2)
                print (f"Your approximate lift force if {lift_force}")
            elif rocket_fins == 2:
                lift_force = 0 #Your rocket does not generate lift without aerodynamic fins
                print(f"Your rocket {lift_force}Newtons")

    elif liquid_fuel_type == 6:
        liquid_Bio_LPG_burn_rate = 0.6  # This is an average of between 0.4 to 0.8 m/s
        liquid_Bio_LPG_density = 560  # This is an average of between 540 to 580 kg/m3
        liquid_Bio_LPG_mfr = (
            liquid_Bio_LPG_burn_rate
            * average_burning_surface_area
            * liquid_Bio_LPG_density
        )
        print(f"Your liquid-BioLPG mass flow rate is {liquid_Bio_LPG_mfr}kg/s")
        liquid_Bio_LPG_isp = 300 #This is an average of between 290 to 310 seconds
        liquid_Bio_LPG_exhaust_velocity = liquid_Bio_LPG_isp * GRAVITATIONAL_ACCELERATION
        print(f"Your exhaust velocity is {liquid_Bio_LPG_exhaust_velocity}s")
        thrust_force = liquid_Bio_LPG_exhaust_velocity * liquid_Bio_LPG_mfr
        print(f"Your approximate thrust is {thrust_force}Newtons")
        mass_of_propellant = (float(input("What is the mass of your fuel/propellant in kilograms?\n")))
        final_rocket_mass = initial_rocket_mass - mass_of_propellant  
        change_in_mass = initial_rocket_mass / final_rocket_mass
        change_in_velocity = liquid_Bio_LPG_exhaust_velocity * math.log(change_in_mass) 
        print(f"Your change in velocity is {change_in_velocity}")
        rocket_altitude = float(input("What is the altitude of your rocket in meters ?\n"))
        #For this equation i asked the user to input their altitude but this can be done using an altimeter
        ground_velocity = float(input("What is your ground velocity in m/s ?\n"))
        wind_velocity = float(input("What is your wind velocity in m/s ?\n"))
        wind_direction = int(input("Is your rocket flying ;\n1.Against the wind(Opposite to the rocket)\n2.In the same direction"))
        if wind_direction == 1:
            air_relative_velocity = ground_velocity + wind_velocity
            print(f"Your Actual air relative velocity is {air_relative_velocity}m/s")
            centripetal_force = (initial_rocket_mass * (air_relative_velocity **2)) / (rocket_height + rocket_altitude + RADIUS_OF_EARTH)
            print(f"Your centripetal force is {centripetal_force}Newtons")
        elif wind_direction == 2:
            air_relative_velocity = ground_velocity - wind_velocity
            print(f"Your Actual air relative velocity is {air_relative_velocity}m/s")
            #The drag coefficient of your rocket can be deteermined before hand by running various tests like wind tunnel testing , CFD , flight testing and empirical estimation
            #It is usually between 0.1 to 1.5
            drag_coefficient = int(input("What is your drag coefficient ?\n"))
            #The formulae for drag is Drag = 0.5 * drag_coefficient * air_density * cross_sec_area * air_relative_-velocity^2
            
            inner_den = SEA_LEVEL_STD_TEMP + (TEMP_LAPSE_RATE * rocket_altitude) #This is the denominator inside the brackets of the air density formulae
            inner_full = SEA_LEVEL_STD_TEMP / inner_den #This is everything inside the bracket of the air density formulae
            outer_power = (GRAVITATIONAL_ACCELERATION * MOLAR_MASS_EARTH_AIR) / (GAS_CONSTANT * TEMP_LAPSE_RATE) #This is everything in the power form for the air density formulae
            inner_power = inner_full * outer_power #This is when everything in the bracket is multiplied by the the full power in the air density formulae
            air_density = SEA_LEVEL_AIR_DENSITY * inner_power
            print(f"The air density is {air_density}kg/m3")
            rocket_cross_sectional_area = float(input("What is the cross-sectional area of your rocket in meters-squared ?\n"))
            drag_force = 0.5 * drag_coefficient * air_density * rocket_cross_sectional_area * (air_relative_velocity ** 2)
            print(f"Your approximate drag is {drag_force}Newtons")
            centripetal_force = (initial_rocket_mass * (ground_velocity **2)) / (rocket_height + rocket_altitude + RADIUS_OF_EARTH)
            print(f"Your centripetal force is {centripetal_force}Newtons")
            rocket_fins = int(input("Does your rocket have aerodynamic fins ?\n1.Yes\n2.No\n"))
            
            if rocket_fins == 1:
                lift_coefficient = int(input("What is your coefficient of lift"))
                wing_area = float(input("What is your reference/wing area in meters-squared ?\n"))
                lift_force = 0.5 * lift_coefficient * air_density * wing_area * (air_relative_velocity ** 2)
                print (f"Your approximate lift force if {lift_force}")
            elif rocket_fins == 2:
                lift_force = 0 #Your rocket does not generate lift without aerodynamic fins
                print(f"Your rocket {lift_force}Newtons")


elif rocket_fuel_type == 3:
    space_engine_rocket_type = int(
        input(
            "What is your Space-Engine rocket type from the list below:\n1.Liquid Hydrogen\n2.Rocket-Grade-Kerosene(RP-1)\n3.Liquid Oxygen\n4.Methane\n5.Hydrazine\n"
        )
    )

    if space_engine_rocket_type == 1:
        liquid_hydrogen_burn_rate = 2.4  # This is an average of between 1.8 to 3.0 m/s
        liquid_hydrogen_density = 70.85  # This is in kg/m3
        liquid_hydrogen_mfr = (
            liquid_hydrogen_burn_rate
            * average_burning_surface_area
            * liquid_hydrogen_density
        )
        print(f"Your liquid hydrogen mass flow rate is{liquid_hydrogen_mfr}kg/s")
        liquid_hydrogen_isp = 455 #This is an average of between 450 and 460 seconds
        liquid_hydrogen_exhaust_velocity = liquid_hydrogen_isp * GRAVITATIONAL_ACCELERATION
        print(f"Your exhaust velocity is {liquid_hydrogen_exhaust_velocity}s")
        thrust_force = liquid_hydrogen_exhaust_velocity * liquid_hydrogen_mfr
        print(f"Your approximate thrust is {thrust_force}Newtons")
        mass_of_propellant = (float(input("What is the mass of your fuel/propellant in kilograms?\n")))
        final_rocket_mass = initial_rocket_mass - mass_of_propellant  
        change_in_mass = initial_rocket_mass / final_rocket_mass
        change_in_velocity = liquid_hydrogen_exhaust_velocity * math.log(change_in_mass) 
        print(f"Your change in velocity is {change_in_velocity}")
        rocket_altitude = float(input("What is the altitude of your rocket in meters ?\n"))
        #For this equation i asked the user to input their altitude but this can be done using an altimeter
        ground_velocity = float(input("What is your ground velocity in m/s ?\n"))
        wind_velocity = float(input("What is your wind velocity in m/s ?\n"))
        wind_direction = int(input("Is your rocket flying ;\n1.Against the wind(Opposite to the rocket)\n2.In the same direction"))
        if wind_direction == 1:
            air_relative_velocity = ground_velocity + wind_velocity
            print(f"Your Actual air relative velocity is {air_relative_velocity}m/s")
            centripetal_force = (initial_rocket_mass * (air_relative_velocity **2)) / (rocket_height + rocket_altitude + RADIUS_OF_EARTH)
            print(f"Your centripetal force is {centripetal_force}Newtons")
        elif wind_direction == 2:
            air_relative_velocity = ground_velocity - wind_velocity
            print(f"Your Actual air relative velocity is {air_relative_velocity}m/s")
            #The drag coefficient of your rocket can be deteermined before hand by running various tests like wind tunnel testing , CFD , flight testing and empirical estimation
            #It is usually between 0.1 to 1.5
            drag_coefficient = int(input("What is your drag coefficient ?\n"))
            #The formulae for drag is Drag = 0.5 * drag_coefficient * air_density * cross_sec_area * air_relative_-velocity^2
            
            inner_den = SEA_LEVEL_STD_TEMP + (TEMP_LAPSE_RATE * rocket_altitude) #This is the denominator inside the brackets of the air density formulae
            inner_full = SEA_LEVEL_STD_TEMP / inner_den #This is everything inside the bracket of the air density formulae
            outer_power = (GRAVITATIONAL_ACCELERATION * MOLAR_MASS_EARTH_AIR) / (GAS_CONSTANT * TEMP_LAPSE_RATE) #This is everything in the power form for the air density formulae
            inner_power = inner_full * outer_power #This is when everything in the bracket is multiplied by the the full power in the air density formulae
            air_density = SEA_LEVEL_AIR_DENSITY * inner_power
            print(f"The air density is {air_density}kg/m3")
            rocket_cross_sectional_area = float(input("What is the cross-sectional area of your rocket in meters-squared ?\n"))
            drag_force = 0.5 * drag_coefficient * air_density * rocket_cross_sectional_area * (air_relative_velocity ** 2)
            print(f"Your approximate drag is {drag_force}Newtons")
            centripetal_force = (initial_rocket_mass * (ground_velocity **2)) / (rocket_height + rocket_altitude + RADIUS_OF_EARTH)
            print(f"Your centripetal force is {centripetal_force}Newtons")
            rocket_fins = int(input("Does your rocket have aerodynamic fins ?\n1.Yes\n2.No\n"))
            
            if rocket_fins == 1:
                lift_coefficient = int(input("What is your coefficient of lift"))
                wing_area = float(input("What is your reference/wing area in meters-squared ?\n"))
                lift_force = 0.5 * lift_coefficient * air_density * wing_area * (air_relative_velocity ** 2)
                print (f"Your approximate lift force if {lift_force}")
            elif rocket_fins == 2:
                lift_force = 0 #Your rocket does not generate lift without aerodynamic fins
                print(f"Your rocket {lift_force}Newtons")

    elif space_engine_rocket_type == 2:
        rocket_grade_kerosene_burn_rate = (
            1.05  # This is an average of between 0.6 to 1.5 m/s
        )
        rocket_grade_kerosene_density = 810  # This is in kg/m3
        rocket_grade_kerosene_mfr = (
            rocket_grade_kerosene_burn_rate
            * average_burning_surface_area
            * rocket_grade_kerosene_density
        )
        print(
            f"Your Rocket-grade kerosene mass flow rate is {rocket_grade_kerosene_mfr}kg/s"
        )
        rocket_grade_kerosene_isp = 315 #This is an average of between 300 to 330 seconds
        rocket_grade_kerosene_exhaust_velocity = rocket_grade_kerosene_isp * GRAVITATIONAL_ACCELERATION
        print(f"Your exhaust velocity is {rocket_grade_kerosene_exhaust_velocity}s")
        thrust_force = rocket_grade_kerosene_exhaust_velocity * rocket_grade_kerosene_mfr
        print(f"Your approximate thrust is {thrust_force}Newtons")
        mass_of_propellant = (float(input("What is the mass of your fuel/propellant in kilograms?\n")))
        final_rocket_mass = initial_rocket_mass - mass_of_propellant  
        change_in_mass = initial_rocket_mass / final_rocket_mass
        change_in_velocity = rocket_grade_kerosene_exhaust_velocity * math.log(change_in_mass) 
        print(f"Your change in velocity is {change_in_velocity}")
        rocket_altitude = float(input("What is the altitude of your rocket in meters ?\n"))
        #For this equation i asked the user to input their altitude but this can be done using an altimeter
        ground_velocity = float(input("What is your ground velocity in m/s ?\n"))
        wind_velocity = float(input("What is your wind velocity in m/s ?\n"))
        wind_direction = int(input("Is your rocket flying ;\n1.Against the wind(Opposite to the rocket)\n2.In the same direction"))
        if wind_direction == 1:
            air_relative_velocity = ground_velocity + wind_velocity
            print(f"Your Actual air relative velocity is {air_relative_velocity}m/s")
            centripetal_force = (initial_rocket_mass * (air_relative_velocity **2)) / (rocket_height + rocket_altitude + RADIUS_OF_EARTH)
            print(f"Your centripetal force is {centripetal_force}Newtons")
        if wind_direction == 2:
            air_relative_velocity = ground_velocity - wind_velocity
            print(f"Your Actual air relative velocity is {air_relative_velocity}m/s")
            #The drag coefficient of your rocket can be deteermined before hand by running various tests like wind tunnel testing , CFD , flight testing and empirical estimation
            #It is usually between 0.1 to 1.5
            drag_coefficient = int(input("What is your drag coefficient ?\n"))
            #The formulae for drag is Drag = 0.5 * drag_coefficient * air_density * cross_sec_area * air_relative_-velocity^2
            
            inner_den = SEA_LEVEL_STD_TEMP + (TEMP_LAPSE_RATE * rocket_altitude) #This is the denominator inside the brackets of the air density formulae
            inner_full = SEA_LEVEL_STD_TEMP / inner_den #This is everything inside the bracket of the air density formulae
            outer_power = (GRAVITATIONAL_ACCELERATION * MOLAR_MASS_EARTH_AIR) / (GAS_CONSTANT * TEMP_LAPSE_RATE) #This is everything in the power form for the air density formulae
            inner_power = inner_full * outer_power #This is when everything in the bracket is multiplied by the the full power in the air density formulae
            air_density = SEA_LEVEL_AIR_DENSITY * inner_power
            print(f"The air density is {air_density}kg/m3")
            rocket_cross_sectional_area = float(input("What is the cross-sectional area of your rocket in meters-squared ?\n"))
            drag_force = 0.5 * drag_coefficient * air_density * rocket_cross_sectional_area * (air_relative_velocity ** 2)
            print(f"Your approximate drag is {drag_force}Newtons")
            centripetal_force = (initial_rocket_mass * (ground_velocity **2)) / (rocket_height + rocket_altitude + RADIUS_OF_EARTH)
            print(f"Your centripetal force is {centripetal_force}Newtons")
            rocket_fins = int(input("Does your rocket have aerodynamic fins ?\n1.Yes\n2.No\n"))
            
            if rocket_fins == 1:
                lift_coefficient = int(input("What is your coefficient of lift"))
                wing_area = float(input("What is your reference/wing area in meters-squared ?\n"))
                lift_force = 0.5 * lift_coefficient * air_density * wing_area * (air_relative_velocity ** 2)
                print (f"Your approximate lift force if {lift_force}")
            elif rocket_fins == 2:
                lift_force = 0 #Your rocket does not generate lift without aerodynamic fins
                print(f"Your rocket {lift_force}Newtons")


    elif space_engine_rocket_type == 3:
        liquid_oxygen_burn_rate = 30  # Heavily depends on different factors like the type of fuel its mixed with , pressure and the combustion chamber design but it falls between the range of 10m/s to 50m/s
        liquid_oxygen_density = 1141  # This is in kg/m3
        liquid_oxygen_mfr = (
            liquid_oxygen_burn_rate
            * average_burning_surface_area
            * liquid_oxygen_density
        )
        print(f"Your liquid oxygen mass flow rate is {liquid_oxygen_mfr}kg/s")
        liquid_oxygen_isp = 288
        liquid_oxygen_exhaust_velocity = liquid_oxygen_isp * GRAVITATIONAL_ACCELERATION
        print(f"Your exhaust velocity is {liquid_oxygen_exhaust_velocity}s")
        thrust_force = liquid_oxygen_exhaust_velocity * liquid_oxygen_mfr
        print(f"Your approximate thrust is {thrust_force}Newtons")
        mass_of_propellant = (float(input("What is the mass of your fuel/propellant in kilograms?\n")))
        final_rocket_mass = initial_rocket_mass - mass_of_propellant  
        change_in_mass = initial_rocket_mass / final_rocket_mass
        change_in_velocity = liquid_oxygen_exhaust_velocity * math.log(change_in_mass) 
        print(f"Your change in velocity is {change_in_velocity}")
        rocket_altitude = float(input("What is the altitude of your rocket in meters ?\n"))
        #For this equation i asked the user to input their altitude but this can be done using an altimeter
        ground_velocity = float(input("What is your ground velocity in m/s ?\n"))
        wind_velocity = float(input("What is your wind velocity in m/s ?\n"))
        wind_direction = int(input("Is your rocket flying ;\n1.Against the wind(Opposite to the rocket)\n2.In the same direction"))
        if wind_direction == 1:
            air_relative_velocity = ground_velocity + wind_velocity
            print(f"Your Actual air relative velocity is {air_relative_velocity}m/s")
            centripetal_force = (initial_rocket_mass * (air_relative_velocity **2)) / (rocket_height + rocket_altitude + RADIUS_OF_EARTH)
            print(f"Your centripetal force is {centripetal_force}Newtons")
        elif wind_direction == 2:
            air_relative_velocity = ground_velocity - wind_velocity
            print(f"Your Actual air relative velocity is {air_relative_velocity}m/s")
            #The drag coefficient of your rocket can be deteermined before hand by running various tests like wind tunnel testing , CFD , flight testing and empirical estimation
            #It is usually between 0.1 to 1.5
            drag_coefficient = int(input("What is your drag coefficient ?\n"))
            #The formulae for drag is Drag = 0.5 * drag_coefficient * air_density * cross_sec_area * air_relative_-velocity^2
            
            inner_den = SEA_LEVEL_STD_TEMP + (TEMP_LAPSE_RATE * rocket_altitude) #This is the denominator inside the brackets of the air density formulae
            inner_full = SEA_LEVEL_STD_TEMP / inner_den #This is everything inside the bracket of the air density formulae
            outer_power = (GRAVITATIONAL_ACCELERATION * MOLAR_MASS_EARTH_AIR) / (GAS_CONSTANT * TEMP_LAPSE_RATE) #This is everything in the power form for the air density formulae
            inner_power = inner_full * outer_power #This is when everything in the bracket is multiplied by the the full power in the air density formulae
            air_density = SEA_LEVEL_AIR_DENSITY * inner_power
            print(f"The air density is {air_density}kg/m3")
            rocket_cross_sectional_area = float(input("What is the cross-sectional area of your rocket in meters-squared ?\n"))
            drag_force = 0.5 * drag_coefficient * air_density * rocket_cross_sectional_area * (air_relative_velocity ** 2)
            print(f"Your approximate drag is {drag_force}Newtons")
            centripetal_force = (initial_rocket_mass * (ground_velocity **2)) / (rocket_height + rocket_altitude + RADIUS_OF_EARTH)
            print(f"Your centripetal force is {centripetal_force}Newtons")
            rocket_fins = int(input("Does your rocket have aerodynamic fins ?\n1.Yes\n2.No\n"))
            
            if rocket_fins == 1:
                lift_coefficient = int(input("What is your coefficient of lift"))
                wing_area = float(input("What is your reference/wing area in meters-squared ?\n"))
                lift_force = 0.5 * lift_coefficient * air_density * wing_area * (air_relative_velocity ** 2)
                print (f"Your approximate lift force if {lift_force}")
            elif rocket_fins == 2:
                lift_force = 0 #Your rocket does not generate lift without aerodynamic fins
                print(f"Your rocket {lift_force}Newtons")


    elif space_engine_rocket_type == 4:
        methane_burn_rate = 2.6  # This is an average of between 2.2 to 3.0 m/s
        methane_density = 422  # This is in kg/m3
        methane_mfr = methane_burn_rate * average_burning_surface_area * methane_density
        print(f"Your methane mass flow rate is {methane_mfr}kg/s")
        methane_isp = 360 #This is an average of between 350 to 370 seconds
        methane_exhaust_velocity = methane_isp * GRAVITATIONAL_ACCELERATION
        print(f"Your exhaust velocity is {methane_exhaust_velocity}s")
        thrust_force = methane_exhaust_velocity * methane_mfr
        print(f"Your approximate thrust is {thrust_force}Newtons")
        mass_of_propellant = (float(input("What is the mass of your fuel/propellant in kilograms?\n")))
        final_rocket_mass = initial_rocket_mass - mass_of_propellant  
        change_in_mass = initial_rocket_mass / final_rocket_mass
        change_in_velocity = methane_exhaust_velocity * math.log(change_in_mass) 
        print(f"Your change in velocity is {change_in_velocity}")
        rocket_altitude = float(input("What is the altitude of your rocket in meters ?\n"))
        #For this equation i asked the user to input their altitude but this can be done using an altimeter
        ground_velocity = float(input("What is your ground velocity in m/s ?\n"))
        wind_velocity = float(input("What is your wind velocity in m/s ?\n"))
        wind_direction = int(input("Is your rocket flying ;\n1.Against the wind(Opposite to the rocket)\n2.In the same direction"))
        if wind_direction == 1:
            air_relative_velocity = ground_velocity + wind_velocity
            print(f"Your Actual air relative velocity is {air_relative_velocity}m/s")
            centripetal_force = (initial_rocket_mass * (air_relative_velocity **2)) / (rocket_height + rocket_altitude + RADIUS_OF_EARTH)
            print(f"Your centripetal force is {centripetal_force}Newtons")
        elif wind_direction == 2:
            air_relative_velocity = ground_velocity - wind_velocity
            print(f"Your Actual air relative velocity is {air_relative_velocity}m/s")
            #The drag coefficient of your rocket can be deteermined before hand by running various tests like wind tunnel testing , CFD , flight testing and empirical estimation
            #It is usually between 0.1 to 1.5
            drag_coefficient = int(input("What is your drag coefficient ?\n"))
            #The formulae for drag is Drag = 0.5 * drag_coefficient * air_density * cross_sec_area * air_relative_-velocity^2
            
            inner_den = SEA_LEVEL_STD_TEMP + (TEMP_LAPSE_RATE * rocket_altitude) #This is the denominator inside the brackets of the air density formulae
            inner_full = SEA_LEVEL_STD_TEMP / inner_den #This is everything inside the bracket of the air density formulae
            outer_power = (GRAVITATIONAL_ACCELERATION * MOLAR_MASS_EARTH_AIR) / (GAS_CONSTANT * TEMP_LAPSE_RATE) #This is everything in the power form for the air density formulae
            inner_power = inner_full * outer_power #This is when everything in the bracket is multiplied by the the full power in the air density formulae
            air_density = SEA_LEVEL_AIR_DENSITY * inner_power
            print(f"The air density is {air_density}kg/m3")
            rocket_cross_sectional_area = float(input("What is the cross-sectional area of your rocket in meters-squared ?\n"))
            drag_force = 0.5 * drag_coefficient * air_density * rocket_cross_sectional_area * (air_relative_velocity ** 2)
            print(f"Your approximate drag is {drag_force}Newtons")
            centripetal_force = (initial_rocket_mass * (ground_velocity **2)) / (rocket_altitude + RADIUS_OF_EARTH)
            print(f"Your centripetal force is {centripetal_force}Newtons")
            rocket_fins = int(input("Does your rocket have aerodynamic fins ?\n1.Yes\n2.No\n"))
            
            if rocket_fins == 1:
                lift_coefficient = int(input("What is your coefficient of lift"))
                wing_area = float(input("What is your reference/wing area in meters-squared ?\n"))
                lift_force = 0.5 * lift_coefficient * air_density * wing_area * (air_relative_velocity ** 2)
                print (f"Your approximate lift force if {lift_force}")
            elif rocket_fins == 2:
                lift_force = 0 #Your rocket does not generate lift without aerodynamic fins
                print(f"Your rocket {lift_force}Newtons")



    elif space_engine_rocket_type == 5:
        hydrazine_burn_rate = 0.4  # This is an average of between 0.2 to 0.6m/s
        hydrazine_density = 1010  # This is in kg/m3
        hydrazine_mfr = (
            hydrazine_burn_rate * average_burning_surface_area * hydrazine_density
        )
        print(f"Your hydrazine mass flow rate is {hydrazine_mfr}kg/s")
        hydrazine_isp = 240 #This is an average of between 220 to 260 seconds
        hydrazine_exhaust_velocity = hydrazine_isp * GRAVITATIONAL_ACCELERATION
        print(f"Your exhaust velocity is {hydrazine_exhaust_velocity}s")
        thrust_force = hydrazine_exhaust_velocity * hydrazine_mfr
        print(f"Your approximate thrust is {thrust_force}Newtons")
        mass_of_propellant = (float(input("What is the mass of your fuel/propellant in kilograms?\n")))
        final_rocket_mass = initial_rocket_mass - mass_of_propellant  
        change_in_mass = initial_rocket_mass / final_rocket_mass
        change_in_velocity = hydrazine_exhaust_velocity * math.log (change_in_mass) 
        print(f"Your change in velocity is {change_in_velocity}")
        #For the drag equation i asked the user to input their ground and wind velocity but this can be found using inertial navigation systems and pitot static tubes respectively
        rocket_altitude = float(input("What is the altitude of your rocket in meters ?\n"))
        #For this equation i asked the user to input their altitude but this can be done using an altimeter
        ground_velocity = float(input("What is your ground velocity in m/s ?\n"))
        wind_velocity = float(input("What is your wind velocity in m/s ?\n"))
        wind_direction = int(input("Is your rocket flying ;\n1.Against the wind(Opposite to the rocket)\n2.In the same direction"))
        if wind_direction == 1:
            air_relative_velocity = ground_velocity + wind_velocity
            print(f"Your Actual air relative velocity is {air_relative_velocity}m/s")
            centripetal_force = (initial_rocket_mass * (air_relative_velocity **2)) / (rocket_height + rocket_altitude + RADIUS_OF_EARTH)
            print(f"Your centripetal force is {centripetal_force}Newtons")
        elif wind_direction == 2:
            air_relative_velocity = ground_velocity - wind_velocity
            print(f"Your Actual air relative velocity is {air_relative_velocity}m/s")
            #The drag coefficient of your rocket can be determined before hand by running various tests like wind tunnel testing , CFD , flight testing and empirical estimation
            #It is usually between 0.1 to 1.5
            drag_coefficient = int(input("What is your drag coefficient ?\n"))
            #The formulae for drag is Drag = 0.5 * drag_coefficient * air_density * cross_sec_area * air_relative_-velocity^2
            
            inner_den = SEA_LEVEL_STD_TEMP + (TEMP_LAPSE_RATE * rocket_altitude) #This is the denominator inside the brackets of the air density formulae
            inner_full = SEA_LEVEL_STD_TEMP / inner_den #This is everything inside the bracket of the air density formulae
            outer_power = (GRAVITATIONAL_ACCELERATION * MOLAR_MASS_EARTH_AIR) / (GAS_CONSTANT * TEMP_LAPSE_RATE) #This is everything in the power form for the air density formulae
            inner_power = inner_full * outer_power #This is when everything in the bracket is multiplied by the the full power in the air density formulae
            air_density = SEA_LEVEL_AIR_DENSITY * inner_power
            print(f"The air density is {air_density}kg/m3") 
            rocket_cross_sectional_area = float(input("What is the cross-sectional area of your rocket in meters-squared ?\n"))
            drag_force = 0.5 * drag_coefficient * air_density * rocket_cross_sectional_area * (air_relative_velocity ** 2)
            print(f"Your approximate drag is {drag_force}Newtons")
            centripetal_force = (initial_rocket_mass * (ground_velocity **2)) / (rocket_height + rocket_altitude + RADIUS_OF_EARTH)
            print(f"Your centripetal force is {centripetal_force}Newtons")
            rocket_fins = int(input("Does your rocket have aerodynamic fins ?\n1.Yes\n2.No\n"))
            
            if rocket_fins == 1:
                lift_coefficient = int(input("What is your coefficient of lift"))
                wing_area = float(input("What is your reference/wing area in meters-squared ?\n"))
                lift_force = 0.5 * lift_coefficient * air_density * wing_area * (air_relative_velocity ** 2)
                print (f"Your approximate lift force if {lift_force}")
            elif rocket_fins == 2:
                lift_force = 0 #Your rocket does not generate lift without aerodynamic fins
                print(f"Your rocket {lift_force}Newtons")




        
#print("---------------------------------------------------------------------------------------------------")

#Centripetal force/Orbital motion
#This is the force that prevents the I.C.B.M from following a degrading orbit
#The general formulae is Centripetal-force(Fc) = (Mass of rocket(kg) * Speed of object in orbit^2 (m/s)) / Radius of circular path(m)
#The radius of the circular path = Radius of the earth + altitude of the rocket
#orbital_velocity  = 
# centripetal_force = initial_rocket_mass    

#After all the forces have been calculated we need to find the NetForce which will be used to find the changing co-ordinates 
