n=int(input("Enter the consumed units"))
if(n<=100):
  t=n*2
elif(n>100):
  t=n*3
else:
  t=n*5
print("Amount to paid ",t)
