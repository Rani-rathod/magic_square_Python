
magic_square = [
    [8, 3, 4],
    [1, 5, 9],
    [6, 7, 2]
]
i=0
total=15
while i<len(magic_square):
    col=0
    sum=0
    s=len(magic_square[i])
    while col<s:
        sum=sum+magic_square[col][col]
        col=col+1
    print(i,"colum",sum)
    a=sum+sum+sum
    i+=1
print(a)
j=0
while j<len(magic_square):
    row=0
    sum1=0
    while row<len(magic_square[j]):
        sum1=sum1+magic_square[row][row]
        row+=1
    print(j,"row",sum1)
    j+=1
diagonal=15
g=0
sum2=0
while g<len(magic_square):
    sum2=sum2+magic_square[g][g]
    g+=1
print("diagonal",sum2)



# magic_square=[
#     [8,3,4],
#     [1,5,9],
#     [6,7,2],
# ]
# i=0
# while i<len(magic_square):
#     j=0
#     sum=0
#     while j<len(magic_square[i]):
#         sum=sum+(magic_square[i][j])
#         j+=1
#     print(sum)
#     i+=1