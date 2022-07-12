#!/usr/bin/env python
# coding: utf-8

# #EJERCICIO1

# In[4]:


T1=["ener","febrero","marzo"]
T2=["abril","mayo","junio"]
T3=["julio","agosto","septiembre"]
T4=["octubre","noviembre","diciembre"]

Anual=T1+T2+T3+T4
print(Anual)


# #EJERCICIO2

# In[8]:


print(Anual[1])


# In[10]:


print(Anual[:3])


# In[11]:


print(Anual[8:10])


# #EJERCICIO3

# In[41]:


Numeros=[5,8,10,6,8,3,2,1,5,7,2,6,4,8,9,3,4,0]
len(Numeros)
x=Numeros.count(3)
y=Numeros.count(4)
z=max(Numeros)
w=min(Numeros)
m=(sorted(Numeros))
n=(m[:3])
print("hay", len(Numeros),"numeros")
print("el numero 3 aparece",x, "veces")
print("el numero 3 y 4 aparecen",(x+y), "veces")
print("el valor maximo es el",z)
print("los valores mas pequeños son",n)
print("el valor maximo es", z, "y el minimo es", w)


# #EJERCICIO4

# In[4]:


compra = { "Pomes" : {"Qty": 5, "€": 0.42 }, "Peres" : {"Qty": 3, "€": 0.66} }
compra ["maduixa"]= {
    "Qty": 20, 
    "€": 0.05 
}
x=compra.get("Peres")
y=x.get("Qty")
z=x.get("€")
print(compra)
print("Las peras han costado", (y*z))


# In[5]:


a=compra.get("Pomes")
b=a.get("Qty")
c=a.get("€")
d=compra.get("maduixa")
e=d.get("Qty")
f=d.get("€")


# In[6]:


print("hemos comprado", y+b+e,"frutas")


# In[9]:


frutas=list(compra.keys())


# In[10]:


precios=[c,z,f]
maximo=max(precios)
indice=precios.index(maximo)
print ("la fruta mas cara han sido las ", frutas[indice])


# In[ ]:




