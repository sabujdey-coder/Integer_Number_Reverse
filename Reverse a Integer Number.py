integer_number=int(input('Enter your integer number: '))

a=str(integer_number)
b=len(a)
print_result=''
for i in range(-1,-b-1,-1):
    c=a[i]
    print_result=print_result+c


print_result=int(print_result)

print(print_result)

    


            

