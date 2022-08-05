# an example of a WHILE loop
# this will loop through code until a certain condition is met

# we will roll two dice
# we will keep rolling until we get snake eyes (1 and 1)
myDice1 = None
myDice2 = None
# keep track of the number of times we run the code
myAttemptCount = 0

# the code below will keep running as long as the condition is true
# we have to make sure that the condition will be false at some point
# or the code will run forever!
print('Condition:', myDice1 != 1 or myDice1 != 1)

# start our while loop
# the syntax is "while condition:"
while myDice1 != 1 or myDice1 != 1: 
    # make an attempt
    myAttemptCount += 1  # augment our attempt count
    myDice1 = randint(1, 6) # roll dice # 1
    myDice1 = randint(1, 6) # roll dice # 2
    # print the results of our attempt
    print('Attempt', myAttemptCount, ':', myDice1, 'and', myDice1)

# the loop will only end once we succeed
print('SNAKE EYES!')
print('it took', myAttemptCount, 'tries')