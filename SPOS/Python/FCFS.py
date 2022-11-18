def findWaitingTime(processes,n,bt,wt):
	wt[0]=0
	for i in range(1,n):
		wt[i]=bt[i-1]+wt[i-1]
		
def findTurnAroundTime(processes,n,bt,wt,tat):
	for i in range(n):
		tat[i]=bt[i]+wt[i]
		
def findavgTime(processes,n,bt):
	wt = [0]*n
	tat = [0]*n
	total_wt = 0
	total_tat = 0
	
	findWaitingTime(processes,n,bt,wt)
	
	findTurnAroundTime(processes,n,bt,wt,tat)
	
	print("Processes Burst Time "+" Waiting Time "+" Turn around Time")
	
	for i in range(n):
		total_wt = total_wt + wt[i]
		
		total_tat = total_tat + tat[i]
		
		print("{}\t{}\t\t{}\t\t{}".format(str(i+1),str(bt[i]),str(wt[i]),str(tat[i])))
		
	print("\nAverage Waiting time is: {}".format((total_wt)/n))
	print("Average Turn around time is: {}".format((total_tat)/n))
	
processes = [1,2,3]

n = len(processes)

burst_time = [10,5,8]

findavgTime(processes,n,burst_time)
