def maxSatisfied(customers, grumpy, minutes):
    n=len(customers)
    res=sum([customers[i]*(1-grumpy[i]) for i in range(n)])    # the customers you can obtain while non grumpy
    best_gain=sum([customers[i]*grumpy[i] for i in range(minutes)])    # first window
    gain=best_gain
    for i in range(minutes,n):
        gain+=customers[i]*grumpy[i]-customers[i-minutes]*grumpy[i-minutes]  # add new, kick out old
        best_gain=max(gain,best_gain)    
    return res+best_gain

if __name__ == '__main__':
    print(maxSatisfied([1,0,1,2,1,1,7,5],[0,1,0,1,0,1,0,1],3))
        
    
