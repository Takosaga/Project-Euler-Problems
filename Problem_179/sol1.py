import math

def countDivisors(n) -> int :
    cnt = 0
    for i in range(1, (int)(math.sqrt(n)) + 1) :
        if (n % i == 0) :

            # If divisors are equal,
            # count only one
            if (n / i == i) :
                cnt = cnt + 1
            else : # Otherwise count both
                cnt = cnt + 2

    return cnt


def solution() -> int:

    consecutive_positive_divisors = 0
    temp_divisors = 0

    for number in range(2,10000000):
        divisors = countDivisors(number)
        if divisors == temp_divisors:
            consecutive_positive_divisors += 1

        temp_divisors = divisors
    return consecutive_positive_divisors

if __name__ == "__main__":
    print(solution())