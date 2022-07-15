import collections.abc

def update(d, u):
    for k, v in u.items():
        if isinstance(v, collections.abc.Mapping):
            d[k] = update(d.get(k, {}), v)
        else:
            d[k] = v
    return d

if __name__ == "__main__":
    d1 = {
        "a": 1, 
        "b": 2,
        "c": {
            "d": 3,
            "e": 4,
        }
    }
    
    d2 = {
        "a": 10,
        "c": {
            "d": 30,
            "f": 50,
        },
        "g": 60
    }
    print(update(d1, d2))