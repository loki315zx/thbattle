# -*- coding: utf-8 -*-
# Character definitions are here.

from baseclasses import *

import parsee
import youmu
import koakuma
import marisa
import daiyousei
import flandre
import alice
import nazrin
import yugi
import patchouli
import tewi
import reimu
import kogasa
import eirin
import shikieiki
import tenshi
import rumia
import yuuka
import rinnosuke
import ran
import remilia
import minoriko
import meirin
import suika
import chen
import yukari
import dummy

import sys
from game.autoenv import Game
if Game.CLIENT_SIDE or (len(sys.argv) > 1 and sys.argv[1] == 'TESTING'):
    register_character(dummy.Dummy)

del sys, Game
