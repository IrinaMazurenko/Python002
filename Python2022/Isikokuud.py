isikukood = input("Please enter ID: ")

while True:
    try:
      user_input = input('Please enter your ID(type exit to quit): ')
      if user_input.lower() == 'Exit':
          break
      int(user_input)
      if len(user_input) != 11:
          if len(user_input) > 11:
              print('ID is wrong')
          else:
              print('ID is too short!')
          raise UserWarning

    except ValueError:
        print('ID you entered is not numeric!')
    except UserWarning:
        print('ID  you entered is not 11 digits long')
    else:
        print(user_input)
        break
