# class C2dvec:
#     def __init__(self, i, j):
#         self.icap = i
#         self.jcap = j

#     def __str__(self):
#         return f"{self.icap}i + {self.jcap}j"

# class C3dVec(C2dvec):
#     def __init__(self, i, j, k):
#         super().__init__(i, j)
#         self.kcap = k

#     def __str__(self):
#         return f"{self.icap}i + {self.jcap}j + {self.kcap}k"

# v2d = C2dvec(1, 3)
# v3d = C3dVec(1, 9, 7)
# print(v2d)
# print(v3d)

# creaye a class pets from a class animals and futher create class dog form pets. Add a method bark to class dog.

# class Complex:
#     def __init__(self, r, i):
#         self.real = r
#         self.imaginary = 1

#     def __add__(self, c):
#         return Complex(self.real + c.real, self.imaginary + c.imaginary)

#     def __mul__(self, c):
#         mulReal = self.real * c.real - self.imaginary * c.imaginary
#         return Complex(self.real + c.real, self.imaginary + c.imaginary)

#     def __str__(self):
#         return f"{self.real} + {self.imaginary}"

# c1 = Complex(1, 11)
# c2 = Complex(8, 6)
# print(c1 + c2)


# Write a class vector representing a vector of n dimension. Overload the + and * operator which calculate the sun and the dot product of them.

# class Vector:
#     def __init__(self, vec):
#         self.vec = vec
#     def __str__(self):
#         str1 = ""
#         index = 0
#         for i in self.vec:
#             str1 += f" {i}a{index} +"
#             index +=1
#         return str1[:-1]

#     def __add__(self, vec2):
#         newList = []
#         for i in range (len(self.vec)):
#             newList.append(self.vec[i] + vec2.vec[i])
#         return Vector(newList)

#     def __mul__(self, vec2):
#         sum = 0
#         for i in range (len(self.vec)):
#             sum += self.vec[i] * vec2.vec[i]
#         return sum

# v1 = Vector([1, 4, 6])
# v2 = Vector([1, 6, 9])
# # print(v1+v2)
# print(v1*v2)


# write __str__() method to print the vector as follows:
# 7i + 8j + 10k Assume vector of dimension 3 for this probelm.

# class Vector:
#     def __init__(self, vec):
#         self.vec = vec
#     def __str__(self):
#         return f"{self.vec[0]}i + {self.vec[1]}j + {self.vec[2]}k"

# v1 = Vector([1, 4, 6])
# v2 = Vector([1, 6, 9])
# print(v1)
# print(v2)


# Override the __len__() method on Vector of problem 5 to display the dimension fo the vector.

class Vector:
    def __init__(self, vec):
        self.vec = vec
    def __str__(self):
        str1 = ""
        index = 0
        for i in self.vec:
            str1 += f" {i}a{index} +"
            index +=1
        return str1[:-1]

    def __add__(self, vec2):
        newList = []
        for i in range (len(self.vec)):
            newList.append(self.vec[i] + vec2.vec[i])
        return Vector(newList)

    def __mul__(self, vec2):
        sum = 0
        for i in range (len(self.vec)):
            sum += self.vec[i] * vec2.vec[i]
        return sum
    
    def __len__(self):
        return len(self.vec)

v1 = Vector([1, 4, 6, 3, 5])
v2 = Vector([1, 6, 9])
print(len(v1))
print(len(v2))
