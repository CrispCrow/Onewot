<h1 align="center">Onewot</h1>
<p>
An opinionated, static typed WotBlitz API wrapper for Python3.

Python >=3.8 are currently supported.

Documentation: [View Here](https://onewot.readthedocs.io/en/latest/)
</p>

## Installation
Install Onewot from PyPi with the following command:

```bash
python -m pip install -U onewot
# Windows users may need to use this instead...
py -3 -m pip install -U onewot
```

----

## Updating

```bash
pip install --upgrade onewot
```

----

## Start up client

```py
import onewot

client = onewot.WOTBClient(application='...')
```

----

## Example

```py
import onewot

client = onewot.WOTBClient(application='...', language=onewot.Language.ENGLISH)

print(client.fetch_user(152870490))
```

----

## Python optimization flags
CPython provides two optimisation flags that remove internal safety checks that are useful for development, and change other internal settings in the interpreter.

- python main.py - no optimisation - this is the default.
- python -O main.py - first level optimisation - features such as internal
    assertions will be disabled.
- python -OO main.py - second level optimisation - more features (**including
    all docstrings**) will be removed from the loaded code at runtime.

**A minimum of first level of optimizations** is recommended when running applications in a production environment.