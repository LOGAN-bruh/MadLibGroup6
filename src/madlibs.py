

# for i in range(2):
#     verb = input("Enter a verb: ")
#     verbs.write(verb + "\n")
#     noun = input("Enter a noun: ")
#     nouns.write(noun + "\n")
#     adjective = input("Enter an adjective: ")
#     adjectives.write(adjective + "\n")
# verbs.close()
# nouns.close()
# adjectives.close()

per_story = {
    1: {"verb": 5, "noun": 8, "adjective": 8},
    2: {"verb": 5, "noun": 6, "adjective": 5},
    3: {"verb": 5, "noun": 6, "adjective": 6},
    4: {"verb": 4, "noun": 4, "adjective": 6}
}

userchoice = int(input("what story (1-4) "))

requirements = per_story[userchoice]
verbs = open("verbs.txt", "w")
nouns = open("nouns.txt", "w")
adjectives = open("adjectives.txt", "w")

req = per_story[userchoice]

for i in range(req["verb"]):
    verb = input("enter verb: ")
    verbs.write(verb + "\n")

for i in range(req["noun"]):
    noun = input("enter noun: ")
    nouns.write(noun + "\n")

for i in range(req["adjective"]):
    adjective = input("enter adjective: ")
    adjectives.write(adjective + "\n")

verbs.close()
nouns.close()
adjectives.close()

with open("verbs.txt") as f:
    verbs = f.read().splitlines()

with open("nouns.txt") as f:
    nouns = f.read().splitlines()

with open("adjectives.txt") as f:
    adjectives = f.read().splitlines()

if userchoice == 1:
    story = f"""
Today at lunch, I ordered the {adjectives[0]} {nouns[0]} with a side of {adjectives[1]} {nouns[1]}.
When I tried to {verbs[0]} it, the {nouns[2]} started to {verbs[1]} across the table!
My {adjectives[2]} friend tried to {verbs[2]} it with a {nouns[3]}, but that only made things {adjectives[3]}.
Now there's {nouns[4]} all over my {adjectives[4]} {nouns[5]} and the lunch lady wants me to {verbs[3]} the entire {adjectives[5]} {nouns[6]}.
"""
    print(story)

elif userchoice == 2:
    story = f"""
I just created the most {adjectives[0]} {nouns[0]} ever!
All you have to do is {verbs[0]} the {adjectives[1]} {nouns[1]}
and it will automatically {verbs[1]} your {nouns[2]}.
My {adjectives[2]} teacher said I could {verbs[2]} it at the
{adjectives[3]} science fair.
I'm going to {verbs[3]} all day to make sure the {nouns[3]} works perfectly!
"""
    print(story)

elif userchoice == 3:
    story = f"""
Our family decided to {verbs[0]} to a {adjectives[0]} {nouns[0]} for vacation.
When we got there, the {nouns[1]} was completely {adjectives[1]}!
Dad tried to {verbs[1]} the situation by finding a {adjectives[2]} {nouns[2]},
but Mom wanted to just {verbs[2]} home.
My {adjectives[3]} sister wouldn't stop trying to {verbs[3]} every
{nouns[3]} she saw!
"""
    print(story)

elif userchoice == 4:
    story = f"""
For the {adjectives[0]} talent show, I decided to {verbs[0]}
while balancing a {nouns[0]} on my {adjectives[1]} {nouns[1]}.
Everyone thought I was {adjectives[2]}, but I practiced how to
{verbs[1]} for weeks!
When it was my turn, I walked onto the {adjectives[3]} stage
and began to {verbs[2]}.
The {adjectives[4]} audience couldn't believe their {nouns[2]}!
"""
    print(story)


# readfile = open("verbs.txt","r")
# verbs = readfile.read().splitlines()
# print( "Verbs:", verbs)
# readfile.close()
# readfile = open("nouns.txt","r")
# nouns = readfile.read().splitlines()
# print( "Nouns:", nouns)
# readfile.close()
# readfile = open("adjectives.txt","r")
# adjectives = readfile.read().splitlines()
# print( "Adjectives:", adjectives)
# readfile.close()


