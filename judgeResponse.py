import os, os.path
import subprocess
import ftfy
import discord
from discord.ext import commands

errcodes = []

def compile(name):
    subprocess.call(['javac', "./{}".format(name)])

def execute(name, num):
    lab = open('./lab_input/L{}.txt'.format(str(num)))
    cmd=['java', name.removesuffix('.java')]
    proc = subprocess.Popen(cmd, shell=True, stdin=lab, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # Catch Standard output 
    outputLines = []
    # Filters
    for x in proc.stdout:
        filterOut = str(x)[2:][:-1]
        if str(filterOut[-2:]) == "\\n":
            newFilterOut = filterOut[:-2]
            if newFilterOut[-2:].lower() == "\\r":
                outputLines.append(newFilterOut[:-2])
            else : outputLines.append(newFilterOut)
        elif str(filterOut[-2:]) == "\\r":
            outputLines.append(filterOut[:-2])
        else:
            outputLines.append(filterOut)
    
    # Catch Standard Error
    for x in proc.stderr:
        filterOut = str(x)[2:][:-1]
        if str(filterOut[-2:]) == "\\n":
            errcodes.append(filterOut[:-2])
        else:
            errcodes.append(filterOut)
    
    #Pull Sample Output
    sampleOut = open('./lab_output/L{}A.txt'.format(str(num))).read().splitlines()

    # Print Results
    # print(sampleOut)
    # print(outputLines)

    # Compare Results and return value
    if sampleOut == outputLines: return True
    else: return False

def test(name, num):
    errcodes = []   #reset error codes
    compile(name)
    return execute(name, num)

# Function to call error codes
def errorResponse(): return errcodes