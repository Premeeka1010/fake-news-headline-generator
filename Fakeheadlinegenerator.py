# Import random module
import random 

# Create subjects
subjects = [
    "Prime Minister KP Oli",
    "Aarju Rana",
    "A group of monkeys",
    "A great Chaiwala",
]

# Create actions
actions = [
    "dances",
    "farts",
    "celebrates",
    "starts a train"
]

# Create places or things
places_or_things = [
    "inside a parliament",
    "in Janakpur",
    "at Swayambhunath",
    "on a plate of pakauda"
]

# Start the headline generation loop
while True: 
    subject = random.choice(subjects)
    action = random.choice(actions)
    place_or_thing = random.choice(places_or_things)

    headline = f"BREAKING NEWS: {subject} {action} {place_or_thing}!"
    print("\n" + headline)

    user_input = input("\nDo you want to generate another headline? (yes/no): ").strip().lower()
    if user_input != "yes":
        print("\nThanks for using the Headline Generator. Have a fun day!")
        break
