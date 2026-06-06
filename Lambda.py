print(f'{"LAMBDA":^80}')
print(f'{"="*40:^80}\n')

'''W/ *args'''
def function (data) :
    output = data*5
    
    return output

result =function(2)
print(f'hasil dari *args = {result}')

'''w/ lambda function'''
# variable = lambda <argument> : <arguments> <expression>
output = lambda data : data*5
print(f'hasil dari lambda = {output(2)}')

output = lambda data, pangkat : data**pangkat
print(f'hasil dari lambda * perpangkatan = {output(2, 10)}')

''''lambda for short list'''
# Basic list (urut)
data_list  = ["Y", "A", "B", "Z", "X", "C"]
data_list.sort()
print(data_list) 

# Basic list (urut dari akhir)
# <variable>.sort(reverse=True)
data_list  = ["Y", "A", "B", "Z", "X", "C"]
data_list.sort(reverse=True)
print(data_list) 

# List berdasarkan panjang/banyak karakter (def + len)
def function (data_list) :
    return len(data_list)

        # import "key"
data_list  = ["ayam betutu terbang terbaik di dunia", "ayam", "ayam betutu", "ay", "ayam betutu terbang"]
data_list.sort(key=len)
print(data_list)

# short list w/ lambda
data_list  = ["ayam betutu terbang terbaik di dunia", "ayam", "ayam betutu", "ay", "ayam betutu terbang"]
data_list.sort(key=lambda list:len(list))





