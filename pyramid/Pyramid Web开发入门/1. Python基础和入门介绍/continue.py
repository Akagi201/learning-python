while True:
    s = raw_input('command: ')
    if s == 'exit':
        break
    if len(s) < 3:
        print 'insufficient length'
        continue
    print 'Length of string is:', len(s)
else:
    print 'I won\'t be executed'

print 'over'
