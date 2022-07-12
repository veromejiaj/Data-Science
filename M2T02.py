#!/usr/bin/env python
# coding: utf-8

# #ejercicio 1

# In[1]:


print("Ingrese la nota")


# In[2]:


Nota=input()


# In[3]:


Nota=int(Nota)
if Nota <5:
    y=("Suspendido")
elif Nota>5 and Nota<7:
    y=("Aprovado")
elif Nota>7 and Nota<9:
    y=("Notable")
elif Nota > 9:
    y=("Excelente")
print (Nota, "corresponde a" ,y)  


# #ejercicio2
# 

# In[8]:


print("ingrese el primer numero")
Num1=float(input())
print("ingrese el segundo numero")
Num2=float(input())


# In[9]:


if Num1 > Num2:
    print("El primer numero es más grande que el segundo")
elif Num2 > Num1:
    print("El segundo numero es más grande que el primero")  
else:
    print("Son iguales")
    


# #ejercicio 3

# In[1]:


print("Cual es tu nombre?")
Nombre=input()
print("Dime un numero")
Numero=int(input())


# In[2]:


x=range(Numero)
for n in x:
    print(Nombre)


# #ejercicio4

# In[3]:


lista =[25, 50, 4, 6, 6, 4, 50, 25]
idx=len(lista)-1
newlist=[]
while (idx >= 0):
    newlist.append(lista[idx])
    idx = idx - 1
    
if lista == newlist:
    print ("es simetrica y tiene ", (len(lista)) ," elementos")
else:
    print ("no es simetrica")
 


# #ejercicio5

# In[6]:


lista =[25, 50, 2, 6, 8, 7, 6, 25]
ind= len(lista)
nueva=[]
indice=0
while indice<ind:
    item=lista[indice]
    if item==indice:
        nueva.append(indice)
    indice= indice + 1    
    
print (nueva, "estos numeros coinciden en su posicion")

