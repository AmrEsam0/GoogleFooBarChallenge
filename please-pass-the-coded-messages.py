from itertools import combinations

def solution(arr):
	arr.sort(reverse = True)
	for i in reversed(range(1, len(arr) + 1)):
		for tup in list(combinations(arr, i)):
			if sum(tup) % 3 == 0: return int(''.join(map(str, tup)))
	return 0