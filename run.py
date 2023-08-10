from functions import *

#main program to run.
def run():
    scanLength = int(input("Enter scan length in microns: "))
    numberOfCaptures = int(input("Enter number of captures requried: "))
    totalTimeInterval = int(input("Enter the total time interval for the heating process in min: "))
    sampleName = input("Enter sample name: ")
    directory = input("Enter the saving folder directory (C:/directory/.../.../) : ")

    repeatCapture(numberOfCaptures, totalTimeInterval, sampleName,  scanLength, directory)
    

if __name__ == '__main__':
    run()



