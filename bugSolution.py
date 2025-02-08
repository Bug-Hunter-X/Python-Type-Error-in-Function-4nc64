def function(a, b):
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return a + b
    else:
        try:
            return float(a) + float(b)
        except ValueError:
            return "Error: Inputs must be numbers or convertible to numbers."

result = function(5, '10')
print(result)
result2 = function(5,10)
print(result2)
result3 = function('hello','world')
print(result3)