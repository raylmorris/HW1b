import random

def numberGame(rangeMax):
	answer = random.randint(1, rangeMax)
	mid = lambda x, y: (x+y)//2
	l_bound = 1
	r_bound = rangeMax
	guess = mid(l_bound, r_bound)
	iter_count = 1*(l_bound==answer) + 2*(r_bound==answer)
	while guess!=answer:
		if r_bound - l_bound == 1:
			l_bound = r_bound
		if guess > answer:
			r_bound = guess
		else:
			l_bound = guess
		guess = mid(l_bound, r_bound)
		iter_count += 1
	print(guess, answer, l_bound, r_bound, iter_count, sep=', ')
	return iter_count
def task1(max):
	return sum([numberGame(int(max)) for x in range(int(1e4))])/1e4
def outputQ1():
	return (task1(1000), task1(1e6))
if __name__ == "__main__":
	print(outputQ1())
