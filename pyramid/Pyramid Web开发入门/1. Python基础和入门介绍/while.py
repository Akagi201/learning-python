number = 53
go = True
while go:
    guess = int(raw_input('input a number please'))
    if guess == number:
        print 'correct'
        go = False
    elif guess < number:
        print 'try a bigger one'
    else:
        print 'try a smaller one'
else:
    print 'it\'s over'
