""""Numerical methods are used to approximate solutions to mathematical problems that are difficult or impossible to solve analytically.
In this project, you will explore the numerical method of bisection to find the square root of a number by iteratively narrowing down the
 possible range of values that contain the square root.
"""
def square_root_bisection(square_target, tolerance=1e-7, max_iterations=100):
    if square_target < 0:
        raise ValueError('Square root of negative number is not defined in real numbers')
    if square_target == 1:
        root = 1
        print(f'The square root of {square_target} is 1')
    elif square_target == 0:
        root = 0
        print(f'The square root of {square_target} is 0')

    else:
        low = 0
        high = max(1, square_target)
        root = None
        
        for _ in range(max_iterations):
            mid = (low + high) / 2
            square_mid = mid**2

            if abs(square_mid - square_target) < tolerance:
                root = mid
                break

            elif square_mid < square_target:
                low = mid
            else:
                high = mid

        if root is None:
            print(f"Failed to converge within {max_iterations} iterations.")
    
        else:   
            print(f'The square root of {square_target} is approximately {root}')
    
    return root
N = 16
square_root_bisection(N)
"""In Python, the max() function returns the largest of the input values
        max(1, 2, 3) # Output: 3
        """
"""The raise statement allows you to force a specific exception to occur. It consists of the raise keyword followed by the exception type,
 and enables you to provide a custom error message:
 raise ValueError("Invalid value")
 """