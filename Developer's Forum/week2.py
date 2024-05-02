triple_quote = """
My name
is Nick,
How are
you?
"""

single_letter = triple_quote[4]
sub_string = triple_quote[2:7]

print(f"Single Letter: {single_letter}")
print(f"Sub String: {sub_string}")

string_list = triple_quote.split()
print(f"String List: {string_list}")







# Create a dictionary mapping Greek letters to their names
greek_letters = {
    'α': 'Alpha',
    'β': 'Beta',
    'γ': 'Gamma',
    'δ': 'Delta'
}

# Display the name for β
print(f"The name for β is: {greek_letters['β']}")

# Display all key/value pairs in the dictionary
for letter, name in greek_letters.items():
    print(f"{letter}: {name}")