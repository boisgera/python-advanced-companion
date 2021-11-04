# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.13.0
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

l = [(1, 2), (2, 2), (3, 2)]

str(l)

repr(l)

s = repr(l)

eval(s)

type(eval(s))

eval(repr(s)) == s


