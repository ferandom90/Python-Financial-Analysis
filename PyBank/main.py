import csv

# ABRIR EL DOCUMENTO Y GUARDARLO EN UNA VARIABLE.
file = open('/Users/fernandoescamilla/python-challenge/PyBank/Resources/budget_data.csv')

# LEER EL DOCUMENTO.
csv_reader = csv.reader(file)

# OBTENER LOS "HEADER" DEL DOCUMENTO.
header = []
header = next(csv_reader)


periods = [] # Obtener los años, solo los años (sin repetir), de la columna "Date".
dates = [] # Obtener todas las fechas de la columna "Date".
amounts = [] # Obtener todos los montos de la columna "Profit/Losses".
row_counter = 0
total_amount = 0


# RECORRER TODAS LAS LÍNEAS DEL DOCUMENTO (OMITIENDO LOS "HEADER").
for row in csv_reader:
    row  
    row_counter += 1 # Obteniendo los meses totales.
    #row_counter = row_counter + 1

    # arr = [   0  ,    1    ]
    # row = [Jan-10, 10888888]
    # row[0] -> Obtener la fecha
    # row[1] -> Obtener el monto.

    total_amount += int(row[1]) # Obteniendo el monto total.

    date = row[0][-2:] # Obteniendo el año, solo el año.
    # date = 10
    # date = 11

    if date not in periods:
        # []
        periods.append(date) # Agregando el año sin repetir.
        # periods = [10]
        # perdios = [10, 11]
        # [10, 11, 12, 13, 14, 15, 16]
    # FIN IF

    dates.append(row[0]) # Agregando las fechas (mes-año).
    # dates [Jan-10, feb-10,...]

    amounts.append(row[1]) # Agregando los montos.
    # amounts = [1088888, 3249999, 23422,...]
# FIN FOR

# OBTENER EL PORCENTAJE:
avg = total_amount / row_counter


# OBTENER  EL MONTO y DATE MÁS ALTOS:
highestDate = dates[0] # highestDate = Jan-10
highestAmount = amounts[0] # highestAmount = 1088888
for e in range(1, len(amounts)):
    # e = 1
    # e = 86
    
    #       1'000,000  >  3'000,000
    if int(amounts[e]) > int(highestAmount):
        highestDate = dates[e]
        highestAmount = amounts[e]


# OBTENER EL MONTO Y DATE MÁS BAJO:
lowestDate = dates[0]
lowestAmount = amounts[0]
for e in range(1, len(amounts)):
    # e = 1
    # e = 86

    if int(amounts[e]) < int(lowestAmount):
        lowestDate = dates[e]
        lowestAmount = amounts[e]



print('')
print('')
print('Financial Analysis')
print('----------------------------------------------------')
print('Total Months: ' + str(row_counter))
print('Total: $' + str(total_amount))
print('Averange Change: $' + str(avg))
print('Greatest Increase in Profits: ' + highestDate.capitalize() + ' ($' + highestAmount + ')')
print('Greatest Decrease in Profits: ' + lowestDate.capitalize() + ' ($' + lowestAmount + ')')
#print('----------------------------------------------------')


# CREANDO ARCHIVO TXT Y ESCRIBIENDO LOS RESULTADOS.
py_bank_file = open('/Users/fernandoescamilla/python-challenge/PyBank/analysis/py_bank_file.txt', 'w')
py_bank_file.write('Financial Analysis\n')
py_bank_file.write('----------------------------------------------------\n')
py_bank_file.write('Total Months: ' + str(row_counter) + '\n')
py_bank_file.write('Total: $' + str(total_amount) + '\n')
py_bank_file.write('Averange Change: $\n')
py_bank_file.write('Greatest Increase in Profits: ' + highestDate.capitalize() + ' ($' + highestAmount + ')\n')
py_bank_file.write('Greatest Decrease in Profits: ' + lowestDate.capitalize() + ' ($' + lowestAmount + ')\n')
py_bank_file.close()
#print('¡ARCHIVO TXT CREADO!')
print('')
print('')