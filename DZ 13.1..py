class FootballPlayer():
    def __init__(self, first_name, last_name, height_cm, weight_kg, goals, y_cards, r_cards):
        self.first_name = first_name
        self.last_name = last_name
        self.height_cm = height_cm
        self.weight_kg = weight_kg
        self.goals = goals
        self.y_cards = y_cards
        self.r_cards = r_cards

print("Enter some football player's data!")
f_name = input("Enter player's first name: ")
l_name = input("Enter player's last name: ")
height = input("Enter player's height: ")
weight = input("Enter player's weight: ")
goals = input("Enter the number of player's goals: ")
y_cards = input("Enter the number of player's yellow cards: ")
r_cards = input("Enter the number of player's red cards: ")

new_player = FootballPlayer(first_name=f_name, last_name=l_name, height_cm=float(height), weight_kg=float(weight),
                            goals=int(goals), y_cards=int(y_cards), r_cards=int(r_cards))

with open("nogometas.txt", "w") as football_file:
    football_file.write(str(new_player.__dict__))
print("Player successfully entered!")
print("Player's data: {0}".format(new_player.__dict__))