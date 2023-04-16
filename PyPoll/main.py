import csv

# ABRIR EL DOCUMENTO Y GUARDARLO EN UNA VARIABLE.
file = open('/Users/fernandoescamilla/python-challenge/PyPoll/Resources/election_data.csv')

# LEER EL DOCUMENTO.
csv_reader = csv.reader(file)

# OBTENER LOS "HEADER" DEL DOCUMENTO.
header = []
header = next(csv_reader)


total_votes = 0 # Variable para guardar el total de votos.
total_candidates = [] # Array para guardar la lista de candidatos (repetidos).
unique_candidates = [] # Array para guardar la lista de candidatos (sin repetir).
total_votes_per_candidate = [] # Array para guardar el total de votos por candidato.
pct_per_candidate = [] # Array para guardar los porcentajes de cada candidato.


for row in csv_reader:
    total_votes += 1 # Contabilizando el total de votos.
    
    total_candidates.append(row[2]) # Agregando candidato (repetido).

    if row[2] not in unique_candidates:
        unique_candidates.append(row[2]) # Agregando candidato único (sin repetir).
     # FIN IF.
# FIN FOR.


for e in range(0, len(unique_candidates)):
     temp_total_votes = 0
     
     for i in range(0, int(total_votes)):
          if unique_candidates[e] == total_candidates[i]:
               temp_total_votes += 1 # Contabilizando el total de votos por candidato.
          # FIN IF
     # FIN FOR.

     total_votes_per_candidate.append(temp_total_votes) # Agregando el total de votos de cada candidato.
     temp_pct = (temp_total_votes * 100) / total_votes # Calculando el porcentaje por candidato.
     pct_per_candidate.append(temp_pct) # Agregando el pct de cada candidato.
# FIN FOR.


votacion_mas_alta = total_votes_per_candidate[0]
condidato_ganador = unique_candidates[0]
for e in range(1, len(unique_candidates)):
     if total_votes_per_candidate[e] > votacion_mas_alta:
          condidato_ganador = unique_candidates[e] # Obteniendo el candidato ganador (con más votos).
     # FIN IF
# FIN FOR


# MOSTRAR RESULTADOS EN CONSOLA.
print('')
print('')


print('Election Results')
print('----------------------------------------------------')
print('Total Votes: ' + str(total_votes))
print('----------------------------------------------------')

for e in range(0, len(unique_candidates)):
     print(unique_candidates[e] + ': {:.3f}'.format(pct_per_candidate[e]) + '% (' + str(total_votes_per_candidate[e]) + ')')
# FIN FOR.

print('----------------------------------------------------')
print('Winner: ' + condidato_ganador)


# CREANDO ARCHIVO TXT Y ESCRIBIENDO LOS RESULTADOS.
py_poll_file = open('/Users/fernandoescamilla/python-challenge/PyPoll/analysis/py_poll_file.txt', 'w')
py_poll_file.write('Election Results\n')
py_poll_file.write('----------------------------------------------------\n')
py_poll_file.write('Total Votes: ' + str(total_votes) + '\n')
py_poll_file.write('----------------------------------------------------\n')

for e in range(0, len(unique_candidates)):
     py_poll_file.write(unique_candidates[e] + ': {:.3f}'.format(pct_per_candidate[e]) + '% (' + str(total_votes_per_candidate[e]) + ')\n')
# FIN FOR.

py_poll_file.write('----------------------------------------------------\n')
py_poll_file.write('Winner: ' + condidato_ganador)
py_poll_file.close()


print('')
print('')