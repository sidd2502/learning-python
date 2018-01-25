import time
import webbrowser
start = 0
while (start < 3): # while code
    time.sleep (5)
    webbrowser.open ("https://www.youtube.com/watch?v=G43RjkcIrPI")
    start = start + 1
    print ("the thing started on" + time.ctime())
    
