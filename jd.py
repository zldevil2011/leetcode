if __name__ == '__main__':
	n,m = map(int,raw_input().split())
	flag = 0
	for i in range(n, m+1):
		bw = i / 100
		sw = i % 100 / 10
		gw = i % 10
		if bw*bw*bw + sw*sw*sw + gw*gw*gw == i:
			print i
			flag = 1
	if flag == 0:
		print "no"