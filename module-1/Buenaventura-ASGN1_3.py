# Roxanne Buenaventura
# CSD325-300
# Assignment 1_3
# This program will run a reverse countdown using the "100 bottles of beer on the wall" song beginning from the intital number of beers entered by the user.

# Retrieve the number of bottles from the user
bottles = int(input("Enter number of bottles: "))

# Countdown function
def count_down(bottles):
    if bottles > 1:
        print(f"\n{bottles} bottles of beer on the wall, {bottles} bottles of beer.")
        print(f"Take one down and pass it around, {bottles - 1} bottle(s) of beer on the wall.")
        return bottles - 1
    elif bottles == 1:
        print(f"\n{bottles} bottle of beer on the wall, {bottles} bottle of beer.")
        print(f"Take one and pass it around, {bottles - 1} bottle(s) of beer on the wall.")
        print("\nTime to buy more bottles of beer.")
        return bottles - 1
    
# Call the function in a loop until there are no more bottles left
while bottles > 0:
    bottles = count_down(bottles)



