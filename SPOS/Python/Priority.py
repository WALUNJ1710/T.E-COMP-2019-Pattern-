def findWaitingTime(processes,n,wt):
	wt[0] = 0
	
	for i in range(1,n):
		wt[i] = processes[i-1][1]+wt[i-1]
		
def findTurnAroundTime(processes,n,wt,tat):
	for i in range(n):
		tat[i] = processes[i][1]+wt[i]
		
def findavgTime(processes,n):
	wt = [0]*n
	tat = [0]*n
	
	total_wt = 0
	total_tat = 0
	
	findWaitingTime(processes,n,wt)
	findTurnAroundTime(processes,n,wt,tat)
	
	print("Process Burst Time "+" Waiting Time "+" Turn Around Time")
	
	for i in range(n):
		total_wt = total_wt+wt[i]
		total_tat = total_tat+tat[i]
		
		print("{}\t\t{}\t\t{}\t\t{}".format(processes[i][0],processes[i][1],wt[i],tat[i]))
		
	print("Average waiting time: {}".format(total_wt/n))
	print("Average turn around time: {}".format(total_tat/n))
	
def priorityScheduling(proc,n):
	proc = sorted(proc, key=lambda proc:proc[2], reverse=True)
	print("Order of processes is:")
	for i in proc:
		print(i[0])
	print("\n")
	
	findavgTime(proc,n)
	
proc = [[1,10,1],[2,5,0],[3,8,1]]
n = 3
priorityScheduling(proc,n)
