def tempConv():
    print('1. To convert to Fahrenheit')
    print('2. To convert to Celsuis')
    print('3. To exit')
    print('')

    try:
        decision = int(input('Input a number based on the operation stated above: '))

        if decision == 1:
            C = int(input('Input value of the temperature in celcuis: '))
            print('')
            F = C * 9/5  + 32
            print( C, 'degree celcuis =', F, 'degree fahrenheit')
            print('')
            tempConv()
        elif decision == 2:
            F = int(input('The value of the temperature in fahrenheit: '))
            print('')
            C = (F -32) * 5/9
            print( F, 'degree celcuis =', C, 'degree fahrenheit')
            print('')
            tempConv()
        elif decision == 3:
            exit()
        else:
            print('Invalid input')
            tempConv()
    except:
        print('Error, try again')

tempConv()
