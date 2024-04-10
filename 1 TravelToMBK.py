Money = int(input())

if Money >= 50 :
    print("Taxi"+"\nno walking")
elif Money >= 40 :
    print("BTS\nwalking")
elif Money >= 25 :
    print("Motorcycle\nno walking")
elif Money >= 8 :
    print("Song Thaeo\nwalking")
elif Money < 8 :
    print("stay home")