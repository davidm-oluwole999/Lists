#Create a 2D list

matrix= [[1,2,3],[4,5,6],[7,8,9]]

print(matrix)

#Number of rows
print(len(matrix))

#Number of columns
print(len(matrix[0]))

#Accessing an element from 2D list
print(matrix[2][1])

#Looping through the values in a 2D list
for i in range(0, len(matrix)):
    for j in range(0, len(matrix[0])):
        print(matrix[i][j], end=" ")
    print("\n")

