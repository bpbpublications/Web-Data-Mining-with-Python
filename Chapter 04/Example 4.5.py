number = 32
 
for i in [1,2,3,4,5]:
    guess = int(input('Enter an integer : '))
    if guess == number:
        print("Congratulations, you guessed it.") 	# New block begins
        print('but you do not win any prizes!') 		# New block ends
        break
    elif guess < number:
        print('No, it is a little higher than that') 		# Another block
    else:
        print('No, it is a little lower than that')
else:
    print('The for loop is over.')
print('Done')
