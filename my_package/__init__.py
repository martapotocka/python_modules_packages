# from .module_in_package import function_four
# from my_package.module_in_package import function_four

# Python3 is looking for module name in the root directory
# (the directory we are in while running the script)
# in this case it's 'Python_test' directory
# Thus to provide the module name we have to implicit provide the
# path using package.module notation
# or use . instead of the package name

__all__ = ['module_in_package']
