import math

def solution():

    total = 1
    add = 1
    while True:
        add += 2
        total += add

        if total > 1020304050607080900:
            num = str(total)
            if int(num[-1]) == 0:
                if int(num[-3]) == 9:
                    if int(num[-5]) == 8:
                        if int(num[-7]) == 7:
                            if int(num[-9]) == 6:
                                if int(num[-11]) == 5:
                                    if int(num[-13]) == 4:
                                        if int(num[-15]) == 3 :
                                            if int(num[-17]) == 2 :
                                                if int(num[-19]) == 1:
                                                    break

    return int(math.sqrt(total))

if __name__ == "__main__":
    print(solution())