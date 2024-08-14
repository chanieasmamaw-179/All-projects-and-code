"""
1.6. Chapter Assessment (Set)
"""
#+++++++++++++++++++++++++++++++++++++++++++++++++++++ Q1 ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
"""
1. You want to count the number of unique visitors to your website. Given the following list of website visit ids,
create a collection with only unique visitor ids and assign it to the variable “unique_visitors”.
"""

website_visitors = [524, 335, 306, 28, 42, 181, 463, 45, 45, 524, 28, 42]

unique_visitors = set(website_visitors) # change this line

print(unique_visitors)

#+++++++++++++++++++++++++++++++++++++++++++++++++++++ Q2 ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

"""
You have created a dating website and want to match people based on their interests. Given an individual (“main_person”)
 and two options (“option_1” and “option_2”), use set operations to determine which person has the most shared interests.
"""
main_person = {"football", "wine", "reading", "travel", "swimming", "golf", "fashion", "long term dating"}
option_1 = {"movies", "math", "netflix", "short term dating", "fashion", "wine", "golf", }
option_2 = {"travel", "long term dating", "golf", "fashion"}

shared_interests_with_option_1 = main_person.intersection(option_1) or main_person.intersection(option_2)
print(shared_interests_with_option_1)

shared_interests_with_option_2 = main_person.intersection(option_2)  # change this line
print(shared_interests_with_option_2)

if len(shared_interests_with_option_1) > len(shared_interests_with_option_2):
    print("Option 1 is the best match")
elif len(shared_interests_with_option_1) < len(shared_interests_with_option_2):
    print("Option 2 is the best match")
else:
    print("Both options are equally good")
#+++++++++++++++++++++++++++++++++++++++++++++++++++++ Q3 ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

"""
5. When nominating a candidate for an election, a voter can write in any name. Only one nomination is needed for a
candidate to appear on the ballot.
Given the following lists of write-in nominations from different polls, create a set with no repeat nominations and
assign it to the variable “unique_nominations”.
"""
poll_a = ["Maxwell Sterling", "Maxwell Sterling", "Harriet Vane", "Leonora Quint", "Harriet Vane", "Maxwell Sterling"]
poll_b = ["Harriet Vane", "Vincent Thorne", "Harriet Vane", "Selina Morrow", "Harriet Vane", "Harriet Vane"]
poll_c = ["Selina Morrow", "Jasper Creed", "Selina Morrow", "Jasper Creed", "Selina Morrow", "Maxwell Sterling"]

# Convert lists to sets to remove duplicates within each poll
combine_set = poll_a + poll_b + poll_c

# Find the symmetric difference between the sets
unique_nominations = set(combine_set)

print(unique_nominations)










