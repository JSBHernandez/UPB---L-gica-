def lenUltPalabra(frase):
   if len(frase)==0:
       return 0
   cant=0
   for n in range(len(frase)):
       if frase[n]!=' ':
           cant+=1
       else:
           if n<len(frase)-1 and frase[n+1]!=' ':
               cant=0
   return cant