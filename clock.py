from time import sleep

def clock():
    attempt = 1
    points = 0
    final_result = {}

    name = input('enter your name : ')
    # print("please 'enter ' to continue  and 'ctrl + c' to close ")
    while True:
        try:
            for digit in range(1,13):
                print(digit)
                sleep(0.3)
        except KeyboardInterrupt:
            print(f'clock stopped at {digit}')
            print(f'{attempt} ')
            print(f'Points are added')

            if digit in [1,2,3,4]:
                points = points + 10
            elif digit in [5,6,7,8]:
                points = points + 20
            elif digit in [9,10,11,12]:
                points = points + 30
            attempt += 1

            if attempt == 4:
                print(f'{name} has scored {points} points')
                final_result[name] = points
                ans = input('is  there any player : y /n : ').lower()
                if ans == 'y':
                    name = input('enter name of player : ')
                    
                    attempt = 1
                    points = 0
                else:
                    print(f'Points table is : {final_result}')
                    return

    
clock()