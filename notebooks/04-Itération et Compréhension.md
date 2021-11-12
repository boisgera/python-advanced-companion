---
jupyter:
  jupytext:
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.3'
      jupytext_version: 1.13.0
  kernelspec:
    display_name: Python 3 (ipykernel)
    language: python
    name: python3
---

# Flux de contrôle et exceptions

```python
for i in range(10):
    print(i)
    if i == 5:
        break
```

```python
for i in range(10):
    print("*", i)
    if (i % 2): # i odd
        continue # skip the rest of this indented block, but keep iterating
    else:
        print(">")
```

```python
for i in range(5):
    print(i)
else:
    print("else")
```

```python
for i in range(5):
    print(i)
    if i == 4:
        break
else:
    print("else")
```

```python
def f(x):
    pass
```

```python
f(1, 2)
```

```python
def g():
    a = 1 + 1
    f(1, a)
    print("jdkjdksjdksjds")

def h():
    z = g()
    print(z)
```

```python
h()
```

```python
try:
    z = f(1, 2)
except TypeError as error:
    print("error detected:", error)
```

```python
raise TypeError("f() takes 1 positional argument but 2 were given")
```

```python
def f(n):
    if n < 0:
        # message defined by a f-string
        message = f"{n} is negative" # str(n) + " is negative"
        raise ValueError(message)
    return n*n
```

```python
f(5)
```

```python
f(-5)
```

# Iteration

```python
for i in [1, 2, 3]:
    print(i)
```

```python
it = iter([1, 2, 3]) # it is an iterator
it
```

```python
next(it)
```

```python
next(it)
```

```python
next(it)
```

```python
next(it)
```

```python
it = iter([1, 2, 3]) # iterable: can produce iterators with iter(iterable)
it # iterator: next(it) makes sense
```

```python
l = [1, 2, 3]

it1 = iter(l)
print(next(it1))
print(next(it1))

it2 = iter(l)
print(next(it2))
print(next(it2))
```

```python
l = [1, 2, 3]

it1 = iter(l)
it2 = iter(it1) # not very useful ...

print(it1 is it2)

print(next(it1))
print(next(it1))

print(next(it2))
print(next(it2))

```

```python
l = list(range(100))
for i in l:
    print(i)
    l.pop(0) # modification during iteration => undefined
```

```python
l = list(range(100))
for i in l[:]: # safer to iterate on a copy of the list
    print(i)
    l.pop(0)
```

Iterables :

  - lists
  
  - tuples
  
  - dicts
  
    - dict keys
    
    - dict values
    
    - dict items
  
  - sets
    
  - strings
  
  - files
  
  - range(100)
  
  - enumerate(...)

```python
d = {"a": 1, "b": 2}
```

```python
d.keys()
```

```python
iter(d.keys())
```

```python
for c in "Hello world!":
    print(c)
```

```python
enumerate([6, 7, 8])
```

```python
for i, number in enumerate([6, 7, 8]):
    print(i, number)
```

```python
iter(enumerate([6, 7, 8]))
```

```python
l1 = [1, 2, 3]
l2 = [4, 8, 16]
for item in zip(l1, l2): # simultaneous iteration on l1 and l2
    print(item)
```

```python
help(list)
```

```python
list([1, 2, 3])
```

```python
list({1: "a", 2: "b", 3: "c"})
```

```python
list("abc")
```

```python
help(max)
```

```python
max(1, 2, 3)
```

```python
max([1, 2, 3])
```

```python
max("Hello world!")
```

# Compréhension

```python
l = [1, 2, 3]
squares_l = []
for i in l:
    square = i * i
    squares_l.append(square)
squares_l
```

```python
[i*i for i in l]
```

```python
l = range(10)
[i*i for i in l if i*i > 20] # "filter in" elements
```

```python
type([i*i for i in l if i*i > 20])
```

```python
{i*i for i in l if i*i > 20}
```

```python
{i: str(i) for i in range(100)}
```

### generator expressions

```python
max([x*x for x in range(10)])
```

```python
max(x*x for x in range(10)) # does not allocate a list of 10 elements
```

```python
max((x*x for x in range(10))) # does not allocate a list of 10 elements
```

```python
x*x for x in range(10)
```

```python
(x*x for x in range(10))
```

```python

```
