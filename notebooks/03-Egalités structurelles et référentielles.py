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

# %%
r = l = ["bold"]

# %%
l.append("large")

# %%
r is l

# %%
r == l

# %%
r

# %%
l

# %%
id(r)

# %%
id(l)

# %%
id(l) == id(r) # equiv. to l is r.

# %% [markdown]
# -------

# %%
r = l = ["bold"]

# %%
l = l + ["large"]

# %%
r is l 

# %%
r == l

# %% [markdown]
# -----

# %%
l = ["large"]

# %%
r = ["large"]

# %%
r is l

# %%
r == l

# %%
