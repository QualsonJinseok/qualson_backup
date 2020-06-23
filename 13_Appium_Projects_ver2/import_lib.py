# -*- coding: utf-8 -*-
# BASE 모듈
import os
import io
import re
import cv2															# pip install opencv-python
import csv
import sys
import json
import time
import numpy 														# pip install numpy
import base64 														# pip install pybase64
import random
import urllib3														# pip install urllib3
import unittest
import psutil
from datetime import datetime
import telegram 													# pip install python-telegram-bot
import subprocess
import array as arr

from PIL import Image, ImageFilter									# pip install pillow

# DB 모듈
import ast 															# pip install ast

# APPIUM 제어 모듈
from appium import webdriver as AP 	  								# pip install appium-python-client

from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.multi_action import MultiAction

# SELENIUM WEBDRIVER 제어 모듈 										# pip install selenium
from selenium import webdriver
from selenium.webdriver.remote.command import Command
from selenium.webdriver import ActionChains

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.ie.options import Options

# GOOGLE VISION API 제어 모듈 										# pip install google-cloud-vision
from google.cloud import vision
from google.cloud.vision import types

# THREAD 제어 모듈
import threading 													# pip install threaded
from _thread import *

# Slack
from slacker import Slacker