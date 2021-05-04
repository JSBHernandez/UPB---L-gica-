def validarID(id):
   cant=0
   while id!=0:
       cant+=1
       id//=10
   return cant>4 or cant<11