# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 19:57:58 2022

@author: TH
"""

import random
import numpy as np
import psychopy
from psychopy import visual, core, event, gui, prefs, sound, monitors, clock,parallel
import random
import pprint
from datetime import datetime,date
import pandas as pd
from psychopy import sound

path=''
sp=''

df=pd.read_excel('sti.xlsx')

ob_1=np.array(df.iloc[:,3][0:20])
ob_1_t=np.array(df.iloc[:,4][0:20])
ob_1=[ob_1,1,ob_1_t]
ob_2=np.array(df.iloc[:,6][0:20])
ob_2_t=np.array(df.iloc[:,7][0:20])
ob_2=[ob_2,1,ob_2_t]
ob_3=np.array(df.iloc[:,9][0:20])
ob_3_t=np.array(df.iloc[:,10][0:20])
ob_3=[ob_3,1,ob_3_t]
ob_4=np.array(df.iloc[:,12][0:20])
ob_4_t=np.array(df.iloc[:,13][0:20])
ob_4=[ob_4,1,ob_4_t]
ob_5=np.array(df.iloc[:,15][0:20])
ob_5_t=np.array(df.iloc[:,16][0:20])
ob_5=[ob_5,1,ob_5_t]
ob_6=np.array(df.iloc[:,3][22:42])
ob_6_t=np.array(df.iloc[:,4][22:42])
ob_6=[ob_6,1,ob_6_t]
ob_7=np.array(df.iloc[:,6][22:42])
ob_7_t=np.array(df.iloc[:,7][22:42])
ob_7=[ob_7,1,ob_7_t]
ob_8=np.array(df.iloc[:,9][22:42])
ob_8_t=np.array(df.iloc[:,10][22:42])
ob_8=[ob_8,1,ob_8_t]
ob_9=np.array(df.iloc[:,12][22:42])
ob_9_t=np.array(df.iloc[:,13][22:42])
ob_9=[ob_9,1,ob_9_t]
ob_10=np.array(df.iloc[:,15][22:42])
ob_10_t=np.array(df.iloc[:,16][22:42])
ob_10=[ob_10,1,ob_10_t]

tb_1=np.array(df.iloc[:,20][0:20])
tb_1_t=np.array(df.iloc[:,21][0:20])
tb_1=[tb_1,2,tb_1_t]
tb_2=np.array(df.iloc[:,23][0:20])
tb_2_t=np.array(df.iloc[:,24][0:20])
tb_2=[tb_2,2,tb_2_t]
tb_3=np.array(df.iloc[:,26][0:20])
tb_3_t=np.array(df.iloc[:,27][0:20])
tb_3=[tb_3,2,tb_3_t]
tb_4=np.array(df.iloc[:,29][0:20])
tb_4_t=np.array(df.iloc[:,30][0:20])
tb_4=[tb_4,2,tb_4_t]
tb_5=np.array(df.iloc[:,32][0:20])
tb_5_t=np.array(df.iloc[:,33][0:20])
tb_5=[tb_5,2,tb_5_t]
tb_6=np.array(df.iloc[:,20][22:42])
tb_6_t=np.array(df.iloc[:,21][22:42])
tb_6=[tb_6,2,tb_6_t]
tb_7=np.array(df.iloc[:,23][22:42])
tb_7_t=np.array(df.iloc[:,24][22:42])
tb_7=[tb_7,2,tb_7_t]
tb_8=np.array(df.iloc[:,26][22:42])
tb_8_t=np.array(df.iloc[:,27][22:42])
tb_8=[tb_8,2,tb_8_t]
tb_9=np.array(df.iloc[:,29][22:42])
tb_9_t=np.array(df.iloc[:,30][22:42])
tb_9=[tb_9,2,tb_9_t]
tb_10=np.array(df.iloc[:,32][22:42])
tb_10_t=np.array(df.iloc[:,33][22:42])
tb_10=[tb_10,2,tb_10_t]


ac=[ob_1,ob_2,ob_3,ob_4,ob_5,
    ob_6,ob_7,ob_8,ob_9,ob_10,
    tb_1,tb_2,tb_3,tb_4,tb_5,
    tb_6,tb_7,tb_8,tb_9,tb_10
    ]

sid=str(input("ID:"))

day=date.today()
date=[]
sub_id=[]
response=[]
response_time=[]
trial_no=[]
clock=psychopy.core.Clock()
keys=[]
rt=[]
ran_dur=[]
interval=[]
iti=[] 
trial_trigger=[]
trial=[]
res_key=[]
res_time=[]

def win_b():
    win.color=(-1,-1,-1)
    win.clearBuffer(color=True)
    fixation_w()
    win.flip()

def win_g():
    win.color=(0,0,0)
    win.clearBuffer(color=True)
    fixation_b()
    win.flip()

def rd():   
    d=[0.15,0.23]
    dr=random.choice(d)
    return (dr)

def dr_l():
    t=[]
    for i in range(20):
        t.append(rd())
    t=np.array(t)    
    return(t)

def fixation_w():
    fix_h=visual.Rect(win,width=60,height=1,units='pix',
                      lineColor=[1,1,1],
                      fillColor=[1,1,1],
                      pos=(0,0))
    fix_v=visual.Rect(win,width=1,height=60,units='pix',
                      lineColor=[1,1,1],
                      fillColor=[1,1,1],
                      pos=(0,0))
    fix_h.draw()
    fix_v.draw()


def fixation_b():
    fix_h=visual.Rect(win,width=60,height=1,units='pix',
                      lineColor=[-1,-1,-1],
                      fillColor=[-1,-1,-1],
                      pos=(0,0))
    fix_v=visual.Rect(win,width=1,height=60,units='pix',
                      lineColor=[-1,-1,-1],
                      fillColor=[-1,-1,-1],
                      pos=(0,0))
    fix_h.draw()
    fix_v.draw()

def condition():
    if c==1:
        cond=psychopy.visual.TextStim(win=win,text="1-back",color=[1,1,1],pos=(0,0),height=(100))
        cond.draw()
    else:
        cond=psychopy.visual.TextStim(win=win,text="2-back",color=[1,1,1],pos=(0,0),height=(100))
        cond.draw()
    win.flip()

def target():
    fix_h=visual.Rect(win,width=60,height=1,units='pix',
                      lineColor=[1,-1,-1],
                      fillColor=[1,-1,-1],
                      pos=(0,0))
    fix_v=visual.Rect(win,width=1,height=60,units='pix',
                      lineColor=[1,-1,-1],
                      fillColor=[1,-1,-1],
                      pos=(0,0))
    fix_h.draw()
    fix_v.draw()
    win.flip()
    
def rest():
    fix_h=visual.Rect(win,width=60,height=1,units='pix',
                      lineColor=[1,1,1],
                      fillColor=[1,1,1],
                      pos=(0,0))
    fix_v=visual.Rect(win,width=1,height=60,units='pix',
                      lineColor=[1,1,1],
                      fillColor=[1,1,1],
                      pos=(0,0))
    fix_h.draw()
    fix_v.draw()
    win.flip()

win=psychopy.visual.Window(
    size=[1000,1000],
    color=[-1,-1,-1],
    units="pix",
    fullscr=False
)

for i in range(len(ac)):
    c=ac[i][1]
    tri=ac[i][2]
    condition()
    core.wait(1) #2
    win_b()
    core.wait(1) #2
    win_g()
    core.wait(0.5)
    t=ac[i][0]
    dt=dr_l()
    for s in range(len(t)):
        win_g() 
        n=t[s]
        trigger=tri[s]
        f=sp+'%s.wav'%n    
        stm=sound.Sound(value=str(f),sampleRate=(44100))
        stm.play()
        start_time=clock.getTime()
        core.wait(stm.getDuration())
        core.wait(dt[s])
        key=event.getKeys(keyList=['space'])
        if "space" in key:
            stop_time=clock.getTime()
            res_key='space'
            res_time= round(stop_time-start_time,4)*1000
            clock.reset()
        else:
            res_key='miss'
            res_time='/'
            clock.reset()
        keys.append(res_key)
        rt.append(res_time)
        
    pass
    res_time=[]
    res_key=[]
    win_b()
    rest()
    core.wait(1)    #5
    core.wait(1) #2
    trial.append(t)
    interval.append(dt)
    trial_no.append(i+1)
    sub_id.append(sid)
    date.append(day)
    response.append(keys)
    response_time.append(rt)
    trial_trigger.append(tri)
    keys=[]
    rt=[]
    
win.close()    
pass

data=pd.DataFrame({'sid':sub_id,
                   'trial_list':trial,
                   'duration':interval,
                   'trial_no':trial_no,
                    'date':date,
                    'trigger':trial_trigger,
                    'response_key':response,
                    'rt':response_time
                    })

spath=''    
file_name= sid+'c_nback_task'+'.csv'
save_path=spath+file_name
data.to_csv(save_path, sep=',',index=False)

print('FINISH') 


