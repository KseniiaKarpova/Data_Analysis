
import numpy as np
import pandas as pd
import random
import csv
import quantecon as qe
import numpy as np
import pandas as pd
# k-means проверить разделит ли на кластеры (4)
#-------------- инициализация --------------------
N=100

data=list(range(4))

print((data))
tv = [[0.25, 0.25, 0.25, 0.25],
      [1/3,   1/3,  1/3,  0],
      [0.5,   0.5,   0,   0],
      [0.5,   0,     0,   0.5]]

tn = [[0.5,  0,     0,    0.5],
      [0,    0,     0.5,  0.5],
      [0,    1/3,   1/3,  1/3],
      [0.25, 0.25, 0.25, 0.25]]

bp =  [[0,      0,    0.5,   0.5],
      [0,      0,     0.5,   0.5],
      [0.5,    0.5,   0,    0],
      [0.5,    0.5,   0,    0]]

bl =  [[0.5,    0.5, 0,    0],
      [0.5,    0.5,  0,    0],
      [0,      0,    0.5,   0.5],
      [0,      0,    0.5,   0.5]]



def generate_sequance(data, len): # data- массив элементов, из которого генерируется последовательность , len - длина последовательности
     list = []
     for i in range(len):
          list.append(random.choice(data))
     return list


def generate_vector_of_probabilities(lenData, lenMAX):
     l = list(map(lambda x: random.randint(0,lenMAX), range(lenData)))
     summ = sum(l)
     return  list(map(lambda x: (l[x]/summ), range(lenData)))
#print(generate_vector_of_probabilities(len(data), 10))



''' ЗАПИСЬ В CSW  файл: '''
TOP = [['sequance', 'matrix']] #'w'
for i in list(map(lambda x: 'a%i'%x , range(1,N+1))):
    TOP[0].append(i)
nameFile = 'data.csv'

topSeq = [['num', 'sequance', 'probabilities']]
seqFile = 'sequance.csv'
def write_to_csw(data, nameFile, type='a'):
    File = open(nameFile, type)
    with File:
        writer = csv.writer(File)
        writer.writerows(data)

write_to_csw(TOP, nameFile, 'w')
write_to_csw(topSeq, seqFile, 'w')

#--------------- main ------------------
def run(p, name, sequence, num, vector_of_probabilities):

    data_of_new_seq=[num, name]
    #sequence = generate_sequance(data, N)
    #print([n,' '.join(sequence)])
    #vector_of_probabilities =generate_vector_of_probabilities(len(data), N)
    write_to_csw([[num, ''.join(str(x) for x in sequence), '-'.join(str(x) for x in vector_of_probabilities)]], seqFile)


    matrix_of_probabilities=[vector_of_probabilities]
    for i in sequence[1:]:
         new=[0]*len(data)
         for j in range(len(data)):
            #print(matrix_of_probabilities)
            new[data.index(i)]+=matrix_of_probabilities[-1][j]*p[j][data.index(i)]
         matrix_of_probabilities.append(new)
         data_of_new_seq.append(sum(matrix_of_probabilities[-1]))
    write_to_csw([data_of_new_seq], nameFile)


     #print(matrix_of_probabilities)
     #print('probabiliti = ',sum(matrix_of_probabilities[-1]))




m1 = [tv, tn, bl, bp]
m2 = ['tv', 'tn', 'bl', 'bp']
for j in range(N):
    #sequence = generate_sequance(data, N)
    vector_of_probabilities = generate_vector_of_probabilities(len(data), N)
    for i in range(4):
        mc1 = qe.MarkovChain(m1[i])
        sequence = mc1.simulate(N, random_state=None)
        run(m1[i], m2[i], sequence, j, vector_of_probabilities)





#p1 = ([
#     [0.1, 0.5, 0.4],
#     [0.3, 0.3, 0.4],
#     [0.8, 0.1, 0.1]])
#
#p2 = ([
#     [0.1, 0.5, 0.4],
#     [0.3, 0.3, 0.4],
#     [0.8, 0, 0.2]])
#
#p3 = ([
#     [0.5, 0, 0.5],
#     [0.05,0.05,0.9],
#     [0.05,0.9,0.05]])
#
#p4 = ([
#     [1/3, 1/3 , 1/3],
#     [1/3, 1/3 , 1/3],
#     [1/3, 1/3 , 1/3]])
