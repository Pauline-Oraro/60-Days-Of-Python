# pip is a package manager for python packages or modules.

# A package contains all the files you need for a module. Modules are python code libraries you can include in your project.

# to check if pip is installed open cmd and type pip --version. If you have python 3.4 or later, pip is included by default.

# downloading a package is very easy. open cmd and tell pip to download the package you want. for example: pip install camelcase.

# once the package is installed it is ready to use. you can import the package in your code and use it.

import camelcase

c = camelcase.CamelCase()

text = "python is a fun and easy programming language to learn."

print(c.hump(text))

# to uninstall a package, open cmd and type pip uninstall package_name. for example: pip uninstall camelcase.

# use the list command to list all the packages installed in your system. open cmd and type pip list.

# to show details about a package, open cmd and type pip show package_name. for example: pip show camelcase.