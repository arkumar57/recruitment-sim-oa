import numpy as np


def final_disk_speed(height: float, length: float, incline: float, mass: float, friction: float, radius: float) -> float:
    """
    Returns the speed of a uniform disk after it reaches the bottom of an inclined slope.

    :param height: the height of the incline (meters)
    :param length: the length of the slope (meters)
    :param incline: the angle of the slope (degrees)
    :param mass: the mass of the ball (kilograms)
    :param friction: kinetic friction coefficient of the slope's surface (0.0 - 1.0)
    :param radius: the radius of the disk (meters)
    :return: the speed of the disk (m/s)
    """
    #g = acceleration due to gravity
    g = 9.81
    #Using work energy principle
    initial_kinetic_energy = 0
    intial_potential_energy = mass*g*height
    final_potential_energy = 0
    work_done = -(friction*mass*g*np.cos(incline)*length)

    #final kinetic energy = Transational + Rotational = 3/4 * mass * (final_velocity)^2
    
    if mass == 0:
        return 0.0;
    if ((4*(intial_potential_energy + work_done))/(3 * mass)) >= 0.0:
        return np.sqrt(((4*(intial_potential_energy + work_done))/3 * mass));
    else:
        return 0.0;

#Test Case 1
v1 = final_disk_speed(height=2.0, length=3.0, incline=np.pi/6, mass=0.0, friction=0.1, radius=0.5)
print(str(v1) + " m/s")


#Test Case 1
v2 = final_disk_speed(height=2.0, length=3.0, incline=np.pi/6, mass=5.0, friction=0.1, radius=0.5)
print(str(v2) + " m/s")
