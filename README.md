# CSCI203  Assignment 2 - Part B -Programming
Queueing Simulation: Boarding Servers + Loading-Desk Servers

Student: Isaac Lim King Ming
Student ID: 1137906
Tutor/Lab: T02F
Submission Date: 14/2/2026
Language: Python 

## Program Description
This program simulates a two-stage service system:

Stage 1 (Total Queue -> Boarding Servers):
- Each passenger arrives and joins the Total Queue.
- The next available Boarding Server takes the next passenger (FCFS).
- Boarding takes the passenger’s boarding_time.

Stage 2 (Loading Queue -> Loading-Desk Servers):
- After boarding finishes, the passenger joins the Loading Queue.
- The next available Loading-Desk Server takes the next passenger (FCFS).
- Loading takes the passenger’s loading_time.

The program then outputs:
- Throughput (total passengers processed)
- Functional time (time when the last passenger exits the system)
- Processing statistics (average time in system, average wait in each queue)
- Queue analysis (maximum queue length for Total Queue and Loading Queue)
- Server efficiency (total idle time per server)

##  Files Included
Tree.py        : Main Python program (simulation + statistics).
A2data2.dat    : Sample input data file (provided).

## Input File Format (.dat)
Line 1:
  S L
  where S = number of Boarding Servers
        L = number of Loading-Desk Servers

Next lines (one passenger per line):
  arrival_time boarding_time loading_time

End of file marker:
  0 0 0

## How to Run 
Open a terminal/command prompt in the folder containing Tree.py and the .dat file.

Mac / Linux:
  python3 Tree.py A2data2.dat

Windows (PowerShell / CMD):
  py Tree.py A2data2.dat
  (or: python Tree.py A2data2.dat)

To run with another input file:
  python3 Tree.py <yourfile.dat>

## Ouput 
The program prints results to the terminal, including:
- Throughput (passengers processed)
- Functional Time (last passenger exits)
- Average time in system
- Average wait in Total Queue
- Average wait in Loading Queue
- Maximum Total Queue length
- Maximum Loading Queue length
- Total idle time for each Boarding Server
- Total idle time for each Loading-Desk Server