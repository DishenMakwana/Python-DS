# Import any required module/s
 
# Function to calculate Euclidean distance between two points
def compute_distance(x1, y1, x2, y2):
	distance = "{:.2f}".format( ((x1-x2)**2 + (y1-y2)**2)**0.5 )
	print("Distance: ", distance)
 
# Main function
if __name__ == '__main__':
    
    # Take the T (test_cases) input
    test_cases = int(input())
    for _ in range(test_cases):
    	x1, y1, x2, y2 = map(int, input().split())
    	compute_distance(x1, y1, x2, y2)