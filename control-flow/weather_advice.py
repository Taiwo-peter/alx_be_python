weather = input("What is the weather like today? (sunny/rainy/cold): ").strip().lower()
if weather == "sunny":
    print("Wear a t-shirt and sunglasses.")
elif weather == "rainy":
    print("Don't forget your umbrella and a raincoat.")
elif weather == "cold":
    print("Make sure to wear a warm coat and a scarf.")
elif weather == "cloudy":
    print("A light jacket should be fine.")
else:
    print("Sorry, I don't have recommendations for this weather.")