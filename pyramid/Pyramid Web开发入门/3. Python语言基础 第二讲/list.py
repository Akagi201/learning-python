item_list = ['apple', 'pear', 'banana']
print 'There are %s items in your list' % len(item_list)
print 'They are:'
for i in item_list:
    print i
print 'I added something...'
item_list.append('carrot')
print 'Now they are:'
for i in item_list:
    print i
print 'I removed something...'
del item_list[0]
print 'Now they are:'
for i in item_list:
    print i
print 'Sort it!'
item_list.sort()
print 'Now they are:'
for i in item_list:
    print i

