import tkinter as tk
import requests
import html
from tkinter import messagebox

from day_34.quiz_app_with_oop.quiz_brain import QuizBrain
from day_34.quiz_app_with_oop.quiz_ui import QuizUI


# nsew = north south east west

q_brain = QuizBrain()
quiz_ui = QuizUI(quiz_brain=q_brain)
print('hiiii')
