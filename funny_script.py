name = input("Please type your name > ")

adjectives = ['funny ', 'smart ', 'silly ', 'beautiful ', 'strange ', 'wonderful ']
verbs = [' is happy to ', ' hates to ', " can't wait to ", " loves to "]
activities = ["daydream about food ", "play computer games ", "eat ice cream alone ", "dress up as a clown "]

import random
my_adjective = random.choice(adjectives)
my_verb = random.choice(verbs)
my_activity = random.choice(activities)

print(my_adjective + name + my_verb + my_activity)

# Write one page essay about what we learned to day.
# Finish the quiz on enudalearn.com/class/4   - Python data types quiz