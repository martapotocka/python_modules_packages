# # Importowanie przez podanie ścieżki do modułu
# import my_package.module_in_package
# my_package.module_in_package.function_four()


# # Użycie as aby urpościć ścieżkę do modułu
# import my_package.module_in_package as my_module
# my_module.function_four()


# # Importowanie modułu do przestrzeni nazw
# from my_package import module_in_package
# module_in_package.function_four()

# ## Importowanie konkretnej funkcji z pakietu
# from my_package.module_in_package import function_four
# function_four()


# importy w __init__.py

# # Można tak zrobić jeśli zrobimy import w __init__.py
# import my_package
# my_package.function_four()

# from my_package import *
# module_in_package.function_four()
