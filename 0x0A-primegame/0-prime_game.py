#!/usr/bin/python3
""" prime game interview question """


def get_first_prime(values):
    for i in values:
        if isPrime(i):
            return [v for v in values if v % i != 0]
    return False


def isPrime(x):
    """ check if number is a prime number """
    if x < 2 or x == 4:
        return False
    for i in range(2, x // 2):
        if x % i == 0:
            return False
    return True


def isWinner(x, nums):
    """ return name of the player that won the most rounds """
    if x != len(nums):
        return None
    M = {"Turn": True, "Score": 0}
    B = {"Turn": False, "Score": 0}
    round = 0
    while (x):
        B["Turn"] = False
        M["Turn"] = True
        if round >= len(nums):
            round = 0
        current = [x for x in range(1, nums[round] + 1)]
        while(len(current) > 1):
            if get_first_prime(current):
                current = get_first_prime(current)
                if M["Turn"]:
                    M["Turn"] = False
                    B["Turn"] = True
                else:
                    B["Turn"] = False
                    M["Turn"] = True
        if M["Turn"]:
            B["Score"] += 1
        else:
            M["Score"] += 1
        round += 1
        x -= 1
    if B["Score"] < M["Score"]:
        return 'Maria'
    return 'Ben'