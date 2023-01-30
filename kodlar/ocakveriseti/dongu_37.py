a=int(input("agacin yuksekligi"))
b=a
for i in range(1,a+1):
    print(b*" ",(2*i-1)*"*")
    b=b-1