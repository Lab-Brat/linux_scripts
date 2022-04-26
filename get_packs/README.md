# get_packs
## Table of contents
- [Introduction](#introduction)
- [How It Works](#how-it-works)
- [Files](#files)
- [How To Run](#how-to-run)

## Introduction
Some systems don't have internet access on them, and to get programs from repositores up and running on them might a bit of a hassle. 
This script is automating most of the work involed in this process.  

## How It Works
Script should be run on a computer with internet access. It will first promt user to enter package name. Then it will list all the dependencies user by the package, after which it will process to download all the dependencies and the package itself to ```./packs``` directory.  

## Files
- ```depends.txt``` - list of dependencies name, needed by the package.
- ```dwn.txt``` - repository links, of the dependencies in ```depends.txt```.
- ```err.txt``` - error log, if any error will occur, it will be logged here.
- ```get_depends.sh``` - script itself.

## How To Run
Make sure script has execute rights  
```chmod +x get_depends.sh```\
\
Run the script  
```./get_depends.sh```\
\
Input needed package name  
Packages should appear in ```./packs```
