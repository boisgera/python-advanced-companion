---
title: Bibliothèques
---

Intro
--------------------------------------------------------------------------------

Bibliothèque standard, PyPi.

(Système de) fichiers
--------------------------------------------------------------------------------

`pathlib` plus ce qui peux manquer et qui est présent dans les autres libs
(`shutil`, etc.)

`gzip` ?

OS, CLI, Terminal, SSH
--------------------------------------------------------------------------------

`time`, `sys`

`sys.argv` -> `argparse` -> `click` ou `typer`.

`subprocess` -> `plumbum`

`paramiko` ?

`e-mail` ? Study <https://realpython.com/python-send-email/>

Web
--------------------------------------------------------------------------------

### `webbrowser`

``` python
>>> import webbrowser
>>> webbrowser.open("https://www.python.org")
```

-----

  - `http.server`

  - `urllib` -> `requests`

  - framework : `flask`, `django`

Formats de sérialization
--------------------------------------------------------------------------------

  - `json`

  - `xml` (/html) ; `etree` et `lxml`

  - `pyyaml` et `strictyaml`

GUI
--------------------------------------------------------------------------------

  - `pyqt`, `pygtk`, etc.?

FFI
--------------------------------------------------------------------------------

  - `ctypes`, `cffi`

  - `cython`.