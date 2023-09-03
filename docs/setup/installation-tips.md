# Installation Tips

Installing the Donkey Car software is a complex process.  It typically takes
about six hours to add the required tools and Python libraries to
a raw NVIDIA or Raspberry Pi OS image.

Here are a few tips.

## Use the -H mode when installing software

We should always use the HOME environment variables when using sudo:

```sh
sudo -H pip install package_name
```

In this command, sudo -H is used to ensure that the home environment variable is set to the home directory of the target user (root in this case), which can sometimes avoid permissions issues that arise when sudo retains your normal user's home directory environment variable. Essentially, the -H option makes sure that the operation is as clean as possible from an environment perspective, which can be important when installing software that might write configuration files or data into the user's home directory.

## Remember to Use Python3 and Pip3

Sometimes older Python2 tools get mixed up with the current Python 3 tools.  By adding the "3" suffix to your commands you can guarantee that that your path will pick up the right version of Python tools.

# When to Use `python3` and `pip3` Over `python` and `pip` in UNIX Shell

## Python Version

1. **Python 2 vs Python 3**: Python 2 and Python 3 are two different versions of the Python programming language. Python 2 is no longer maintained as of January 1, 2020, but it still exists on some systems for legacy reasons. `python3` explicitly runs Python 3.x, whereas `python` might run either Python 2.x or Python 3.x depending on the system configuration.

### System Configuration

1. **Multiple Python Installations**: On some systems, you may have both Python 2 and Python 3 installed. In such cases, `python` usually refers to Python 2 and `python3` to Python 3. Similarly, `pip` might point to the package manager for Python 2, and `pip3` will point to Python 3. Always use `python3` and `pip3` to ensure that you're working with Python 3.x.

2. **Aliases**: Some systems alias `python` to `python3`. This is common in more recent Linux distributions. On such systems, it may not matter if you use `python` or `python3`. However, using `python3` is more explicit and can avoid ambiguity.

### Script Compatibility

1. **Version-Specific Code**: If you're running or writing code that is specific to Python 3, use `python3`. Similarly, if you're installing packages that are intended for use with Python 3, use `pip3`.

2. **Portability**: If you're writing a script that you plan to share with others, it's safer to specify `python3` if your code is not compatible with Python 2.

### Virtual Environments

1. **Virtualenv**: If you're using a Python virtual environment, the `python` and `pip` commands will point to the versions associated with the active environment, regardless of whether it's Python 2 or 3. So, within a Python 3 virtual environment, `python` and `pip` will be equivalent to `python3` and `pip3`.

### Best Practices

1. **Explicit is Better**: If you're in doubt, being explicit is usually better. Using `python3` and `pip3` makes it clear that you're using Python 3.

2. **Check Version**: If ever in doubt, you can always check which version you're running by using `python --version` or `python3 --version` and `pip --version` or `pip3 --version`.

---

In summary, if you want to make sure you are using Python 3 and its associated package manager, use `python3` and `pip3`.
