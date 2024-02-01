n=int(input("enter a number: "))
temp=n
rev=0
while temp>0:
    dig=temp%10
    rev=rev*10+dig
    temp=temp//10
if n==rev:
    print("palindrome")
else:
    print("not palindrome")