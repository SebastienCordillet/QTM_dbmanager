# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""

import xml.etree.ElementTree as ET
import pandas as pd
# from scipy import signal
from xmlExtractor import printChilds, QTMsessionDataAsCrop
from tkinter import filedialog


listVariable =[
    # 'Left Ankle Angles_CGM',
    # 'Left Ankle Moment',
    # 'Left Ankle Power',
    # 'Left Foot Pitch Angles',
    # 'Left Foot Progression',
    # 'Left Hip Angles',
    # 'Left Hip Moment',
    # 'Left Hip Power',
    'Left Knee Angles',
    'Left Knee Moment',
    'Left Knee Power',
    # 'Left Pelvic Angles',
    # 'PelvisPos',
    # 'Right Ankle Angles_CGM',
    # 'Right Ankle Moment',
    # 'Right Ankle Power',
    # 'Right Foot Pitch Angles',
    # 'Right Foot Progression',
    # 'Right GRF',
    # 'Right Hip Angles',
    # 'Right Hip Moment',
    # 'Right Hip Power',
    'Right Knee Angles',
    'Right Knee Moment',
    'Right Knee Power',
    # 'Right Pelvic Angles',
    ]


       
path2Protocol='U:\DRI\prj_recurvatum\db_protocol.xml'
tree2 = ET.parse(path2Protocol)
root2= tree2.getroot()        
printChilds(root2.find('Database'))

process=root2.find('Process')
listVariable2=(var.attrib['name'] for var in root2.find('Process').findall('Variable'))

#Initialisation de la base de donnée 
db=pd.DataFrame()
for patient in root2.find('Database').findall('Patient'):
    print('--------')
    print(patient.attrib['Folder'])
    printChilds(patient)
    for session in patient.findall('Session'):
        printChilds(session)
        for condition in session.findall('Condition'):
            print(condition.find('BiomechanicsData').text)
            filePath=[root2.find('Database').attrib['Path'],
                      patient.attrib['Folder'],
                      session.attrib['Folder'],
                      condition.attrib['Folder'],
                      condition.find('BiomechanicsData').text.replace('"','')]
            current_cond=QTMsessionDataAsCrop("\\".join(filePath), listVariable)
            db=db.append(current_cond)          
                      
            


    
        
    
    
    
    # plotHS(events_LHS,events_RHS,trials.attrib['value'])
    
   
#transformation en dataset
# dataset_angle=xr.concat(session_angle, dim='trial')# ca ne marche pas car pas même durée
# print(session_angle)        


# angle = getModelVariable(trial,MV = listVariable, axis= ['X','Y','Z'])
# ANGLES=Angles(angle) #pour créer un obj angles pyomeca
# ANGLES= ANGLES.assign_coords({"channel": listVariable })



# printChilds(root[0]) #CORRESPOND AU PREMIER ESSAI
# OUT
# type {'value': 'ANALOG'}
# type {'value': 'EVENT_LABEL'}
# type {'value': 'LINK_MODEL_BASED'}
# type {'value': 'METRIC'}

# printChilds(root[0][1]) #return 'ORIGINAL'
# printChilds(root[0][1][0])
# OUT
# name {'value': 'LHS'}
# name {'value': 'LTO'}
# name {'value': 'RHS'}
# name {'value': 'RMS'}
# name {'value': 'ROFF'}
# name {'value': 'RON'}
# name {'value': 'RTO'}
# name {'value': 'start'}

# printChilds(root[0][1][0][0])

# ESSAI pour récupérer un angle et l'afficher      
# print(getEvents(root[0], event='RHS')) #RENVOI BIEN LES EVENEMTNS
# angle=getModelVariable(root[0], MV='Left Ankle Angles_CGM', axis='X')
# plt.plot(angle)
# plt.title('time serie')
# plt.show()


# ESSAI pour afficher un angle normalize sur le cycle de marche
# LHS=getEvents(root[0], event='LHS')
# LHS_frame=np.rint(LHS*150).astype(int)
# crop = getCropVariable(angle,LHS_frame)
# plt.figure()
# plt.plot(crop.T)
# plt.title('crop angle')


# anglesComponent = root[0][2][1][1]

# fr=150 #frame rate in our lab
    
# array= np.fromstring(anglesComponent[0].attrib.get("data"), sep=',')
# event = np.fromstring(root[0][1][0][0][0].attrib.get("data"),sep=',')
# event_frame =np.rint(event*fr).astype(int)

# crop = getCropVariable(array,event_frame)
# # print(crop)

# for cycle in crop:
#     plt.plot(cycle)
    
# plt.show()


# events= 
# plt.plot(array)
# plt.show()


# for i in range(len(event)-1):
#     temp=signal.resample_poly(array[event_frame[i]:event_frame[i+1]],
#                   100,
#                   len(array[event_frame[i]:event_frame[i+1]]),
#                   padtype='line')
#     plt.plot(temp)
#     # plt.plot(array[event_frame[i]:event_frame[i+1]])
    
    
# plt.show()
#     # print(array[event_frame[i]:event_frame[i+1]])


# for i in range(len(event)-1):
#     temp=signal.resample_poly(array[event_frame[i]:event_frame[i+1]],
#                   100,
#                   len(array[event_frame[i]:event_frame[i+1]]),
#                   padtype='line')
#     plt.plot(temp)
#     # plt.plot(array[event_frame[i]:event_frame[i+1]])
    
    
# plt.show()
#     # print(array[event_frame[i]:event_frame[i+1]])



