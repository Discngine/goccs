

## About
goccs is a parallel cross platform CCS prediction software implemented in go.

CCS values can be easily computed in a few steps:

![CCS calculation in simple steps.](https://github.com/jmwoll/goccs/blob/master/doc/animation_usage.gif)

## Overview
Running the command
```
goccs_windows_386.exe -xyzfile example.xyz -approximation PA -parameters mobcal
```
gives out the CCS value in angstrom^2, where approximation is either 'PA' or 'EHS'.
Note that the name of the executable varies depending on the platform used. Custom parameters can be
specified in the JSON format:
```
goccs_windows_386.exe -xyzfile example.xyz -approximation PA -parameters '{"H": 1.23, "C": 2.34, "N": 3.45, "O": 4.56}'
```

Binaries for several platforms (Linux, OSX, Windows) can be found under ```bin/``` .

The number of processes are controlled via the ```-processes``` flag (defaults to 10).
For example, the command
```
goccs_windows_386.exe -xyzfile example.xyz -approximation PA -parameters mobcal -processes 100
```
uses 100 processes in parallel.

Citations for the parameters can be found below:

Mobcal parameters:
```
SM. F. Mesleh, J. M. Hunter, A. A. Shvartsburg, G. C. Schatz, M. F. Jarrold, Structural Information from Ion Mobility Measurements:  Effects of the Long-Range Potential, J. Phys. Chem. 1996, 100, 16082-16086.
J. Phys. Chem. A 1997, 101, 968.
A. A.Shvartsburg, M. F. Jarrold, An exact hard-spheres scattering model for the mobilities of polyatomic ions, Chem. Phys. Lett. 1996, 261, 86-91.
```

Default parameters:
```
C.-K. Siu, Y. Guo, I. S. Saminathan, A. C. Hopkinson, K. M. Siu, Optimization of ion-mobility calculation for conformational analyses, J. Phys. Chem. B, 2010, 114, 1204-1212.
```

## Benchmark
Here a Projection Approximation (PA) benchmark against the established Mobcal software:

![PA Benchmark.](https://github.com/jmwoll/goccs/blob/master/benchmark/benchmark_pa.png)

The PA CCS values exhibit excellent agreement with the literature values. For the
exact hard sphere (EHS) method, we observe slight implementation-dependent
differences to the Mobcal implementation. Generally, values predicted by goccs tend
to lie nearer to the Trajectory Method (TM) values than the Mobcal calculation.

Here an Exact Hard Sphere Scattering (EHS) benchmark against the established Mobcal software:

![PA Benchmark.](https://github.com/jmwoll/goccs/blob/master/benchmark/benchmark_ehs.png)

## Docker build

If you do not want to install anything for running goccs nor for the xyz preparation script for protein structures, then you can build and use a docker image containing all of the software embedded. 

### Building the docker image 

`docker build -t goccs .`

### Transform a PDB to XYZ file for goccs

In order to use goccs you need to prepare an input xyz file. Here a preparation script is provided allowing you to transform a PDB file to the required xyz file. 

docker run goccs 

#### How to prepare your PDB file

The preparation script can be run on standard PDB files. It'll strip off hetero atoms, especially waters itself. You should prepare your protein structure before, complete missing side-chains, atoms and loops.

### Running goccs

To run goccs and show help on how to use it run goccs in docker the following way: 

`docker run goccs`

```
USAGE: python goccs.py --input=input.pdb --keep
or   : python goccs.py --input=input.xyz
       available arguments: 
       -i / --input         : Input PDB or xyz file
       -k / --keep          : Specify if you want to keep the intermediate PDB file
       -a / --approximation : Optional - CCS approximation should be PA (projection approximation) or EHS (exact hard sphere)
       -p / --processes     : Optional - number of CPU's to use for the calculation
```

Let us suppose you are in your data directory where you have your input pdbfile 1uyd.pdb. In order to calculate the CCS from the PDB file run : 

`docker run -v $PWD:/data goccs python goccs.py -i /data/1uyd.pdb`

to see the help message from before : 

`docker run -v $PWD:/data goccs python goccs.py -h`

Note that calculating the CCS can take a while depending on the number of CPU's you have at hand