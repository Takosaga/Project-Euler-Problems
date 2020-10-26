def solution():

    total = 2 ** 12710
    count = 12710
    p_count = 45
    while True:
        total *= 2
        count += 1

        if str(total)[0] == "1" and str(total)[1] == "2" and str(total)[2] == "3":
            p_count +=1 
    

        if p_count == 678910:
            break
    return p_count

if __name__ == "__main__":
    print(solution())
