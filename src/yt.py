import arg_taker
from arg_taker import argsList, helpDisplay
import sys
import os
import datetime
import re
import getpass
from os import path
from pytube import Search, YouTube

#### FUNCTIONS ####

def show_results(l,s,next_page):
    j=1
    skipCount=0
    numOfResultRefresh=10
    if next_page:
        nextText=" following " 
        s.get_next_results()
        i = l+1
        l = i+numOfResultRefresh-1
    else:
        i=1
        nextText=" "

    os.system('clear')
    print("\nResults for "+sys.argv[2]+":\n")

    for result in s.results:
        if not i==j:
            j+=1
            skipCount+=1
            continue
        else:
            print("[" + str(i) + "]")
            print("Title: " + result.title)
            print("Length: " + str(datetime.timedelta(seconds = result.length)))
            print("Author: " + result.author)
            print("Views: " + str(result.views))
            if i==l:
                break
            else: 
                i+=1
                j+=1
    
    print("\n-------------------------------------------")
    print("Showing"+nextText+""+str(i-skipCount)+" results...\nPick the number of the video you wanna download")
    print("next -> show next page of results\nquit -> leave the program")
    print("-------------------------------------------")
    response = input("> ")
    if response == 'quit':
        print("Quitting...")
        exit()
    elif response == 'next':
        show_results(l,s,True)
    else:
        try:
            intResponse = int(response)
        except:
            print(f"Error: unknown input, your options were: ['next', 'quit', a number between (1-{i})]")
            exit()

        if intResponse <= i:
            print(f"You've selected: {str(s.results[int(response)-1].title)}")
            check = input("Is this correct? (y/n)\n> ")
            if check == 'y':
                chosenUrl = filter(str(s.results[int(response)-1]),"videoId=(.*?)>")
                download_vid(chosenUrl)
            else:
                print(f"Error: unknown input, your options were: ['y', 'n']")
                exit()

def filter(regExpression,pattern):
    resultingString = re.search(pattern,regExpression).group(1)
    return resultingString

def download_vid(videoUrl):
    try:
        print("Getting url...")
        yt = YouTube("https://www.youtube.com/watch?v="+videoUrl)
    except:
        print("\n-----------------------")
        print("Error:url not found :(")
        print("Usage: 'python yt.py -d https://www.youtube.com/watch?v=the_url_goes_here'")
        print("-----------------------\n")
        exit()
    
    possib = yt.streams.filter(file_extension='mp4', progressive=True)
    n=1

    print("\nChoose the video quality:")
    for p in possib:
        if p.includes_audio_track:
            res = filter(str(p),'res="(.*?)"')
            print(f"[ {n} ]: {res}\n")
            n += 1

    qualityResponse = input("> ")

    usr=getpass.getuser()
    winPath = "C:/Users/" + usr + "/Downloads"
    lnxPath = "/home/" + usr + "/Downloads"

    if os.name=="nt":
        defaultPath= winPath
    elif os.name=="posix":
        defaultPath= lnxPath
    else:
        print("Error: OS not supported :(")
        exit()

    try:
        if int(qualityResponse)>len(possib) or int(qualityResponse)<1:
            print("Error: That's not a valid quality ! Look over the options again.")
            exit()
        else:
            print("Chosen quality: "+filter(str(possib[int(qualityResponse)-1]),'res="(.*?)"'))
            itag = filter(str(possib[int(qualityResponse)-1]),'itag="(.*?)"')
    except:
            print("Error: That's not a valid quality ! Look over the options again.")
            exit()
            
    videoStreamFiltered = yt.streams.filter(file_extension='mp4', progressive=True).get_by_itag(int(itag))

    print("\nFinally, choose the path where you want the video to be saved")
    print(f'You can write "default" if you want it to be saved in the default path (default windows path: {winPath}, default linux path: {lnxPath})')

    chosenPath = input("> ")
    if chosenPath=='default':
        chosenPath=defaultPath
    elif not path.exists(chosenPath):
        print("Error: Invalid path")
        exit()

    try:
        print("Downloading...")
        videoStreamFiltered.download(output_path=chosenPath)
    except:
        print("Error: couldn't download the video, srry")
    else:
        print("Success!")

#### COMMAND HANDLING ####

try:
    arg = arg_taker.main()
except arg_taker.unknown_parameter:
    print("\n-----------------------")
    print("Error: unknown parameter, try again")
    print(f"The possibilities are: {argsList}")
    print("-----------------------\n")
    exit()

if arg=="-s" or arg=="--search":
    search = Search(sys.argv[2])
    if (len(sys.argv)>=4):
        try: 
            limit = int(sys.argv[3])
        except:
            print("\n-----------------------")
            print("Error: Remember you must NOT use spaces for video titles, try instead using '_'")
            print("Instead of 'python yt.py -s cats and dogs' -> 'python yt.py -s cats_and_dogs' ")
            print("-----------------------\n")
            exit()
    else: 
        limit=10
    show_results(limit,search,False)

if arg=='-d' or arg=='--download':
    download_vid(sys.argv[2])

if arg=='-h' or arg=='--help':
    arg_taker.helpDisplay()
    exit()
