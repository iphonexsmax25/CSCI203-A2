# CSCI203  Assignment 2 - Part B -Programming


## Overview
This program simulates passenger processing through **two stages**:

1. **Total Queue → Boarding Servers**
2. **Loading Queue → Loading-Desk Servers**

Passengers arrive over time (FCFS order). After finishing boarding, they join the loading queue.  
The program calculates throughput, functional time, average waiting times, maximum queue lengths, and server idle times.

---

## Files
- `Tree.py` – main Python program (simulation + statistics)
- `A2data2.dat` – example input data file

---

## Requirements
- Python 3 (recommended: Python 3.8+)
- Uses only standard libraries: `sys`, `dataclasses`, `collections`, `typing`

---

## How to Run 
Open a terminal/command prompt in the folder containing Tree.py and the .dat file.

Mac / Linux:

  ```
  python3 Tree.py A2data2.dat

  ```

Windows (PowerShell / CMD):

 ``` 
  py Tree.py A2data2.dat
  
  (or: python Tree.py A2data2.dat)
```

To run with another input file:

 ``` 
 python3 Tree.py <yourfile.dat>

 ```

or 

```python Tree.py A2data2.dat```

