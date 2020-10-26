import math

def solution():

    total = 2 ** 1
    count = 1
    p_count = 0
    numbers = 3

    while True:
        total *= 2
        count += 1
        check = str(total)
        length = len(check)

        if length > numbers:
            numbers = length
            if total//10 ** (int(math.log(total,10))-2) == 123:
                p_count +=1
                if p_count == 1000:
                    break
    return count

if __name__ == "__main__":
    print(solution())
