def fis(l, from_system=10, in_system=2, s=None, alf="0123456789ABCDEF"):
  if type(alf) != str:
    raise ValueError("The alf input data must be of the string type.")
  if type(s) != str and s != None:
    raise ValueError("The s input data must be of the string or None type.")
  if type(l) != int and type(l) != list:
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
    for i in from_list:
      if type(i) != int:
        raise ValueError("The input data type of the variable from_system must be a list with integers or an integer.")
  if type(in_system) != int:
    if len(in_system) != len(l):
      raise ValueError("the length of the input data of the in_system variable must be equal to the length of the input data of the l variable.")
  if type(from_system) != int:
    if len(from_system) != len(l):
      raise ValueError("the length of the input data of the from_system variable must be equal to the length of the input data of the l variable.")
  if type(l)
