up = []
down = []
lift_status = "up"
current_floor = 0

while(True):
    floor_rn = int(input("Enter your current floor: "))
    floor_req = int(input("Enter the floor you wish to go: ")
    if floor_rn < floor_req:
        up.append(floor_req)
    elif floor_rn > floor_req:
        down.append(floor_req)
    else:
        print("Enter a valid floor number from 1 to 10!")
    q = input("Do you want to continue (y/n)? ")
    q = q.lower()
    if q == "y":
        continue
    else:
        False
