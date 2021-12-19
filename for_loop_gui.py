#Challenge: Display the image below where the 0 is going to be ' ', and the 1 is going to be '*'.
# This will reveal an image!

picture = [
  [0,0,0,1,0,0,0],
  [0,0,1,1,1,0,0],
  [0,1,1,1,1,1,0],
  [1,1,1,1,1,1,1],
  [0,0,0,1,0,0,0],
  [0,0,0,1,0,0,0]
]


for each_list in picture:
    for char in each_list:
        if char == 0:
            print(' ', end='')
        else:
            print('*', end='')
    print('')        