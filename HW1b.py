import random
import time

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
        #print(r_bound-l_bound)
        if r_bound - l_bound == 1:
            l_bound = r_bound
        #print(l_bound, r_bound)
        if guess > answer:
            r_bound = guess
        else:
            l_bound = guess
        guess = mid(l_bound, r_bound)
        iter_count += 1
        #print(l_bound, r_bound, guess)
    #print(guess, answer, l_bound, r_bound, iter_count, sep=', ')
    return iter_count
def task1(max):
    return sum([numberGame(int(max)) for x in range(int(1e4))])/1e4
def outputQ1():
    return (task1(1000), task1(1e6))
def printQ1():
    for i in enumerate(outputQ1()):
        print(
            i[0],
            '. The random numbers between 1 .. 1K:',
            ' Total guesses:',int(i[1]*1e4),' Avg:',i[1]
        )
def timeEfficiency(funcName, *args):
    start = time.time()
