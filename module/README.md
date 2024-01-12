In Python, a module is a file which contains Python definitions and statements. The file name is the module name with the suffix `.py`. For example, if you have a file named `my_module.py`, it can be imported as a module in another Python script or program.

Modules allow a programmer to organize Python codes into reusable units. They provide a way to structure large programs and encourage code reusability. The functions, variables, and classes defined in a module can be reused by importing them into another script or program.

Below a simple example:

Suppose you have a module named `math_operations.py` with the following content:

```python
""" math_operations.py """

def add_num(x, y):
    return x + y

def subtract_num(x, y):
    return x - y

def multiply_num(x, y):
    return x * y

def divide_num(x, y):
    return x / y
```

Now, in another Python script, we can import and use the functions from this module:

```python
""" main_script.py.
The script that imports the module.
The module is imported without its `.py` extension.
"""

import math_operations

result_sum = math_operations.add_num(5, 3)
result_diff = math_operations.subtract_num(8, 4)
result_mul = math_operations.multiply_num(7, 6)
result_div = math_operations.divide_num(20, 5)

print("Sum:", result_sum)
print("Difference:", result_diff)
print("Multiplication:", multiply_num)
print("Division:", divide_num)
```

In this example, `math_operations` is a module, and `add_num`, `subtract_num`, `multiply_num` and `divide_num` are functions defined within that module. The `main_script.py` file imports the `math_operations` module to use its functions. The module is imported without its `.py` extension. So, basically, there are two files - one containes the module and the other is the script where the module is used (imported).