from timeit import timeit

code1 = """
def calculate_xfactor(age):
    if age <= 0:
        # Lze vyvolat vlastní výjimku s využitím built-in exceptions (viz internet)
        # Riziko zpomalení kódu
        raise ValueError("Age cannot be 0 or less 0")
    return 10 / age


try:
    xfactor = calculate_xfactor(-1)
    print(f"Xfactor: {xfactor}")
except ValueError as error:
    pass
"""

code2 = """
def calculate_xfactor(age):
    if age <= 0:
        return None
    return 10 / age


xfactor = calculate_xfactor(-1)
if xfactor == None:
    pass
"""
# Zjištění efektivity kódu - čas provedení 10000x
print("First: ", timeit(code1, number=10000))
print("Second: ", timeit(code2, number=10000))
