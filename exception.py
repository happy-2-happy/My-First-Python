def exception():
    try:
        answer = 5/0
    except ArithmeticError as error:
        print(f'Exception Occured {error}')
    else:
        print('No Exception Occured')
    finally:
        print('End of the Exception Block')
