birth_year = input("Enter birth year: ")    # Each var declared is always treated as a string in python
age = 2024 - int(birth_year)   # Whenever we input anything in python ,except string,we have to convert it after dec
print("Age:", age)
print(type(birth_year))
print(type(age))
