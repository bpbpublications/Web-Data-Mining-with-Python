number = 32
choice = int(input('Enter an integer : '))
if choice == number:
    print("Congratulations, you guessed it.") 	# If block begins
    print('but you do not win any prizes!') 	# If block ends here
elif choice < number:
    print('No, it is a little higher than that') 	# Else block
    # You can have few more statements in this block 
else:
    print('No, it is a little lower than that')
    # you must have guess > number to reach here
print('Done')
