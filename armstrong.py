
n=int(input("Enter the number : "))
t=n
r=0
sum=0
while n>0:
    d=n%10
    r=d*d*d
    sum=sum+r
    n=n//10
if t==sum:
    print(sum,"is armstrong number")
else:
    print("not armstrong")





# n=int(input("Enter the limit"))
# for i in range(1,n+1):
#     t=i
#     r=0
#     while i>0:
#         d=i%10
#         r=(d*d*d)+r
#         i=i//10
#     if t==r:
#         print(t)