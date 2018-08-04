rewards = [
    "Coke Sakto",
    "Boy Bawang",
    "15 pcs. Yucky Candy",
    "15 pcs. Pintura Candy",
    "15 PHP Load",
    "3 pcs. Dove Conditioner",
    "Cottonbuds",
    "One sheet of Biogesic",
    "100mL Pepper/Pintura"
]

reward_input = int(input("Enter reward: "))
name_input = input("Enter name: ").title()
gender_input = input("Enter gender: ")
final_reward = reward_input-1

print(f'Hi {name_input}! You have successfully redeemed reward #{reward_input} - {rewards[final_reward]}! Thank you for choosing Aling Nenas Sari Sari Store.')