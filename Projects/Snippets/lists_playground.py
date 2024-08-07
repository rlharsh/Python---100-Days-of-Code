list = ['larry', 'curly', 'moe']
list.append('shemp')            ## append elem at end
list.insert(0, 'xxx')           ## insert elem at index 0
list.extend(['yyy', 'zzz'])     ## add list of elems at end
print(list)
print(list.index('curly'))

list.remove('curly')            ## search for and remove curly
list.pop(1)                     ## removes and returns 'larry'
print(list)
