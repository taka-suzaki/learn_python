d1 = {
    "a": 2,
    "b": 3,
    "c": {
        "A": 11,
    }
}

d2 = {
    "d": 1,
    "e": 4,
    "f": "F"
}

s1 = "s1"
s2 = "s2"

def f1():
    return "A"


def f2():
    return "B"


print((d1, s1) == (d2, s2))
print((d1, s1) == (d1, s1))
print((f1, s1) == (f1, s1))
print((f1, s1) == (f1, s2))
print((f1, s1) == (f2, s1))