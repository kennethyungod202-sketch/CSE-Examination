def gps_tracker():
    # Starting position
    x, y = 0, 0
    print("Starting at position (0, 0)")
    print("Enter N/S/E/W to move or STOP to end.")

    while True:
        move = input("Enter direction: ").strip().lower()

        if move in ["stop"]:
            break
        elif move in ["n", "north"]:
            y += 1
        elif move in ["s", "south"]:
            y -= 1
        elif move in ["e", "east"]:
            x += 1
        elif move in ["w", "west"]:
            x -= 1
        else:
            print("Invalid input! Use N, S, E, W or STOP.")
            continue

        print(f"Current position: ({x}, {y})")

    # End session
    print(f"\nFinal position: ({x}, {y})")
    if (x, y) == (0, 0):
        print("You returned to the origin (0, 0).")
    else:
        print("You did not return to the origin.")

# Run the program
gps_tracker()
