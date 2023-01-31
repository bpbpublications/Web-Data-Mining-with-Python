number = 32
running = True
 
while running:
    choice = int(input('Enter an integer : '))
    if choice == number:
        print("Congratulations, you guessed it.")   # If block begins
        print('but you do not win any prizes!')     # If block ends
        running = False           # while loop will stop as running becomes ‘False’
    elif choice < number:
        print('No, it is a little higher than that')    # End block begins
    else:
        print('No, it is a little lower than that')
else:
    print('The while loop is over.')
print('Done')
