def hcf(a, b): 
    if(b == 0): 
        return a 
    else: 
        return hcf(b, a % b) 

print("Enter two numbers") 

a = int(input()) 

b = int(input()) 

print(f"The gcd of {a} and {b} is : ",hcf(a,b))
