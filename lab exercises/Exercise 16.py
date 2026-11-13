# Dice Simulator using Random Module
import random

rolls = int(input("How many times do you want to roll? "))

for i in range(rolls):
    result = random.randint(1, 6)
    print("Roll", i + 1, ":", result)

print("Dice simulation completed.")
