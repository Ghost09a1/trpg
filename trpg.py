print("One good Morning. You find yourself sitting half asleep on your toilet.")
print("And just when you want to reach out to the TP.")
print("POOOF!")
print("SWUISH!")
print("BANG!!!")
print(
    "You materialize in a medieval toilet, surrounded by humorous graffiti on the walls."
)


def teleport_toilet():
    print("Options: ")
    print("(1) Wait")
    print("(2) Search for toilet paper")
    print("(3) Read the graffiti")
    choice = input("Enter your choice: ")

    if choice == "1":
        print(
            "You decide to wait. Time seems to stretch on as you contemplate the mysteries of existence."
        )
        print(
            "Why does Toast always land on the wrong Side? Are Polititians even human? When licking a Bumblebee, taste it like Bumble or Bee?"
        )
        print("After a while, you fart, breaking the silence. You're still waiting.")
        teleport_toilet()  # Loop 
    elif choice == "2":
        print("You search around desperately for toilet paper, but find none.")
        print(
            "However, you do find a pamphlet from something that looks like ill dressed Clowns somehow named 'Bündnis 90 die Grünen'."
        )
        print("Options: ")
        print("(1) Use the pamphlet as toilet paper")
        print("(2) Go back")
        sub_choice = input("Enter your choice: ")
        if sub_choice == "1":
            print("You use the pamphlet as makeshift toilet paper. ")
            print(
                "It's not comfortable, but it gets the job done and you somehow get the mustaches right where they belong."
            )
            leave_toilet()
        else:
            teleport_toilet()  # Go back to the toilet options
    elif choice == "3":
        print(
            "You read the graffiti on the walls. Some of the jokes are darkly humorous, others are just strange like:"
        )
        print("When I was young and had no sense.")
        print("I pissed on an electric fence")
        print("It shocked my dick,")
        print("it shocked my balls")
        print("And made me shit in my overalls")
        teleport_toilet()  # Go back to the toilet options
    else:
        teleport_toilet()  # invalid input


def leave_toilet():
    print(
        "You step out of the magical teleporting toilet and find yourself in front of what was once a bustling inn."
    )
    print(
        "Now, it stands as a weathered and crumbling ruin, its former glory faded by time. Ivy creeps up the walls, "
    )
    print(
        "and the roof is missing in places, allowing sunlight to filter through the gaps."
    )
    print("Options: ")
    print("(1) Explore the kitchen")
    print("(2) Check out the eating area")
    print("(3) Investigate the guestrooms")
    print("(4) Examine the fireplace")
    print("(5) Enter the storage room")
    choice = input("Enter your choice: ")

    if choice == "1":
        explore_kitchen()
    elif choice == "2":
        check_eating_area()
    elif choice == "3":
        investigate_guestrooms()
    elif choice == "4":
        examine_fireplace()
    elif choice == "5":
        enter_storage_room()
    else:
        leave_toilet()  # invalid input


def explore_kitchen():
    print("You cautiously enter the remains of the inn's kitchen.")
    print(
        "Rusty pots and pans hang from hooks on the walls, coated in a thick layer of dust."
    )
    print(
        "The stone hearth, once a source of warmth and nourishment, is now cold and lifeless."
    )
    print("Cobwebs drape the corners, and a sense of abandonment lingers in the air.")
    print("A lonely rat scurries away as you disturb its quiet refuge.")
    print("Options:")
    print("(1) Search the cabinets")
    print("(2) Search the stove")
    print("(3) Go back to explore more areas")

    choice = input("Enter your choice: ")

    if choice == "1":
        search_cabinets()
    elif choice == "2":
        search_stove()
    elif choice == "3":
        exploring_inn()
    else:
        explore_kitchen()  # invalid input


def search_cabinets():
    print(
        "You search the cabinets but find nothing but old pots and dusty kitchen equipment."
    )
    exploring_inn()


def search_stove():
    global has_flint_and_stone
    print("You examine the stove closely.")
    print(
        "Slightly rusted pans and pots catch your eye, but something else glimmers beneath them."
    )
    print("You discover a Flint and stone hidden among the cookware.")
    print("Options:")
    print("(1) Take the Flint and stone")
    print("(2) Leave it")

    choice = input("Enter your choice: ")

    if choice == "1":
        has_flint_and_stone = True
        print("You take the Flint and stone and put it in your pocket.")
        exploring_inn()
    elif choice == "2":
        print("You decide to leave the Flint and stone where you found it.")
        exploring_inn()
    else:
        search_stove()  # invalid input


def exploring_inn():
    print("Do you want to explore more?")
    print("Options:")
    print("(1) Explore the kitchen")
    print("(2) Check out the eating area")
    print("(3) Investigate the guestrooms")
    print("(4) Examine the fireplace")
    print("(5) Enter the storage room")
    choice = input("Enter your choice: ")

    if choice == "1":
        explore_kitchen()
    elif choice == "2":
        check_eating_area()
    elif choice == "3":
        investigate_guestrooms()
    elif choice == "4":
        examine_fireplace()
    elif choice == "5":
        enter_storage_room()
    else:
        exploring_inn()  # invalid input


def check_eating_area():
    has_wood = False


def check_eating_area():
    print(
        "Walking further into the inn, you enter what must have been the eating area."
    )
    print(
        "Splintered tables and broken chairs lie scattered across the floor, testament to the inn's bygone days of hospitality."
    )
    print(
        "Sunlight streams through shattered windows, illuminating the motes of dust dancing in the air."
    )
    print(
        "A thick layer of grime coats the surfaces, and the once-vibrant tapestries that adorned the walls now hang in tatters."
    )
    print("Options:")
    print("(1) Search the room")
    print("(2) Go back to explore more areas")

    choice = input("Enter your choice: ")

    if choice == "1":
        search_eating_area()
    elif choice == "2":
        exploring_inn()
    else:
        check_eating_area()  # invalid input


def search_eating_area():
    global has_wood
    print("You search the eating area, sifting through debris and shattered furniture.")
    print("Your efforts yield a piece of broken wood, perhaps useful for something.")
    print("Options:")
    print("(1) Take the broken wood")
    print("(2) Leave it")

    choice = input("Enter your choice: ")

    if choice == "1":
        has_wood = True
        print("You take the broken wood, considering its potential usefulness.")
        exploring_inn()
    elif choice == "2":
        print("You decide to leave the broken wood behind.")
        exploring_inn()
    else:
        search_eating_area()  # invalid input


def investigate_guestrooms():
    print("Venturing up a creaky staircase, you explore the guestrooms.")
    print("Each door you open reveals a scene frozen in time.")
    print("Tattered curtains sway in the breeze that wafts through broken windows.")
    print("Cobwebs drape across bed frames, creating delicate yet haunting patterns.")
    print("Forgotten belongings lie strewn about, forgotten by their owners long ago.")
    print(
        "A sense of melancholy hangs in the air, as if the rooms themselves remember the stories of those who stayed within their walls."
    )
    print("Options:")
    print("(1) Go back to explore more areas")

    choice = input("Enter your choice: ")

    if choice == "1":
        exploring_inn()
    else:
        investigate_guestrooms()  # invalid input


def examine_fireplace():
    has_blankets = False


lit_fireplace = False
has_honey = False
lock_one_solved = False
lock_two_solved = False


def examine_fireplace():
    global has_blankets, lit_fireplace, has_honey, lock_one_solved, lock_two_solved
    print(
        "You find yourself in what was once the heart of the inn—a grand fireplace that served as a gathering place for patrons seeking warmth and companionship."
    )
    print("Now, it's a hollow space filled with ashes and memories.")
    print(
        "Spiderwebs stretch across the mantle, adorned with glistening dewdrops that catch the faint sunlight."
    )
    print(
        "The remnants of charred logs lie at the base, a testament to the fires that once crackled here."
    )

    if lit_fireplace:
        print(
            "The fireplace crackles warmly, casting a comforting glow around the room."
        )

    if has_blankets and not lit_fireplace:
        print("Options:")
        print("(1) Light the fireplace")
        print("(2) Build a sleeping place with blankets")
        print("(3) Eat some honey")
        print("(4) Inspect the metal box")
        print("(5) Rest by the fireplace")
    else:
        print("Options:")
        print("(1) Inspect the metal box")
        print("(2) Rest by the fireplace")

    choice = input("Enter your choice: ")

    if choice == "1":
        inspect_metal_box()
    elif choice == "2":
        rest_by_fireplace()
    elif has_blankets and not lit_fireplace:
        if choice == "3":
            eat_honey()
        elif choice == "4":
            inspect_metal_box()
        elif choice == "5":
            rest_by_fireplace()
        elif choice == "1" and not lit_fireplace:
            light_fireplace()
        elif choice == "2" and not lit_fireplace:
            build_sleeping_place()
        else:
            examine_fireplace()  # invalid input
    else:
        examine_fireplace()  # invalid input


def light_fireplace():
    global lit_fireplace
    print(
        "You decide to light the fireplace, hoping to bring warmth and light to the room."
    )
    print(
        "Using the Flint and stone, you strike a spark onto the pile of wood, and soon, flames begin to dance and crackle."
    )
    lit_fireplace = True
    examine_fireplace()


def build_sleeping_place():
    global has_blankets
    print(
        "Using the broken wood you found earlier, you fashion a simple sleeping place near the fireplace."
    )
    print("You spread the blankets across it, creating a makeshift bed.")
    has_blankets = False  # Blankets are used
    examine_fireplace()


def eat_honey():
    global has_honey
    print(
        "You open the jar of honey and take a satisfying spoonful, savoring its sweetness."
    )
    has_honey = False  # Honey is consumed
    examine_fireplace()


def inspect_metal_box():
    global lock_one_solved, lock_two_solved
    print("Upon inspecting the metal box, you notice a numerical lock on it.")
    print("Two questions are engraved above the lock:")
    print("1. What is 8³?")
    answer_one = int(input("Enter your answer: "))
    if answer_one == 512:
        lock_one_solved = True
        print("You hear a click as the first lock is unlocked.")
    else:
        print("The lock remains in place.")

    print("2. When true means double, then false means one. 23.")
    answer_two = int(input("Enter your answer: "))
    if answer_two == 46:
        lock_two_solved = True
        print("You hear another click as the second lock is unlocked.")

    if lock_one_solved and lock_two_solved:
        print("Both locks are now unlocked. You hear a final click, and the box opens.")
        print("Inside, you find three shrunken heads.")
        print(
            "One appears fat and smells like McDonald's, another one looks like a beardy hobo, and the last one looks like a bald retarded man."
        )
        print(
            "They open their mouths, and instead of words, an endless stream of shit flows out."
        )
        print(
            "In shock, you try to move away, but it's too late. The room fills with the foul substance,"
        )
        print("and you find yourself overwhelmed, unable to escape.")
        print("The world goes dark as you succumb to the disgusting fate.")
        print("You have drowned in the shrunken heads' unpleasant offering.")
        exit()  # End the game
    else:
        examine_fireplace()


def rest_by_fireplace():
    if lit_fireplace:
        print("You decide to rest by the warmth of the fireplace.")
        print("The crackling flames and the comforting heat soothe your weary body.")
        print(
            "As you settle in, you have a moment of calm amidst the chaos of the inn."
        )
        print("Options:")
        print("(1) Inspect the metal box")
        print("(2) Go to sleep")
        choice = input("Enter your choice: ")

        if choice == "1":
            inspect_metal_box()
        elif choice == "2":
            sleep_by_fireplace()
        else:
            rest_by_fireplace()  # invalid input
    else:
        print("You decide to rest by the fireplace, hoping to find some warmth.")
        print(
            "However, without a fire, the cold creeps in, and the room becomes chillier."
        )
        print("As the hours pass, you find it increasingly difficult to stay awake.")
        print(
            "You have fallen asleep by the unlit fireplace and succumbed to the cold. Another victim of climate change."
        )
        exit()  # End the game


def sleep_by_fireplace():
    print(
        "You settle down on the makeshift bed by the fireplace, the warmth and flickering light lulling you into drowsiness."
    )
    print("Before you know it, your eyes grow heavy, and you slip into a deep slumber.")

    if lit_fireplace:
        print(
            "As you sleep with the fireplace crackling beside you, you feel safe and warm."
        )
        print(
            "Suddenly, you are jolted awake by a group of goblins brandishing crude weapons, busting through the windows and door."
        )
        print("They hiss and laugh as they surround you, their intentions clear.")
        print(
            "Panicked, you realize that the fire, combined with your presence, has produced CO2 and you earlier dump, methane."
        )
        print(
            "The goblins, dressed in shirts that say 'climate & thought police', begin stabing you to death. Screeching and screaming their pronouns"
        )
        exit()  # End the game
    else:
        print(
            "You have fallen asleep by the unlit fireplace and succumbed to the cold. Another victim of climate change."
        )
        exit()  # End the game


found_blankets = False
found_rusty_sword = False
found_honey = False


def enter_storage_room():
    print(
        "Your exploration leads you to a dusty storage room tucked away in a corner of the inn."
    )
    print("Crates and barrels, long forgotten, line the walls.")
    print("The air is musty, carrying the scent of aged wood and decay.")
    print(
        "Spindly spiderwebs drape the corners, their inhabitants watching as you step gingerly through the clutter."
    )
    print(
        "In the dim light, you glimpse the glint of forgotten treasures, locked away in the darkness."
    )
    print("Options:")
    print("(1) Search the crates")
    print("(2) Go back to explore more areas")

    choice = input("Enter your choice: ")

    if choice == "1":
        search_crates()
    elif choice == "2":
        exploring_inn()
    else:
        enter_storage_room()  # Handle invalid input


def search_crates():
    global found_blankets, found_rusty_sword, found_honey
    print(
        "You carefully search through the crates, moving aside dusty blankets and old wood."
    )

    if not found_blankets:
        print("You find a bundle of dusty blankets, perhaps useful for warmth.")
        print("Options:")
        print("(1) Take the blankets")
        print("(2) Leave them")

        choice = input("Enter your choice: ")

        if choice == "1":
            found_blankets = True
            print(
                "You take the blankets and imagine them providing comfort on cold nights."
            )
            enter_storage_room()
        elif choice == "2":
            print("You decide to leave the blankets where you found them.")
            enter_storage_room()
        else:
            search_crates()  # Handle invalid input

    elif not found_rusty_sword:
        print(
            "Among the clutter, you notice a rusty sword resting against the side of a crate."
        )
        print("Options:")
        print("(1) Take the rusty sword")
        print("(2) Leave it")

        choice = input("Enter your choice: ")

        if choice == "1":
            found_rusty_sword = True
            print("You take the rusty sword, its blade worn by time and neglect.")
            enter_storage_room()
        elif choice == "2":
            print("You decide to leave the rusty sword behind.")
            enter_storage_room()
        else:
            search_crates()  # Handle invalid input

    elif not found_honey:
        print("Hidden beneath some rags, you find a jar of honey.")
        print("Options:")
        print("(1) Take the jar of honey")
        print("(2) Leave it")

        choice = input("Enter your choice: ")

        if choice == "1":
            found_honey = True
            print("You take the jar of honey, its sweet scent filling the air.")
            enter_storage_room()
        elif choice == "2":
            print("You decide to leave the jar of honey behind.")
            enter_storage_room()
        else:
            search_crates()  # Handle invalid input

    else:
        print(
            "As you search the crates once again, you only find old rags and remnants."
        )
        print("It seems there's nothing left of value here.")
        exploring_inn()


# Start the game
teleport_toilet()
