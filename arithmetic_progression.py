from functools import reduce
 
# Function to calculate Euclidean distance between two points
def generate_AP(a1, d, n):
 
    AP_series = []
 
    # Complete this function to return A.P. series
    curr_term = a1
    for i in range(1, n+1):
        AP_series.append(curr_term)
        curr_term += d
 
 
    return AP_series
 
 
# Main function
if __name__ == '__main__':
    
    # take the T (test_cases) input
    test_cases = int(input(''))
    for _ in range(test_cases):
        a1, d, n = map(int, input().split())
     
            # Once you have all 3 values, call the generate_AP function to find A.P. series and print it
        AP_series = generate_AP(a1, d, n)
     
            # Using lambda and map functions, find squares of terms in AP series and print it
        sqr_AP_series = list(map(lambda x: x ** 2, AP_series))
     
            # Using lambda and reduce functions, find sum of squares of terms in AP series and print it
        sum_sqr_AP_series = reduce((lambda x, y: x+y), sqr_AP_series)

        print(*AP_series)
        print(*sqr_AP_series)
        print(sum_sqr_AP_series)