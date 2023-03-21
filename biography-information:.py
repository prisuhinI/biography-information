def biography_information():
    name = input("Write your name: ")
    for i in range(len(name)):
        if name.lower()[i] not in 'abcdefghijklmnopqrstuvwxyz' and name[i] != ' ':
            print('incorrect name, please write again')
    date_of_birth = input('Please write youy date of birth: ')
    adress = input('Write your adress here: ')
    personal_goals = input('Write small letter about you ')
    print(f'- Name: John Doe {name}')
    print(f'- Date of birth: {date_of_birth}')
    print(f'- Address: {adress}')
    print(f'- Personal goals: {personal_goals}')


   


biography_information()