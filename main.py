#Math 4330 Quiz 3
#Andres Suarez

#dot takes 2 vectors and returns the dot product when they are multiplied.

def dot(vector1, vector2):
  '''
This function takes 2 vectors of the same length and computes the dot product. First we check to see if the vectors are compatible. Then, a solution integer is initialized which will store our answer. The zip function is used to merge the 2 vectors of the same length into pairs. This way we match each element of the same index position to calculate the product and then add up the sum of the products. The final result is stored in the integer solution.
  '''
  #Check if input is valid
  if len(vector1) == len(vector2):
    solution = 0
    #Checks each element of vector1
    for i in range(len(vector1)):
      solution += vector1[i] * vector2[i]
    return solution
  else:
    return "The input is invalid"

#vecSubtract takes 2 vectors and returns the difference between the 2 vectors (vector1 - vector2)

def vecSubtract(vector1, vector2):
  '''
This function takes 2 vectors of the same length and computes the difference. A solution vector is initialized to return our final answer. Then a temporary result vector is initialized along with a temporary integer "item". The item integer computes the difference between the elements of the 2 vectors and stores it in our temporary result vector. The result vector now contains 3 lists inside of it with the difference between each element in vector1 with all elements of vector2. Since we are looking for the difference between the elements in matching index positions, we take out the correct difference from each list in our result vector and append it to our solution vector. The final result is solution = (vector1 - vector2)
  '''
  #Check if input is valid
  if len(vector1) == len(vector2):
    solution = []
    for i in range(len(vector1)):
      #temporary vector and integer
      result = []
      item = 0
      for j in range(len(vector2)):
        #takes difference between 1 element in vector1 and all elements in vector2
        item = vector1[j] - vector2[i]
        #appends all 3 lists into our temporary vector
        result.append(item)
      #appends only the correct difference into the solution
      solution.append(result[i])
    return solution
  else:
    return "The input is invalid"

#scalarVecMulti takes a scalar and a vector and returns the corresponding scalar-vector multiplication. 

def scalarVecMulti(scalar,vector1):
    '''
This function takes a scalar and a vector as it's arguments. An temporary integer "item" is created to store the product of the scalar with each element in the vector. Each result for "item" is stored in the empty "solution" list. Solution is returned which contains the product of the scalar and vector.
    '''
    item = 0
    solution = []
    for i in range(len(vector1)):
        item = scalar * vector1[i]
        solution.append(item)
    return solution

#infNorm takes a vector and returns the infinity norm of that vector

def infNorm(vector1):
  '''
This function takes one vector as its argument and computes the infinity norm of that vector. This is done by essentially calculating the max value of the vector. A maximum integer is set at 0 and forloop updates the value of the maximum to any value that is greater than the previous element inside the vector
  '''
  maximum = 0
  for i in range(len(vector1)):
    #if the element is more than 0 the max becomes that value
    if abs(vector1[i]) > maximum:
      maximum = abs(vector1[i])
    return maximum
  

#Normalize takes a vector and returns the normalized vector with respect to the infinity norm 
#[(1/infNorm(vector1))*(vector1)]

def Normalize(vector1):
  '''
  This function takes a vector as its argument. First sets a temporary integer "item" as the result of dividing 1 by the infinity norm value of our vector. Our "solution" integer is then set to return the product of the item by our vector. The solution is the product vector.
  '''
  item = 1 / infNorm(vector1)
  solution = scalarVecMulti(item, vector1)

  return solution

#These are test variables being initialized to test the above functions.

vector1 = [6,5,4]
vector2 = [3,2,1]
scalar = 2

invalidvector1 = [3,2,1]
invalidvector2 = [7,6,5,4]

print("The dot product of the 2 vectors is:" ,dot(vector1, vector2))
#print(dot(invalidvector1, invalidvector2))
print("The difference of the 2 vectors is:" ,vecSubtract(vector1, vector2))
#print(vecSubtract(invalidvector1, invalidvector2))
print("The scalar-vec product is:" ,scalarVecMulti(scalar, vector1))
print("The infinity norm of the vector is:" ,infNorm(vector1))
print("The normalized vector is:" ,Normalize(vector1))
