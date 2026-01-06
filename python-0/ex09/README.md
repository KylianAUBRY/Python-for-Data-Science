# ft_package

A sample test package.

This package contains a simple function `count_in_list(lst, item)` that counts how many times an item appears in a list.

## Installation

After building the package, you can install it via pip:

```bash
# Build the package
python3 setup.py sdist bdist_wheel

# Install the package
pip install ./dist/ft_package-0.0.1.tar.gz
# or
pip install ./dist/ft_package-0.0.1-py3-none-any.whl


pip list
pip show -v ft_package
# to see the package or its characteristics