
def bubbleSort(array):
  for i in range(len(array)):
    for j in range(0, len(array) - i - 1):
      if array[j] > array[j + 1]:
        temp = array[j]
        array[j] = array[j+1]
        array[j+1] = temp
        
  return array
    
def combinar(lista1,lista2):
    listanueva = lista1+lista2
    return bubbleSort(listanueva)
    
lista1 = [45,7,54,5,6,43,7,45,3]
lista2 = [1,0,5,4,33,42,12]


print(combinar(bubbleSort(lista1),bubbleSort(lista2)))