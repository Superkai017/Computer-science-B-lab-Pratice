import random
My_Tuple = (1,4,5,6,7,8,9,10 , 'A', 'B', 'C', 'D', 'E', 'F')
Pop = random.choices(My_Tuple ,k=4)
print(f'any ticket matching these 4 numbers or letter wins a 1 week trip to epstien island: {Pop}')