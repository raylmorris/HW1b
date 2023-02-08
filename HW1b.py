import random
import time
from math import sqrt
import re

avg = lambda x: sum(x)/len(x)

def numberGame(rangeMax):
    answer = random.randint(1, rangeMax)
    mid = lambda x, y: (x+y)//2
    l_bound = 1
    r_bound = rangeMax
    guess = mid(l_bound, r_bound)
    iter_count = 1
    if l_bound == answer:
        return iter_count
    iter_count += 1
    if r_bound == answer:
        return iter_count
    while guess!=answer:
        if r_bound - l_bound == 1:
            l_bound = r_bound
        if guess > answer:
            r_bound = guess
        else:
            l_bound = guess
        guess = mid(l_bound, r_bound)
        iter_count += 1
    return iter_count
def task1(max):
    return sum([numberGame(int(max)) for x in range(int(1e4))])/1e4
def outputQ1():
    return (task1(1000), task1(1e6))
def driverQ1():
    suffix = 'None'
    for i in enumerate(outputQ1()):
        if suffix == 'K': suffix = 'M'
        else: suffix = 'K'
        print(
            i[0],
            f'. The random numbers between 1 .. 1{suffix}:',
            ' Total guesses:',int(i[1]*1e4),' Avg:',i[1]
        )
        
def timeEfficiency(funcName, *args):
    start = time.time_ns()
    result = funcName(*args)
    end = time.time_ns()
    return start/(1e9), end/(1e9), (end - start) / (1e9), result
def isPrime(ii):
    if ii < 2: return False
    for pf in range(2, 1+int(sqrt(ii))):
        if ii%pf == 0:
            return False
    return True
def listPrimeNumbers(theMaxNum):
    result_list = []
    for i in range(int(theMaxNum)+1):
        if isPrime(i): result_list.append(i)
    return result_list
def driverQ2():
    user_number = int(input('Enter a whole number for the list of prime numbers: '))
    return_value = timeEfficiency(listPrimeNumbers, user_number)
    print(f'List of prime numbers of {user_number}','{')
    print(f'\tstart: {return_value[0]}',
        f'end: {return_value[1]}',
        f'time efficiency: {return_value[2]}',
        f'result {return_value[3][:5]+["..."]+return_value[3][-5:]}'.replace("'...'",'... '),
        sep = '\n\t')
    print('}')

def generateRandom():
    return str(random.randint(0,999)).zfill(3)
def deterministicBruteForce(answer):
    for guess in range(10**3):
        if str(guess).zfill(3) == answer:
            return guess
    return -1
def pureRandomAlgorithm(answer):
    counter = 1
    while True:
        if answer == generateRandom():
            return counter
        counter += 1
def driverQ3():
    determ = [deterministicBruteForce(generateRandom()) for y in range(10000)]
    pure_rand = [pureRandomAlgorithm(generateRandom()) for y in range(10000)]
    determ_stats = {
        "algorithm" : "a) Deterministic brute-force guessing algorithm",
        "num_tries" : len(determ),
        "max_guesses" : max(determ),
        "min_guesses" : min(determ),
        "avg_guesses" : avg(determ)
    }
    pure_rand_stats = {
        "algorithm" : "b) Pure random guessing algorithm",
        "num_tries" : len(pure_rand),
        "max_guesses" : max(pure_rand),
        "min_guesses" : min(pure_rand),
        "avg_guesses" : avg(pure_rand)
    }
    for item in [determ_stats, pure_rand_stats]:
        print(
            f"{item['algorithm']}:",
            f"Number of Tries: {item['num_tries']}",
            f"The highest number of guesses in a try: {item['max_guesses']}",
            f"The lowest number of guesses in a try: {item['min_guesses']}",
            f"The average number of guesses in a try: {item['avg_guesses']:0.2f}",
            sep="\n\t"
        )
def driverQ4():
    with open(input('Enter a file name: '), "r") as f:
        file_out = sorted(re.split(r'[^a-z]+',f.read().lower()))
    word_counts = sorted(
        {x: file_out.count(x) for x in set(file_out)}.items(),
        key=lambda kvp: kvp[1],
        reverse = True
    )
    nn = int(input('See top "n" words by inputting an integer for n: '))
    for word in word_counts[:nn]:
        print(word[0]+' : '+str(word[1]))

    
if __name__ == "__main__":
    driverQ1()
    driverQ2()
    driverQ3()
    driverQ4()
    #driverQ5()
