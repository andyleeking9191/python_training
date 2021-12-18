# challenge: create a simple program that ckecks
#  if magicain and expert and output: you are a master magician.
#  if magicain but not expert and output: At least you are getting there. 
#  if not a magician and output: You are not a magician, you need magic powers.

is_magician = True
is_expert = True

if  is_magician == False:
    print("You are not a magician, you need magic powers")

elif is_magician == True and is_expert == False:
    print("At least you are getting there")
    
else:
    print("You are and master magician")
    