#Fibonacci's sequence is a sequence of numbers
#where every number is the sum of the previous two numbers.


def fibonacci_with_stopper(stopper):
    """
    Create the fibonacci sequence, giving it a number as a stopper.

    Args:
        stopper (int): A given number that stops the sequences

    Yield:
        (generator): A generator class object containing the generated
        fibonacci 
    """
    a, b = 0, 1
    while a <= stopper:
        a, b = b, a + b
        yield a
        
fibonacci = list(fibonacci_with_stopper(20))
print(fibonacci)