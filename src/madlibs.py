import story

userContinue = True

# 1 is original, 2-4 are the new 15-prompt stories
per_story = {
    1: {"verb": 4, "noun": 7, "adjective": 6},
    2: {"verb": 5, "noun": 5, "adjective": 5},
    3: {"verb": 5, "noun": 5, "adjective": 5},
    4: {"verb": 5, "noun": 5, "adjective": 5}
}

while userContinue:
    userchoice = input("\nPick a story (1-4) or 'q' to quit: ")
    
    if userchoice.lower() == 'q':
        break
        
    if not userchoice.isdigit() or int(userchoice) not in per_story:
        print("Invalid choice. Pick 1, 2, 3, or 4.")
        continue

    choice_int = int(userchoice)
    req = per_story[choice_int]

    print(f"\n--- Give me {req['verb']} verbs, {req['noun']} nouns, and {req['adjective']} adjectives ---")
    
    # Save inputs to files
    with open("verbs.txt", "w") as v_file:
        for i in range(req["verb"]):
            v_file.write(input(f"Enter verb {i+1}: ") + "\n")

    with open("nouns.txt", "w") as n_file:
        for i in range(req["noun"]):
            n_file.write(input(f"Enter noun {i+1}: ") + "\n")

    with open("adjectives.txt", "w") as a_file:
        for i in range(req["adjective"]):
            a_file.write(input(f"Enter adjective {i+1}: ") + "\n")

    # Read files back into lists
    with open("verbs.txt") as f: verbs = f.read().splitlines()
    with open("nouns.txt") as f: nouns = f.read().splitlines()
    with open("adjectives.txt") as f: adjectives = f.read().splitlines()

    # Play the chosen story
    print("\n--- YOUR MAD LIB ---")
    if choice_int == 1:
        print(story.get_story1(adjectives, nouns, verbs))
    elif choice_int == 2:
        print(story.get_story2(adjectives, nouns, verbs))
    elif choice_int == 3:
        print(story.get_story3(adjectives, nouns, verbs))
    elif choice_int == 4:
        print(story.get_story4(adjectives, nouns, verbs))
