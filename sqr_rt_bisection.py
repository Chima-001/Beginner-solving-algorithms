def square_root_bisection(number, tolerance = 0.01, max_iteration = 100):
    if number < 0:
        raise ValueError('Square root of negative number is not defined in real numbers')

    if number == 0 or number == 1:
        print(f'The square root of {number} is {number}')
        return number

    low = 0
    high = max(number, 1)
    iteration = 0

    while iteration < max_iteration:
        mid = (low + high) / 2
        squared_mid = mid * mid

        if abs(high - low) <= tolerance :
            
            print(f'The square root of {number} is approximately {mid}')
            return mid

        if squared_mid > number:
            high = mid
        else:
            low = mid
        
        iteration += 1
            

    print(f'Failed to converge within {max_iteration} iterations')
    return None
    
square_root_bisection(0.001, 0.01, 50)
square_root_bisection(0.25, 1e-7, 50)
square_root_bisection(144, 1e-7, 50)