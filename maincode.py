import math
print('What form are you starting with?')
form1=int(input("(1 = standard, 2 = factored, 3 = vertex)"))
if (form1==1):
  a=float(input("Enter a:"))
  b=float(input("Enter b:"))
  c=float(input("Enter c:"))
  print('Your original equation is:')
  print 'y =',a,'x^2 +',b,'x +',c
  print('')
  print('What form are you converting to?')
  form2=int(input("(2 = factored, 3 = vertex)"))
elif (form1==2):
  a=float(input("Enter a:"))
  m=float(input("Enter m:"))
  n=float(input("Enter n:"))
  print('Your original equation is:')
  print 'y =',a,'( x -',m,') ( x -',n,')'
  print('')
  print('What form are you converting to?')
  form2=int(input("(1 = standard, 3 = vertex)"))
elif (form1==3):
  a=float(input("Enter a:"))
  h=float(input("Enter h:"))
  k=float(input("Enter k:"))
  print('Your original equation is:')
  print 'y =',a,'( x -',h,') ^ 2 +',k
  print('')
  print('What form are you converting to?')
  form2=int(input("(1 = standard, 2 = factored)"))
if (form1==1) and (form2==2):
  print('Converting from standard to factored form')
  m = round((-b - (math.sqrt(b**2 - 4*a*c))) / (2*a), 4)
  n = round((-b + (math.sqrt(b**2 - 4*a*c))) / (2*a), 4)
  print('The converted equation is:')
  print 'y =',a,'( x -',m,') ( x -',n,')'
elif (form1==1) and (form2==3):
  print('Converting from standard to vertex form.')
  h = -b/(2*a)
  k = c - (b**2/(4*a))
  print('The converted equation is:')
  print 'y =',a,'( x -',h,') ^ 2 +',k
elif (form1==2) and (form2==1):
  print('Converting from factored to standard form.')
  b = - a*m - a*n
  c = a*m*n
  print('The converted equation is:')
  print 'y =',a,'x^2 +',b,'x +',c
elif (form1==2) and (form2==3):
  print('Converting from factored to vertex form.')
  b = - a*m - a*n
  c = a*m*n
  h = -b/(2*a)
  k = c - (b**2/(4*a))
  print('The converted equation is:')
  print 'y =',a,'( x -',h,') ^ 2 +',k
elif (form1==3) and (form2==1):
  print('Converting from vertex to standard form.')
  b = -2*a*h
  c = a*h**2 + k
  print('The converted equation is:')
  print 'y =',a,'x^2 +',b,'x +',c
elif (form1==3) and (form2==2):
  print('Converting from vertex to factored form.')
  b = -2*a*h
  c = a*h**2 + k
  m = round((-b - (math.sqrt(b**2 - 4*a*c))) / (2*a), 4)
  n = round((-b + (math.sqrt(b**2 - 4*a*c))) / (2*a), 4)
  print('The converted equation is:')
  print 'y =',a,'( x -',m,') ( x -',n,')'
