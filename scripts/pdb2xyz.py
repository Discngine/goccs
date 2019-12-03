import sys
import os
import time
from Bio import PDB
import pdbfixer
from simtk.openmm.app import PDBFile


def pdb2xyz(inputfile,outputPrefix,keepIntermediate=False):
    """pdb2xyz: Transform a pdb file to a goccs compatible xyz file with number of atoms, elements and coordinates into an ouputfile, prefixed with outputPrefix.xyz. If you set keepIntermediate to true then the pdb file written by PDBFixer will be kept in the output folder. """
    
    pdbfixedfilename=outputPrefix+"_fixed.pdb"
    xyzoutfilename=outputPrefix+".xyz"
    fixer=pdbfixer.PDBFixer(inputfile)
    fixer.removeHeterogens(False)
    PDBFile.writeFile(fixer.topology, fixer.positions, open(pdbfixedfilename, 'w'))

    parser=PDB.PDBParser()
    #parser = PDB.MMCIFParser() #in case it's a cif file

    structure=parser.get_structure("input",pdbfixedfilename)

    #print(dir(structure))


    natoms=sum(1 for _ in structure.get_atoms())

    #print("Writing output")
    outputhandle=open(xyzoutfilename,"w")
    outputhandle.write("""%d
    empty line\n"""%(natoms))


    for atom in structure.get_atoms():
        element=atom.element
        coords=atom.get_coord()
        outputhandle.write("%s     %.3f     %.3f     %.3f\n"%(element,coords[0],coords[1],coords[2]))
    outputhandle.close()
    if not keepIntermediate:
        os.remove(pdbfixedfilename)

if __name__ == "__main__":
    if len(sys.argv)==3 and os.path.exists(sys.argv[1]):
        inputfilename=sys.argv[1]
        outputPrefix=sys.argv[2]+"_out"
    else:
        sys.exit("Usage: python pdb2xyz.py input.pdb outputPrefix")

