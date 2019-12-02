import os
import sys,getopt
sys.path.append("scripts")
import pdb2xyz

argumentList = sys.argv[1:]
unixOptions = "hi:kap"
gnuOptions = ["help","input=","keep","approximation","processes"]


def runGoccs(inputfile,approximation,ncpus):
    if ncpus is not None:
        os.system("bin/goccs_linux_amd64 -xyzfile %s -approximation %s -processes %d"%(inputfile,approximation,ncpus))
    else :
        os.system("bin/goccs_linux_amd64 -xyzfile %s -approximation %s"%(inputfile,approximation))

def printUsage():
    print("""
USAGE: python goccs.py --input=input.pdb --keep
or   : python goccs.py --input=input.xyz
       available arguments: 
       -i / --input         : Input PDB or xyz file
       -k / --keep          : Specify if you want to keep the intermediate PDB file
       -a / --approximation : Optional - CCS approximation should be PA (projection approximation) or EHS (exact hard sphere)
       -p / --processes     : Optional - number of CPU's to use for the calculation
    """)


try:
    arguments, values = getopt.getopt(argumentList, unixOptions, gnuOptions)
except getopt.error as err:
    # output error, and return with an error code
    printUsage()
    print (str(err))
    sys.exit(2)

mode=""  #set the calculation mode (from pdb or xyz)
filename=""
keep=False
approximation="PA"
ncpus=None

for currentArgument, currentValue in arguments:
    if currentArgument in ("-h", "--help"):
        printUsage()
        sys.exit()
    elif currentArgument in ("-k", "--keep"):
        keep=1
    elif currentArgument in ("-a", "--approximation"):
        approximation=currentValue
    elif currentArgument in ("-p", "--processes"):
        ncpus=int(currentValue)
    elif currentArgument in ("-i", "--input"):
        print (("Input file: %s") % (currentValue))
        if(len(currentValue.split("."))==2):
            extension=currentValue.split(".")[1]
            filename=currentValue
            if extension=="pdb":
                mode="pdb"
            elif extension=="xyz":
                mode="xyz"
            else:
                printUsage()
                sys.exit("ERROR: only pdb or xyz files with according file extensions are supported")
        else: 
            printUsage()
            sys.exit("Please provide a valid input file with either the extension .pdb or .xyz")

#print(filename)
#print(keep)
#print(mode)

if filename and mode:
    if mode=="pdb":
        outprefix=filename.split(".")[0]
        pdb2xyz.pdb2xyz(filename,outprefix,keepIntermediate=keep)
        runGoccs(filename,approximation,ncpus)


    if mode=="xyz":
        runGoccs(filename,approximation,ncpus)

else :
    printUsage()
    sys.exit("Please specify an input file to analyze")