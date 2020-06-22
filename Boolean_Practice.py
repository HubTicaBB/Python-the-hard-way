my_answer = False
right_answer = 3 == 3 and (not ("testing" == "testing" or "Python" == "Fun"))

print(f"\nMy answer:\t{my_answer}")
print(f"Right answer:\t{right_answer}")

if my_answer == right_answer:
    print("\n\tYou right!")
else:
    print("\n\tYou suck!")