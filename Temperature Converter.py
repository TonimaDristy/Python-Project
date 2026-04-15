def c_to_f(c):
    return (c * 9/5) + 32

def f_to_c(f):
    return (f - 32) * 5/9

print("1. C to F")
print("2. F to C")

choice = input("Choice: ")

if choice == "1":
    c = float(input("Celsius: "))
    print("Fahrenheit:", c_to_f(c))

elif choice == "2":
    f = float(input("Fahrenheit: "))
    print("Celsius:", f_to_c(f))