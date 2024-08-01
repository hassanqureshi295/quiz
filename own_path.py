import time
name = input("Enter your name: ")
print(f"Welcome {name} to this adventure!")

print(f"You are {name}, a young explorer with a passion for adventure and technology. One sunny morning, you decide to venture into the Cyber Forest, a futuristic world filled with towering neon trees, holographic animals, and hidden tech treasures. Equipped with your high-tech backpack and a smart map, you step into the glowing woods, ready for whatever comes your way.")

time.sleep(2)

print("After walking for a few hours, you reach a fork in the road. The path splits into two, and you must decide which way to go.")
time.sleep(2)

op1 = int(input("""
Option 1: The right path, leading to a bustling cyber city rumored to be built on advanced technology.
Option 2: The left path, leading to a quiet village known for its friendly inhabitants and hidden tech secrets.
Which path will you choose?
(Type 1 for Option 1 and 2 for Option 2)
"""))

if op1 == 1:
    print("You take the right path, excited to explore the high-tech city. The trail is well-lit with neon signs, and you feel a sense of anticipation as you walk. After a few hours, the trees begin to thin, and you see the shimmering skyscrapers and busy streets ahead. The city is magnificent, with buildings that touch the sky and streets filled with people and robots.")
    time.sleep(2)
    print("As you wander through the city, you come across a futuristic library. Inside, the shelves are filled with digital books and glowing artifacts. The librarian, a friendly AI, notices your curiosity and approaches you.")
    op = int(input("""
                    Option 1: Ask the AI about the city's history and technological advancements.
                    Option 2: Browse the shelves and see if you can find a book about hidden tech treasures.
                    Which action will you take? 
                    (Type 1 for Option 1 and 2 for Option 2)"""))

    if op == 1:
        print("""The AI librarian smiles and invites you to sit. It tells you about the city's origins, built by brilliant engineers and scientists. It reveals that beneath the city lies a network of ancient tunnels filled with advanced tech and secret labs. Intrigued, you thank the AI and decide to explore these tunnels.

        Armed with a map from the AI, you find the entrance to the tunnels. Inside, the air is cool and filled with the faint glow of holographic runes. You navigate the labyrinth, discovering tech treasures and overcoming security systems. Your adventure in the city leads you to incredible discoveries and new allies who share your passion for technology.""")
    elif op == 2:
        print("""You browse the shelves, your fingers trailing over the glowing spines of digital books. One particular book catches your eye, titled "The Lost Tech of the Cyber Forest." Excited, you open the book and begin to read. It details a hidden treasure buried deep within the forest, guarded by robotic creatures and intricate puzzles.

        Determined to find this treasure, you gather supplies and set off back into the forest. With the knowledge from the book, you navigate through hidden paths and solve tech riddles, leading you to the treasure's hidden location. Your journey in the city equips you with the skills and knowledge to uncover the forest's greatest secrets.""")
    else:
        print("You died.")
        quit()
elif op1 == 2:
    print("""You take the left path, drawn by the promise of a quiet village and its hidden tech secrets. The path is narrow and winding, lined with neon flowers and the sound of electronic birdsong. After a few hours, you arrive at a quaint village with charming cottages and friendly villagers.

    As you explore the village, you hear stories about a mystical data spring hidden in the nearby hills. The spring is said to grant wishes to those who find it and prove their worth.""")    
    op2 = int(input("""Option 1: Ask the villagers for more information about the spring and how to find it.
    Option 2: Explore the village first and see if you can find clues about the spring's location.
    (Type 1 for Option 1 and 2 for Option 2) """))
    if op2 == 1:
        print("""You approach the village elder and ask about the mystical data spring. The elder smiles and tells you about the trials one must face to reach the spring. She offers to guide you to the start of the path and gives you advice on overcoming the challenges ahead.

        With her guidance, you embark on a quest to find the spring. The journey is filled with trials testing your courage, wisdom, and kindness. Each challenge brings you closer to the spring, and when you finally reach it, you make a wish that changes your life forever.

""")
    elif op2 == 2:
        print("""You decide to explore the village, hoping to find clues about the spring's location. As you wander, you meet various villagers who share their stories and knowledge. You come across an old, abandoned cottage on the outskirts of the village. Inside, you find a journal filled with entries about the spring and a detailed map showing its location.

        With the map in hand, you set off on your own to find the spring. The journey is challenging but rewarding, as you navigate through dense forests and rocky hills. When you finally reach the spring, you realize that the journey itself has taught you valuable lessons, and you make a wish that reflects your newfound wisdom.""")
    else:
        print("You died.")
        quit()

else:
    print("You died.")
    quit()
