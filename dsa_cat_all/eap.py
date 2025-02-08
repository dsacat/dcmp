def fis(l, from_system=10, in_system=2, alf="0123456789ABCDEF", s=None, k=False):
  if type(alf) != list and type(alf) != str:
    raise ValueError("The alf input data must be a string or a list.")
  elif type(alf) == str:
    alf = list(alf)
  if type(s) != str and s != None:
    raise ValueError("The s input data must be of the string or None type.")
  if type(l) != int and type(l) != list and type(l) != str:
    raise ValueError("The input data type of the variable l must be a list with integers or an integer.")
  if type(in_system) != int and type(in_system) != list:
    raise ValueError("The input data type of the variable in_system must be a list with integers or an integer.")
  if type(from_system) != int and type(from_system) != list:
    raise ValueError("The input data type of the variable from_system must be a list with integers or an integer.")
  if type(l) == list:
    for i in l:
      if type(i) != int:
        raise ValueError("The input data type of the variable l must be a list with integers or an integer.")
  if type(in_system) == list:
    for i in in_system:
      if type(i) != int:
        raise ValueError("The input data type of the variable in_system must be a list with integers or an integer.")
  if type(from_system) == list:
    for i in from_system:
      if type(i) != int:
        raise ValueError("The input data type of the variable from_system must be a list with integers or an integer.")
  if type(in_system) != int:
    if len(in_system) != len(l):
      raise ValueError("the length of the input data of the in_system variable must be equal to the length of the input data of the l variable.")
  if type(from_system) != int:
    if len(from_system) != len(l):
      raise ValueError("the length of the input data of the from_system variable must be equal to the length of the input data of the l variable.")
  if type(l) == list:
    l = list(map(str, l))
  if type(l) == int:
    l = [str(l)]
  if type(l) == str:
    l = [l]
  if type(in_system) == int:
    in_system = [in_system]*len(l)
  if type(from_system) == int:
    from_system = [from_system]*len(l)
  l2 = []
  for i, i4 in zip(l, from_system):
    g = 0
    for i2, i3 in zip(list(reversed(i)), range(len(i))):
      try:
        g+=alf.index(i2)*(i4**i3)
      except:
        raise ValueError("The item in the l list is not in the alf list.")
    l2+=[g]
  if k == False:
    l = [""]*len(l2)
    for i, i2, i3 in zip(l2, in_system, range(len(l2))):
      m = i
      while m // i2 != 0:
        try:
          l[i3] = alf[m % i2] + l[i3]
        except:
          raise ValueError("The item in the l list is not in the alf list.")
        m = m // i2
      try:
        l[i3] = alf[m % i2] + l[i3]
      except:
        raise ValueError("The item in the l list is not in the alf list.")
  else:
    l = []*len(l2)
    for i, i2, i3 in zip(l2, in_system, range(len(l2))):
      m = i
      while m // i2 != 0:
        try:
          l[i3] = [alf[m % i2]] + l[i3]
        except:
          raise ValueError("The item in the l list is not in the alf list.")
        m = m // i2
      try:
        l[i3] = [alf[m % i2]] + l[i3]
      except:
        raise ValueError("The item in the l list is not in the alf list.")
  if s == None:
    return l
  else:
    if type(s) == str:
      return s.join(l)
    else:
      raise ValueError("The s input data must be a string.")
