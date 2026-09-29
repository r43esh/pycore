age=-1
try:
    if age < 19:
        raise ValueError("age cant be negative")
except Exception as e:
    print(e)
print("now code will continue even after eror")
