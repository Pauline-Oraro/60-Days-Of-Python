# Python PIP

**PIP** is the package manager for Python. It allows you to install, manage, and remove Python packages — which are libraries of reusable code you can include in your projects.

> **Note:** If you have Python 3.4 or later, PIP is included by default. To verify, open your terminal or command prompt and run:
> ```
> pip --version
> ```

---

## 1. Installing a Package

Open your terminal or command prompt and use the `pip install` command followed by the package name.

```bash
pip install camelcase
```

---

## 2. Using an Installed Package

Once installed, import the package in your code and use it.

```python
import camelcase

c = camelcase.CamelCase()

text = "python is a fun and easy programming language to learn."
print(c.hump(text))
# Python Is A Fun And Easy Programming Language To Learn.
```

---

## 3. Uninstalling a Package

Use `pip uninstall` followed by the package name to remove it.

```bash
pip uninstall camelcase
```

---

## 4. Listing Installed Packages

Use `pip list` to see all packages currently installed on your system.

```bash
pip list
```

Example output:

```
Package    Version
---------- -------
camelcase  0.2
pip        23.0
setuptools 65.5
```

---

## 5. Showing Package Details

Use `pip show` to display detailed information about a specific package.

```bash
pip show camelcase
```

Example output:

```
Name: camelcase
Version: 0.2
Summary: Converts a string to Camel Case
Home-page: https://github.com/...
Author: ...
Location: /usr/local/lib/python3.x/site-packages
```

---

## Quick Reference

| Command | Description |
|---------|-------------|
| `pip --version` | Check if PIP is installed and see its version |
| `pip install package_name` | Install a package |
| `pip uninstall package_name` | Uninstall a package |
| `pip list` | List all installed packages |
| `pip show package_name` | Show details about a specific package |
