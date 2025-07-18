from math import sqrt


def printFactors(num):
    factors = []
    for i in range(1, num + 1):
        if num % i == 0:
            factors.append(i)
    return factors


def goodSolutionFactors(num):
    factors = []
    for i in range(1, num // 2 + 1):
        if num % i == 0:
            factors.append(i)
    factors.append(num)
    return factors


def optimalSolutionFactors(num):
    factors = []
    for i in range(1, int(sqrt(num)) + 1):
        if num % i == 0:
            factors.append(i)
            if num // i != i:
                factors.append(num // i)
    factors.sort()
    return factors

    # 1----36
    # 2----18
    # 3----12
    # 4----9
    # 6----6


def main():
    n = 20
    numFactors = printFactors(n)
    print(numFactors)
    goodNumFactors = goodSolutionFactors(n)
    print(goodNumFactors)
    optimalNumFactors = optimalSolutionFactors(n)
    print(optimalNumFactors)


if __name__ == "__main__":
    main()
