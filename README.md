# LP and MIP examples in Python with Scipy and PuLP (CBC or GLPK)

### MacOS Setup

Requires Python3 and brew

```
# Install GLPK
brew install glpk
glpsol --version

# Create and activate virtual environment
python3 -m venv env && source env/bin/activate

# Install scipy and pulp
pip install -U scipy pulp
pulptest

# Run examples
python scipy-example1.py
python scipy-example2.py
python pulp-cbc-example1.py
python pulp-glpk-example1.py
python pulp-glpk-example2.py
```

### Other OS's

Same but use your packet manager for installing `glpk`:

Debian/Ubuntu

```
sudo apt install glpk glpk-utils
```

Fedora

```
sudo dnf install glpk-utils
```

...

doc: `https://realpython.com/linear-programming-python/`
