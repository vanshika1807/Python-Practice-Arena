'''
Suggest an activity based on the weather 
Sunny - Go for a walk
Rainy - Read a book
Snowy - Buid a Snow man
'''

weather = input("enter a weather: ").lower()
if weather =='sunny':
    activity = "Go for a walk"

elif weather == 'rainy':
    activity = "Read a book"

elif weather == "snowy":
    activity = "Build a Snowman"
else:
   activity = "wrong i/p"

print(activity)