# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""

import xml.etree.ElementTree as ET
import pandas as pd
# from scipy import signal
from xmlExtractor import printChilds, QTMsessionDataAsCrop
# from tkinter import filedialog




       
# path2Protocol='U:\DRI\prj_recurvatum\db_protocol.xml'
path2Protocol='U:\DRI\prj_recurvatum\db_protocol.xml'
tree2 = ET.parse(path2Protocol)
root2= tree2.getroot()        
printChilds(root2.find('Database'))

process=root2.find('Process')
listVariable=[var.attrib['name'] for var in root2.find('Process').findall('Variable')]

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
                      
            
db.to_excel('db.xlsx')

    
        
    
    
    
# listVariable =[
#     # 'Left Ankle Angles_CGM',
#     # 'Left Ankle Moment',
#     # 'Left Ankle Power',
#     # 'Left Foot Pitch Angles',
#     # 'Left Foot Progression',
#     # 'Left Hip Angles',
#     # 'Left Hip Moment',
#     # 'Left Hip Power',
#     'Left Knee Angles',
#     'Left Knee Moment',
#     'Left Knee Power',
#     # 'Left Pelvic Angles',
#     # 'PelvisPos',
#     # 'Right Ankle Angles_CGM',
#     # 'Right Ankle Moment',
#     # 'Right Ankle Power',
#     # 'Right Foot Pitch Angles',
#     # 'Right Foot Progression',
#     # 'Right GRF',
#     # 'Right Hip Angles',
#     # 'Right Hip Moment',
#     # 'Right Hip Power',
#     'Right Knee Angles',
#     'Right Knee Moment',
#     'Right Knee Power',
#     # 'Right Pelvic Angles',
#     ]
