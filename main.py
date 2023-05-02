class Auto:
  def __init__(self,marca,precio):
    self.marca = marca
    self.precio = precio

  def __repr__(self):
    return f'Auto({self.marca},{self.precio})'

  def __str__(self):
    return f'Auto marca {self.marca}, tiene un precio de ${self.precio}.'
    
 a1 = Auto('Ford',35000)
 
import os 
import pickle
flag = os.path.exists('vehiculo.bin')
if flag:
  f = open('vehiculo.bin', 'wb')
  pickle.dump(a1,f)
  f.close()
else:
  f = open('vehiculo.bin','rb')
  getAuto = pickle.load(f)
  f.close()
  print(getAuto.marca)
  
