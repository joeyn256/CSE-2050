def price_to_profit(L): 
    profits=[0]
    for i in range(0,len(L)-1):
        p = L[i+1]-L[i]
        profits.append(p)
    return profits

# brute force solution
def max_profit_brute(L):
    """Finds maximum profit. Assumes L is a list of profits (i.e. change in price every day), not raw prices"""
    n = len(L)
    max_sum = 0 # assume we can at least break even - buy and sell on the same day

    # outer loop finds the max profit for each buy day
    for i in range(n):
       # total profit if we bought on day i and sold on day j
        total = L[i]
        ##### THE MISSING CHECK #####
        if total > max_sum: max_sum = total 
        
        for j in range(i+1, n): 
            total += L[j] # total profit if we sell on day j
                          # we assume L[j] is the profit if we bought on day j-1 and sold on day j
                          # i.e., L is the change in value each day, relative to the day before
            if total > max_sum: max_sum = total

    return max_sum
##### TODO 2 #####

def max_profit_helper(L,left,right):
    
    if left == right:
        return 0
  
    median = (left+right)//2

    left1 = max_profit_helper(L, left, median)      #P1 max profit in the left
    right1 = max_profit_helper(L, median+1, right)  #P2 max profit in the right
    cross1 = max_profit_crossing(L, left, right, median) #P3 max_profit that crosses

    return max(left1, right1, cross1)  # return best case across three

# you'll need a helper function or default parameters here

def max_profit(L):  # O(nlogn)
   #tempy = max_profit_crossing(L,left,right,median)
   return max_profit_helper(L,left=0,right=len(L)-1)

##### TODO 3 #####

def max_profit_crossing(L, left, right, median, Testcase = None):
# Variables Required
  maxpa = 0
  temp_pa_sum=0
  maxpb=0
  temp_pb_sum = 0
  maxpc = 0
  #Pa case
  for i in range(median, left-1, -1):
    temp_pa_sum = temp_pa_sum + L[i]
    if (temp_pa_sum > maxpa):
      maxpa = temp_pa_sum
  #Pb case
  for i in range(median + 1 , right + 1):
    temp_pb_sum = L[i] + temp_pb_sum
    if (temp_pb_sum > maxpb):
      maxpb = temp_pb_sum
  #Pc case
  maxpc = maxpa + maxpb
  if Testcase == 'pa': return maxpa
  elif Testcase == 'pb': return maxpb
  elif Testcase == 'pc': return maxpc
  else: return max(maxpa,maxpb,maxpc)