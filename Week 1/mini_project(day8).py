# --- Mad Libs Generator (Conventional Style) ---

print("Welcome to the Mad Libs Generator!")
print("In this program, you will be asked to provide various words to create a fun story.")
print("Let's get started!\n")

# --- Step 1: Gather all inputs and store them in variables ---
adj1 = input('Enter an adjective: ')
noun1 = input('Enter a noun: ')
place = input('Enter a place: ')
verb1 = input('Enter a verb: ')
plural_noun = input('Enter a plural noun: ')
adj2 = input('Enter another adjective: ')
noun2 = input('Enter another noun: ')
verb_ing = input('Enter a verb ending in "ing": ')
noun3 = input('Enter a final noun: ')


# --- Step 2: Build the final story using the variables ---
story = f"""
Once upon a time, there was a {adj1} {noun1} who lived in a
{place}. Every day, it would {verb1} with its
{plural_noun}. One day, it met a {adj2} {noun2} who changed its
life forever. They went on an adventure to {verb_ing} the {noun3} and discovered a hidden treasure.
"""

# --- Step 3: Print the final result ---
print("\n--- Your Amazing Story ---")
print(story)
