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

from itertools import permutations



# Ensure that relative paths start from the same directory as this script

_thisDir = os.path.dirname(os.path.abspath(__file__))  
os.chdir(_thisDir) 



# Store info about the experiment session
psychopyVersion = '2021.2.3'
expName = 'Real-Time Fatigue Measurement'  # from the Builder filename that created this script
expInfo = {'Name': '', 'Age' : '' ,'College': '', 'Student_ID' : '' , '은행' : '' , '계좌번호' : '', 'Block' : '' }
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_' % (expInfo['Name'], expInfo['Student_ID'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\PsychoPY\commit',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
# logFile = logging.LogFile(filename+'.log', level=  logging.EXP)
# logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file 

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame



# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='VUE28', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, size= (1920,1080),
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
    text='흐릿함',
    font='Arial',
    pos=(-0.4, 0.4), height=0.04, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0)

VFSQ2 = visual.TextStim(win=win, name='안구 건조',
    text='안구 건조',
    font='Arial',
    pos=(-0.4, 0.2), height=0.04, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0)

VFSQ3 = visual.TextStim(win=win, name='눈시림',
    text='눈시림\n(눈이 뻐근함)',
    font='Arial',
    pos=(-0.4, 0), height=0.04, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0)

VFSQ4 = visual.TextStim(win=win, name='작열감',
    text='작열감\n(모래가 들어간 듯한 자극)',
    font='Arial',
    pos=(-0.4, -0.2), height=0.04, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0)

VFSQ5 = visual.TextStim(win=win, name='눈 통증',
    text='눈 통증',
    font='Arial',
    pos=(-0.4, -0.4), height=0.04, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0)

VFSQ6 = visual.TextStim(win=win, name='눈 따가움',
    text='눈 따가움',
    font='Arial',
    pos=(-0.4, 0.4), height=0.04, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0)

VFSQ7 = visual.TextStim(win=win, name='눈 피로',
    text='눈 피로',
    font='Arial',
    pos=(-0.4, 0.2), height=0.04, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0)

VFSQ8 = visual.TextStim(win=win, name='희미한 시야',
    text='희미한 시야(뿌옇게 보이는 시야)',
    font='Arial',
    pos=(-0.4, 0), height=0.04, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0)

VFSQ9 = visual.TextStim(win=win, name='눈충혈',
    text='눈충혈 및 부종',
    font='Arial',
    pos=(-0.4, -0.2), height=0.04, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0)

VFSQ10 = visual.TextStim(win=win, name='눈 떨림',
    text='눈 떨림',
    font='Arial',
    pos=(-0.4, -0.4), height=0.04, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0)

VFSQ11 = visual.TextStim(win=win, name='눈물',
    text='눈물 분비',
    font='Arial',
    pos=(-0.4, 0.4), height=0.04, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0)

VFSQ12 = visual.TextStim(win=win, name='머리',
    text='머리가 무거워지는 느낌',
    font='Arial',
    pos=(-0.4, 0.2), height=0.04, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0)

VFSQ13 = visual.TextStim(win=win, name='몸',
    text='몸이 무거워지는 느낌',
    font='Arial',
    pos=(-0.4, 0), height=0.04, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0)

VFSQ14 = visual.TextStim(win=win, name='집중력',
    text='집중력 장애',
    font='Arial',
    pos=(-0.4, -0.2), height=0.04, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0)

VFSQ15 = visual.TextStim(win=win, name='어지러움',
    text='어지러움',
    font='Arial',
    pos=(-0.4, -0.4), height=0.04, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0)

VFSQ16 = visual.TextStim(win=win, name='어깨 결림',
    text='어깨 결림',
    font='Arial',
    pos=(-0.4, 0.4), height=0.04, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0)

VFSQ17 = visual.TextStim(win=win, name='목 결림',
    text='목 결림',
    font='Arial',
    pos=(-0.4, 0.2), height=0.04, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0)

VFSQ18 = visual.TextStim(win=win, name='졸림',
    text='졸림',
    font='Arial',
    pos=(-0.4, 0), height=0.04, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0)

VFSQ19 = visual.TextStim(win=win, name='구토 증상',
    text='구토 증상',
    font='Arial',
    pos=(-0.4, -0.2), height=0.04, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0)

VFSQ20 = visual.TextStim(win=win, name='현기증',
    text='현기증',
    font='Arial',
    pos=(-0.4, -0.4), height=0.04, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0)

VFSQ21 = visual.TextStim(win=win, name='메스꺼움',
    text='메스꺼움',
    font='Arial',
    pos=(-0.4, 0.4), height=0.04, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0)

VFSQ22 = visual.TextStim(win=win, name='초점 장애',
    text='초점 장애\n(초점을 잡기가 어려움)',
    font='Arial',
    pos=(-0.4, 0.2), height=0.04, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0)

VFSQ23 = visual.TextStim(win=win, name='다시증',
    text='다시증\n(상이 두개로 나뉘어 보임)',
    font='Arial',
    pos=(-0.4, 0), height=0.04, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0)

VFSQ24 = visual.TextStim(win=win, name='윈시 증상',
    text='원시\n(가까이 있는 것이 잘 안보임)',
    font='Arial',
    pos=(-0.4, -0.2), height=0.04, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0)

VFSQ25 = visual.TextStim(win=win, name='근시 증상',
    text='근시\n(멀리 있는 것이 잘 안보임)',
    font='Arial',
    pos=(-0.4, -0.4), height=0.04, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0)

VFSQ26 = visual.TextStim(win=win, name='관자놀이',
    text='관자놀이 통증',
    font='Arial',
    pos=(-0.4, 0.3), height=0.04, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0)

VFSQ27 = visual.TextStim(win=win, name='이마',
    text='이마 중앙 통증',
    font='Arial',
    pos=(-0.4, 0.0), height=0.04, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0)

VFSQ28 = visual.TextStim(win=win, name='뒷통수',
    text='뒷통수 통증',
    font='Arial',
    pos=(-0.4, -0.3), height=0.04, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0)

Break_time = visual.TextStim(win=win, name='Break',
    text='잠시 쉬는 시간입니다. ',
    font='Arial',
    pos=(0, 0), height=0.06, wrapWidth=None, ori=0, 
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
    choices = [ '1', '2', '3', '4', '5', '6', '7'],
    singleClick = True, 
    scale=None, showAccept=False,
    marker = 'circle', mouseOnly = True )

ratingscale0_2 = visual.RatingScale(win=win,
    size= 1 , pos=(0.3, 0.4),
    choices = [ '1', '2', '3', '4', '5', '6', '7'],
    singleClick = True, 
    scale=None, showAccept=False,
    marker = 'circle', mouseOnly = True )


ratingscale0_3 = visual.RatingScale(win=win,
    size= 1, pos=(0.3, 0),
    choices = [ '1', '2', '3', '4', '5', '6', '7'],
    singleClick = True, 
    scale=None, showAccept=False,
    marker = 'circle', mouseOnly = True )

ratingscale0_4 = visual.RatingScale(win=win,
    size= 1 , pos=(0.3, -0.4),
    choices = [ '1', '2', '3', '4', '5', '6', '7'],
    singleClick = True, 
    scale=None, showAccept=False,
    marker = 'circle', mouseOnly = True )

ratingscale0_5 = visual.RatingScale(win=win,
    size= 1 , pos=(0.3, -0.8),
    choices = [ '1', '2', '3', '4', '5', '6', '7'],
    singleClick = True, 
    scale=None, showAccept=False,
    marker = 'circle', mouseOnly = True )

ratingscale0_6 = visual.RatingScale(win=win,
    size= 1 , pos=(0.3, 0.8),
    choices = [ '1', '2', '3', '4', '5', '6', '7'],
    singleClick = True,
    scale=None, showAccept=False,
    marker = 'circle', mouseOnly = True )

ratingscale0_7 = visual.RatingScale(win=win,
    size= 1 , pos=(0.3, 0.4),
    choices = [ '1', '2', '3', '4', '5', '6', '7'],
    singleClick = True, 
    scale=None, showAccept=False,
    marker = 'circle', mouseOnly = True )

ratingscale0_8 = visual.RatingScale(win=win,
    size= 1 , pos=(0.3, 0),
    choices = [ '1', '2', '3', '4', '5', '6', '7'],
    singleClick = True, 
    scale=None, showAccept=False,
    marker = 'circle', mouseOnly = True )

ratingscale0_9 = visual.RatingScale(win=win,
    size= 1 , pos=(0.3, -0.4),
    choices = [ '1', '2', '3', '4', '5', '6', '7'],
    singleClick = True, 
    scale=None, showAccept=False,
    marker = 'circle', mouseOnly = True )

ratingscale0_10 = visual.RatingScale(win=win,
    size= 1 , pos=(0.3, -0.8),
    choices = [ '1', '2', '3', '4', '5', '6', '7'],
    singleClick = True, 
    scale=None, showAccept=False,
    marker = 'circle', mouseOnly = True )

ratingscale0_11 = visual.RatingScale(win=win,
    size= 1 , pos=(0.3, 0.8),
    choices = [ '1', '2', '3', '4', '5', '6', '7'],
    singleClick = True, 
    scale=None, showAccept=False,
    marker = 'circle', mouseOnly = True )

ratingscale0_12 = visual.RatingScale(win=win,
    size= 1 , pos=(0.3, 0.4),
    choices = [ '1', '2', '3', '4', '5', '6', '7'],
    singleClick = True,  
    scale=None, showAccept=False,
    marker = 'circle', mouseOnly = True )

ratingscale0_13 = visual.RatingScale(win=win,
    size= 1 , pos=(0.3, 0),
    choices = [ '1', '2', '3', '4', '5', '6', '7'],
    singleClick = True, 
    scale=None, showAccept=False,
    marker = 'circle', mouseOnly = True )

ratingscale0_14 = visual.RatingScale(win=win,
    size= 1 , pos=(0.3, -0.4),
    choices = [ '1', '2', '3', '4', '5', '6', '7'],
    singleClick = True, 
    scale=None, showAccept=False,
    marker = 'circle', mouseOnly = True )

ratingscale0_15 = visual.RatingScale(win=win,
    size= 1 , pos=(0.3, -0.8),
    choices = [ '1', '2', '3', '4', '5', '6', '7'],
    singleClick = True, 
    scale=None, showAccept=False,
    marker = 'circle', mouseOnly = True )

ratingscale0_16 = visual.RatingScale(win=win,
    size= 1 , pos=(0.3, 0.8),
    choices = [ '1', '2', '3', '4', '5', '6', '7'],
    singleClick = True,
    scale=None, showAccept=False,
    marker = 'circle', mouseOnly = True )

ratingscale0_17 = visual.RatingScale(win=win,
    size= 1 , pos=(0.3, 0.4),
    choices = [ '1', '2', '3', '4', '5', '6', '7'],
    singleClick = True, 
    scale=None, showAccept=False,
    marker = 'circle', mouseOnly = True )

ratingscale0_18 = visual.RatingScale(win=win,
    size= 1 , pos=(0.3, 0),
    choices = [ '1', '2', '3', '4', '5', '6', '7'],
    singleClick = True,
    scale=None, showAccept=False,
    marker = 'circle', mouseOnly = True )

ratingscale0_19 = visual.RatingScale(win=win,
    size= 1 , pos=(0.3, -0.4),
    choices = [ '1', '2', '3', '4', '5', '6', '7'],
    singleClick = True, 
    scale=None, showAccept=False,
    marker = 'circle', mouseOnly = True )

ratingscale0_20 = visual.RatingScale(win=win,
    size= 1 , pos=(0.3, -0.8),
    choices = [ '1', '2', '3', '4', '5', '6', '7'],
    singleClick = True,
    scale=None, showAccept=False,
    marker = 'circle', mouseOnly = True )

ratingscale0_21 = visual.RatingScale(win=win,
    size= 1 , pos=(0.3, 0.8),
    choices = [ '1', '2', '3', '4', '5', '6', '7'],
    singleClick = True, 
    scale=None, showAccept=False,
    marker = 'circle', mouseOnly = True )

ratingscale0_22 = visual.RatingScale(win=win,
    size= 1 , pos=(0.3, 0.4),
    choices = [ '1', '2', '3', '4', '5', '6', '7'],
    singleClick = True,  
    scale=None, showAccept=False,
    marker = 'circle', mouseOnly = True )

ratingscale0_23 = visual.RatingScale(win=win,
    size= 1 , pos=(0.3, 0),
    choices = [ '1', '2', '3', '4', '5', '6', '7'],
    singleClick = True, 
    scale=None, showAccept=False,
    marker = 'circle', mouseOnly = True )

ratingscale0_24 = visual.RatingScale(win=win,
    size= 1 , pos=(0.3, -0.4),
    choices = [ '1', '2', '3', '4', '5', '6', '7'],
    singleClick = True, 
    scale=None, showAccept=False,
    marker = 'circle', mouseOnly = True )

ratingscale0_25 = visual.RatingScale(win=win,
    size= 1 , pos=(0.3, -0.8),
    choices = [ '1', '2', '3', '4', '5', '6', '7'],
    singleClick = True, 
    scale=None, showAccept=False,
    marker = 'circle', mouseOnly = True )

ratingscale0_26 = visual.RatingScale(win=win,
    size= 1 , pos=(0.3, 0.6),
    choices = [ '1', '2', '3', '4', '5', '6', '7'],
    singleClick = True, 
    scale=None, showAccept=False,
    marker = 'circle', mouseOnly = True )

ratingscale0_27 = visual.RatingScale(win=win,
    size= 1 , pos=(0.3, 0),
    choices = [ '1', '2', '3', '4', '5', '6', '7'],
    singleClick = True, 
    scale=None, showAccept=False,
    marker = 'circle', mouseOnly = True )

ratingscale0_28 = visual.RatingScale(win=win,
    size= 1 , pos=(0.3, -0.6),
    choices = [ '1', '2', '3', '4', '5', '6', '7'],
    singleClick = True, 
    scale=None, showAccept=False,
    marker = 'circle', mouseOnly = True )



#/////////////////////////////// Initialize components for Routine "Trial1" ////////////////////////////////////////#

# Clock 1 for clock timer

Trial1Clock = core.Clock()   

# Trial 1 Video compoent

Video1 = visual.MovieStim3(
    win=win, name='Video_1',
    size = (1920,1080),
    noAudio = True,
    filename='./High_MS/Bright/1.mp4',
    ori=0, pos=(0,0 ), opacity=1, 
    loop=False, 
    depth=0.0,
    )

Video2 = visual.MovieStim3(
    win=win, name='Video_2',
    size = (1920,1080),
    noAudio = True,
    filename='./High_MS/Bright/2.mp4',
    ori=0, pos=(0,0 ), opacity=1, 
    loop=False, 
    depth=0.0,
    )


Video3 = visual.MovieStim3(
    win=win, name='Video_3',
    size = (1920,1080),
    noAudio = True,
    filename='./High_MS/Bright/3.mp4',
    ori=0, pos=(0, 0 ), opacity=1, 
    loop=False, 
    depth=0.0,
    )

Video4 = visual.MovieStim3(
    win=win, name='Video_4',
    size = (1920,1080),
    noAudio = True,
    filename='./High_MS/Bright/4.mp4',
    ori=0, pos=(0, 0), opacity=1, 
    loop=False, 
    depth=0.0,
    )

Video5 = visual.MovieStim3(
    win=win, name='Video_5',
    size = (1920,1080),
    noAudio = True,
    filename='./High_MS/Bright/5.mp4',
    ori=0, pos=(0, 0), opacity=1, 
    loop=False, 
    depth=0.0,
    )


# "mean_rating" for mean rating of eye-strain

Mean_rt_txt = visual.TextStim(win=win, name='Mean',
        text='영상의 평균적인\n 눈시림(눈의 뻐근함) 정도를\n 표시해주세요',
        font='Arial',
        pos=(0, 0), height=0.06, wrapWidth=None, ori=0, 
        color='black', colorSpace='rgb', opacity=1, 
        languageStyle='LTR', 
        depth=0.0)

Mean_rt_1 = visual.RatingScale(win=win,
        size= 1.0 , pos=(0, -0.7),
        choices = [ '1', '2', '3', '4', '5', '6', '7'],
        singleClick = True, 
        scale=None, showAccept=False,
        marker = 'circle', mouseOnly = True )

Mean_rt_2 = visual.RatingScale(win=win,
        size= 1.0 , pos=(0, -0.7),
        choices = [ '1', '2', '3', '4', '5', '6', '7'],
        singleClick = True, 
        scale=None, showAccept=False,
        marker = 'circle', mouseOnly = True )

Mean_rt_3 = visual.RatingScale(win=win,
        size= 1.0 , pos=(0, -0.7),
        choices = [ '1', '2', '3', '4', '5', '6', '7'],
        singleClick = True, 
        scale=None, showAccept=False,
        marker = 'circle', mouseOnly = True )

Mean_rt_4 = visual.RatingScale(win=win,
        size= 1.0 , pos=(0, -0.7),
        choices = [ '1', '2', '3', '4', '5', '6', '7'],
        singleClick = True, 
        scale=None, showAccept=False,
        marker = 'circle', mouseOnly = True )

Mean_rt_5 = visual.RatingScale(win=win,
        size= 1.0 , pos=(0, -0.7),
        choices = [ '1', '2', '3', '4', '5', '6', '7'],
        singleClick = True, 
        scale=None, showAccept=False,
        marker = 'circle', mouseOnly = True )


#  "slider1" for real-time rating
slider1 = visual.Slider(win=win, name='slider1',      
    size=(0.8, 0.05), pos=(0, -0.4), units=None, 
    labels=('Very Low','Medium','Very High'), ticks=(1, 2, 3, 4, 5, 6, 7),
    granularity=0, style=['triangleMarker'],
    color='white', font='HelveticaBold', depth=-8.0,
    flip=False, labelHeight = .03)


# VFSQ for trial1

ratingscale1_1 = visual.RatingScale(win=win,
    size= 1  , pos=(0.3, 0.8),
    choices = [ '1', '2', '3', '4', '5', '6', '7'],
    singleClick = True, 
    scale=None, showAccept=False,
    marker = 'circle', mouseOnly = True )

ratingscale1_2 = visual.RatingScale(win=win,
    size= 1 , pos=(0.3, 0.4),
    choices = [ '1', '2', '3', '4', '5', '6', '7'],
    singleClick = True, 
    scale=None, showAccept=False,
    marker = 'circle', mouseOnly = True )


ratingscale1_3 = visual.RatingScale(win=win,
    size= 1, pos=(0.3, 0),
    choices = [ '1', '2', '3', '4', '5', '6', '7'],
    singleClick = True, 
    scale=None, showAccept=False,
    marker = 'circle', mouseOnly = True )

ratingscale1_4 = visual.RatingScale(win=win,
    size= 1 , pos=(0.3, -0.4),
    choices = [ '1', '2', '3', '4', '5', '6', '7'],
    singleClick = True, 
    scale=None, showAccept=False,
    marker = 'circle', mouseOnly = True )

ratingscale1_5 = visual.RatingScale(win=win,
    size= 1 , pos=(0.3, -0.8),
    choices = [ '1', '2', '3', '4', '5', '6', '7'],
    singleClick = True, 
    scale=None, showAccept=False,
    marker = 'circle', mouseOnly = True )

ratingscale1_6 = visual.RatingScale(win=win,
    size= 1 , pos=(0.3, 0.8),
    choices = [ '1', '2', '3', '4', '5', '6', '7'],
    singleClick = True,
    scale=None, showAccept=False,
    marker = 'circle', mouseOnly = True )

ratingscale1_7 = visual.RatingScale(win=win,
    size= 1 , pos=(0.3, 0.4),
    choices = [ '1', '2', '3', '4', '5', '6', '7'],
    singleClick = True, 
    scale=None, showAccept=False,
    marker = 'circle', mouseOnly = True )

ratingscale1_8 = visual.RatingScale(win=win,
    size= 1 , pos=(0.3, 0),
    choices = [ '1', '2', '3', '4', '5', '6', '7'],
    singleClick = True, 
    scale=None, showAccept=False,
    marker = 'circle', mouseOnly = True )

ratingscale1_9 = visual.RatingScale(win=win,
    size= 1 , pos=(0.3, -0.4),
    choices = [ '1', '2', '3', '4', '5', '6', '7'],
    singleClick = True, 
    scale=None, showAccept=False,
    marker = 'circle', mouseOnly = True )

ratingscale1_10 = visual.RatingScale(win=win,
    size= 1 , pos=(0.3, -0.8),
    choices = [ '1', '2', '3', '4', '5', '6', '7'],
    singleClick = True, 
    scale=None, showAccept=False,
    marker = 'circle', mouseOnly = True )

ratingscale1_11 = visual.RatingScale(win=win,
    size= 1 , pos=(0.3, 0.8),
    choices = [ '1', '2', '3', '4', '5', '6', '7'],
    singleClick = True, 
    scale=None, showAccept=False,
    marker = 'circle', mouseOnly = True )

ratingscale1_12 = visual.RatingScale(win=win,
    size= 1 , pos=(0.3, 0.4),
    choices = [ '1', '2', '3', '4', '5', '6', '7'],
    singleClick = True,  
    scale=None, showAccept=False,
    marker = 'circle', mouseOnly = True )

ratingscale1_13 = visual.RatingScale(win=win,
    size= 1 , pos=(0.3, 0),
    choices = [ '1', '2', '3', '4', '5', '6', '7'],
    singleClick = True, 
    scale=None, showAccept=False,
    marker = 'circle', mouseOnly = True )

ratingscale1_14 = visual.RatingScale(win=win,
    size= 1 , pos=(0.3, -0.4),
    choices = [ '1', '2', '3', '4', '5', '6', '7'],
    singleClick = True, 
    scale=None, showAccept=False,
    marker = 'circle', mouseOnly = True )

ratingscale1_15 = visual.RatingScale(win=win,
    size= 1 , pos=(0.3, -0.8),
    choices = [ '1', '2', '3', '4', '5', '6', '7'],
    singleClick = True, 
    scale=None, showAccept=False,
    marker = 'circle', mouseOnly = True )

ratingscale1_16 = visual.RatingScale(win=win,
    size= 1 , pos=(0.3, 0.8),
    choices = [ '1', '2', '3', '4', '5', '6', '7'],
    singleClick = True,
    scale=None, showAccept=False,
    marker = 'circle', mouseOnly = True )

ratingscale1_17 = visual.RatingScale(win=win,
    size= 1 , pos=(0.3, 0.4),
    choices = [ '1', '2', '3', '4', '5', '6', '7'],
    singleClick = True, 
    scale=None, showAccept=False,
    marker = 'circle', mouseOnly = True )

ratingscale1_18 = visual.RatingScale(win=win,
    size= 1 , pos=(0.3, 0),
    choices = [ '1', '2', '3', '4', '5', '6', '7'],
    singleClick = True,
    scale=None, showAccept=False,
    marker = 'circle', mouseOnly = True )

ratingscale1_19 = visual.RatingScale(win=win,
    size= 1 , pos=(0.3, -0.4),
    choices = [ '1', '2', '3', '4', '5', '6', '7'],
    singleClick = True, 
    scale=None, showAccept=False,
    marker = 'circle', mouseOnly = True )

ratingscale1_20 = visual.RatingScale(win=win,
    size= 1 , pos=(0.3, -0.8),
    choices = [ '1', '2', '3', '4', '5', '6', '7'],
    singleClick = True,
    scale=None, showAccept=False,
    marker = 'circle', mouseOnly = True )

ratingscale1_21 = visual.RatingScale(win=win,
    size= 1 , pos=(0.3, 0.8),
    choices = [ '1', '2', '3', '4', '5', '6', '7'],
    singleClick = True, 
    scale=None, showAccept=False,
    marker = 'circle', mouseOnly = True )

ratingscale1_22 = visual.RatingScale(win=win,
    size= 1 , pos=(0.3, 0.4),
    choices = [ '1', '2', '3', '4', '5', '6', '7'],
    singleClick = True,  
    scale=None, showAccept=False,
    marker = 'circle', mouseOnly = True )

ratingscale1_23 = visual.RatingScale(win=win,
    size= 1 , pos=(0.3, 0),
    choices = [ '1', '2', '3', '4', '5', '6', '7'],
    singleClick = True, 
    scale=None, showAccept=False,
    marker = 'circle', mouseOnly = True )

ratingscale1_24 = visual.RatingScale(win=win,
    size= 1 , pos=(0.3, -0.4),
    choices = [ '1', '2', '3', '4', '5', '6', '7'],
    singleClick = True, 
    scale=None, showAccept=False,
    marker = 'circle', mouseOnly = True )

ratingscale1_25 = visual.RatingScale(win=win,
    size= 1 , pos=(0.3, -0.8),
    choices = [ '1', '2', '3', '4', '5', '6', '7'],
    singleClick = True, 
    scale=None, showAccept=False,
    marker = 'circle', mouseOnly = True )

ratingscale1_26 = visual.RatingScale(win=win,
    size= 1 , pos=(0.3, 0.6),
    choices = [ '1', '2', '3', '4', '5', '6', '7'],
    singleClick = True, 
    scale=None, showAccept=False,
    marker = 'circle', mouseOnly = True )

ratingscale1_27 = visual.RatingScale(win=win,
    size= 1 , pos=(0.3, 0),
    choices = [ '1', '2', '3', '4', '5', '6', '7'],
    singleClick = True, 
    scale=None, showAccept=False,
    marker = 'circle', mouseOnly = True )

ratingscale1_28 = visual.RatingScale(win=win,
    size= 1 , pos=(0.3, -0.6),
    choices = [ '1', '2', '3', '4', '5', '6', '7'],
    singleClick = True, 
    scale=None, showAccept=False,
    marker = 'circle', mouseOnly = True )





#////////////////////////////// Initialize components for Routine "Trial2" /////////////////////////////////////#


# Clock 2 for clock timer

Trial2Clock = core.Clock()   

# Trial 2 Video compoent

Video6 = visual.MovieStim3(
    win=win, name='Video_6',
    size = (1920,1080),
    noAudio = True,
    filename='./High_MS/Dark/6.mp4',
    ori=0, pos=(0, 0), opacity=1, 
    loop=False, 
    depth=0.0,
    )

Video7 = visual.MovieStim3(
    win=win, name='Video_7',
    size = (1920,1080),
    noAudio = True,
    filename='./High_MS/Dark/7.mp4',
    ori=0, pos=(0, 0), opacity=1, 
    loop=False, 
    depth=0.0,
    )

Video8 = visual.MovieStim3(
    win=win, name='Video_8',
    size = (1920,1080),
    noAudio = True,
    filename='./High_MS/Dark/8.mp4',
    ori=0, pos=(0, 0), opacity=1, 
    loop=False, 
    depth=0.0,
    )

Video9 = visual.MovieStim3(
    win=win, name='Video_9',
    size = (1920,1080),
    noAudio = True,
    filename='./High_MS/Dark/9.mp4',
    ori=0, pos=(0, 0), opacity=1, 
    loop=False, 
    depth=0.0,
    )

Video10 = visual.MovieStim3(
    win=win, name='Video_10',
    size = (1920,1080),
    noAudio = True,
    filename='./High_MS/Dark/10.mp4',
    ori=0, pos=(0, 0), opacity=1, 
    loop=False, 
    depth=0.0,
    )

# "mean_rating" for mean rating of eye-strain
Mean_rt_txt = visual.TextStim(win=win, name='Mean',
        text='영상의 평균적인\n 눈시림(눈의 뻐근함) 정도를\n 표시해주세요',
        font='Arial',
        pos=(0, 0), height=0.06, wrapWidth=None, ori=0, 
        color='black', colorSpace='rgb', opacity=1, 
        languageStyle='LTR', 
        depth=0.0)

Mean_rt_6 = visual.RatingScale(win=win,
        size= 1.0 , pos=(0, -0.7),
        choices = [ '1', '2', '3', '4', '5', '6', '7'],
        singleClick = True, 
        scale=None, showAccept=False,
        marker = 'circle', mouseOnly = True )

Mean_rt_7 = visual.RatingScale(win=win,
        size= 1.0 , pos=(0, -0.7),
        choices = [ '1', '2', '3', '4', '5', '6', '7'],
        singleClick = True, 
        scale=None, showAccept=False,
        marker = 'circle', mouseOnly = True )

Mean_rt_8 = visual.RatingScale(win=win,
        size= 1.0 , pos=(0, -0.7),
        choices = [ '1', '2', '3', '4', '5', '6', '7'],
        singleClick = True, 
        scale=None, showAccept=False,
        marker = 'circle', mouseOnly = True )

Mean_rt_9 = visual.RatingScale(win=win,
        size= 1.0 , pos=(0, -0.7),
        choices = [ '1', '2', '3', '4', '5', '6', '7'],
        singleClick = True, 
        scale=None, showAccept=False,
        marker = 'circle', mouseOnly = True )

Mean_rt_10 = visual.RatingScale(win=win,
        size= 1.0 , pos=(0, -0.7),
        choices = [ '1', '2', '3', '4', '5', '6', '7'],
        singleClick = True, 
        scale=None, showAccept=False,
        marker = 'circle', mouseOnly = True )


# "slider2" for real-time rating
slider2 = visual.Slider(win=win, name='slider2',      
    size=(0.8, 0.05), pos=(0, -0.4), units=None, 
    labels=('Very Low','Medium','Very High'), ticks=(1, 2, 3, 4, 5, 6, 7),
    granularity=0, style=['triangleMarker'],
    color='white', font='HelveticaBold', depth=-8.0,
    flip=False, labelHeight = .03)

# VFSQ for trial2

ratingscale2_1 = visual.RatingScale(win=win,
    size= 1  , pos=(0.3, 0.8),
    choices = [ '1', '2', '3', '4', '5', '6', '7'],
    singleClick = True, 
    scale=None, showAccept=False,
    marker = 'circle', mouseOnly = True )

ratingscale2_2 = visual.RatingScale(win=win,
    size= 1 , pos=(0.3, 0.4),
    choices = [ '1', '2', '3', '4', '5', '6', '7'],
    singleClick = True, 
    scale=None, showAccept=False,
    marker = 'circle', mouseOnly = True )


ratingscale2_3 = visual.RatingScale(win=win,
    size= 1, pos=(0.3, 0),
    choices = [ '1', '2', '3', '4', '5', '6', '7'],
    singleClick = True, 
    scale=None, showAccept=False,
    marker = 'circle', mouseOnly = True )

ratingscale2_4 = visual.RatingScale(win=win,
    size= 1 , pos=(0.3, -0.4),
    choices = [ '1', '2', '3', '4', '5', '6', '7'],
    singleClick = True, 
    scale=None, showAccept=False,
    marker = 'circle', mouseOnly = True )

ratingscale2_5 = visual.RatingScale(win=win,
    size= 1 , pos=(0.3, -0.8),
    choices = [ '1', '2', '3', '4', '5', '6', '7'],
    singleClick = True, 
    scale=None, showAccept=False,
    marker = 'circle', mouseOnly = True )

ratingscale2_6 = visual.RatingScale(win=win,
    size= 1 , pos=(0.3, 0.8),
    choices = [ '1', '2', '3', '4', '5', '6', '7'],
    singleClick = True,
    scale=None, showAccept=False,
    marker = 'circle', mouseOnly = True )

ratingscale2_7 = visual.RatingScale(win=win,
    size= 1 , pos=(0.3, 0.4),
    choices = [ '1', '2', '3', '4', '5', '6', '7'],
    singleClick = True, 
    scale=None, showAccept=False,
    marker = 'circle', mouseOnly = True )

ratingscale2_8 = visual.RatingScale(win=win,
    size= 1 , pos=(0.3, 0),
    choices = [ '1', '2', '3', '4', '5', '6', '7'],
    singleClick = True, 
    scale=None, showAccept=False,
    marker = 'circle', mouseOnly = True )

ratingscale2_9 = visual.RatingScale(win=win,
    size= 1 , pos=(0.3, -0.4),
    choices = [ '1', '2', '3', '4', '5', '6', '7'],
    singleClick = True, 
    scale=None, showAccept=False,
    marker = 'circle', mouseOnly = True )

ratingscale2_10 = visual.RatingScale(win=win,
    size= 1 , pos=(0.3, -0.8),
    choices = [ '1', '2', '3', '4', '5', '6', '7'],
    singleClick = True, 
    scale=None, showAccept=False,
    marker = 'circle', mouseOnly = True )

ratingscale2_11 = visual.RatingScale(win=win,
    size= 1 , pos=(0.3, 0.8),
    choices = [ '1', '2', '3', '4', '5', '6', '7'],
    singleClick = True, 
    scale=None, showAccept=False,
    marker = 'circle', mouseOnly = True )

ratingscale2_12 = visual.RatingScale(win=win,
    size= 1 , pos=(0.3, 0.4),
    choices = [ '1', '2', '3', '4', '5', '6', '7'],
    singleClick = True,  
    scale=None, showAccept=False,
    marker = 'circle', mouseOnly = True )

ratingscale2_13 = visual.RatingScale(win=win,
    size= 1 , pos=(0.3, 0),
    choices = [ '1', '2', '3', '4', '5', '6', '7'],
    singleClick = True, 
    scale=None, showAccept=False,
    marker = 'circle', mouseOnly = True )

ratingscale2_14 = visual.RatingScale(win=win,
    size= 1 , pos=(0.3, -0.4),
    choices = [ '1', '2', '3', '4', '5', '6', '7'],
    singleClick = True, 
    scale=None, showAccept=False,
    marker = 'circle', mouseOnly = True )

ratingscale2_15 = visual.RatingScale(win=win,
    size= 1 , pos=(0.3, -0.8),
    choices = [ '1', '2', '3', '4', '5', '6', '7'],
    singleClick = True, 
    scale=None, showAccept=False,
    marker = 'circle', mouseOnly = True )

ratingscale2_16 = visual.RatingScale(win=win,
    size= 1 , pos=(0.3, 0.8),
    choices = [ '1', '2', '3', '4', '5', '6', '7'],
    singleClick = True,
    scale=None, showAccept=False,
    marker = 'circle', mouseOnly = True )

ratingscale2_17 = visual.RatingScale(win=win,
    size= 1 , pos=(0.3, 0.4),
    choices = [ '1', '2', '3', '4', '5', '6', '7'],
    singleClick = True, 
    scale=None, showAccept=False,
    marker = 'circle', mouseOnly = True )

ratingscale2_18 = visual.RatingScale(win=win,
    size= 1 , pos=(0.3, 0),
    choices = [ '1', '2', '3', '4', '5', '6', '7'],
    singleClick = True,
    scale=None, showAccept=False,
    marker = 'circle', mouseOnly = True )

ratingscale2_19 = visual.RatingScale(win=win,
    size= 1 , pos=(0.3, -0.4),
    choices = [ '1', '2', '3', '4', '5', '6', '7'],
    singleClick = True, 
    scale=None, showAccept=False,
    marker = 'circle', mouseOnly = True )

ratingscale2_20 = visual.RatingScale(win=win,
    size= 1 , pos=(0.3, -0.8),
    choices = [ '1', '2', '3', '4', '5', '6', '7'],
    singleClick = True,
    scale=None, showAccept=False,
    marker = 'circle', mouseOnly = True )

ratingscale2_21 = visual.RatingScale(win=win,
    size= 1 , pos=(0.3, 0.8),
    choices = [ '1', '2', '3', '4', '5', '6', '7'],
    singleClick = True, 
    scale=None, showAccept=False,
    marker = 'circle', mouseOnly = True )

ratingscale2_22 = visual.RatingScale(win=win,
    size= 1 , pos=(0.3, 0.4),
    choices = [ '1', '2', '3', '4', '5', '6', '7'],
    singleClick = True,  
    scale=None, showAccept=False,
    marker = 'circle', mouseOnly = True )

ratingscale2_23 = visual.RatingScale(win=win,
    size= 1 , pos=(0.3, 0),
    choices = [ '1', '2', '3', '4', '5', '6', '7'],
    singleClick = True, 
    scale=None, showAccept=False,
    marker = 'circle', mouseOnly = True )

ratingscale2_24 = visual.RatingScale(win=win,
    size= 1 , pos=(0.3, -0.4),
    choices = [ '1', '2', '3', '4', '5', '6', '7'],
    singleClick = True, 
    scale=None, showAccept=False,
    marker = 'circle', mouseOnly = True )

ratingscale2_25 = visual.RatingScale(win=win,
    size= 1 , pos=(0.3, -0.8),
    choices = [ '1', '2', '3', '4', '5', '6', '7'],
    singleClick = True, 
    scale=None, showAccept=False,
    marker = 'circle', mouseOnly = True )

ratingscale2_26 = visual.RatingScale(win=win,
    size= 1 , pos=(0.3, 0.6),
    choices = [ '1', '2', '3', '4', '5', '6', '7'],
    singleClick = True, 
    scale=None, showAccept=False,
    marker = 'circle', mouseOnly = True )

ratingscale2_27 = visual.RatingScale(win=win,
    size= 1 , pos=(0.3, 0),
    choices = [ '1', '2', '3', '4', '5', '6', '7'],
    singleClick = True, 
    scale=None, showAccept=False,
    marker = 'circle', mouseOnly = True )

ratingscale2_28 = visual.RatingScale(win=win,
    size= 1 , pos=(0.3, -0.6),
    choices = [ '1', '2', '3', '4', '5', '6', '7'],
    singleClick = True, 
    scale=None, showAccept=False,
    marker = 'circle', mouseOnly = True )



#////////////////////////////// Initialize components for Routine "Trial3" /////////////////////////////////////#


# Clock 3 for clock timer

Trial3Clock = core.Clock()   

# Trial 3 Video compoent

Video11 = visual.MovieStim3(
    win=win, name='Video_11',
    size = (1920,1080),
    noAudio = True,
    filename='./Low_MS/Bright/11.mp4',
    ori=0, pos=(0, 0), opacity=1, 
    loop=False, 
    depth=0.0,
    )

Video12 = visual.MovieStim3(
    win=win, name='Video_12',
    size = (1920,1080),
    noAudio = True,
    filename='./Low_MS/Bright/12.mp4',
    ori=0, pos=(0, 0), opacity=1, 
    loop=False, 
    depth=0.0,
    )

Video13 = visual.MovieStim3(
    win=win, name='Video_13',
    size = (1920,1080),
    noAudio = True,
    filename='./Low_MS/Bright/13.mp4',
    ori=0, pos=(0, 0), opacity=1, 
    loop=False, 
    depth=0.0,
    )

Video14 = visual.MovieStim3(
    win=win, name='Video_14',
    size = (1920,1080),
    noAudio = True,
    filename='./Low_MS/Bright/14.mp4',
    ori=0, pos=(0, 0), opacity=1, 
    loop=False, 
    depth=0.0,
    )

Video15 = visual.MovieStim3(
    win=win, name='Video_15',
    size = (1920,1080),
    noAudio = True,
    filename='./Low_MS/Bright/15.mp4',
    ori=0, pos=(0, 0), opacity=1, 
    loop=False, 
    depth=0.0,
    )

# "mean_rating" for mean rating of eye-strain
Mean_rt_txt = visual.TextStim(win=win, name='Mean',
        text='영상의 평균적인\n 눈시림(눈의 뻐근함) 정도를\n 표시해주세요',
        font='Arial',
        pos=(0, 0), height=0.06, wrapWidth=None, ori=0, 
        color='black', colorSpace='rgb', opacity=1, 
        languageStyle='LTR', 
        depth=0.0)

Mean_rt_11 = visual.RatingScale(win=win,
        size= 1.0 , pos=(0, -0.7),
        choices = [ '1', '2', '3', '4', '5', '6', '7'],
        singleClick = True, 
        scale=None, showAccept=False,
        marker = 'circle', mouseOnly = True )

Mean_rt_12= visual.RatingScale(win=win,
        size= 1.0 , pos=(0, -0.7),
        choices = [ '1', '2', '3', '4', '5', '6', '7'],
        singleClick = True, 
        scale=None, showAccept=False,
        marker = 'circle', mouseOnly = True )

Mean_rt_13 = visual.RatingScale(win=win,
        size= 1.0 , pos=(0, -0.7),
        choices = [ '1', '2', '3', '4', '5', '6', '7'],
        singleClick = True, 
        scale=None, showAccept=False,
        marker = 'circle', mouseOnly = True )

Mean_rt_14 = visual.RatingScale(win=win,
        size= 1.0 , pos=(0, -0.7),
        choices = [ '1', '2', '3', '4', '5', '6', '7'],
        singleClick = True, 
        scale=None, showAccept=False,
        marker = 'circle', mouseOnly = True )

Mean_rt_15 = visual.RatingScale(win=win,
        size= 1.0 , pos=(0, -0.7),
        choices = [ '1', '2', '3', '4', '5', '6', '7'],
        singleClick = True, 
        scale=None, showAccept=False,
        marker = 'circle', mouseOnly = True )


# "slider3" for real-time rating
slider3 = visual.Slider(win=win, name='slider3',      
    size=(0.8, 0.05), pos=(0, -0.4), units=None, 
    labels=('Very Low','Medium','Very High'), ticks=(1, 2, 3, 4, 5, 6, 7),
    granularity=0, style=['triangleMarker'],
    color='white', font='HelveticaBold', depth=-8.0,
    flip=False, labelHeight = .03)


# VFSQ for trial3
ratingscale3_1 = visual.RatingScale(win=win,
    size= 1  , pos=(0.3, 0.8),
    choices = [ '1', '2', '3', '4', '5', '6', '7'],
    singleClick = True, 
    scale=None, showAccept=False,
    marker = 'circle', mouseOnly = True )

ratingscale3_2 = visual.RatingScale(win=win,
    size= 1 , pos=(0.3, 0.4),
    choices = [ '1', '2', '3', '4', '5', '6', '7'],
    singleClick = True, 
    scale=None, showAccept=False,
    marker = 'circle', mouseOnly = True )


ratingscale3_3 = visual.RatingScale(win=win,
    size= 1, pos=(0.3, 0),
    choices = [ '1', '2', '3', '4', '5', '6', '7'],
    singleClick = True, 
    scale=None, showAccept=False,
    marker = 'circle', mouseOnly = True )

ratingscale3_4 = visual.RatingScale(win=win,
    size= 1 , pos=(0.3, -0.4),
    choices = [ '1', '2', '3', '4', '5', '6', '7'],
    singleClick = True, 
    scale=None, showAccept=False,
    marker = 'circle', mouseOnly = True )

ratingscale3_5 = visual.RatingScale(win=win,
    size= 1 , pos=(0.3, -0.8),
    choices = [ '1', '2', '3', '4', '5', '6', '7'],
    singleClick = True, 
    scale=None, showAccept=False,
    marker = 'circle', mouseOnly = True )

ratingscale3_6 = visual.RatingScale(win=win,
    size= 1 , pos=(0.3, 0.8),
    choices = [ '1', '2', '3', '4', '5', '6', '7'],
    singleClick = True,
    scale=None, showAccept=False,
    marker = 'circle', mouseOnly = True )

ratingscale3_7 = visual.RatingScale(win=win,
    size= 1 , pos=(0.3, 0.4),
    choices = [ '1', '2', '3', '4', '5', '6', '7'],
    singleClick = True, 
    scale=None, showAccept=False,
    marker = 'circle', mouseOnly = True )

ratingscale3_8 = visual.RatingScale(win=win,
    size= 1 , pos=(0.3, 0),
    choices = [ '1', '2', '3', '4', '5', '6', '7'],
    singleClick = True, 
    scale=None, showAccept=False,
    marker = 'circle', mouseOnly = True )

ratingscale3_9 = visual.RatingScale(win=win,
    size= 1 , pos=(0.3, -0.4),
    choices = [ '1', '2', '3', '4', '5', '6', '7'],
    singleClick = True, 
    scale=None, showAccept=False,
    marker = 'circle', mouseOnly = True )

ratingscale3_10 = visual.RatingScale(win=win,
    size= 1 , pos=(0.3, -0.8),
    choices = [ '1', '2', '3', '4', '5', '6', '7'],
    singleClick = True, 
    scale=None, showAccept=False,
    marker = 'circle', mouseOnly = True )

ratingscale3_11 = visual.RatingScale(win=win,
    size= 1 , pos=(0.3, 0.8),
    choices = [ '1', '2', '3', '4', '5', '6', '7'],
    singleClick = True, 
    scale=None, showAccept=False,
    marker = 'circle', mouseOnly = True )

ratingscale3_12 = visual.RatingScale(win=win,
    size= 1 , pos=(0.3, 0.4),
    choices = [ '1', '2', '3', '4', '5', '6', '7'],
    singleClick = True,  
    scale=None, showAccept=False,
    marker = 'circle', mouseOnly = True )

ratingscale3_13 = visual.RatingScale(win=win,
    size= 1 , pos=(0.3, 0),
    choices = [ '1', '2', '3', '4', '5', '6', '7'],
    singleClick = True, 
    scale=None, showAccept=False,
    marker = 'circle', mouseOnly = True )

ratingscale3_14 = visual.RatingScale(win=win,
    size= 1 , pos=(0.3, -0.4),
    choices = [ '1', '2', '3', '4', '5', '6', '7'],
    singleClick = True, 
    scale=None, showAccept=False,
    marker = 'circle', mouseOnly = True )

ratingscale3_15 = visual.RatingScale(win=win,
    size= 1 , pos=(0.3, -0.8),
    choices = [ '1', '2', '3', '4', '5', '6', '7'],
    singleClick = True, 
    scale=None, showAccept=False,
    marker = 'circle', mouseOnly = True )

ratingscale3_16 = visual.RatingScale(win=win,
    size= 1 , pos=(0.3, 0.8),
    choices = [ '1', '2', '3', '4', '5', '6', '7'],
    singleClick = True,
    scale=None, showAccept=False,
    marker = 'circle', mouseOnly = True )

ratingscale3_17 = visual.RatingScale(win=win,
    size= 1 , pos=(0.3, 0.4),
    choices = [ '1', '2', '3', '4', '5', '6', '7'],
    singleClick = True, 
    scale=None, showAccept=False,
    marker = 'circle', mouseOnly = True )

ratingscale3_18 = visual.RatingScale(win=win,
    size= 1 , pos=(0.3, 0),
    choices = [ '1', '2', '3', '4', '5', '6', '7'],
    singleClick = True,
    scale=None, showAccept=False,
    marker = 'circle', mouseOnly = True )

ratingscale3_19 = visual.RatingScale(win=win,
    size= 1 , pos=(0.3, -0.4),
    choices = [ '1', '2', '3', '4', '5', '6', '7'],
    singleClick = True, 
    scale=None, showAccept=False,
    marker = 'circle', mouseOnly = True )

ratingscale3_20 = visual.RatingScale(win=win,
    size= 1 , pos=(0.3, -0.8),
    choices = [ '1', '2', '3', '4', '5', '6', '7'],
    singleClick = True,
    scale=None, showAccept=False,
    marker = 'circle', mouseOnly = True )

ratingscale3_21 = visual.RatingScale(win=win,
    size= 1 , pos=(0.3, 0.8),
    choices = [ '1', '2', '3', '4', '5', '6', '7'],
    singleClick = True, 
    scale=None, showAccept=False,
    marker = 'circle', mouseOnly = True )

ratingscale3_22 = visual.RatingScale(win=win,
    size= 1 , pos=(0.3, 0.4),
    choices = [ '1', '2', '3', '4', '5', '6', '7'],
    singleClick = True,  
    scale=None, showAccept=False,
    marker = 'circle', mouseOnly = True )

ratingscale3_23 = visual.RatingScale(win=win,
    size= 1 , pos=(0.3, 0),
    choices = [ '1', '2', '3', '4', '5', '6', '7'],
    singleClick = True, 
    scale=None, showAccept=False,
    marker = 'circle', mouseOnly = True )

ratingscale3_24 = visual.RatingScale(win=win,
    size= 1 , pos=(0.3, -0.4),
    choices = [ '1', '2', '3', '4', '5', '6', '7'],
    singleClick = True, 
    scale=None, showAccept=False,
    marker = 'circle', mouseOnly = True )

ratingscale3_25 = visual.RatingScale(win=win,
    size= 1 , pos=(0.3, -0.8),
    choices = [ '1', '2', '3', '4', '5', '6', '7'],
    singleClick = True, 
    scale=None, showAccept=False,
    marker = 'circle', mouseOnly = True )

ratingscale3_26 = visual.RatingScale(win=win,
    size= 1 , pos=(0.3, 0.6),
    choices = [ '1', '2', '3', '4', '5', '6', '7'],
    singleClick = True, 
    scale=None, showAccept=False,
    marker = 'circle', mouseOnly = True )

ratingscale3_27 = visual.RatingScale(win=win,
    size= 1 , pos=(0.3, 0),
    choices = [ '1', '2', '3', '4', '5', '6', '7'],
    singleClick = True, 
    scale=None, showAccept=False,
    marker = 'circle', mouseOnly = True )

ratingscale3_28 = visual.RatingScale(win=win,
    size= 1 , pos=(0.3, -0.6),
    choices = [ '1', '2', '3', '4', '5', '6', '7'],
    singleClick = True, 
    scale=None, showAccept=False,
    marker = 'circle', mouseOnly = True )




#////////////////////////////// Initialize components for Routine "Trial4" /////////////////////////////////////#


# Clock 4 for clock timer

Trial4Clock = core.Clock()   

# Trial 4 Video compoent

Video16 = visual.MovieStim3(
    win=win, name='Video_16',
    size = (1920,1080),
    noAudio = True,
    filename='./Low_MS/Dark/16.mp4',
    ori=0, pos=(0, 0), opacity=1, 
    loop=False, 
    depth=0.0,
    )

Video17 = visual.MovieStim3(
    win=win, name='Video_17',
    size = (1920,1080),
    noAudio = True,
    filename='./Low_MS/Dark/17.mp4',
    ori=0, pos=(0, 0), opacity=1, 
    loop=False, 
    depth=0.0,
    )

Video18 = visual.MovieStim3(
    win=win, name='Video_18',
    size = (1920,1080),
    noAudio = True,
    filename='./Low_MS/Dark/18.mp4',
    ori=0, pos=(0, 0), opacity=1, 
    loop=False, 
    depth=0.0,
    )

Video19 = visual.MovieStim3(
    win=win, name='Video_19',
    size = (1920,1080),
    noAudio = True,
    filename='./Low_MS/Dark/19.mp4',
    ori=0, pos=(0, 0), opacity=1, 
    loop=False, 
    depth=0.0,
    )

Video20 = visual.MovieStim3(
    win=win, name='Video_20',
    size = (1920,1080),
    noAudio = True,
    filename='./Low_MS/Dark/20.mp4',
    ori=0, pos=(0, 0), opacity=1, 
    loop=False, 
    depth=0.0,
    )

# "mean_rating" for mean rating of eye-strain
Mean_rt_txt = visual.TextStim(win=win, name='Mean',
        text='영상의 평균적인\n 눈시림(눈의 뻐근함) 정도를\n 표시해주세요',
        font='Arial',
        pos=(0, 0), height=0.06, wrapWidth=None, ori=0, 
        color='black', colorSpace='rgb', opacity=1, 
        languageStyle='LTR', 
        depth=0.0)

Mean_rt_16 = visual.RatingScale(win=win,
        size= 1.0 , pos=(0, -0.7),
        choices = [ '1', '2', '3', '4', '5', '6', '7'],
        singleClick = True, 
        scale=None, showAccept=False,
        marker = 'circle', mouseOnly = True )

Mean_rt_17= visual.RatingScale(win=win,
        size= 1.0 , pos=(0, -0.7),
        choices = [ '1', '2', '3', '4', '5', '6', '7'],
        singleClick = True, 
        scale=None, showAccept=False,
        marker = 'circle', mouseOnly = True )

Mean_rt_18 = visual.RatingScale(win=win,
        size= 1.0 , pos=(0, -0.7),
        choices = [ '1', '2', '3', '4', '5', '6', '7'],
        singleClick = True, 
        scale=None, showAccept=False,
        marker = 'circle', mouseOnly = True )

Mean_rt_19 = visual.RatingScale(win=win,
        size= 1.0 , pos=(0, -0.7),
        choices = [ '1', '2', '3', '4', '5', '6', '7'],
        singleClick = True, 
        scale=None, showAccept=False,
        marker = 'circle', mouseOnly = True )

Mean_rt_20 = visual.RatingScale(win=win,
        size= 1.0 , pos=(0, -0.7),
        choices = [ '1', '2', '3', '4', '5', '6', '7'],
        singleClick = True, 
        scale=None, showAccept=False,
        marker = 'circle', mouseOnly = True )


# "slider4" for real-time rating
slider4 = visual.Slider(win=win, name='slider4',      
    size=(0.8, 0.05), pos=(0, -0.4), units=None, 
    labels=('Very Low','Medium','Very High'), ticks=(1, 2, 3, 4, 5, 6, 7),
    granularity=0, style=['triangleMarker'],
    color='white', font='HelveticaBold', depth=-8.0,
    flip=False, labelHeight = .03)


# VFSQ for trial4
ratingscale4_1 = visual.RatingScale(win=win,
    size= 1  , pos=(0.3, 0.8),
    choices = [ '1', '2', '3', '4', '5', '6', '7'],
    singleClick = True, 
    scale=None, showAccept=False,
    marker = 'circle', mouseOnly = True )

ratingscale4_2 = visual.RatingScale(win=win,
    size= 1 , pos=(0.3, 0.4),
    choices = [ '1', '2', '3', '4', '5', '6', '7'],
    singleClick = True, 
    scale=None, showAccept=False,
    marker = 'circle', mouseOnly = True )


ratingscale4_3 = visual.RatingScale(win=win,
    size= 1, pos=(0.3, 0),
    choices = [ '1', '2', '3', '4', '5', '6', '7'],
    singleClick = True, 
    scale=None, showAccept=False,
    marker = 'circle', mouseOnly = True )

ratingscale4_4 = visual.RatingScale(win=win,
    size= 1 , pos=(0.3, -0.4),
    choices = [ '1', '2', '3', '4', '5', '6', '7'],
    singleClick = True, 
    scale=None, showAccept=False,
    marker = 'circle', mouseOnly = True )

ratingscale4_5 = visual.RatingScale(win=win,
    size= 1 , pos=(0.3, -0.8),
    choices = [ '1', '2', '3', '4', '5', '6', '7'],
    singleClick = True, 
    scale=None, showAccept=False,
    marker = 'circle', mouseOnly = True )

ratingscale4_6 = visual.RatingScale(win=win,
    size= 1 , pos=(0.3, 0.8),
    choices = [ '1', '2', '3', '4', '5', '6', '7'],
    singleClick = True,
    scale=None, showAccept=False,
    marker = 'circle', mouseOnly = True )

ratingscale4_7 = visual.RatingScale(win=win,
    size= 1 , pos=(0.3, 0.4),
    choices = [ '1', '2', '3', '4', '5', '6', '7'],
    singleClick = True, 
    scale=None, showAccept=False,
    marker = 'circle', mouseOnly = True )

ratingscale4_8 = visual.RatingScale(win=win,
    size= 1 , pos=(0.3, 0),
    choices = [ '1', '2', '3', '4', '5', '6', '7'],
    singleClick = True, 
    scale=None, showAccept=False,
    marker = 'circle', mouseOnly = True )

ratingscale4_9 = visual.RatingScale(win=win,
    size= 1 , pos=(0.3, -0.4),
    choices = [ '1', '2', '3', '4', '5', '6', '7'],
    singleClick = True, 
    scale=None, showAccept=False,
    marker = 'circle', mouseOnly = True )

ratingscale4_10 = visual.RatingScale(win=win,
    size= 1 , pos=(0.3, -0.8),
    choices = [ '1', '2', '3', '4', '5', '6', '7'],
    singleClick = True, 
    scale=None, showAccept=False,
    marker = 'circle', mouseOnly = True )

ratingscale4_11 = visual.RatingScale(win=win,
    size= 1 , pos=(0.3, 0.8),
    choices = [ '1', '2', '3', '4', '5', '6', '7'],
    singleClick = True, 
    scale=None, showAccept=False,
    marker = 'circle', mouseOnly = True )

ratingscale4_12 = visual.RatingScale(win=win,
    size= 1 , pos=(0.3, 0.4),
    choices = [ '1', '2', '3', '4', '5', '6', '7'],
    singleClick = True,  
    scale=None, showAccept=False,
    marker = 'circle', mouseOnly = True )

ratingscale4_13 = visual.RatingScale(win=win,
    size= 1 , pos=(0.3, 0),
    choices = [ '1', '2', '3', '4', '5', '6', '7'],
    singleClick = True, 
    scale=None, showAccept=False,
    marker = 'circle', mouseOnly = True )

ratingscale4_14 = visual.RatingScale(win=win,
    size= 1 , pos=(0.3, -0.4),
    choices = [ '1', '2', '3', '4', '5', '6', '7'],
    singleClick = True, 
    scale=None, showAccept=False,
    marker = 'circle', mouseOnly = True )

ratingscale4_15 = visual.RatingScale(win=win,
    size= 1 , pos=(0.3, -0.8),
    choices = [ '1', '2', '3', '4', '5', '6', '7'],
    singleClick = True, 
    scale=None, showAccept=False,
    marker = 'circle', mouseOnly = True )

ratingscale4_16 = visual.RatingScale(win=win,
    size= 1 , pos=(0.3, 0.8),
    choices = [ '1', '2', '3', '4', '5', '6', '7'],
    singleClick = True,
    scale=None, showAccept=False,
    marker = 'circle', mouseOnly = True )

ratingscale4_17 = visual.RatingScale(win=win,
    size= 1 , pos=(0.3, 0.4),
    choices = [ '1', '2', '3', '4', '5', '6', '7'],
    singleClick = True, 
    scale=None, showAccept=False,
    marker = 'circle', mouseOnly = True )

ratingscale4_18 = visual.RatingScale(win=win,
    size= 1 , pos=(0.3, 0),
    choices = [ '1', '2', '3', '4', '5', '6', '7'],
    singleClick = True,
    scale=None, showAccept=False,
    marker = 'circle', mouseOnly = True )

ratingscale4_19 = visual.RatingScale(win=win,
    size= 1 , pos=(0.3, -0.4),
    choices = [ '1', '2', '3', '4', '5', '6', '7'],
    singleClick = True, 
    scale=None, showAccept=False,
    marker = 'circle', mouseOnly = True )

ratingscale4_20 = visual.RatingScale(win=win,
    size= 1 , pos=(0.3, -0.8),
    choices = [ '1', '2', '3', '4', '5', '6', '7'],
    singleClick = True,
    scale=None, showAccept=False,
    marker = 'circle', mouseOnly = True )

ratingscale4_21 = visual.RatingScale(win=win,
    size= 1 , pos=(0.3, 0.8),
    choices = [ '1', '2', '3', '4', '5', '6', '7'],
    singleClick = True, 
    scale=None, showAccept=False,
    marker = 'circle', mouseOnly = True )

ratingscale4_22 = visual.RatingScale(win=win,
    size= 1 , pos=(0.3, 0.4),
    choices = [ '1', '2', '3', '4', '5', '6', '7'],
    singleClick = True,  
    scale=None, showAccept=False,
    marker = 'circle', mouseOnly = True )

ratingscale4_23 = visual.RatingScale(win=win,
    size= 1 , pos=(0.3, 0),
    choices = [ '1', '2', '3', '4', '5', '6', '7'],
    singleClick = True, 
    scale=None, showAccept=False,
    marker = 'circle', mouseOnly = True )

ratingscale4_24 = visual.RatingScale(win=win,
    size= 1 , pos=(0.3, -0.4),
    choices = [ '1', '2', '3', '4', '5', '6', '7'],
    singleClick = True, 
    scale=None, showAccept=False,
    marker = 'circle', mouseOnly = True )

ratingscale4_25 = visual.RatingScale(win=win,
    size= 1 , pos=(0.3, -0.8),
    choices = [ '1', '2', '3', '4', '5', '6', '7'],
    singleClick = True, 
    scale=None, showAccept=False,
    marker = 'circle', mouseOnly = True )

ratingscale4_26 = visual.RatingScale(win=win,
    size= 1 , pos=(0.3, 0.6),
    choices = [ '1', '2', '3', '4', '5', '6', '7'],
    singleClick = True, 
    scale=None, showAccept=False,
    marker = 'circle', mouseOnly = True )

ratingscale4_27 = visual.RatingScale(win=win,
    size= 1 , pos=(0.3, 0),
    choices = [ '1', '2', '3', '4', '5', '6', '7'],
    singleClick = True, 
    scale=None, showAccept=False,
    marker = 'circle', mouseOnly = True )

ratingscale4_28 = visual.RatingScale(win=win,
    size= 1 , pos=(0.3, -0.6),
    choices = [ '1', '2', '3', '4', '5', '6', '7'],
    singleClick = True, 
    scale=None, showAccept=False,
    marker = 'circle', mouseOnly = True )


# Trial Shuffle

cat_dic = { 'HMHB' : [Video1, Video2, Video3, Video4, Video5] , "HMLB" : [Video6, Video7, Video8, Video9, Video10], "LMHB" : [Video11, Video12, Video13, Video14, Video15], "LMLB" : [Video16, Video17, Video18, Video19, Video20] }

Count_bal = []

for list_ in permutations( cat_dic ) :
    Count_bal.append( list_ )
 
Count_bal = np.array(Count_bal)

# Video Suffle
Trial1 = cat_dic[ Count_bal[ int( expInfo['Block'])-1, 0 ]  ] 
Trial2 = cat_dic[ Count_bal[ int( expInfo['Block'])-1, 1 ]  ] 
Trial3 = cat_dic[ Count_bal[ int( expInfo['Block'])-1, 2 ]  ] 
Trial4 = cat_dic[ Count_bal[ int( expInfo['Block'])-1, 3 ]  ] 

random.shuffle(Trial1)
random.shuffle(Trial2)
random.shuffle(Trial3)
random.shuffle(Trial4)




# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 


#/////////////////////// Routine Introduction ///////////////////////////////////////#


# ------Prepare to start Routine "Introduciton"-------
continueRoutine = True
routineTimer.add(155.0) # 95s

# update component parameters for each repeat
# keep track of which components have finished
IntroComponents = [Intro,Break_time,\
    VFSQ1, VFSQ2, VFSQ3, VFSQ4, VFSQ5, VFSQ6, VFSQ7,VFSQ8, VFSQ9, VFSQ10, VFSQ11, VFSQ12, VFSQ13, VFSQ14, VFSQ15, VFSQ16, VFSQ17, VFSQ18, VFSQ19, VFSQ20, VFSQ21,VFSQ22, VFSQ23, VFSQ24, VFSQ25, VFSQ26, VFSQ27, VFSQ28, \
    ratingscale0_1, ratingscale0_2, ratingscale0_3, ratingscale0_4, ratingscale0_5, ratingscale0_6, ratingscale0_7, ratingscale0_8, ratingscale0_9, ratingscale0_10, ratingscale0_11, ratingscale0_12, ratingscale0_13, ratingscale0_14, \
    ratingscale0_15, ratingscale0_16, ratingscale0_17, ratingscale0_18, ratingscale0_19, ratingscale0_20, ratingscale0_21, ratingscale0_22, ratingscale0_23, ratingscale0_24, ratingscale0_25, ratingscale0_26, ratingscale0_27, ratingscale0_28]

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


# -------Run Routine "Introduction"-------    
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

        VFSQ6.setAutoDraw(True)
        VFSQ7.setAutoDraw(True)
        VFSQ8.setAutoDraw(True)
        VFSQ9.setAutoDraw(True)
        VFSQ10.setAutoDraw(True)
        ratingscale0_6.setAutoDraw(True)
        ratingscale0_7.setAutoDraw(True)
        ratingscale0_8.setAutoDraw(True)
        ratingscale0_9.setAutoDraw(True)
        ratingscale0_10.setAutoDraw(True)
    
    if tThisFlip >= 45.0 - frameTolerance : # 25s

        VFSQ6.setAutoDraw(False)
        VFSQ7.setAutoDraw(False)
        VFSQ8.setAutoDraw(False)
        VFSQ9.setAutoDraw(False)
        VFSQ10.setAutoDraw(False)
        ratingscale0_6.setAutoDraw(False)
        ratingscale0_7.setAutoDraw(False)
        ratingscale0_8.setAutoDraw(False)
        ratingscale0_9.setAutoDraw(False)
        ratingscale0_10.setAutoDraw(False)

        VFSQ11.setAutoDraw(True)
        VFSQ12.setAutoDraw(True)
        VFSQ13.setAutoDraw(True)
        VFSQ14.setAutoDraw(True)
        VFSQ15.setAutoDraw(True)
        ratingscale0_11.setAutoDraw(True)
        ratingscale0_12.setAutoDraw(True)
        ratingscale0_13.setAutoDraw(True)
        ratingscale0_14.setAutoDraw(True)
        ratingscale0_15.setAutoDraw(True)


    if tThisFlip >= 65.0 - frameTolerance : # 35s

        VFSQ11.setAutoDraw(False)
        VFSQ12.setAutoDraw(False)
        VFSQ13.setAutoDraw(False)
        VFSQ14.setAutoDraw(False)
        VFSQ15.setAutoDraw(False)
        ratingscale0_11.setAutoDraw(False)
        ratingscale0_12.setAutoDraw(False)
        ratingscale0_13.setAutoDraw(False)
        ratingscale0_14.setAutoDraw(False)
        ratingscale0_15.setAutoDraw(False)

        VFSQ16.setAutoDraw(True)
        VFSQ17.setAutoDraw(True)
        VFSQ18.setAutoDraw(True)
        VFSQ19.setAutoDraw(True)
        VFSQ20.setAutoDraw(True)
        ratingscale0_16.setAutoDraw(True)
        ratingscale0_17.setAutoDraw(True)
        ratingscale0_18.setAutoDraw(True)
        ratingscale0_19.setAutoDraw(True)
        ratingscale0_20.setAutoDraw(True)         
    
    if tThisFlip >= 85.0 - frameTolerance : #45s

        VFSQ16.setAutoDraw(False)
        VFSQ17.setAutoDraw(False)
        VFSQ18.setAutoDraw(False)
        VFSQ19.setAutoDraw(False)
        VFSQ20.setAutoDraw(False)          
        ratingscale0_16.setAutoDraw(False)
        ratingscale0_17.setAutoDraw(False)
        ratingscale0_18.setAutoDraw(False)
        ratingscale0_19.setAutoDraw(False)
        ratingscale0_20.setAutoDraw(False)     

        VFSQ21.setAutoDraw(True)
        VFSQ22.setAutoDraw(True)
        VFSQ23.setAutoDraw(True)
        VFSQ24.setAutoDraw(True)
        VFSQ25.setAutoDraw(True)
        ratingscale0_21.setAutoDraw(True)
        ratingscale0_22.setAutoDraw(True)
        ratingscale0_23.setAutoDraw(True)
        ratingscale0_24.setAutoDraw(True)
        ratingscale0_25.setAutoDraw(True)

    if tThisFlip >= 105.0 - frameTolerance : # 55s 

        VFSQ21.setAutoDraw(False)
        VFSQ22.setAutoDraw(False)
        VFSQ23.setAutoDraw(False)
        VFSQ24.setAutoDraw(False)
        VFSQ25.setAutoDraw(False)
        ratingscale0_21.setAutoDraw(False)
        ratingscale0_22.setAutoDraw(False)
        ratingscale0_23.setAutoDraw(False)
        ratingscale0_24.setAutoDraw(False)
        ratingscale0_25.setAutoDraw(False)

        VFSQ26.setAutoDraw(True)
        VFSQ27.setAutoDraw(True)
        VFSQ28.setAutoDraw(True)
        ratingscale0_26.setAutoDraw(True)
        ratingscale0_27.setAutoDraw(True)
        ratingscale0_28.setAutoDraw(True)

    if tThisFlip >= 125.0 - frameTolerance : # 65s

        VFSQ26.setAutoDraw(False)
        VFSQ27.setAutoDraw(False)
        VFSQ28.setAutoDraw(False)
        ratingscale0_26.setAutoDraw(False)
        ratingscale0_27.setAutoDraw(False)
        ratingscale0_28.setAutoDraw(False)

        Break_time.setAutoDraw(True)
        VFSQ_before = [ratingscale0_1.getRating(), ratingscale0_2.getRating(), ratingscale0_3.getRating(), ratingscale0_4.getRating(), ratingscale0_5.getRating(), \
                                ratingscale0_6.getRating(), ratingscale0_7.getRating(), ratingscale0_8.getRating(), ratingscale0_9.getRating(), ratingscale0_10.getRating(), ratingscale0_11.getRating(), \
                                ratingscale0_12.getRating(), ratingscale0_13.getRating(), ratingscale0_14.getRating(), ratingscale0_15.getRating(), ratingscale0_16.getRating(), ratingscale0_17.getRating(), \
                                ratingscale0_18.getRating(), ratingscale0_19.getRating(), ratingscale0_20.getRating(), ratingscale0_21.getRating(), ratingscale0_22.getRating(), ratingscale0_23.getRating(), \
                                ratingscale0_24.getRating(), ratingscale0_25.getRating(), ratingscale0_26.getRating(), ratingscale0_27.getRating(), ratingscale0_28.getRating() ]
    
    if tThisFlip > 155.0 -frameTolerance : # 95s

        Break_time.setAutoDraw(False)

        
    
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




#//////////////////////////////////////////// Routine Trial1 ///////////////////////////////////////////////////////////////#


# ------Prepare to start Routine "Trial1"-------

continueRoutine = True
routineTimer.add(800.5) # 850.5s

# update component parameters for each repeat
#slider.reset()
# keep track of which components have finished
TrialComponents = [Trial1[0], Trial1[1], Trial1[2], Trial1[3], Trial1[4], slider1, Mean_rt_txt, Mean_rt_1, Mean_rt_2, Mean_rt_3, Mean_rt_4, Mean_rt_5, Break_time, \
                VFSQ1, VFSQ2, VFSQ3, VFSQ4, VFSQ5, VFSQ6, VFSQ7,VFSQ8, VFSQ9, VFSQ10, VFSQ11, VFSQ12, VFSQ13, VFSQ14, VFSQ15, VFSQ16, VFSQ17, VFSQ18, VFSQ19, VFSQ20, VFSQ21,VFSQ22, VFSQ23, VFSQ24, VFSQ25, VFSQ26, VFSQ27, VFSQ28,\
                ratingscale1_1, ratingscale1_2, ratingscale1_3, ratingscale1_4, ratingscale1_5, ratingscale1_6, ratingscale1_7, ratingscale1_8, ratingscale1_9, ratingscale1_10, ratingscale1_11, ratingscale1_12, ratingscale1_13, ratingscale1_14, \
                ratingscale1_15, ratingscale1_16, ratingscale1_17, ratingscale1_18, ratingscale1_19, ratingscale1_20, ratingscale1_21, ratingscale1_22, ratingscale1_23, ratingscale1_24, ratingscale1_25, ratingscale1_26, ratingscale1_27, ratingscale1_28]

for thisComponent in TrialComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Trial1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# Empty DataFrame creating
data_save_1 = { 'Order' : [] ,'Time' : [] , 'Rating' : [] }
detect_mv_1 = 0

# -------Run Routine "Trial1"-------
while continueRoutine and routineTimer.getTime() > 0:

    # get current time
    t = Trial1Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Trial1Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame


######################### Video1 #####################################

    # Vidoe1 updates
    if Trial1[0].status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:  

        # keep track of start time/frame for later
        Trial1[0].frameNStart = frameN  # exact frame index
        Trial1[0].tStart = t  # local t and not account for scr refresh
        Trial1[0].tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Trial1[0], 'tStartRefresh')  # time at next scr refresh

        Trial1[0].setAutoDraw(True)
        slider1.setAutoDraw(True)
        slider1.marker.size = 0.03
        slider1.markerPos = 4

        i_video1 = 1



    if Trial1[0].status == STARTED :

        # Save data in DataFrame
        data_save_1['Order'].append(f'{Trial1[0].name}_{i_video1}')
        data_save_1['Time'].append(tThisFlip - Trial1[0].tStart )
        data_save_1['Rating'].append(slider1.markerPos)

        i_video1 += 1
        

        # is it time to stop? (based on local clock)
        if tThisFlip > 120.0-frameTolerance: # 120s

            # keep track of stop time/frame for later
            Trial1[0].frameNStop = frameN  # exact frame index
            Trial1[0].tStop = t  # not accounting for scr refresh
            Trial1[0].tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Trial1[0], 'tStopRefresh')  # time at next scr refresh

            Trial1[0].setAutoDraw(False)
            slider1.setAutoDraw(False)

            Mean_rt_txt.setAutoDraw(True)
            Mean_rt_1.setAutoDraw(True)

            
    if tThisFlip > 130.0-frameTolerance :  # 130s
        mean_1 = Mean_rt_1.getRating()
        



        
######################### Video2 #####################################    

    # Video2 updates            
    if Trial1[1].status == NOT_STARTED and tThisFlip >= 130.0-frameTolerance:   # 130s

        # keep track of start time/frame for later
        Trial1[1].frameNStart = frameN  # exact frame index
        Trial1[1].tStart = t  # local t and not account for scr refresh
        Trial1[1].tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Trial1[1], 'tStartRefresh')  # time at next scr refresh

        Mean_rt_txt.setAutoDraw(False)
        Mean_rt_1.setAutoDraw(False)

        Trial1[1].setAutoDraw(True)
        slider1.setAutoDraw(True)
        slider1.marker.size = 0.03
        slider1.markerPos = 4
        i_video2 = 1
    

    if Trial1[1].status == STARTED :

        # Save data in DataFrame
        data_save_1['Order'].append(f'{Trial1[1].name}_{i_video2}')
        data_save_1['Time'].append(tThisFlip - Trial1[1].tStart )
        data_save_1['Rating'].append(slider1.markerPos)

        i_video2 += 1


        # is it time to stop? (based on local clock)
        if tThisFlip > 250-frameTolerance:  # 250s
            # keep track of stop time/frame for later
            Trial1[1].frameNStop = frameN  # exact frame index
            Trial1[1].tStop = t  # not accounting for scr refresh
            win.timeOnFlip(Trial1[1], 'tStopRefresh')  # time at next scr refresh

            Trial1[1].setAutoDraw(False)
            slider1.setAutoDraw(False)

            Mean_rt_txt.setAutoDraw(True)
            Mean_rt_2.setAutoDraw(True)

    if tThisFlip > 260.0-frameTolerance : # 260s
        mean_2 = Mean_rt_2.getRating()



######################### Video3 #####################################    

    #Video3 updates  
    if Trial1[2].status == NOT_STARTED and tThisFlip >= 260.0-frameTolerance:  #260s

        # keep track of start time/frame for later
        Trial1[2].frameNStart = frameN  # exact frame index
        Trial1[2].tStart = t  # local t and not account for scr refresh
        Trial1[2].tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Trial1[2], 'tStartRefresh')  # time at next scr refresh

        Mean_rt_txt.setAutoDraw(False)
        Mean_rt_2.setAutoDraw(False)

        Trial1[2].setAutoDraw(True)
        slider1.setAutoDraw(True)
        slider1.marker.size = 0.03
        slider1.markerPos = 4
        
        i_video3 = 1

    if Trial1[2].status == STARTED :

        # Save data in DataFrame
        data_save_1['Order'].append(f'{Trial1[2].name}_{i_video3}')
        data_save_1['Time'].append(tThisFlip - Trial1[2].tStart )
        data_save_1['Rating'].append(slider1.markerPos)

        i_video3 += 1

        # is it time to stop? (based on local clock)
        if tThisFlip > 380-frameTolerance: # 380s
            # keep track of stop time/frame for later
            Trial1[2].frameNStop = frameN  # exact frame index
            Trial1[2].tStop = t  # not accounting for scr refresh
            win.timeOnFlip(Trial1[2], 'tStopRefresh')  # time at next scr refresh

            Trial1[2].setAutoDraw(False)
            slider1.setAutoDraw(False)

            Mean_rt_txt.setAutoDraw(True)
            Mean_rt_3.setAutoDraw(True)

    if tThisFlip > 390.0-frameTolerance : # 390s
        mean_3 = Mean_rt_3.getRating()



########################## Video4 #####################################    

    # Video4 updates
    if Trial1[3].status == NOT_STARTED and tThisFlip >= 390.0-frameTolerance:  #390s
        # keep track of start time/frame for later
        Trial1[3].frameNStart = frameN  # exact frame index
        Trial1[3].tStart = t  # local t and not account for scr refresh
        Trial1[3].tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Trial1[3], 'tStartRefresh')  # time at next scr refresh

        Mean_rt_txt.setAutoDraw(False)
        Mean_rt_3.setAutoDraw(False)

        Trial1[3].setAutoDraw(True)
        slider1.setAutoDraw(True)
        slider1.marker.size = 0.03
        slider1.markerPos = 4

        i_video4 = 1

    if Trial1[3].status == STARTED :

        # Save data in DataFrame
        data_save_1['Order'].append(f'{Trial1[3].name}_{i_video4}')
        data_save_1['Time'].append(tThisFlip - Trial1[3].tStart )
        data_save_1['Rating'].append(slider1.markerPos)

        i_video4 += 1

        # is it time to stop? (based on local clock)
        if tThisFlip > 510-frameTolerance: # 510s
            # keep track of stop time/frame for later
            Trial1[3].frameNStop = frameN  # exact frame index
            Trial1[3].tStop = t  # not accounting for scr refresh
            win.timeOnFlip(Trial1[3], 'tStopRefresh')  # time at next scr refresh

            Trial1[3].setAutoDraw(False)
            slider1.setAutoDraw(False)

            Mean_rt_txt.setAutoDraw(True)
            Mean_rt_4.setAutoDraw(True)

    if tThisFlip > 520.0-frameTolerance : #520s
        mean_4 = Mean_rt_4.getRating()


########################## Video5 #####################################    

    # Video5 updates
    if Trial1[4].status == NOT_STARTED and tThisFlip >= 520.0-frameTolerance:  #520s
        # keep track of start time/frame for later
        Trial1[4].frameNStart = frameN  # exact frame index
        Trial1[4].tStart = t  # local t and not account for scr refresh
        Trial1[4].tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Trial1[4], 'tStartRefresh')  # time at next scr refresh

        Mean_rt_txt.setAutoDraw(False)
        Mean_rt_4.setAutoDraw(False)

        Trial1[4].setAutoDraw(True)
        slider1.setAutoDraw(True)
        slider1.marker.size = 0.03
        slider1.markerPos = 4

        i_video5 = 1

    if Trial1[4].status == STARTED :

        # Save data in DataFrame
        data_save_1['Order'].append(f'{Trial1[4].name}_{i_video5}')
        data_save_1['Time'].append(tThisFlip - Trial1[4].tStart )
        data_save_1['Rating'].append(slider1.markerPos)

        i_video5 += 1

        # is it time to stop? (based on local clock)
        if tThisFlip > 640-frameTolerance: # 640s
            # keep track of stop time/frame for later
            Trial1[4].frameNStop = frameN  # exact frame index
            Trial1[4].tStop = t  # not accounting for scr refresh
            win.timeOnFlip(Trial1[4], 'tStopRefresh')  # time at next scr refresh

            Trial1[4].setAutoDraw(False)
            slider1.setAutoDraw(False)

            Mean_rt_txt.setAutoDraw(True)
            Mean_rt_5.setAutoDraw(True)

    if tThisFlip > 650.0 -frameTolerance : #650s
        mean_5 = Mean_rt_5.getRating()



######################## VFSQ1 ######################################

    if tThisFlip >= 650.0 - frameTolerance: # 650s

        Mean_rt_txt.setAutoDraw(False)
        Mean_rt_5.setAutoDraw(False)

        VFSQ1.setAutoDraw(True)
        VFSQ2.setAutoDraw(True)
        VFSQ3.setAutoDraw(True)
        VFSQ4.setAutoDraw(True)
        VFSQ5.setAutoDraw(True)
        ratingscale1_1.setAutoDraw(True)
        ratingscale1_2.setAutoDraw(True)
        ratingscale1_3.setAutoDraw(True)
        ratingscale1_4.setAutoDraw(True)
        ratingscale1_5.setAutoDraw(True)
    
    if tThisFlip >= 670.0 - frameTolerance : # 660s 
        
        VFSQ1.setAutoDraw(False)
        VFSQ2.setAutoDraw(False)
        VFSQ3.setAutoDraw(False)
        VFSQ4.setAutoDraw(False)
        VFSQ5.setAutoDraw(False)
        ratingscale1_1.setAutoDraw(False)
        ratingscale1_2.setAutoDraw(False)
        ratingscale1_3.setAutoDraw(False)
        ratingscale1_4.setAutoDraw(False)
        ratingscale1_5.setAutoDraw(False)

        VFSQ6.setAutoDraw(True)
        VFSQ7.setAutoDraw(True)
        VFSQ8.setAutoDraw(True)
        VFSQ9.setAutoDraw(True)
        VFSQ10.setAutoDraw(True)
        ratingscale1_6.setAutoDraw(True)
        ratingscale1_7.setAutoDraw(True)
        ratingscale1_8.setAutoDraw(True)
        ratingscale1_9.setAutoDraw(True)
        ratingscale1_10.setAutoDraw(True)
    
    if tThisFlip >= 690.0 - frameTolerance : # 670s

        VFSQ6.setAutoDraw(False)
        VFSQ7.setAutoDraw(False)
        VFSQ8.setAutoDraw(False)
        VFSQ9.setAutoDraw(False)
        VFSQ10.setAutoDraw(False)
        ratingscale1_6.setAutoDraw(False)
        ratingscale1_7.setAutoDraw(False)
        ratingscale1_8.setAutoDraw(False)
        ratingscale1_9.setAutoDraw(False)
        ratingscale1_10.setAutoDraw(False)

        VFSQ11.setAutoDraw(True)
        VFSQ12.setAutoDraw(True)
        VFSQ13.setAutoDraw(True)
        VFSQ14.setAutoDraw(True)
        VFSQ15.setAutoDraw(True)
        ratingscale1_11.setAutoDraw(True)
        ratingscale1_12.setAutoDraw(True)
        ratingscale1_13.setAutoDraw(True)
        ratingscale1_14.setAutoDraw(True)
        ratingscale1_15.setAutoDraw(True)


    if tThisFlip >= 710.0 - frameTolerance : # 680s

        VFSQ11.setAutoDraw(False)
        VFSQ12.setAutoDraw(False)
        VFSQ13.setAutoDraw(False)
        VFSQ14.setAutoDraw(False)
        VFSQ15.setAutoDraw(False)
        ratingscale1_11.setAutoDraw(False)
        ratingscale1_12.setAutoDraw(False)
        ratingscale1_13.setAutoDraw(False)
        ratingscale1_14.setAutoDraw(False)
        ratingscale1_15.setAutoDraw(False)

        VFSQ16.setAutoDraw(True)
        VFSQ17.setAutoDraw(True)
        VFSQ18.setAutoDraw(True)
        VFSQ19.setAutoDraw(True)
        VFSQ20.setAutoDraw(True)
        ratingscale1_16.setAutoDraw(True)
        ratingscale1_17.setAutoDraw(True)
        ratingscale1_18.setAutoDraw(True)
        ratingscale1_19.setAutoDraw(True)
        ratingscale1_20.setAutoDraw(True)         
    
    if tThisFlip >= 730.0 - frameTolerance : # 690s

        VFSQ16.setAutoDraw(False)
        VFSQ17.setAutoDraw(False)
        VFSQ18.setAutoDraw(False)
        VFSQ19.setAutoDraw(False)
        VFSQ20.setAutoDraw(False)          
        ratingscale1_16.setAutoDraw(False)
        ratingscale1_17.setAutoDraw(False)
        ratingscale1_18.setAutoDraw(False)
        ratingscale1_19.setAutoDraw(False)
        ratingscale1_20.setAutoDraw(False)     

        VFSQ21.setAutoDraw(True)
        VFSQ22.setAutoDraw(True)
        VFSQ23.setAutoDraw(True)
        VFSQ24.setAutoDraw(True)
        VFSQ25.setAutoDraw(True)
        ratingscale1_21.setAutoDraw(True)
        ratingscale1_22.setAutoDraw(True)
        ratingscale1_23.setAutoDraw(True)
        ratingscale1_24.setAutoDraw(True)
        ratingscale1_25.setAutoDraw(True)

    if tThisFlip >= 750.0 - frameTolerance : # 700s 

        VFSQ21.setAutoDraw(False)
        VFSQ22.setAutoDraw(False)
        VFSQ23.setAutoDraw(False)
        VFSQ24.setAutoDraw(False)
        VFSQ25.setAutoDraw(False)
        ratingscale1_21.setAutoDraw(False)
        ratingscale1_22.setAutoDraw(False)
        ratingscale1_23.setAutoDraw(False)
        ratingscale1_24.setAutoDraw(False)
        ratingscale1_25.setAutoDraw(False)

        VFSQ26.setAutoDraw(True)
        VFSQ27.setAutoDraw(True)
        VFSQ28.setAutoDraw(True)
        ratingscale1_26.setAutoDraw(True)
        ratingscale1_27.setAutoDraw(True)
        ratingscale1_28.setAutoDraw(True)

    if tThisFlip >= 770.0 - frameTolerance : # 710s

        VFSQ26.setAutoDraw(False)
        VFSQ27.setAutoDraw(False)
        VFSQ28.setAutoDraw(False)
        ratingscale1_26.setAutoDraw(False)
        ratingscale1_27.setAutoDraw(False)
        ratingscale1_28.setAutoDraw(False)

        Break_time.setAutoDraw(True)
    
    if tThisFlip > 800.5 - frameTolerance : # 740s

        Break_time.setAutoDraw(False)

    


######################### slider1 #####################################  

    # slider1 updates 
    
    if slider1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:  

        slider1.setAutoDraw(True)

        # slider intialize
        slider1.marker.size = 0.03
        slider1.markerPos = 4


    if slider1.status == STARTED and tThisFlip <= 800.0 - frameTolerance:

        X_pos_1 = joy.getX()*0.021
        slider1.markerPos += X_pos_1

        if X_pos_1 == 0 :
            detect_mv_1 += 1 

        

# check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running

    for thisComponent in TrialComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()


# -------Ending Routine "Trial1"-------
for thisComponent in TrialComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)






#/////////////////////////////////////////////////////////////////////////////// Routine Trial2 //////////////////////////////////////////////////////////////////////////////////////////////////////#


# ------Prepare to start Routine "Trial2"-------

continueRoutine = True
routineTimer.add(800.5) # 740s

# update component parameters for each repeat
#slider.reset()
# keep track of which components have finished
TrialComponents = [Trial2[0], Trial2[1], Trial2[2], Trial2[3], Trial2[4], slider2, Mean_rt_txt, Mean_rt_6, Mean_rt_7, Mean_rt_8, Mean_rt_9, Mean_rt_10, Break_time, \
                VFSQ1, VFSQ2, VFSQ3, VFSQ4, VFSQ5, VFSQ6, VFSQ7,VFSQ8, VFSQ9, VFSQ10, VFSQ11, VFSQ12, VFSQ13, VFSQ14, VFSQ15, VFSQ16, VFSQ17, VFSQ18, VFSQ19, VFSQ20, VFSQ21,VFSQ22, VFSQ23, VFSQ24, VFSQ25, VFSQ26, VFSQ27, VFSQ28,\
                ratingscale2_1, ratingscale2_2, ratingscale2_3, ratingscale2_4, ratingscale2_5, ratingscale2_6, ratingscale2_7, ratingscale2_8, ratingscale2_9, ratingscale2_10, ratingscale2_11, ratingscale2_12, ratingscale2_13, ratingscale2_14, \
                ratingscale2_15, ratingscale2_16, ratingscale2_17, ratingscale2_18, ratingscale2_19, ratingscale2_20, ratingscale2_21, ratingscale2_22, ratingscale2_23, ratingscale2_24, ratingscale2_25, ratingscale2_26, ratingscale2_27, ratingscale2_28]


for thisComponent in TrialComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Trial2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# Empty DataFrame creating
data_save_2 = { 'Order' : [] ,'Time' : [] , 'Rating' : [] }
detect_mv_2 = 0

# -------Run Routine "Trial2"-------
while continueRoutine and routineTimer.getTime() > 0:

    # get current time
    t = Trial2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Trial2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame


######################### Video6 #####################################

    # Vidoe6 updates
    if Trial2[0].status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:  

        # keep track of start time/frame for later
        Trial2[0].frameNStart = frameN  # exact frame index
        Trial2[0].tStart = t  # local t and not account for scr refresh
        Trial2[0].tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Trial2[0], 'tStartRefresh')  # time at next scr refresh

        Trial2[0].setAutoDraw(True)
        slider2.setAutoDraw(True)
        slider2.marker.size = 0.03
        slider2.markerPos = 4

        i_video1 = 1



    if Trial2[0].status == STARTED :

        # Save data in DataFrame
        data_save_2['Order'].append(f'{Trial2[0].name}_{i_video1}')
        data_save_2['Time'].append(tThisFlip - Trial2[0].tStart)
        data_save_2['Rating'].append(slider2.markerPos)

        i_video1 += 1
        

        # is it time to stop? (based on local clock)
        if tThisFlip > 120.0-frameTolerance: # 120s

            # keep track of stop time/frame for later
            Trial2[0].frameNStop = frameN  # exact frame index
            Trial2[0].tStop = t  # not accounting for scr refresh
            Trial2[0].tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Trial2[0], 'tStopRefresh')  # time at next scr refresh

            Trial2[0].setAutoDraw(False)
            slider2.setAutoDraw(False)

            Mean_rt_txt.setAutoDraw(True)
            Mean_rt_6.setAutoDraw(True)

            
    if tThisFlip > 130.0-frameTolerance :  # 130s
        mean_6 = Mean_rt_6.getRating()



        
######################### Video7 #####################################    

    # Video2 updates            
    if Trial2[1].status == NOT_STARTED and tThisFlip >= 130.0-frameTolerance:   # 130s

        # keep track of start time/frame for later
        Trial2[1].frameNStart = frameN  # exact frame index
        Trial2[1].tStart = t  # local t and not account for scr refresh
        Trial2[1].tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Trial2[1], 'tStartRefresh')  # time at next scr refresh

        Mean_rt_txt.setAutoDraw(False)
        Mean_rt_6.setAutoDraw(False)

        Trial2[1].setAutoDraw(True)
        slider2.setAutoDraw(True)
        slider2.marker.size = 0.03
        slider2.markerPos = 4
        i_video2 = 1
    

    if Trial2[1].status == STARTED :

        # Save data in DataFrame
        data_save_2['Order'].append(f'{Trial2[1].name}_{i_video2}')
        data_save_2['Time'].append(tThisFlip - Trial2[1].tStart )
        data_save_2['Rating'].append(slider2.markerPos)

        i_video2 += 1


        # is it time to stop? (based on local clock)
        if tThisFlip > 250-frameTolerance:  # 250s
            # keep track of stop time/frame for later
            Trial2[1].frameNStop = frameN  # exact frame index
            Trial2[1].tStop = t  # not accounting for scr refresh
            win.timeOnFlip(Trial1[1], 'tStopRefresh')  # time at next scr refresh

            Trial2[1].setAutoDraw(False)
            slider2.setAutoDraw(False)

            Mean_rt_txt.setAutoDraw(True)
            Mean_rt_7.setAutoDraw(True)

    if tThisFlip > 260.0-frameTolerance : # 260s
        mean_7 = Mean_rt_7.getRating()



######################### Video8 #####################################    

    #Video3 updates  
    if Trial2[2].status == NOT_STARTED and tThisFlip >= 260.0-frameTolerance:  #260s

        # keep track of start time/frame for later
        Trial2[2].frameNStart = frameN  # exact frame index
        Trial2[2].tStart = t  # local t and not account for scr refresh
        Trial2[2].tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Trial2[2], 'tStartRefresh')  # time at next scr refresh

        Mean_rt_txt.setAutoDraw(False)
        Mean_rt_7.setAutoDraw(False)

        Trial2[2].setAutoDraw(True)
        slider2.setAutoDraw(True)
        slider2.marker.size = 0.03
        slider2.markerPos = 4
        
        i_video3 = 1

    if Trial2[2].status == STARTED :

        # Save data in DataFrame
        data_save_2['Order'].append(f'{Trial2[2].name}_{i_video3}')
        data_save_2['Time'].append(tThisFlip - Trial2[2].tStart)
        data_save_2['Rating'].append(slider2.markerPos)

        i_video3 += 1

        # is it time to stop? (based on local clock)
        if tThisFlip > 380-frameTolerance: # 380s
            # keep track of stop time/frame for later
            Trial2[2].frameNStop = frameN  # exact frame index
            Trial2[2].tStop = t  # not accounting for scr refresh
            win.timeOnFlip(Trial2[2], 'tStopRefresh')  # time at next scr refresh

            Trial2[2].setAutoDraw(False)
            slider2.setAutoDraw(False)

            Mean_rt_txt.setAutoDraw(True)
            Mean_rt_8.setAutoDraw(True)

    if tThisFlip > 390.0-frameTolerance : # 390s
        mean_8 = Mean_rt_8.getRating()



########################## Video9 #####################################    

    # Video4 updates
    if Trial2[3].status == NOT_STARTED and tThisFlip >= 390.0-frameTolerance:  #390s
        # keep track of start time/frame for later
        Trial2[3].frameNStart = frameN  # exact frame index
        Trial2[3].tStart = t  # local t and not account for scr refresh
        Trial2[3].tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Trial2[3], 'tStartRefresh')  # time at next scr refresh

        Mean_rt_txt.setAutoDraw(False)
        Mean_rt_8.setAutoDraw(False)

        Trial2[3].setAutoDraw(True)
        slider2.setAutoDraw(True)
        slider2.marker.size = 0.03
        slider2.markerPos = 4

        i_video4 = 1

    if Trial2[3].status == STARTED :

        # Save data in DataFrame
        data_save_2['Order'].append(f'{Trial2[3].name}_{i_video4}')
        data_save_2['Time'].append(tThisFlip - Trial2[3].tStart)
        data_save_2['Rating'].append(slider2.markerPos)

        i_video4 += 1

        # is it time to stop? (based on local clock)
        if tThisFlip > 510-frameTolerance: # 510s
            # keep track of stop time/frame for later
            Trial2[3].frameNStop = frameN  # exact frame index
            Trial2[3].tStop = t  # not accounting for scr refresh
            win.timeOnFlip(Trial2[3], 'tStopRefresh')  # time at next scr refresh

            Trial2[3].setAutoDraw(False)
            slider2.setAutoDraw(False)

            Mean_rt_txt.setAutoDraw(True)
            Mean_rt_9.setAutoDraw(True)

    if tThisFlip > 520.0 - frameTolerance : #520s
        mean_9 = Mean_rt_9.getRating()


########################## Video10 #####################################    

    # Video5 updates
    if Trial2[4].status == NOT_STARTED and tThisFlip >= 520.0-frameTolerance:  #520s
        # keep track of start time/frame for later
        Trial2[4].frameNStart = frameN  # exact frame index
        Trial2[4].tStart = t  # local t and not account for scr refresh
        Trial2[4].tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Trial2[4], 'tStartRefresh')  # time at next scr refresh

        Mean_rt_txt.setAutoDraw(False)
        Mean_rt_9.setAutoDraw(False)

        Trial2[4].setAutoDraw(True)
        slider2.setAutoDraw(True)
        slider2.marker.size = 0.03
        slider2.markerPos = 4

        i_video5 = 1

    if Trial2[4].status == STARTED :

        # Save data in DataFrame
        data_save_2['Order'].append(f'{Trial2[4].name}_{i_video5}')
        data_save_2['Time'].append(tThisFlip - Trial2[4].tStart )
        data_save_2['Rating'].append(slider2.markerPos)

        i_video5 += 1

        # is it time to stop? (based on local clock)
        if tThisFlip > 640-frameTolerance: # 640s
            # keep track of stop time/frame for later
            Trial2[4].frameNStop = frameN  # exact frame index
            Trial2[4].tStop = t  # not accounting for scr refresh
            win.timeOnFlip(Trial2[4], 'tStopRefresh')  # time at next scr refresh

            Trial2[4].setAutoDraw(False)
            slider2.setAutoDraw(False)

            Mean_rt_txt.setAutoDraw(True)
            Mean_rt_10.setAutoDraw(True)

    if tThisFlip > 650.0 - frameTolerance : #650s
        mean_10 = Mean_rt_10.getRating()


######################## VFSQ2 ######################################

    if tThisFlip >= 650.0 - frameTolerance: # 650s

        Mean_rt_txt.setAutoDraw(False)
        Mean_rt_10.setAutoDraw(False)

        VFSQ1.setAutoDraw(True)
        VFSQ2.setAutoDraw(True)
        VFSQ3.setAutoDraw(True)
        VFSQ4.setAutoDraw(True)
        VFSQ5.setAutoDraw(True)
        ratingscale2_1.setAutoDraw(True)
        ratingscale2_2.setAutoDraw(True)
        ratingscale2_3.setAutoDraw(True)
        ratingscale2_4.setAutoDraw(True)
        ratingscale2_5.setAutoDraw(True)
    
    if tThisFlip >= 670.0 - frameTolerance : # 660s
        
        VFSQ1.setAutoDraw(False)
        VFSQ2.setAutoDraw(False)
        VFSQ3.setAutoDraw(False)
        VFSQ4.setAutoDraw(False)
        VFSQ5.setAutoDraw(False)
        ratingscale2_1.setAutoDraw(False)
        ratingscale2_2.setAutoDraw(False)
        ratingscale2_3.setAutoDraw(False)
        ratingscale2_4.setAutoDraw(False)
        ratingscale2_5.setAutoDraw(False)

        VFSQ6.setAutoDraw(True)
        VFSQ7.setAutoDraw(True)
        VFSQ8.setAutoDraw(True)
        VFSQ9.setAutoDraw(True)
        VFSQ10.setAutoDraw(True)
        ratingscale2_6.setAutoDraw(True)
        ratingscale2_7.setAutoDraw(True)
        ratingscale2_8.setAutoDraw(True)
        ratingscale2_9.setAutoDraw(True)
        ratingscale2_10.setAutoDraw(True)
    
    if tThisFlip >= 690.0 - frameTolerance : # 670s

        VFSQ6.setAutoDraw(False)
        VFSQ7.setAutoDraw(False)
        VFSQ8.setAutoDraw(False)
        VFSQ9.setAutoDraw(False)
        VFSQ10.setAutoDraw(False)
        ratingscale2_6.setAutoDraw(False)
        ratingscale2_7.setAutoDraw(False)
        ratingscale2_8.setAutoDraw(False)
        ratingscale2_9.setAutoDraw(False)
        ratingscale2_10.setAutoDraw(False)

        VFSQ11.setAutoDraw(True)
        VFSQ12.setAutoDraw(True)
        VFSQ13.setAutoDraw(True)
        VFSQ14.setAutoDraw(True)
        VFSQ15.setAutoDraw(True)
        ratingscale2_11.setAutoDraw(True)
        ratingscale2_12.setAutoDraw(True)
        ratingscale2_13.setAutoDraw(True)
        ratingscale2_14.setAutoDraw(True)
        ratingscale2_15.setAutoDraw(True)


    if tThisFlip >= 710.0 - frameTolerance : # 680s

        VFSQ11.setAutoDraw(False)
        VFSQ12.setAutoDraw(False)
        VFSQ13.setAutoDraw(False)
        VFSQ14.setAutoDraw(False)
        VFSQ15.setAutoDraw(False)
        ratingscale2_11.setAutoDraw(False)
        ratingscale2_12.setAutoDraw(False)
        ratingscale2_13.setAutoDraw(False)
        ratingscale2_14.setAutoDraw(False)
        ratingscale2_15.setAutoDraw(False)

        VFSQ16.setAutoDraw(True)
        VFSQ17.setAutoDraw(True)
        VFSQ18.setAutoDraw(True)
        VFSQ19.setAutoDraw(True)
        VFSQ20.setAutoDraw(True)
        ratingscale2_16.setAutoDraw(True)
        ratingscale2_17.setAutoDraw(True)
        ratingscale2_18.setAutoDraw(True)
        ratingscale2_19.setAutoDraw(True)
        ratingscale2_20.setAutoDraw(True)         
    
    if tThisFlip >= 730.0 - frameTolerance : # 690s

        VFSQ16.setAutoDraw(False)
        VFSQ17.setAutoDraw(False)
        VFSQ18.setAutoDraw(False)
        VFSQ19.setAutoDraw(False)
        VFSQ20.setAutoDraw(False)          
        ratingscale2_16.setAutoDraw(False)
        ratingscale2_17.setAutoDraw(False)
        ratingscale2_18.setAutoDraw(False)
        ratingscale2_19.setAutoDraw(False)
        ratingscale2_20.setAutoDraw(False)     

        VFSQ21.setAutoDraw(True)
        VFSQ22.setAutoDraw(True)
        VFSQ23.setAutoDraw(True)
        VFSQ24.setAutoDraw(True)
        VFSQ25.setAutoDraw(True)
        ratingscale2_21.setAutoDraw(True)
        ratingscale2_22.setAutoDraw(True)
        ratingscale2_23.setAutoDraw(True)
        ratingscale2_24.setAutoDraw(True)
        ratingscale2_25.setAutoDraw(True)

    if tThisFlip >= 750.0 - frameTolerance : # 700s 

        VFSQ21.setAutoDraw(False)
        VFSQ22.setAutoDraw(False)
        VFSQ23.setAutoDraw(False)
        VFSQ24.setAutoDraw(False)
        VFSQ25.setAutoDraw(False)
        ratingscale2_21.setAutoDraw(False)
        ratingscale2_22.setAutoDraw(False)
        ratingscale2_23.setAutoDraw(False)
        ratingscale2_24.setAutoDraw(False)
        ratingscale2_25.setAutoDraw(False)

        VFSQ26.setAutoDraw(True)
        VFSQ27.setAutoDraw(True)
        VFSQ28.setAutoDraw(True)
        ratingscale2_26.setAutoDraw(True)
        ratingscale2_27.setAutoDraw(True)
        ratingscale2_28.setAutoDraw(True)

    if tThisFlip >= 770.0 - frameTolerance : # 710s

        VFSQ26.setAutoDraw(False)
        VFSQ27.setAutoDraw(False)
        VFSQ28.setAutoDraw(False)
        ratingscale2_26.setAutoDraw(False)
        ratingscale2_27.setAutoDraw(False)
        ratingscale2_28.setAutoDraw(False)

        Break_time.setAutoDraw(True)
    
    if tThisFlip > 800.5 - frameTolerance : # 740s

        Break_time.setAutoDraw(False)


######################### slider2 #####################################  

    # slider2 updates 
    if slider2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:  

        slider2.setAutoDraw(True)

        # slider intialize
        slider2.marker.size = 0.03
        slider2.markerPos = 4

    if slider2.status == STARTED and tThisFlip <= 800.0 - frameTolerance:

        X_pos_2 = joy.getX()*0.021
        slider2.markerPos += X_pos_2

        if X_pos_2 == 0 :
            detect_mv_2 += 1 


# check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running

    for thisComponent in TrialComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()


# -------Ending Routine "Trial2"-------
for thisComponent in TrialComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)






#/////////////////////////////////////////////////////////////////////////////// Routine Trial3 //////////////////////////////////////////////////////////////////////////////////////////////////////#


# ------Prepare to start Routine "Trial3"-------

continueRoutine = True
routineTimer.add(800.5) # 740s

# update component parameters for each repeat
#slider.reset()
# keep track of which components have finished
TrialComponents = [Trial3[0], Trial3[1], Trial3[2], Trial3[3], Trial3[4], slider3, Mean_rt_txt, Mean_rt_11, Mean_rt_12, Mean_rt_13, Mean_rt_14, Mean_rt_15, Break_time, \
                VFSQ1, VFSQ2, VFSQ3, VFSQ4, VFSQ5, VFSQ6, VFSQ7,VFSQ8, VFSQ9, VFSQ10, VFSQ11, VFSQ12, VFSQ13, VFSQ14, VFSQ15, VFSQ16, VFSQ17, VFSQ18, VFSQ19, VFSQ20, VFSQ21,VFSQ22, VFSQ23, VFSQ24, VFSQ25, VFSQ26, VFSQ27, VFSQ28,\
                ratingscale3_1, ratingscale3_2, ratingscale3_3, ratingscale3_4, ratingscale3_5, ratingscale3_6, ratingscale3_7, ratingscale3_8, ratingscale3_9, ratingscale3_10, ratingscale3_11, ratingscale3_12, ratingscale3_13, ratingscale3_14, \
                ratingscale3_15, ratingscale3_16, ratingscale3_17, ratingscale3_18, ratingscale3_19, ratingscale3_20, ratingscale3_21, ratingscale3_22, ratingscale3_23, ratingscale3_24, ratingscale3_25, ratingscale3_26, ratingscale3_27, ratingscale3_28]


for thisComponent in TrialComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Trial3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# Empty DataFrame creating
data_save_3 = { 'Order' : [] ,'Time' : [] , 'Rating' : [] }
detect_mv_3 = 0

# -------Run Routine "Trial3"-------
while continueRoutine and routineTimer.getTime() > 0:

    # get current time
    t = Trial3Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Trial3Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame


######################### Video11 #####################################

    # Vidoe11 updates
    if Trial3[0].status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:  

        # keep track of start time/frame for later
        Trial3[0].frameNStart = frameN  # exact frame index
        Trial3[0].tStart = t  # local t and not account for scr refresh
        Trial3[0].tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Trial3[0], 'tStartRefresh')  # time at next scr refresh

        Trial3[0].setAutoDraw(True)
        slider3.setAutoDraw(True)
        slider3.marker.size = 0.03
        slider3.markerPos = 4

        i_video1 = 1



    if Trial3[0].status == STARTED :

        # Save data in DataFrame
        data_save_3['Order'].append(f'{Trial3[0].name}_{i_video1}')
        data_save_3['Time'].append(tThisFlip - Trial3[0].tStart)
        data_save_3['Rating'].append(slider3.markerPos)

        i_video1 += 1
        

        # is it time to stop? (based on local clock)
        if tThisFlip > 120.0-frameTolerance: # 120s

            # keep track of stop time/frame for later
            Trial3[0].frameNStop = frameN  # exact frame index
            Trial3[0].tStop = t  # not accounting for scr refresh
            Trial3[0].tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Trial3[0], 'tStopRefresh')  # time at next scr refresh

            Trial3[0].setAutoDraw(False)
            slider3.setAutoDraw(False)

            Mean_rt_txt.setAutoDraw(True)
            Mean_rt_11.setAutoDraw(True)

            
    if tThisFlip > 130.0-frameTolerance :  # 130s
        mean_11 = Mean_rt_11.getRating()
        



        
######################### Video12 #####################################    

    # Video12 updates            
    if Trial3[1].status == NOT_STARTED and tThisFlip >= 130.0-frameTolerance:   # 130s

        # keep track of start time/frame for later
        Trial3[1].frameNStart = frameN  # exact frame index
        Trial3[1].tStart = t  # local t and not account for scr refresh
        Trial3[1].tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Trial3[1], 'tStartRefresh')  # time at next scr refresh

        Mean_rt_txt.setAutoDraw(False)
        Mean_rt_11.setAutoDraw(False)

        Trial3[1].setAutoDraw(True)
        slider3.setAutoDraw(True)
        slider3.marker.size = 0.03
        slider3.markerPos = 4
        i_video2 = 1
    

    if Trial3[1].status == STARTED :

        # Save data in DataFrame
        data_save_3['Order'].append(f'{Trial3[1].name}_{i_video2}')
        data_save_3['Time'].append(tThisFlip - Trial3[1].tStart )
        data_save_3['Rating'].append(slider3.markerPos)

        i_video2 += 1


        # is it time to stop? (based on local clock)
        if tThisFlip > 250-frameTolerance:  # 250s
            # keep track of stop time/frame for later
            Trial3[1].frameNStop = frameN  # exact frame index
            Trial3[1].tStop = t  # not accounting for scr refresh
            win.timeOnFlip(Trial3[1], 'tStopRefresh')  # time at next scr refresh

            Trial3[1].setAutoDraw(False)
            slider3.setAutoDraw(False)

            Mean_rt_txt.setAutoDraw(True)
            Mean_rt_12.setAutoDraw(True)

    if tThisFlip > 260.0-frameTolerance : # 260s
        mean_12 = Mean_rt_12.getRating()



######################### Video13 #####################################    

    #Video3 updates  
    if Trial3[2].status == NOT_STARTED and tThisFlip >= 260.0-frameTolerance:  #260s

        # keep track of start time/frame for later
        Trial3[2].frameNStart = frameN  # exact frame index
        Trial3[2].tStart = t  # local t and not account for scr refresh
        Trial3[2].tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Trial3[2], 'tStartRefresh')  # time at next scr refresh

        Mean_rt_txt.setAutoDraw(False)
        Mean_rt_12.setAutoDraw(False)

        Trial3[2].setAutoDraw(True)
        slider3.setAutoDraw(True)
        slider3.marker.size = 0.03
        slider3.markerPos = 4
        
        i_video3 = 1

    if Trial3[2].status == STARTED :

        # Save data in DataFrame
        data_save_3['Order'].append(f'{Trial3[2].name}_{i_video3}')
        data_save_3['Time'].append(tThisFlip - Trial3[2].tStart )
        data_save_3['Rating'].append(slider3.markerPos)

        i_video3 += 1

        # is it time to stop? (based on local clock)
        if tThisFlip > 380-frameTolerance: # 380s
            # keep track of stop time/frame for later
            Trial3[2].frameNStop = frameN  # exact frame index
            Trial3[2].tStop = t  # not accounting for scr refresh
            win.timeOnFlip(Trial3[2], 'tStopRefresh')  # time at next scr refresh

            Trial3[2].setAutoDraw(False)
            slider3.setAutoDraw(False)

            Mean_rt_txt.setAutoDraw(True)
            Mean_rt_13.setAutoDraw(True)

    if tThisFlip > 390.0-frameTolerance : # 390s
        mean_13 = Mean_rt_13.getRating()



########################## Video14 #####################################    

    # Video4 updates
    if Trial3[3].status == NOT_STARTED and tThisFlip >= 390.0-frameTolerance:  #390s
        # keep track of start time/frame for later
        Trial3[3].frameNStart = frameN  # exact frame index
        Trial3[3].tStart = t  # local t and not account for scr refresh
        Trial3[3].tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Trial3[3], 'tStartRefresh')  # time at next scr refresh

        Mean_rt_txt.setAutoDraw(False)
        Mean_rt_13.setAutoDraw(False)

        Trial3[3].setAutoDraw(True)
        slider3.setAutoDraw(True)
        slider3.marker.size = 0.03
        slider3.markerPos = 4

        i_video4 = 1

    if Trial3[3].status == STARTED :

        # Save data in DataFrame
        data_save_3['Order'].append(f'{Trial3[3].name}_{i_video4}')
        data_save_3['Time'].append(tThisFlip - Trial3[3].tStart)
        data_save_3['Rating'].append(slider3.markerPos)

        i_video4 += 1

        # is it time to stop? (based on local clock)
        if tThisFlip > 510-frameTolerance: # 510s
            # keep track of stop time/frame for later
            Trial3[3].frameNStop = frameN  # exact frame index
            Trial3[3].tStop = t  # not accounting for scr refresh
            win.timeOnFlip(Trial3[3], 'tStopRefresh')  # time at next scr refresh

            Trial3[3].setAutoDraw(False)
            slider3.setAutoDraw(False)

            Mean_rt_txt.setAutoDraw(True)
            Mean_rt_14.setAutoDraw(True)

    if tThisFlip > 520.0 - frameTolerance : #520s
        mean_14 = Mean_rt_14.getRating()


########################## Video15 #####################################    

    # Video15 updates
    if Trial3[4].status == NOT_STARTED and tThisFlip >= 520.0-frameTolerance:  #520s
        # keep track of start time/frame for later
        Trial3[4].frameNStart = frameN  # exact frame index
        Trial3[4].tStart = t  # local t and not account for scr refresh
        Trial3[4].tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Trial3[4], 'tStartRefresh')  # time at next scr refresh

        Mean_rt_txt.setAutoDraw(False)
        Mean_rt_14.setAutoDraw(False)

        Trial3[4].setAutoDraw(True)
        slider3.setAutoDraw(True)
        slider3.marker.size = 0.03
        slider3.markerPos = 4

        i_video5 = 1

    if Trial3[4].status == STARTED :

        # Save data in DataFrame
        data_save_3['Order'].append(f'{Trial3[4].name}{i_video5}')
        data_save_3['Time'].append(tThisFlip - Trial3[4].tStart)
        data_save_3['Rating'].append(slider3.markerPos)

        i_video5 += 1

        # is it time to stop? (based on local clock)
        if tThisFlip > 640-frameTolerance: # 640s
            # keep track of stop time/frame for later
            Trial3[4].frameNStop = frameN  # exact frame index
            Trial3[4].tStop = t  # not accounting for scr refresh
            win.timeOnFlip(Trial3[4], 'tStopRefresh')  # time at next scr refresh

            Trial3[4].setAutoDraw(False)
            slider3.setAutoDraw(False)

            Mean_rt_txt.setAutoDraw(True)
            Mean_rt_15.setAutoDraw(True)

    if tThisFlip > 650.0 - frameTolerance : #650s
        mean_15 = Mean_rt_15.getRating()


######################## VFSQ3 ######################################

    if tThisFlip >= 650.0 - frameTolerance: # 650s

        Mean_rt_txt.setAutoDraw(False)
        Mean_rt_15.setAutoDraw(False)

        VFSQ1.setAutoDraw(True)
        VFSQ2.setAutoDraw(True)
        VFSQ3.setAutoDraw(True)
        VFSQ4.setAutoDraw(True)
        VFSQ5.setAutoDraw(True)
        ratingscale3_1.setAutoDraw(True)
        ratingscale3_2.setAutoDraw(True)
        ratingscale3_3.setAutoDraw(True)
        ratingscale3_4.setAutoDraw(True)
        ratingscale3_5.setAutoDraw(True)
    
    if tThisFlip >= 670.0 - frameTolerance : # 660s
        
        VFSQ1.setAutoDraw(False)
        VFSQ2.setAutoDraw(False)
        VFSQ3.setAutoDraw(False)
        VFSQ4.setAutoDraw(False)
        VFSQ5.setAutoDraw(False)
        ratingscale3_1.setAutoDraw(False)
        ratingscale3_2.setAutoDraw(False)
        ratingscale3_3.setAutoDraw(False)
        ratingscale3_4.setAutoDraw(False)
        ratingscale3_5.setAutoDraw(False)

        VFSQ6.setAutoDraw(True)
        VFSQ7.setAutoDraw(True)
        VFSQ8.setAutoDraw(True)
        VFSQ9.setAutoDraw(True)
        VFSQ10.setAutoDraw(True)
        ratingscale3_6.setAutoDraw(True)
        ratingscale3_7.setAutoDraw(True)
        ratingscale3_8.setAutoDraw(True)
        ratingscale3_9.setAutoDraw(True)
        ratingscale3_10.setAutoDraw(True)
    
    if tThisFlip >= 690.0 - frameTolerance : # 670s

        VFSQ6.setAutoDraw(False)
        VFSQ7.setAutoDraw(False)
        VFSQ8.setAutoDraw(False)
        VFSQ9.setAutoDraw(False)
        VFSQ10.setAutoDraw(False)
        ratingscale3_6.setAutoDraw(False)
        ratingscale3_7.setAutoDraw(False)
        ratingscale3_8.setAutoDraw(False)
        ratingscale3_9.setAutoDraw(False)
        ratingscale3_10.setAutoDraw(False)

        VFSQ11.setAutoDraw(True)
        VFSQ12.setAutoDraw(True)
        VFSQ13.setAutoDraw(True)
        VFSQ14.setAutoDraw(True)
        VFSQ15.setAutoDraw(True)
        ratingscale3_11.setAutoDraw(True)
        ratingscale3_12.setAutoDraw(True)
        ratingscale3_13.setAutoDraw(True)
        ratingscale3_14.setAutoDraw(True)
        ratingscale3_15.setAutoDraw(True)


    if tThisFlip >= 710.0 - frameTolerance : # 680s

        VFSQ11.setAutoDraw(False)
        VFSQ12.setAutoDraw(False)
        VFSQ13.setAutoDraw(False)
        VFSQ14.setAutoDraw(False)
        VFSQ15.setAutoDraw(False)
        ratingscale3_11.setAutoDraw(False)
        ratingscale3_12.setAutoDraw(False)
        ratingscale3_13.setAutoDraw(False)
        ratingscale3_14.setAutoDraw(False)
        ratingscale3_15.setAutoDraw(False)

        VFSQ16.setAutoDraw(True)
        VFSQ17.setAutoDraw(True)
        VFSQ18.setAutoDraw(True)
        VFSQ19.setAutoDraw(True)
        VFSQ20.setAutoDraw(True)
        ratingscale3_16.setAutoDraw(True)
        ratingscale3_17.setAutoDraw(True)
        ratingscale3_18.setAutoDraw(True)
        ratingscale3_19.setAutoDraw(True)
        ratingscale3_20.setAutoDraw(True)         
    
    if tThisFlip >= 730.0 - frameTolerance : # 690s

        VFSQ16.setAutoDraw(False)
        VFSQ17.setAutoDraw(False)
        VFSQ18.setAutoDraw(False)
        VFSQ19.setAutoDraw(False)
        VFSQ20.setAutoDraw(False)          
        ratingscale3_16.setAutoDraw(False)
        ratingscale3_17.setAutoDraw(False)
        ratingscale3_18.setAutoDraw(False)
        ratingscale3_19.setAutoDraw(False)
        ratingscale3_20.setAutoDraw(False)     

        VFSQ21.setAutoDraw(True)
        VFSQ22.setAutoDraw(True)
        VFSQ23.setAutoDraw(True)
        VFSQ24.setAutoDraw(True)
        VFSQ25.setAutoDraw(True)
        ratingscale3_21.setAutoDraw(True)
        ratingscale3_22.setAutoDraw(True)
        ratingscale3_23.setAutoDraw(True)
        ratingscale3_24.setAutoDraw(True)
        ratingscale3_25.setAutoDraw(True)

    if tThisFlip >= 750.0 - frameTolerance : # 700s 

        VFSQ21.setAutoDraw(False)
        VFSQ22.setAutoDraw(False)
        VFSQ23.setAutoDraw(False)
        VFSQ24.setAutoDraw(False)
        VFSQ25.setAutoDraw(False)
        ratingscale3_21.setAutoDraw(False)
        ratingscale3_22.setAutoDraw(False)
        ratingscale3_23.setAutoDraw(False)
        ratingscale3_24.setAutoDraw(False)
        ratingscale3_25.setAutoDraw(False)

        VFSQ26.setAutoDraw(True)
        VFSQ27.setAutoDraw(True)
        VFSQ28.setAutoDraw(True)
        ratingscale3_26.setAutoDraw(True)
        ratingscale3_27.setAutoDraw(True)
        ratingscale3_28.setAutoDraw(True)

    if tThisFlip >= 770.0 - frameTolerance : # 710s

        VFSQ26.setAutoDraw(False)
        VFSQ27.setAutoDraw(False)
        VFSQ28.setAutoDraw(False)
        ratingscale3_26.setAutoDraw(False)
        ratingscale3_27.setAutoDraw(False)
        ratingscale3_28.setAutoDraw(False)

        Break_time.setAutoDraw(True)
    
    if tThisFlip > 800.5 - frameTolerance : # 740s

        Break_time.setAutoDraw(False)


######################### slider3 #####################################  

    # slider3 updates 
    if slider3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:  

        slider3.setAutoDraw(True)

        # slider intialize
        slider3.marker.size = 0.021
        slider3.markerPos = 4

    if slider3.status == STARTED and tThisFlip <= 800.0 - frameTolerance:

        X_pos_3 = joy.getX()*0.021
        slider3.markerPos += X_pos_3

        if X_pos_3 == 0 :
            detect_mv_3 += 1 



#     # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running

    for thisComponent in TrialComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Trial3"-------
for thisComponent in TrialComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)




#/////////////////////////////////////////////////////////////////////////////// Routine Trial4 //////////////////////////////////////////////////////////////////////////////////////////////////////#


# ------Prepare to start Routine "Trial4"-------

continueRoutine = True
routineTimer.add(780.5) # 740s

# update component parameters for each repeat
#slider.reset()
# keep track of which components have finished
TrialComponents = [Trial4[0], Trial4[1], Trial4[2], Trial4[3], Trial4[4], slider4, Mean_rt_txt, Mean_rt_16, Mean_rt_17, Mean_rt_18, Mean_rt_19, Mean_rt_20, Break_time, \
                VFSQ1, VFSQ2, VFSQ3, VFSQ4, VFSQ5, VFSQ6, VFSQ7,VFSQ8, VFSQ9, VFSQ10, VFSQ11, VFSQ12, VFSQ13, VFSQ14, VFSQ15, VFSQ16, VFSQ17, VFSQ18, VFSQ19, VFSQ20, VFSQ21,VFSQ22, VFSQ23, VFSQ24, VFSQ25, VFSQ26, VFSQ27, VFSQ28,\
                ratingscale4_1, ratingscale4_2, ratingscale4_3, ratingscale4_4, ratingscale4_5, ratingscale4_6, ratingscale4_7, ratingscale4_8, ratingscale4_9, ratingscale4_10, ratingscale4_11, ratingscale4_12, ratingscale4_13, ratingscale4_14, \
                ratingscale4_15, ratingscale4_16, ratingscale4_17, ratingscale4_18, ratingscale4_19, ratingscale4_20, ratingscale4_21, ratingscale4_22, ratingscale4_23, ratingscale4_24, ratingscale4_25, ratingscale4_26, ratingscale4_27, ratingscale4_28]


for thisComponent in TrialComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Trial4Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# Empty DataFrame creating
data_save_4 = { 'Order' : [] ,'Time' : [] , 'Rating' : [] }
detect_mv_4 = 0

# -------Run Routine "Trial4"-------
while continueRoutine and routineTimer.getTime() > 0:

    # get current time
    t = Trial4Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Trial4Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame


######################### Video16 #####################################

    # Vidoe16 updates
    if Trial4[0].status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:  

        # keep track of start time/frame for later
        Trial4[0].frameNStart = frameN  # exact frame index
        Trial4[0].tStart = t  # local t and not account for scr refresh
        Trial4[0].tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Trial4[0], 'tStartRefresh')  # time at next scr refresh

        Trial4[0].setAutoDraw(True)
        slider4.setAutoDraw(True)
        slider4.marker.size = 0.03
        slider4.markerPos = 4

        i_video1 = 1



    if Trial4[0].status == STARTED :

        # Save data in DataFrame
        data_save_4['Order'].append(f'{Trial4[0].name}_{i_video1}')
        data_save_4['Time'].append(tThisFlip - Trial4[0].tStart)
        data_save_4['Rating'].append(slider4.markerPos)

        i_video1 += 1
        

        # is it time to stop? (based on local clock)
        if tThisFlip > 120.0-frameTolerance: # 120s

            # keep track of stop time/frame for later
            Trial4[0].frameNStop = frameN  # exact frame index
            Trial4[0].tStop = t  # not accounting for scr refresh
            Trial4[0].tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Trial4[0], 'tStopRefresh')  # time at next scr refresh

            Trial4[0].setAutoDraw(False)
            slider4.setAutoDraw(False)

            Mean_rt_txt.setAutoDraw(True)
            Mean_rt_16.setAutoDraw(True)

            
    if tThisFlip > 130.0-frameTolerance :  # 130s
        mean_16 = Mean_rt_16.getRating()
        



        
######################### Video17 #####################################    

    # Video17 updates            
    if Trial4[1].status == NOT_STARTED and tThisFlip >= 130.0-frameTolerance:   # 130s

        # keep track of start time/frame for later
        Trial4[1].frameNStart = frameN  # exact frame index
        Trial4[1].tStart = t  # local t and not account for scr refresh
        Trial4[1].tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Trial4[1], 'tStartRefresh')  # time at next scr refresh

        Mean_rt_txt.setAutoDraw(False)
        Mean_rt_16.setAutoDraw(False)

        Trial4[1].setAutoDraw(True)
        slider4.setAutoDraw(True)
        slider4.marker.size = 0.03
        slider4.markerPos = 4
        i_video2 = 1
    

    if Trial4[1].status == STARTED :

        # Save data in DataFrame
        data_save_4['Order'].append(f'{Trial4[1].name}_{i_video2}')
        data_save_4['Time'].append(tThisFlip - Trial4[1].tStart)
        data_save_4['Rating'].append(slider4.markerPos)

        i_video2 += 1


        # is it time to stop? (based on local clock)
        if tThisFlip > 250-frameTolerance:  # 250s
            # keep track of stop time/frame for later
            Trial4[1].frameNStop = frameN  # exact frame index
            Trial4[1].tStop = t  # not accounting for scr refresh
            win.timeOnFlip(Trial4[1], 'tStopRefresh')  # time at next scr refresh

            Trial4[1].setAutoDraw(False)
            slider4.setAutoDraw(False)

            Mean_rt_txt.setAutoDraw(True)
            Mean_rt_17.setAutoDraw(True)

    if tThisFlip > 260.0-frameTolerance : # 260s
        mean_17 = Mean_rt_17.getRating()



######################### Video18 #####################################    

    #Video4 updates  
    if Trial4[2].status == NOT_STARTED and tThisFlip >= 260.0-frameTolerance:  #260s

        # keep track of start time/frame for later
        Trial4[2].frameNStart = frameN  # exact frame index
        Trial4[2].tStart = t  # local t and not account for scr refresh
        Trial4[2].tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Trial4[2], 'tStartRefresh')  # time at next scr refresh

        Mean_rt_txt.setAutoDraw(False)
        Mean_rt_17.setAutoDraw(False)

        Trial4[2].setAutoDraw(True)
        slider4.setAutoDraw(True)
        slider4.marker.size = 0.03
        slider4.markerPos = 4
        
        i_video3 = 1

    if Trial4[2].status == STARTED :

        # Save data in DataFrame
        data_save_4['Order'].append(f'{Trial4[2].name}_{i_video3}')
        data_save_4['Time'].append(tThisFlip - Trial4[2].tStart)
        data_save_4['Rating'].append(slider4.markerPos)

        i_video3 += 1

        # is it time to stop? (based on local clock)
        if tThisFlip > 380-frameTolerance: # 380s
            # keep track of stop time/frame for later
            Trial4[2].frameNStop = frameN  # exact frame index
            Trial4[2].tStop = t  # not accounting for scr refresh
            win.timeOnFlip(Trial4[2], 'tStopRefresh')  # time at next scr refresh

            Trial4[2].setAutoDraw(False)
            slider4.setAutoDraw(False)

            Mean_rt_txt.setAutoDraw(True)
            Mean_rt_18.setAutoDraw(True)

    if tThisFlip > 390.0-frameTolerance : # 390s
        mean_18 = Mean_rt_18.getRating()



########################## Video19 #####################################    

    # Video19 updates
    if Trial4[3].status == NOT_STARTED and tThisFlip >= 390.0-frameTolerance:  #390s
        # keep track of start time/frame for later
        Trial4[3].frameNStart = frameN  # exact frame index
        Trial4[3].tStart = t  # local t and not account for scr refresh
        Trial4[3].tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Trial4[3], 'tStartRefresh')  # time at next scr refresh

        Mean_rt_txt.setAutoDraw(False)
        Mean_rt_18.setAutoDraw(False)

        Trial4[3].setAutoDraw(True)
        slider4.setAutoDraw(True)
        slider4.marker.size = 0.03
        slider4.markerPos = 4

        i_video4 = 1

    if Trial4[3].status == STARTED :

        # Save data in DataFrame
        data_save_4['Order'].append(f'{Trial4[3].name}_{i_video4}')
        data_save_4['Time'].append(tThisFlip - Trial4[3].tStart)
        data_save_4['Rating'].append(slider4.markerPos)

        i_video4 += 1

        # is it time to stop? (based on local clock)
        if tThisFlip > 510-frameTolerance: # 510s
            # keep track of stop time/frame for later
            Trial4[3].frameNStop = frameN  # exact frame index
            Trial4[3].tStop = t  # not accounting for scr refresh
            win.timeOnFlip(Trial4[3], 'tStopRefresh')  # time at next scr refresh

            Trial4[3].setAutoDraw(False)
            slider4.setAutoDraw(False)

            Mean_rt_txt.setAutoDraw(True)
            Mean_rt_19.setAutoDraw(True)

    if tThisFlip > 520.0 - frameTolerance : #520s
        mean_19 = Mean_rt_19.getRating()


########################## Video20 #####################################    

    # Video20 updates
    if Trial4[4].status == NOT_STARTED and tThisFlip >= 520.0-frameTolerance:  #520s
        # keep track of start time/frame for later
        Trial4[4].frameNStart = frameN  # exact frame index
        Trial4[4].tStart = t  # local t and not account for scr refresh
        Trial4[4].tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Trial4[4], 'tStartRefresh')  # time at next scr refresh

        Mean_rt_txt.setAutoDraw(False)
        Mean_rt_19.setAutoDraw(False)

        Trial4[4].setAutoDraw(True)
        slider4.setAutoDraw(True)
        slider4.marker.size = 0.03
        slider4.markerPos = 4

        i_video5 = 1

    if Trial4[4].status == STARTED :

        # Save data in DataFrame
        data_save_4['Order'].append(f'{Trial4[4].name}_{i_video5}')
        data_save_4['Time'].append(tThisFlip - Trial4[4].tStart)
        data_save_4['Rating'].append(slider4.markerPos)

        i_video5 += 1

        # is it time to stop? (based on local clock)
        if tThisFlip > 640-frameTolerance: # 640s
            # keep track of stop time/frame for later
            Trial4[4].frameNStop = frameN  # exact frame index
            Trial4[4].tStop = t  # not accounting for scr refresh
            win.timeOnFlip(Trial4[4], 'tStopRefresh')  # time at next scr refresh

            Trial4[4].setAutoDraw(False)
            slider4.setAutoDraw(False)

            Mean_rt_txt.setAutoDraw(True)
            Mean_rt_20.setAutoDraw(True)

    if tThisFlip > 650.0 - frameTolerance : #650s
        mean_20 = Mean_rt_20.getRating()


######################## VFSQ4 ######################################

    if tThisFlip >= 650.0 - frameTolerance: # 650s

        Mean_rt_txt.setAutoDraw(False)
        Mean_rt_20.setAutoDraw(False)

        VFSQ1.setAutoDraw(True)
        VFSQ2.setAutoDraw(True)
        VFSQ3.setAutoDraw(True)
        VFSQ4.setAutoDraw(True)
        VFSQ5.setAutoDraw(True)
        ratingscale4_1.setAutoDraw(True)
        ratingscale4_2.setAutoDraw(True)
        ratingscale4_3.setAutoDraw(True)
        ratingscale4_4.setAutoDraw(True)
        ratingscale4_5.setAutoDraw(True)
    
    if tThisFlip >= 670.0 - frameTolerance : # 660s
        
        VFSQ1.setAutoDraw(False)
        VFSQ2.setAutoDraw(False)
        VFSQ3.setAutoDraw(False)
        VFSQ4.setAutoDraw(False)
        VFSQ5.setAutoDraw(False)
        ratingscale4_1.setAutoDraw(False)
        ratingscale4_2.setAutoDraw(False)
        ratingscale4_3.setAutoDraw(False)
        ratingscale4_4.setAutoDraw(False)
        ratingscale4_5.setAutoDraw(False)

        VFSQ6.setAutoDraw(True)
        VFSQ7.setAutoDraw(True)
        VFSQ8.setAutoDraw(True)
        VFSQ9.setAutoDraw(True)
        VFSQ10.setAutoDraw(True)
        ratingscale4_6.setAutoDraw(True)
        ratingscale4_7.setAutoDraw(True)
        ratingscale4_8.setAutoDraw(True)
        ratingscale4_9.setAutoDraw(True)
        ratingscale4_10.setAutoDraw(True)
    
    if tThisFlip >= 690.0 - frameTolerance : # 670s

        VFSQ6.setAutoDraw(False)
        VFSQ7.setAutoDraw(False)
        VFSQ8.setAutoDraw(False)
        VFSQ9.setAutoDraw(False)
        VFSQ10.setAutoDraw(False)
        ratingscale4_6.setAutoDraw(False)
        ratingscale4_7.setAutoDraw(False)
        ratingscale4_8.setAutoDraw(False)
        ratingscale4_9.setAutoDraw(False)
        ratingscale4_10.setAutoDraw(False)

        VFSQ11.setAutoDraw(True)
        VFSQ12.setAutoDraw(True)
        VFSQ13.setAutoDraw(True)
        VFSQ14.setAutoDraw(True)
        VFSQ15.setAutoDraw(True)
        ratingscale4_11.setAutoDraw(True)
        ratingscale4_12.setAutoDraw(True)
        ratingscale4_13.setAutoDraw(True)
        ratingscale4_14.setAutoDraw(True)
        ratingscale4_15.setAutoDraw(True)


    if tThisFlip >= 710.0 - frameTolerance : # 680s

        VFSQ11.setAutoDraw(False)
        VFSQ12.setAutoDraw(False)
        VFSQ13.setAutoDraw(False)
        VFSQ14.setAutoDraw(False)
        VFSQ15.setAutoDraw(False)
        ratingscale4_11.setAutoDraw(False)
        ratingscale4_12.setAutoDraw(False)
        ratingscale4_13.setAutoDraw(False)
        ratingscale4_14.setAutoDraw(False)
        ratingscale4_15.setAutoDraw(False)

        VFSQ16.setAutoDraw(True)
        VFSQ17.setAutoDraw(True)
        VFSQ18.setAutoDraw(True)
        VFSQ19.setAutoDraw(True)
        VFSQ20.setAutoDraw(True)
        ratingscale4_16.setAutoDraw(True)
        ratingscale4_17.setAutoDraw(True)
        ratingscale4_18.setAutoDraw(True)
        ratingscale4_19.setAutoDraw(True)
        ratingscale4_20.setAutoDraw(True)         
    
    if tThisFlip >= 730.0 - frameTolerance : # 690s

        VFSQ16.setAutoDraw(False)
        VFSQ17.setAutoDraw(False)
        VFSQ18.setAutoDraw(False)
        VFSQ19.setAutoDraw(False)
        VFSQ20.setAutoDraw(False)          
        ratingscale4_16.setAutoDraw(False)
        ratingscale4_17.setAutoDraw(False)
        ratingscale4_18.setAutoDraw(False)
        ratingscale4_19.setAutoDraw(False)
        ratingscale4_20.setAutoDraw(False)     

        VFSQ21.setAutoDraw(True)
        VFSQ22.setAutoDraw(True)
        VFSQ23.setAutoDraw(True)
        VFSQ24.setAutoDraw(True)
        VFSQ25.setAutoDraw(True)
        ratingscale4_21.setAutoDraw(True)
        ratingscale4_22.setAutoDraw(True)
        ratingscale4_23.setAutoDraw(True)
        ratingscale4_24.setAutoDraw(True)
        ratingscale4_25.setAutoDraw(True)

    if tThisFlip >= 750.0 - frameTolerance : # 700s 

        VFSQ21.setAutoDraw(False)
        VFSQ22.setAutoDraw(False)
        VFSQ23.setAutoDraw(False)
        VFSQ24.setAutoDraw(False)
        VFSQ25.setAutoDraw(False)
        ratingscale4_21.setAutoDraw(False)
        ratingscale4_22.setAutoDraw(False)
        ratingscale4_23.setAutoDraw(False)
        ratingscale4_24.setAutoDraw(False)
        ratingscale4_25.setAutoDraw(False)

        VFSQ26.setAutoDraw(True)
        VFSQ27.setAutoDraw(True)
        VFSQ28.setAutoDraw(True)
        ratingscale4_26.setAutoDraw(True)
        ratingscale4_27.setAutoDraw(True)
        ratingscale4_28.setAutoDraw(True)

    if tThisFlip >= 770.0 - frameTolerance : # 710s

        VFSQ26.setAutoDraw(False)
        VFSQ27.setAutoDraw(False)
        VFSQ28.setAutoDraw(False)
        ratingscale4_26.setAutoDraw(False)
        ratingscale4_27.setAutoDraw(False)
        ratingscale4_28.setAutoDraw(False)

        Break_time.setAutoDraw(True)
    
    if tThisFlip > 780.5 - frameTolerance : # 740s

        Break_time.setAutoDraw(False)


######################### slider4 #####################################  

    # slider4 updates 
    if slider4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:  

        slider4.setAutoDraw(True)

        # slider intialize
        slider4.marker.size = 0.03
        slider4.markerPos = 4


    if slider4.status == STARTED and tThisFlip <= 780.0 - frameTolerance :

        X_pos_4 = joy.getX()*0.021
        slider4.markerPos += X_pos_4

        if X_pos_4 == 0 :
            detect_mv_4 += 1 


#     # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running

    for thisComponent in TrialComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Trial3"-------
for thisComponent in TrialComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)




# Dynamic Rating data save 

data_1_df = pd.DataFrame(data_save_1)
data_1_df.set_index('Order')
data_1_df.to_csv('./data_trial/%s_%s_%s.csv'%( Count_bal[ int( expInfo['Block'])-1, 0 ], expInfo['Name'], expInfo['Student_ID']) )

data_2_df = pd.DataFrame(data_save_2)
data_2_df.set_index('Order')
data_2_df.to_csv('./data_trial/%s_%s_%s.csv'%( Count_bal[ int( expInfo['Block'])-1, 1 ], expInfo['Name'], expInfo['Student_ID']))

data_3_df = pd.DataFrame(data_save_3)
data_3_df.set_index('Order')
data_3_df.to_csv('./data_trial/%s_%s_%s.csv'%( Count_bal[ int( expInfo['Block'])-1, 2 ], expInfo['Name'], expInfo['Student_ID']))

data_4_df = pd.DataFrame(data_save_4)
data_4_df.set_index('Order')
data_4_df.to_csv('./data_trial/%s_%s_%s.csv'%( Count_bal[ int( expInfo['Block'])-1, 3 ], expInfo['Name'], expInfo['Student_ID']))



# Video order and means data save
video_order = [ Trial1[0].name, Trial1[1].name, Trial1[2].name, Trial1[3].name, Trial1[4].name, \
            Trial2[0].name, Trial2[1].name, Trial2[2].name, Trial2[3].name, Trial2[4].name, \
            Trial3[0].name, Trial3[1].name, Trial3[2].name, Trial3[3].name, Trial3[4].name, \
            Trial4[0].name, Trial4[1].name, Trial4[2].name, Trial4[3].name, Trial4[4].name]

strain_means = [ mean_1, mean_2, mean_3, mean_4, mean_5, mean_6, mean_7, mean_8, mean_9, mean_10, mean_11, mean_12, mean_13, mean_14, mean_15, mean_16, mean_17, mean_18, mean_19, mean_20 ]


Order_means_df = pd.DataFrame( {'Video_Order' : video_order , 'Strain_means' : strain_means } )
Order_means_df.set_index( keys = "Video_Order" , drop=True, inplace=True)
Order_means_df.to_csv('./data/Order_and_Means_%s_%s_.csv'%(expInfo['Name'], expInfo['Student_ID']))


# VFSQ data save
items = ['Bleary' , 'Dry Eyed' , 'Eyestrain', 'Gritty', 'Eye-Ache', 'Sting', 'Heavy Eyes', 'Hazy', 'Warm Eyes', 'Flickering', 'Watery Eyes', 'Feeling heavy in the head', 'Feel heavy', \
        'Difficulty concentrating', 'Dizzy', 'Stiff shoulder', 'Stiff neck', 'Sleepy', 'Vomiiting', 'Vertigo', 'Nausea', 'Difficulty focussing', 'Double vision', 'Near vision difficulty', \
        'Far vision difficulty', 'Pain in the temple', 'Pain in the middle of the head', 'Pain in the back of the head' ]

VFSQ_block1 = [ratingscale1_1.getRating(), ratingscale1_2.getRating(), ratingscale1_3.getRating(), ratingscale1_4.getRating(), ratingscale1_5.getRating(), \
            ratingscale1_6.getRating(), ratingscale1_7.getRating(), ratingscale1_8.getRating(), ratingscale1_9.getRating(), ratingscale1_10.getRating(), ratingscale1_11.getRating(), \
            ratingscale1_12.getRating(), ratingscale1_13.getRating(), ratingscale1_14.getRating(), ratingscale1_15.getRating(), ratingscale1_16.getRating(), ratingscale1_17.getRating(), \
            ratingscale1_18.getRating(), ratingscale1_19.getRating(), ratingscale1_20.getRating(), ratingscale1_21.getRating(), ratingscale1_22.getRating(), ratingscale1_23.getRating(), \
            ratingscale1_24.getRating(), ratingscale1_25.getRating(), ratingscale1_26.getRating(), ratingscale1_27.getRating(), ratingscale1_28.getRating() ]

VFSQ_block2 = [ratingscale2_1.getRating(), ratingscale2_2.getRating(), ratingscale2_3.getRating(), ratingscale2_4.getRating(), ratingscale2_5.getRating(), \
            ratingscale2_6.getRating(), ratingscale2_7.getRating(), ratingscale2_8.getRating(), ratingscale2_9.getRating(), ratingscale2_10.getRating(), ratingscale2_11.getRating(), \
            ratingscale2_12.getRating(), ratingscale2_13.getRating(), ratingscale2_14.getRating(), ratingscale2_15.getRating(), ratingscale2_16.getRating(), ratingscale2_17.getRating(), \
            ratingscale2_18.getRating(), ratingscale2_19.getRating(), ratingscale2_20.getRating(), ratingscale2_21.getRating(), ratingscale2_22.getRating(), ratingscale2_23.getRating(), \
            ratingscale2_24.getRating(), ratingscale2_25.getRating(), ratingscale2_26.getRating(), ratingscale2_27.getRating(), ratingscale2_28.getRating() ]   

VFSQ_block3 = [ ratingscale3_1.getRating(), ratingscale3_2.getRating(), ratingscale3_3.getRating(), ratingscale3_4.getRating(), ratingscale3_5.getRating(), \
            ratingscale3_6.getRating(), ratingscale3_7.getRating(), ratingscale3_8.getRating(), ratingscale3_9.getRating(), ratingscale3_10.getRating(), ratingscale3_11.getRating(), \
            ratingscale3_12.getRating(), ratingscale3_13.getRating(), ratingscale3_14.getRating(), ratingscale3_15.getRating(), ratingscale3_16.getRating(), ratingscale3_17.getRating(), \
            ratingscale3_18.getRating(), ratingscale3_19.getRating(), ratingscale3_20.getRating(), ratingscale3_21.getRating(), ratingscale3_22.getRating(), ratingscale3_23.getRating(), \
            ratingscale3_24.getRating(), ratingscale3_25.getRating(), ratingscale3_26.getRating(), ratingscale3_27.getRating(), ratingscale3_28.getRating() ] 

VFSQ_block4 = [ ratingscale4_1.getRating(), ratingscale4_2.getRating(), ratingscale4_3.getRating(), ratingscale4_4.getRating(), ratingscale4_5.getRating(), \
            ratingscale4_6.getRating(), ratingscale4_7.getRating(), ratingscale4_8.getRating(), ratingscale4_9.getRating(), ratingscale4_10.getRating(), ratingscale4_11.getRating(), \
            ratingscale4_12.getRating(), ratingscale4_13.getRating(), ratingscale4_14.getRating(), ratingscale4_15.getRating(), ratingscale4_16.getRating(), ratingscale4_17.getRating(), \
            ratingscale4_18.getRating(), ratingscale4_19.getRating(), ratingscale4_20.getRating(), ratingscale4_21.getRating(), ratingscale4_22.getRating(), ratingscale4_23.getRating(), \
            ratingscale4_24.getRating(), ratingscale4_25.getRating(), ratingscale4_26.getRating(), ratingscale4_27.getRating(), ratingscale4_28.getRating() ]


VFSQ_list = { 'Before' : VFSQ_before ,'Block_1' : VFSQ_block1, 'Block_2' : VFSQ_block2, 'Block_3' : VFSQ_block3, 'Block_4' : VFSQ_block4 }
VFSQ_df = pd.DataFrame(VFSQ_list)
VFSQ_df.index = items
VFSQ_df.columns = [ 'Befoe', Count_bal[ int( expInfo['Block'])-1, 0 ], Count_bal[ int( expInfo['Block'])-1, 1 ], Count_bal[ int( expInfo['Block'])-1, 2 ], Count_bal[ int( expInfo['Block'])-1, 3 ] ]
VFSQ_df.to_csv('./data/VFSQ_%s_%s_.csv'%(expInfo['Name'], expInfo['Student_ID']))


# Info of participants

thisExp.addData( 'Block', expInfo['Block'] )
thisExp.addData( 'Name', expInfo['Name'] )
thisExp.addData( 'Age', expInfo['Age'] )
thisExp.addData( 'College' , expInfo['College'] )
thisExp.addData( 'Student_ID', expInfo['Student_ID'])
thisExp.addData( '은행', expInfo['은행'])
thisExp.addData( '계좌번호', expInfo['계좌번호'])

win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
# logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
