f = open("..\\states.txt", "r")

us_state = ['Alabama','Alaska','Arizona','Arkansas','California','Colorado','Connecticut','Delaware','District of Columbia','Florida','Georgia','Hawaii','Idaho','Illinois','Indiana','Iowa','Kansas','Kentucky','Louisiana','Maine','Maryland','Massachusetts','Michigan','Minnesota','Mississippi','Missouri','Montana','Nebraska','Nevada','New Hampshire','New Jersey','New Mexico','New York','North Carolina','North Dakota','Ohio','Oklahoma','Oregon','Pennsylvania','Puerto Rico','Rhode Island','South Carolina','South Dakota','Tennessee','Texas','Utah','Vermont','Virgin Islands','Washington','Virginia','Wisconsin','Wyoming']

completed = []
missing = []
for state in us_state:
    f.seek(0)
    if str(state) in f.read():
        completed.append(state)
    else:
        missing.append(state)
f.close()

print("Complete - "+str(len(completed)))
print("--------------")
for x in completed:
    print(x)
print()
print("Missing - "+str(len(missing)))
print("--------------")
for x in missing:
    print(x)