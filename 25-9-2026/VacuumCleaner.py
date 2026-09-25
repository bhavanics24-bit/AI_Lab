vaccum_location="a"
room_a_status="dirty"
room_b_status="dirty"

print(f"start: vacuum is in {vaccum_location}. a is {room_a_status}. b is {room_b_status}\n")

if vaccum_location=="a":
    if room_a_status=="dirty":
        print("room a is dirty,action suck")
        room_a_status="clean"

    print("room a is clean,go to room b-move right")
    vaccum_location="b"

if vaccum_location=="b":
    if room_b_status=="dirty":
        print("room b is dirty,action suck")
        room_b_status="clean"

    print("room b is clean,go to room a-move left")

print(f"room a is {room_a_status},room b is {room_b_status}")
    
 


    
