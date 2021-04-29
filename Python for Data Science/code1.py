# 1 meter = 117.64 barleycorns
# 1 furlong = 220 yards
# 1 fortnight = 2 weeks
# 1 MACH = speed of sound
# The speed of sound = 1130
#     feet per second
# 1 PSL is a speed compared to the
#     speed of light.
# The speed of light is 299,792,458
#     meters per second
# 1 Foot = .3048 Meters

def convert():
   mph = int(input("Please input a speed in Miles Per Hour : "))

   #1 meter = 117.64 barleycorns
   #1 foot = .3048 meters
   #1 mile = 5,280 feet
   #5,280 feet * .3048 = meters in a mile
   #5,280 feet * .3048 * 117.64 = barleycorns in a mile

   #1 day = 24 hours
   #hours * 24 = hours in terms of days
   
   #barleyCornsPerDay = (mph * 5280 * .3048 * 117.64 / 24)

   #1 furlong = 220 yards
   #1 fortnight = 2 weeks
   #1 mile = 5,280 feet
   #5,280 feet / 3 = yards in a mile
   #5,280 feet / 3 / 220 = furlongs in a mile

   #1 day = 24 hours
   #2 week = 14 days
   #hours * 24 = hours in terms of days
   #hours * 24 * 14 = hours in terms of fortnights

   #furlongsPerFortnight = (mph * 5280 / 3 / 220 / 24 / 14)

   #1 MACH = speed of sound
   #The speed of sound = 1130 feet per second
   #1 mile * 5,280 feet = miles in terms of feet
   #60 minutes in 1 hour
   #60 seconds in 1 minute
   #1 hour * 60 = 1 hour in terms of minutes
   #1 hour * 60 * 60 = 1 hour in terms of seconds

   SoS = (mph * 5280 / 60 / 60)
   machNumber = SoS / 1130

   #5,280 feet * .3048 = meters in a mile
   #60 minutes in 1 hour
   #60 seconds in 1 minute
   #1 hour * 60 = 1 hour in terms of minutes
   #1 hour * 60 * 60 = 1 hour in terms of seconds
   # The speed of light is 299,792,458 meters per second

   metersPerSecond = (mph * 5280 * .3048 / 60 / 60)
   percentSoL = metersPerSecond/299792458*100

    # 2nd logic
   kph = 1.609344*mph
   barleycornperday = kph*1000*117.647/24
   furlongsperfortnight = kph*1093.61*24*14/220
   machnumber = kph*0.911344/1130
   psl = kph*1000/60/60/299792458

   print()
   print("Miles Per Hour is:         " + str(mph))
   print("KiloMiles Per Hour is:     " + str(kph))
   print("Barleycorns Per Day:       " + str(barleycornperday))
   print("Furlongs Per Fortnight:    " + str(furlongsperfortnight))
   print("Mach Number of:            " + str(machnumber))
   print("Percent Speed of Light of: " + str(psl))

#function call (main method)
convert()