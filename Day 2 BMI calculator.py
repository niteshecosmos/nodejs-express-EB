height = input()
weight = input()

#type(height,weight)
weight_as_int = int(weight)
height_as_float = float(height)

bmi = (weight_as_int / height_as_float **2)
print(bmi)