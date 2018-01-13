import rabbit
import statistics
import time

numSimulations=10000  # The number of simulations to run
numFailures=0     # The number of failures (ie, we never reach 100,000 rabbits)
trials=[]         # List containing the successful trials
start_time=time.time()


for i in range(numSimulations):
    print("Trial ", i+1)
    w=rabbit.Warren()

    failed=False
    genCount=1
    rabbitCount=2
    while rabbitCount<100000:
        genCount+=1
        rabbitCount=w.nextGen()
        if rabbitCount==-1:   # failures
            numFailures+=1
            failed=True
            break
            
    if not failed:
        trials.append(genCount)
    
# print (trials)   #debug
print("--- %s seconds ---" % (time.time()-start_time))
print ("Failures: ",numFailures)
print("Failure Percentage:  ", (numFailures*1.0/numSimulations*1.0)*100,"%")
print ("Median: ", statistics.median(trials))
print ("Mean: ", statistics.mean(trials))
print ("Mode: ", statistics.mode(trials))