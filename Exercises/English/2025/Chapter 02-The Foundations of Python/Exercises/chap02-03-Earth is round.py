pi = 3.14159265359
radius_in_mi = 3959
radius_in_km = 6371
earth_area_in_mi = 4 * pi * (radius_in_mi ** 2)
earth_area_in_km = 4 * pi * (radius_in_km ** 2)
print("The surface area of the Earth:",
     "\n\tin square miles is", earth_area_in_mi,
     "\n\tand in square kilometers is", earth_area_in_km)