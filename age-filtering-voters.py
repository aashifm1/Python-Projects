voters = [
    ("Alice", 22),
    ("Bob", 16),
    ("Charlie", 18),
    ("Daisy", 15),
    ("Ethan", 30)
]

eligible_voters = []
not_eligible_voters = []

for name, age in voters:
    if age >= 18:
        eligible_voters.append(name)
    else:
        not_eligible_voters.append(name)

print("Eligible voters:", eligible_voters)
print("Not eligible voters:", not_eligible_voters)
