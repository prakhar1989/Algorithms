import sys 

def minPalPartion(str1): 

    n = len(str1); 
    C = [0]*(n+1); 
    P = [[False for x in range(n+1)] for y in range(n+1)]; 
     
    for i in range(n): 
        P[i][i] = True; 
        
    for L in range(2, n + 1): 
        for i in range(n - L + 1): 
            j = i + L - 1; 
         
            if (L == 2): 
                P[i][j] = (str1[i] == str1[j]); 
            else: 
                P[i][j] = ((str1[i] == str1[j]) and P[i + 1][j - 1]); 
    for i in range(n): 
        if (P[0][i] == True): 
            C[i] = 0; 
        else: 
            C[i] = sys.maxsize; 
            for j in range(i): 
                if(P[j + 1][i] == True and 1 + C[j] < C[i]): 
                    C[i] = 1 + C[j]; 
 
    return C[n - 1];  
  
str1 = "ababbbabbababa";  
print("Min cuts needed for Palindrome Partitioning is",minPalPartion(str1));  
