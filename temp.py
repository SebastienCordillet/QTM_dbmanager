# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""

import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt
import numpy as np
from scipy import signal
from xmlExtractor import getCropVariable, printDict, printChilds, getEvents, getModelVariable, plotHS
from pyomeca import Angles

tree = ET.parse('session_data.xml')
root = tree.getroot()


# listVariable =dict([
#     ('Left Ankle Angles_CGM','LHS'),
#     ('Left Ankle Moment','LHS'),
#     ('Left Ankle Power','LHS'),
#     ('Left Foot Pitch Angles','LHS'),
#     ('Left Foot Progression','LHS'),
#     ('Left Hip Angles','LHS'),
#     ('Left Hip Moment','LHS'),
#     ('Left Hip Power','LHS'),
#     ('Left Knee Angles','LHS'),
#     ('Left Knee Moment','LHS'),
#     ('Left Knee Power','LHS'),
#     ('Left Pelvic Angles','LHS'),
#     ('PelvisPos','LHS'),
#     ('Right Ankle Angles_CGM','RHS'),
#     ('Right Ankle Moment','RHS'),
#     ('Right Ankle Power','RHS'),
#     ('Right Foot Pitch Angles','RHS'),
#     ('Right Foot Progression','RHS'),
#     ('Right GRF','RHS'),
#     ('Right Hip Angles','RHS'),
#     ('Right Hip Moment','RHS'),
#     ('Right Hip Power','RHS'),
#     ('Right Knee Angles','RHS'),
#     ('Right Knee Moment','RHS'),
#     ('Right Knee Power','RHS'),
#     ('Right Pelvic Angles','RHS')
#     ])

listVariable =[
    'Left Ankle Angles_CGM',
    'Left Ankle Moment',
    'Left Ankle Power',
    'Left Foot Pitch Angles',
    'Left Foot Progression',
    'Left Hip Angles',
    'Left Hip Moment',
    'Left Hip Power',
    'Left Knee Angles',
    'Left Knee Moment',
    'Left Knee Power',
    'Left Pelvic Angles',
    'PelvisPos',
    'Right Ankle Angles_CGM',
    'Right Ankle Moment',
    'Right Ankle Power',
    'Right Foot Pitch Angles',
    'Right Foot Progression',
    'Right GRF',
    'Right Hip Angles',
    'Right Hip Moment',
    'Right Hip Power',
    'Right Knee Angles',
    'Right Knee Moment',
    'Right Knee Power',
    'Right Pelvic Angles',
    ]

# printDict(listVariable) #DEBUG 

# printChilds(root) list les essais
# OUT
# owner {'value': 'Gait LB - CGM 1.c3d'}
# owner {'value': 'Gait LB - CGM 3.c3d'}
# owner {'value': 'Gait LB - CGM 6.c3d'}
# data = np.random.random(size=(1, 1, 100))
# print(class)
# print(data[0,0,:])

session_angle=[]
for trials in root:   
    print(trials.attrib['value']) # ESSAI EN COURS D'ANALYSE
    events_LHS=getEvents(trials, event='LHS')
    events_RHS=getEvents(trials, event='RHS')
    session_angle.append(getModelVariable(trials,listVariable))
    # plotHS(events_LHS,events_RHS,trials.attrib['value'])
    
    
angle = getModelVariable(trials,MV = listVariable, axis= ['X','Y','Z'])
ANGLES=Angles(angle, dims=("axis", "channel", "time"),
            coords={
                "channel": listVariable}
            )
# ANGLES.assign_coords({
#     'axis': ['X','Y','Z']
#     })
print(ANGLES.coords)
# print(ANGLES)
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
      
# print(getEvents(root[0], event='RHS')) #RENVOI BIEN LES EVENEMTNS
# angle=getModelVariable(root[0], MV='Left Ankle Angles_CGM', axis='X')
# plt.plot(angle)
# plt.title('time serie')
# plt.show()



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



