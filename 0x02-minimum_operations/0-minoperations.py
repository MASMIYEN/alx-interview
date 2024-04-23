def minOperations(n):
    # If n is 0 or negative, it's impossible to achieve
    if n <= 0:
        return 0

    # Calculate the number of operations based on the binary representation of
    # n
    operations = 0
    while n > 1:
        n //= 2  # Divide n by 2
        operations += 1  # Increment the number of operations

    # If n is 1, we've reached the desired number of 'H' characters
    # If n is greater than 1, we need one more operation to reach the exact
    # number
    if n == 1:
        return operations
    else:
        return operations + 1
