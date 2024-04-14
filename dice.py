# import library
import random

# ● ┌ ─ ┐ │ └ ┘

dice_throw = {

1: ("┌─────────┐",
    "│         │",
    "│    ●    │",
    "│         │",
    "└─────────┘"),

2: ("┌─────────┐",
    "│  ●      │",
    "│         │",
    "│      ●  │",
    "└─────────┘"),

3: ("┌─────────┐",
    "│  ●      │",
    "│    ●    │",
    "│      ●  │",
    "└─────────┘"),

4: ("┌─────────┐",
    "│  ●   ●  │",
    "│         │",
    "│  ●   ●  │",
    "└─────────┘"),

5: ("┌─────────┐",
    "│  ●   ●  │",
    "│    ●    │",
    "│  ●   ●  │",
    "└─────────┘"),

6: ("┌─────────┐",
    "│  ●   ●  │",
    "│  ●   ●  │",
    "│  ●   ●  │",
    "└─────────┘")
}

dice = []
total = 0
num_of_dice = int(input("How many dice?: "))

for die in range (num_of_dice):
    dice.append(random.randint(1,6))
    
# dice print vertical
# for die in range(num_of_dice):
#     for line in dice_throw.get(dice[die]):
#         print(line)

for line in range(5):
    for die in dice:
        print(dice_throw.get(die)[line], end="")
    print()
 

for die in dice:
    total += die
print(f"Total: {total}")
