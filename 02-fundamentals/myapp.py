from physic import physics
gravity_earth = physics.EARTH_GRAVITY
gravity_mars = 3.721
speed_water = 1500
speed_air = physics.SPEED_OF_SOUND
physics.rozdil_mezi_gravitacemi_earth_moon(gravity_earth, gravity_mars, jmeno1="země", jmeno2="marsu")
physics.rozdil_mezi_rychlost_light_sound(speed_water, speed_air, jmeno1="vody", jmeno2="vzduchu")

