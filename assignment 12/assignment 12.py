#question1
from datetime import date
days=['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
print(days[date.weekday(date.today())])
#question 2
import webbrowser
video=webbrowser.open("https://www.youtube.com/watch?v=DUMb9fxWrN4")
print(video)
#question 3
import os
os.rename('myfile.txt','myfile.jpg')

