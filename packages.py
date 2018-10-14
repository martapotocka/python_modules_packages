# # Importowanie przez podanie ścieżki do modułu
# import my_package.module_in_package
# my_package.module_in_package.function_four()


# # Użycie as aby urpościć ścieżkę do modułu
# import my_package.module_in_package as module1
# module1.function_four()


# # Importowanie modułu do przestrzeni nazw
# from my_package import module_in_package
# module_in_package.function_four()

# ## Importowanie konkretnej funkcji z pakietu
# from my_package.module_in_package import function_four
# function_four()

# import my_package
# my_package.function_four()

from my_package import *
module_in_package.function_four()
