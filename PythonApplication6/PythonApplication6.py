
X = int(input("Введите количество мальчиков (X): "))
Y = int(input("Введите количество девочек (Y): "))

if abs(X - Y) > 1:
    print("Нет решения")
else:
    result = []
    if X >= Y:
  
        extra_men = X - Y
        
        while X > 0 or Y > 0:
            if X > 0:
                result.append('B')
                X -= 1
            if Y > 0:
                result.append('G')
                Y -= 1
        

        for i in range(extra_men):
            if i < len(result) - 1:
                result.insert(i * 2 + 1, 'B')
            else:
                result.append('B')
    else:
      
        extra_girls = Y - X
        
        while X > 0 or Y > 0:
            if Y > 0:
                result.append('G')
                Y -= 1
            if X > 0:
                result.append('B')
                X -= 1
        
     
        for i in range(extra_girls):
            if i < len(result) - 1:
                result.insert(i * 2 + 1, 'G')
            else:
                result.append('G')


    print("".join(result))
