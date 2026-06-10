# Example 03: Earth is round

THE_EARTH_IS_FLAT = False
THE_EARTH_IS_DONUT_SHAPED = False

if THE_EARTH_IS_FLAT:
    print("Savdhaan rahein, edge se girne se bachein!")
elif THE_EARTH_IS_DONUT_SHAPED:
    print("Hmm, interesting theory.")
    print("Iski calculation kaise karein, yeh abhi clear nahi hai.")
else:
    PI = 3.14159265359
    RADIUS_IN_MI = 3959
    RADIUS_IN_KM = 6371

    earth_area_in_mi = 4 * PI * (RADIUS_IN_MI ** 2)
    earth_area_in_km = 4 * PI * (RADIUS_IN_KM ** 2)

    print("Earth ka surface area:")
    print(f"Square miles mein: {earth_area_in_mi}")
    print(f"Square kilometers mein: {earth_area_in_km}")
