import math

def paint_calc(height, width, cover):
    area = height * width
    num_of_cans = area / cover
    round_up_cans = math.ceil(num_of_cans)
    print(f"You'll need {round_up_cans} cans of paint.")


test_h = int(input("Enter height of wall: "))
test_w = int(input("Enter width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)

    
