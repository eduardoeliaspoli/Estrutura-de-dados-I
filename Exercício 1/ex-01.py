# Implementação do BubbleSort
def bubbleSort(v):
    i = 0
    v_len = len(v) - 1
    while i < v_len:
        j = 0
        while j < v_len - i:
            if v[j] > v[j+1]:
                tmp = v[j]
                v[j] = v[j + 1]
                v[j+1] = tmp
            j+=1
        i+=1

vect = [3,90,65,71,-2,22,30]
bubbleSort(vect)
print(vect)

# Implementação do QuickSort
def particiona(v, a, b):
    x = v[a]
    while a < b:
        while v[a] < x:
            a += 1
        while v[b] > x:
            b -= 1
        if a <= b:
            troca(v, a, b)
    return a


def troca (v,a,b):
   temp = v[a]
   v[a] = v[b]
   v[b] = temp

def quickSort(v,a,b):
   if a < b:
       p = particiona(v,a,b)
       quickSort(v,a,p - 1)
       quickSort(v,p + 1,b)


vect = [10, 7, 8, 9, 1, 5]
n = len(vect)
quickSort(vect, 0, n - 1)
print(vect)



def merge_sort(A):
    if len(A) <= 1:
        return A
    
    
    meio = len(A) // 2
    esquerda = merge_sort(A[:meio])
    direita = merge_sort(A[meio:])
    
    
    return merge(esquerda, direita)

def merge(esquerda, direita):
    resultado = []
    i, j = 0, 0
    while i < len(esquerda) and j < len(direita):
        if esquerda[i] <= direita[j]:
            resultado.append(esquerda[i])
            i += 1
        else:
            resultado.append(direita[j])
            j += 1
    resultado += esquerda[i:]
    resultado += direita[j:]
    return resultado

b = [5,75,60,25,30,1,50,10]
b = merge_sort(b)
print(b)