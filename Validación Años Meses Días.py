import datetime
meses = ('Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio','Agosto','Septiembre','Octubre','Noviembre','Diciembre')
año = int(input("Ingrese el año al que corresponde su busqueda: "))
while año < 2018 or año > 2021: 
  print("ERROR! El año que ingresó esta fuera de rango.")
  print("Por favor eliga un año entre 2018 y",datetime.date.today().year,":")
  año = int(input())
mes = int(input("Ingrese el mes al que corresponde su busqueda: "))
if año==datetime.date.today().year and mes > datetime.date.today().month:
  print("ERROR! El mes que ingresó esta fuera de rango.")
  print("Por favor eliga un mes entre 1 y",datetime.date.today().month,":")
  mes = int(input())
elif año!=datetime.date.today().year:
  while mes < 1 or mes > 12: 
    print("ERROR! El mes que ingresó esta fuera de rango.")
    print("Por favor eliga un mes entre 1 y 12")
    mes = int(input())
dia_inicio = int(input("Ingrese el día al que corresponde al inicio del rango de la busqueda: "))
if mes==datetime.date.today().month and dia_inicio > datetime.date.today().day - 1:
  print("ERROR! El día que ingresó esta fuera de rango.")
  print("Por favor eliga un día entre 1 y",datetime.date.today().day - 1,":")
  dia_inicio = int(input())
elif mes==2:
  while dia_inicio < 1 or dia_inicio > 28: 
    print("ERROR! El día que ingresó esta fuera de rango.")
    print("Por favor eliga un día entre 1 y 28")
    dia_inicio = int(input())
elif mes==4 or mes==6 or mes==9 or mes==11:
  while dia_inicio < 1 or dia_inicio > 30: 
    print("ERROR! El día que ingresó esta fuera de rango.")
    print("Por favor eliga un día entre 1 y 30")
    dia_inicio = int(input())
else:
  while dia_inicio < 1 or dia_inicio > 31: 
    print("ERROR! El día que ingresó esta fuera de rango.")
    print("Por favor eliga un día entre 1 y 31")
    dia_inicio = int(input())
dia_fin = int(input("Ingrese el día al que corresponde al final del rango de la busqueda: "))
while dia_fin < dia_inicio:
  print("ERROR! El día de fin es menor al día de inicio.")
  print("Por favor eliga un día entre ",dia_inicio,"y","31: ")
  dia_fin = int(input())
if mes==datetime.date.today().month and dia_fin > datetime.date.today().day - 1:
  print("ERROR! El día que ingresó esta fuera de rango.")
  print("Por favor eliga un día entre 1 y",datetime.date.today().day - 1,":")
  dia_fin = int(input())
elif mes==2:
  while dia_fin < 1 or dia_fin > 28: 
    print("ERROR! El día que ingresó esta fuera de rango.")
    print("Por favor eliga un día entre 1 y 28")
    dia_fin = int(input())
elif mes==4 or mes==6 or mes==9 or mes==11:
  while dia_fin < 1 or dia_fin > 30: 
    print("ERROR! El día que ingresó esta fuera de rango.")
    print("Por favor eliga un día entre 1 y 30")
    dia_fin = int(input())
else:
  while dia_fin < 1 or dia_fin > 31: 
    print("ERROR! El día que ingresó esta fuera de rango.")
    print("Por favor eliga un día entre 1 y 31")
    dia_fin = int(input())
mes = meses[mes-1]
