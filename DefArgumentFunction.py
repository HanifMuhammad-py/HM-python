print ("Def-Argument Function\n")

# def <variable>(Argument) :
def test(angka_1, angka_2) :
    hasil = angka_1 + angka_2
    print(f'{angka_1} + {angka_2} = {hasil}')
pass

test(10,10)
test(5,3)
test(-3,4)

def data_programmer(data) :
    data[2] = "JS" 
    data_copy = data.copy()
    for i in data_copy :
        print(f'si raja {i}')        

data_X = ["python", "C++", "JavaScript"]

data_programmer(data_X)



