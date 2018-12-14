def type_ip(ip, masque):
  
  masque = int(masque)
  
  ip = ip.split(".")
  list_ip = ip
  if len(list_ip) !=4 :
    return "False"
    
  #boucle pour verifier si c'est des nombre
  i=0
  while i !=4 :
    if str(list_ip[i]).isdigit()==True :
      list_ip[i]=int(list_ip[i])
    else:
      return False
    i += 1
      
  #boucle pour verifier si la valeur est entre 255 et 0
  i=0
  while i !=4 :
    if 0<=list_ip[i]<=255:
      pass
    else:
      return False
    i += 1 
    
  if list_ip[0]==0:
    if list_ip[1]==0 and list_ip[2]==0 and list_ip[3]==0:
      return True
    else:
      return False


  if list_ip[0]  == 10:
    if masque >= 8:
      return "privateA"
    else:
      return "invalid"
      
  if list_ip[0] == 172 and list_ip[1] >= 16 and list_ip[1] <= 31:
    if masque >= 12:
      return "privateB"
    else:
      return "invalid"
      
  if list_ip[0] == 192 and list_ip[1] == 168:
    if masque >= 16:
      return "privateC"
    else:
      return "invalid" 
    


  if list_ip[0] >= 1 and list_ip[0] <= 126:
    return 'publicA'
    
  if list_ip[0] >= 128 and list_ip[0] <= 191 and list_ip[0] != 169 and list_ip[1] != 254:
    return 'publicB'
    
  if list_ip[0] >= 192 and list_ip[0] <= 223:
    return 'publicC'
    
  if list_ip[0] == 127:
    return 'localhost'
    
  if list_ip[0] == 169 and list_ip[1] == 254:
    return 'apipa'
  
  if list_ip[0] >= 224 and list_ip[0] <= 239:
    return "multicast"  
    
  if list_ip[0] >= 240 and list_ip[0] <= 255:
    return "experimental"
