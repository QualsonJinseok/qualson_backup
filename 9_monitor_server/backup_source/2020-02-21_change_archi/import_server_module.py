import json
import time
import atexit
import requests
import logging
import telegram
import pyautogui
import subprocess
import pyperclip
from datetime import datetime
from slacker import Slacker
from selenium import webdriver
from flask import Flask, make_response
from flask_apscheduler import APScheduler
from selenium.webdriver.chrome.options import Options
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.schedulers.background import BackgroundScheduler
