# functions to be used to help capture the maginified view from Zygo Optical profilometer.

#requried python package to run the program 
import pyautogui
import time

#Scanlength paired with the time it takes to finish scan
def waitTime(scanLength):
    match scanLength:
        case 5:
            return 1
        case 10:
            return 1
        case 20:
            return 2
        case 40:
            return 3
        case 65:
            return 5
        case 100:
            return 7
        case 150:
            return 10

def adjustLight():
    time.sleep(0.2)
    pyautogui.press('f5')

    print("f5pressed")
    time.sleep(1)

def takePicture():
    time.sleep(0.2)
    pyautogui.press('f4')

    print("f4pressed")
    time.sleep(1)

#the format is: C:/directory/ ...  /
def save(directory , sampleName):
    time.sleep(0.5)
    pyautogui.hotkey('ctrl', 's')

    print("ctrl + s pressed")
    pyautogui.typewrite(directory + sampleName)
    
    ## need to find the lcoation of OK button from the compurer screen size
    # pysutogui.position().
    # pyautogui.move (x,y, time)
    # pyautogui.click()


def repeatCapture(numberOfCaptures, totalTimeInterval, sampleName, scanLength, directory): #time in minute

    for i in range(numberOfCaptures):
        sampleName = sampleName + "AtTime" + str(i*(totalTimeInterval / numberOfCaptures)) + "Min"
        print(sampleName)
        time.sleep(0.1)
        adjustLight()
        takePicture()
        time.sleep(waitTime(scanLength))
        save(directory, sampleName)

        # waiting for the heating time interval
        time.sleep((totalTimeInterval / numberOfCaptures))














