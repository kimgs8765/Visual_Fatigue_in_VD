 #!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.2.3),
    on Tue May 17 18:35:03 2022
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division
from operator import truediv
from sqlite3 import InternalError
from statistics import mean
from this import s
from xml.dom import VALIDATION_ERR

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import pandas as pd

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding
import random

from psychopy.hardware import keyboard


# Ensure that relative paths start from the same directory as this script

_thisDir = os.path.dirname(os.path.abspath(__file__))  
os.chdir(_thisDir) 



# Store info about the experiment session
psychopyVersion = '2021.2.3'
expName = 'Real-Time Fatigue Measurement'  # from the Builder filename that created this script
expInfo = {'Name': '', 'Age' : '' ,'College': '', 'Student_ID' : '', '은행' : '', '계좌번호' : '', 'Block' : '' }
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
#filename = _thisDir + os.sep + u'data/%s_%s_' % (expInfo['Name'], expInfo['Student_ID'])

# An ExperimentHandler isn't essential but helps with data saving
# thisExp = data.ExperimentHandler(name=expName, version='',
#     extraInfo=expInfo, runtimeInfo=None,
#     originPath='C:\PsychoPY\commit',
#     savePickle=True, saveWideText=True,
#     dataFileName=filename)
# save a log file for detail verbose info
#logFile = logging.LogFile(filename+'.log', level=  logging.EXP)
# logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file 

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame



# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='VUE28', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, size= (2560, 1440),
    units='height')

# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()


# Setup the joystick
from psychopy.hardware import joystick 
joystick.backend = 'pyglet'

nJoys = joystick.getNumJoysticks
joy = joystick.Joystick(0)




#/////////////////////////////////////////////////// VFSQ  ////////////////////////////////////////////////////

VFSQ1 = visual.TextStim(win=win, name='흐릿함',
    text='1-7중 하나를 선택하세요',
    font='Arial',
    pos=(-0.4, 0.4), height=0.04, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0)

VFSQ2 = visual.TextStim(win=win, name='안구 건조',
    text='1-7중 하나를 선택하세요',
    font='Arial',
    pos=(-0.4, 0.2), height=0.04, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0)

VFSQ3 = visual.TextStim(win=win, name='눈시림',
    text='1-7중 하나를 선택하세요',
    font='Arial',
    pos=(-0.4, 0), height=0.04, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0)

VFSQ4 = visual.TextStim(win=win, name='작열감',
    text='1-7중 하나를 선택하세요',
    font='Arial',
    pos=(-0.4, -0.2), height=0.04, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0)

VFSQ5 = visual.TextStim(win=win, name='눈 통증',
    text='1-7중 하나를 선택하세요',
    font='Arial',
    pos=(-0.4, -0.4), height=0.04, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0)





# /////////////////////////////// Initialize components for Routine "Intorduction" //////////////////////////////////#

IntroductionClock = core.Clock()

Intro = visual.TextStim(win=win, name='Intro',
    text='Real-Time Fatigue Measurement',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0)


ratingscale0_1 = visual.RatingScale(win=win,
    size= 1  , pos=(0.3, 0.8),
    choices = [ 'Low', '2', '3', '4', '5', '6', 'High'],
    singleClick = True, 
    scale=None, showAccept=False,
    marker = 'circle', mouseOnly = True )

ratingscale0_2 = visual.RatingScale(win=win,
    size= 1 , pos=(0.3, 0.4),
    choices = [ 'Low', '2', '3', '4', '5', '6', 'High'],
    singleClick = True, 
    scale=None, showAccept=False,
    marker = 'circle', mouseOnly = True )


ratingscale0_3 = visual.RatingScale(win=win,
    size= 1, pos=(0.3, 0),
    choices = [ 'Low', '2', '3', '4', '5', '6', 'High'],
    singleClick = True, 
    scale=None, showAccept=False,
    marker = 'circle', mouseOnly = True )

ratingscale0_4 = visual.RatingScale(win=win,
    size= 1 , pos=(0.3, -0.4),
    choices = [ 'Low', '2', '3', '4', '5', '6', 'High'],
    singleClick = True, 
    scale=None, showAccept=False,
    marker = 'circle', mouseOnly = True )

ratingscale0_5 = visual.RatingScale(win=win,
    size= 1 , pos=(0.3, -0.8),
    choices = [ 'Low', '2', '3', '4', '5', '6', 'High'],
    singleClick = True, 
    scale=None, showAccept=False,
    marker = 'circle', mouseOnly = True )


Video1 = visual.MovieStim3(
    win=win, name='Video1',
    size = (1920,10800),
    noAudio = True,
    filename='./video1.mp4',
    ori=0, pos=(0,0 ), opacity=1, 
    loop=False, 
    depth=0.0,
    )

slider1 = visual.Slider(win=win, name='slider1',      
    size=(0.8, 0.05), pos=(0, -0.4), units=None, 
    labels=('Very Low','Medium','Very High'), ticks=(1, 2, 3, 4, 5, 6, 7),
    granularity=0, style=['triangleMarker'],
    color='white', font='HelveticaBold', depth=-8.0,
    flip=False, labelHeight = .03)

Mean_rt_txt = visual.TextStim(win=win, name='Mean',
        text='영상의 평균적인\n 눈시림(눈의 뻐근함) 정도를\n 표시해주세요',
        font='Arial',
        pos=(0, 0), height=0.06, wrapWidth=None, ori=0, 
        color='black', colorSpace='rgb', opacity=1, 
        languageStyle='LTR', 
        depth=0.0)

Mean_rt_1 = visual.RatingScale(win=win,
        size= 1.0 , pos=(0, -0.7),
        choices = [ 'Low', '2', '3', '4', '5', '6', 'High'],
        singleClick = True, 
        scale=None, showAccept=False,
        marker = 'circle', mouseOnly = True )







# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 


#/////////////////////// Routine Introduction ///////////////////////////////////////#


# ------Prepare to start Routine "Introduciton"-------
continueRoutine = True
routineTimer.add(120.0) # 95s

# update component parameters for each repeat
# keep track of which components have finished
IntroComponents = [ Intro, Video1, slider1, Mean_rt_txt, Mean_rt_1, \
                    VFSQ1, VFSQ2, VFSQ3, VFSQ4, VFSQ5, ratingscale0_1, ratingscale0_2, ratingscale0_3, ratingscale0_4, ratingscale0_5]

for thisComponent in IntroComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
IntroductionClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip   
frameN = -1


# ----------------Run Routine "Introduction"-----------------    
while continueRoutine :
    # get current time
    t = IntroductionClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=IntroductionClock)             
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # Introduction updates
    if Intro.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance: 
        # keep track of start time/frame for later
        Intro.frameNStart = frameN  # exact frame index
        Intro.tStart = t  # local t and not account for scr refresh
        Intro.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Intro, 'tStartRefresh')  # time at next scr refresh
        Intro.setAutoDraw(True)

    if Intro.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)

        if tThisFlip > 5.0 - frameTolerance: # 5s 
            # keep track of stop time/frame for later
            Intro.tStop = t  # not accounting for scr refresh
            Intro.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Intro, 'tStopRefresh')  # time at next scr refresh
            Intro.setAutoDraw(False)


    if tThisFlip >= 5.0 - frameTolerance: # 5s
        VFSQ1.setAutoDraw(True)
        VFSQ2.setAutoDraw(True)
        VFSQ3.setAutoDraw(True)
        VFSQ4.setAutoDraw(True)
        VFSQ5.setAutoDraw(True)
        ratingscale0_1.setAutoDraw(True)
        ratingscale0_2.setAutoDraw(True)
        ratingscale0_3.setAutoDraw(True)
        ratingscale0_4.setAutoDraw(True)
        ratingscale0_5.setAutoDraw(True)
    
    if tThisFlip >= 25.0 - frameTolerance : # 15s
        
        VFSQ1.setAutoDraw(False)
        VFSQ2.setAutoDraw(False)
        VFSQ3.setAutoDraw(False)
        VFSQ4.setAutoDraw(False)
        VFSQ5.setAutoDraw(False)
        ratingscale0_1.setAutoDraw(False)
        ratingscale0_2.setAutoDraw(False)
        ratingscale0_3.setAutoDraw(False)
        ratingscale0_4.setAutoDraw(False)
        ratingscale0_5.setAutoDraw(False)

        Video1.setAutoDraw(True)
        slider1.setAutoDraw(True)
    

    if tThisFlip >= 55.0 - frameTolerance : 
        Video1.setAutoDraw(False)
        slider1.setAutoDraw(False)

        Mean_rt_txt.setAutoDraw(True)
        Mean_rt_1.setAutoDraw(True)

    if tThisFlip >= 95.0 - frameTolerance : 
        Mean_rt_txt.setAutoDraw(False)
        Mean_rt_1.setAutoDraw(False)

    
    

    if slider1.status == NOT_STARTED and tThisFlip > 0.0-frameTolerance:  
        
        slider1.marker.size = 0.025
        slider1.markerPos = 4


    if slider1.status == STARTED :

        X_pos_1 = joy.getX()*0.021
        slider1.markerPos += X_pos_1





    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break

    continueRoutine = False  # will revert to True if at least one component still running

    for thisComponent in IntroComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()


# -------Ending Routine "Introduction"-------
for thisComponent in IntroComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

win.flip()

# these shouldn't be strictly necessary (should auto-save)
# thisExp.saveAsWideText(filename+'.csv')
# thisExp.saveAsPickle(filename)
# logging.flush()
# make sure everything is closed down
# thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()







 