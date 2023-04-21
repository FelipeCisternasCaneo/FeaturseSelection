# import numpy as np
# from FS.Problem import FeatureSelection as fs

# individuo = np.random.randint(low=0, high=2, size = 34)
# individuo = np.ones(34)
# seleccion = np.where(individuo == 1)[0]

# instance = fs('ionosphere.data')

# print(instance.getDatos())
# print(instance.getClases())

# fitness, cm, accuracy, f1Score, presicion, recall, mcc, errorRate = instance.fitness(seleccion)
# fitness, accuracy, f1Score, presicion, recall, mcc, errorRate, totalFeatureSelected = instance.fitness(seleccion)

# print(fitness)
# print(cm)
# print(accuracy)
# print(f1Score)
# print(presicion)
# print(recall)
# print(mcc)
# print(errorRate)
# print(totalFeatureSelected)


# from util import util
# from BD.sqlite import BD

# bd = BD()
# data = bd.obtenerArchivos()

# for d in data:

#     nombreArchivo = d[0]
#     archivo = d[1]

#     direccionDestiono = './Resultados/Transitorio/'+nombreArchivo+'.csv'
#     util.writeTofile(archivo,direccionDestiono)

# from Problem.EMPATIA.model.hyperparameter_optimization import load_parameters

# opt = load_parameters("./Problem/EMPATIA/model/")

# print(opt)

# import json

# DS_actions = [
#     'V1-STD', 'V1-COM', 'V1-PS', 'V1-ELIT',
#     'V2-STD', 'V2-COM', 'V2-PS', 'V2-ELIT',
#     'V3-STD', 'V3-COM', 'V3-PS', 'V3-ELIT',
#     'V4-STD', 'V4-COM', 'V4-PS', 'V4-ELIT',
#     'S1-STD', 'S1-COM', 'S1-PS', 'S1-ELIT',
#     'S2-STD', 'S2-COM', 'S2-PS', 'S2-ELIT',
#     'S3-STD', 'S3-COM', 'S3-PS', 'S3-ELIT',
#     'S4-STD', 'S4-COM', 'S4-PS', 'S4-ELIT',
# ]

# paramsML = {
#     'MinMax'        : 'min',
#     'DS_actions'    : DS_actions,
#     'gamma'         : 0.4,
#     'policy'        : 'e-greedy',
#     'qlAlphaType'   : 'static',
#     'rewardType'    : 'withPenalty1',
#     'stateQ'        : 2
# }

# print(paramsML)

# print(paramsML['DS_actions'][10].split("-"))

# from Problem.FS.Problem import FeatureSelection as fs
# import numpy as np

# instance = fs("only_clinic")

# clasificador = "Xgboost"
# parametrosC = None
# pop = 10
# fitness                 = 0
# accuracy                = 0
# f1Score                 = 0
# presicion               = 0
# recall                  = 0
# mcc                     = 0
# errorRate               = 0
# totalFeatureSelected    = 0
# # poblacion = np.random.randint(low=0, high=2, size = instance.getTotalFeature())
# poblacion = np.ones(instance.getTotalFeature())


# seleccion = np.where(poblacion == 1)[0]
# fitness, accuracy, f1Score, presicion, recall, mcc, errorRate, totalFeatureSelected = instance.fitness(seleccion, clasificador, parametrosC)

# print(f'Clasificador {clasificador} obtuvo un f-score de {f1Score}')

import numpy as np
poblacion = np.ones(shape = (10,30))

print(poblacion)