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


def main():
    n = 20
    numFactors = printFactors(n)
    print(numFactors)
    goodNumFactors = goodSolutionFactors(n)
    print(goodNumFactors)


if __name__ == "__main__":
    main()
