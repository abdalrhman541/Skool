length =  input('Please inter a length of the pyramid : ')
for i in list(range(int(length) + 1)):
    for j in list( range(i)):
         print('*' , end = ' ')
    print()
