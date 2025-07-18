def printFactors(num):
    factors = []
    for i in range(1, num + 1):
        if num % i == 0:
            factors.append(i)
    return factors


def main():
    n = 43
    numFactors = printFactors(n)
    print(numFactors)


if __name__ == "__main__":
    main()
