# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.13.0
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %% [markdown]
# # Flux de contrôle et exceptions

# %%
for i in range(10):
    print(i)
    if i == 5:
        break

# %%
for i in range(10):
    print("*", i)
    if (i % 2): # i odd
        continue # skip the rest of this indented block, but keep iterating
    else:
        print(">")

# %%
for i in range(5):
    print(i)
else:
    print("else")

# %%
for i in range(5):
    print(i)
    if i == 4:
        break
else:
    print("else")


# %%
def f(x):
    pass


# %%
f(1, 2)


# %%
def g():
    a = 1 + 1
    f(1, a)
    print("jdkjdksjdksjds")

def h():
    z = g()
    print(z)


# %%
h()

# %%
try:
    z = f(1, 2)
except TypeError as error:
    print("error detected:", error)

# %%
raise TypeError("f() takes 1 positional argument but 2 were given")


# %%
def f(n):
    if n < 0:
        # message defined by a f-string
        message = f"{n} is negative" # str(n) + " is negative"
        raise ValueError(message)
    return n*n


# %%
f(5)

# %%
f(-5)

# %% [markdown]
# # Iteration

# %%
for i in [1, 2, 3]:
    print(i)

# %%
it = iter([1, 2, 3]) # it is an iterator
it

# %%
next(it)

# %%
next(it)

# %%
next(it)

# %%
next(it)

# %%
it = iter([1, 2, 3]) # iterable: can produce iterators with iter(iterable)
it # iterator: next(it) makes sense

# %%
l = [1, 2, 3]

it1 = iter(l)
print(next(it1))
print(next(it1))

it2 = iter(l)
print(next(it2))
print(next(it2))

# %%
l = [1, 2, 3]

it1 = iter(l)
it2 = iter(it1) # not very useful ...

print(it1 is it2)

print(next(it1))
print(next(it1))

print(next(it2))
print(next(it2))


# %%
l = list(range(100))
for i in l:
    print(i)
    l.pop(0) # modification during iteration => undefined

# %%
l = list(range(100))
for i in l[:]: # safer to iterate on a copy of the list
    print(i)
    l.pop(0)

# %% [markdown]
# Iterables :
#
#   - lists
#   
#   - tuples
#   
#   - dicts
#   
#     - dict keys
#     
#     - dict values
#     
#     - dict items
#   
#   - sets
#     
#   - strings
#   
#   - files
#   
#   - range(100)
#   
#   - enumerate(...)

# %%
d = {"a": 1, "b": 2}

# %%
d.keys()

# %%
iter(d.keys())

# %%
for c in "Hello world!":
    print(c)

# %%
enumerate([6, 7, 8])

# %%
for i, number in enumerate([6, 7, 8]):
    print(i, number)

# %%
iter(enumerate([6, 7, 8]))

# %%
l1 = [1, 2, 3]
l2 = [4, 8, 16]
for item in zip(l1, l2): # simultaneous iteration on l1 and l2
    print(item)

# %%
help(list)

# %%
list([1, 2, 3])

# %%
list({1: "a", 2: "b", 3: "c"})

# %%
list("abc")

# %%
help(max)

# %%
max(1, 2, 3)

# %%
max([1, 2, 3])

# %%
max("Hello world!")

# %% [markdown]
# # Compréhension

# %%
l = [1, 2, 3]
squares_l = []
for i in l:
    square = i * i
    squares_l.append(square)
squares_l

# %%
[i*i for i in l]

# %%
l = range(10)
[i*i for i in l if i*i > 20] # "filter in" elements

# %%
type([i*i for i in l if i*i > 20])

# %%
{i*i for i in l if i*i > 20}

# %%
{i: str(i) for i in range(100)}

# %% [markdown]
# ### generator expressions

# %%
max([x*x for x in range(10)])

# %%
max(x*x for x in range(10)) # does not allocate a list of 10 elements

# %%
max((x*x for x in range(10))) # does not allocate a list of 10 elements

# %%
x*x for x in range(10)

# %%
(x*x for x in range(10))

# %%
