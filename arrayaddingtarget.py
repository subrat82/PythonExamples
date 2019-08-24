# array addition to a target number

def pair_sum(array, t):
    if len(array) < 2:
          return print('too small')

    seen = set()
    output = set()
    

    for num in array:
         target = t - num

         if target not in seen:
            seen.add(num)
           # print(array.index(num))

         else:
             print("index:", array.index(num))
             i = array.index(num)
             if target in array:
                print("index:" , array.index(target))
                #output.add(array.index(num))
             output.add((min(num, target), max(num, target)))
             

    print('\n'.join(map(str, list(output))))
    
    
pair_sum((2,7,5,4), 9)

