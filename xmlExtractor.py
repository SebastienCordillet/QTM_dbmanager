# -*- coding: utf-8 -*-
"""
Created on Wed Nov 17 13:41:58 2021

Ensemble de fonction pour extraire les données d'un fichier XML générer par QTM pour le reporting'

@author: cordillet
"""

def getCropVariable(timeVariable, events, nPoints=100):
    import numpy as np
    from scipy import signal
    
    crop = np.ndarray(shape=(len(events)-1,100), dtype=float)
    for i in range(len(events)-1):
        crop[i,]=signal.resample_poly(timeVariable[events[i]:events[i+1]],
                                  100,
                                  len(timeVariable[events[i]:events[i+1]]),
                                  padtype='line')
    return (crop)

def printDict(D):
    for k,v in D.items():
        print(k,v)
        
def printChilds(r):
    for child in r:   
        print(child.tag, child.attrib)
        
def getEvents(xmlroot, event = 'LHS'):
    import numpy as np
    # DEBUG 
    # print('ok')
    # printChilds(xmlroot[1][0][0])
    # print('ok')
    if event =='LHS':
        event_time = np.fromstring(xmlroot[1][0][0][0].attrib.get("data"),sep=',')
    elif event =='RHS':
        event_time = np.fromstring(xmlroot[1][0][2][0].attrib.get("data"),sep=',')
    return(event_time)


def plotHS(LHS,RHS, title='Heel strike'):
    import matplotlib.pyplot as plt
    import numpy as np
    
    
    y=np.concatenate((np.ones(len(LHS)-1),2*np.ones((len(RHS)-1))), axis=0)
    if len(RHS)<2:
        y=np.append(y,2)
        
    if len(LHS)<2:
        y=np.insert(y,0,1)
      
        
    ##Colors 
    colors=[]
    color_RHS='#336dff'
    color_LHS='#ff3d33'
    for i in y:
        if i ==1:
            colors.append(color_LHS)
        elif i ==2:
            colors.append(color_RHS)
    
    # print(y)
    if len(LHS)>=2:
        cycle_duration_LHS= LHS[1:]-LHS[:-1]
    else:
        cycle_duration_LHS= np.zeros(1)
    if len(RHS)>=2:
        cycle_duration_RHS= RHS[1:]-RHS[:-1]
    else:
        cycle_duration_RHS= np.zeros(1)
    duration= np.concatenate((cycle_duration_LHS,cycle_duration_RHS), axis=0)  
    # print(duration)
    
    
    
    ## Start of cycle
    start = np.concatenate((LHS[:-1],RHS[:-1]),axis=0)
    if len(LHS)<2:
        start=np.insert(start,0,0)
    if len(RHS)<2:
        start=np.append(start,0)
    # print(start)
        
    fig, ax = plt.subplots()
    ax.scatter(LHS,np.ones(len(LHS)), zorder=2, color=color_LHS, s=200, marker='D')
    ax.scatter(RHS,np.ones(len(RHS))*2, zorder=2, color=color_RHS, s=200, marker='D')
    ax.barh(y, duration, left = start, height=0.10, color=colors)
    ax.set_title(title)
    ax.set_xlim(left=0)
    ax.set_ylim(bottom=0, top=3)
    ax.set_yticks([1,2])
    ax.set_yticklabels(['LHS','RHS'], minor=False)
    

def getModelVariable(xmlroot, MV = 'Left Ankle Moment', axis='X'):
    import numpy as np
    # print('ok')
    # printChilds(xmlroot[2][0])
    # print('ok')
    ANGLES= xmlroot[2][0]
    
    n_axis = len(axis)
    n_channel = len(MV)
    n_frames = len(np.fromstring(ANGLES[0][0].attrib['data'].replace('nodata','nan'),sep=','))
    data = np.random.random(size=(n_axis, n_channel, n_frames))
    # print('===== Analyse angles =========')
    # print('initialisation ...')
    # print('class de la variable :  {}'.format(type(data)))
    # print('nombre de frames  : {}'.format(n_frames))
    
    # print(type(data))
    
    for child in ANGLES:
        for mv in MV:
            if child.attrib['value']== mv:
                current_var=child
            # print(current_var.attrib['value'])
            # printChilds(current_var)
                for dim in current_var:
                # print(dim.attrib['value'])
                    if dim.attrib['value']==axis:
                    # print(dim.attrib['data'].replace('nodata','nan'))
                    # print(np.fromstring(dim.attrib["data"].replace('nodata','nan'), sep=','))
                        # print(data[axis.index(dim.attrib['value']),MV.index(mv),:])
                        # print(MV.index(mv))
                        data[axis.index(dim.attrib['value']),MV.index(mv),:]=np.fromstring(dim.attrib["data"].replace('nodata','nan'), sep=',').T
    return(data)           
                
# def pyomecaAnglesFromQTMxml(xml)                
    # return('fsin')       
        # print(child.attrib['value'])
    
    # array= np.fromstring(anglesComponent[0].attrib.get("data"), sep=',')
    
    # root
    # if event =='LHS':
    #     event_time = np.fromstring(xmlroot[1][0][0][0].attrib.get("data"),sep=',')
    # elif event =='RHS':
    #     event_time = np.fromstring(xmlroot[1][0][2][0].attrib.get("data"),sep=',')
    # return(event_time)
     
        
    

        
        
    
        