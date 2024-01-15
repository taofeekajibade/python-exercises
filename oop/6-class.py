class Sample:
    pass

x = Sample()
x.name = "Oriolowo"
y = Sample()
y.name = "Kayegbo"
y.year = "1996"
y.version = 2.5

print(y.version)
print(x.name)
print(y.name)
print(x.__dict__)
print(f"This is the content of y: {y.__dict__}")
