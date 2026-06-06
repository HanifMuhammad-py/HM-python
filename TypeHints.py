print(f'{"Type Hints":^80}')
print(f'{"="*40:^80}\n')

# def type_Hints(arguments: int) -> int:
#              ^^^^^^^^^^^       ^^^^
#              tipe parameter    tipe return value

# arguments: int → bilang ke Python: "parameter ini harusnya integer"
# -> int → bilang ke Python: "fungsi ini return intege

'''int'''
def type_Hints_int (arguments:int) -> int:
    result = arguments**2 
    return result

output = type_Hints_int (2)
print(f'Output INT = {output}')


import string
'''str'''
def type_Hints_str (arguments:string) -> str:
    print(arguments)

type_Hints_str(f'Output STR = {"string"}')