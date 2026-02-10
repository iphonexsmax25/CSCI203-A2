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

## Input file Format

The data file must follow this structure:

## Line 1:
```
S L
```

- S = number of Boarding Servers
- L = number of Loading-Desk Servers

### Next lines (one passenger per line):
```
arrival_time boarding_time loading_time
```
### End of file marker:
```
0 0 0
```

Example:
```
2 2
0 6 5
2 4 3
...
0 0 0
```


## Output (What the program prints)

The program prints:

  - Throughput (number of passengers processed)

  - Functional Time (time when the last passenger finishes loading)

  - Average time in system

  - Average wait in Total Queue

  - Average wait in Loading Queue

  - Maximum Total Queue length

  - Maximum Loading Queue length

  - Idle time for each Boarding Server

  - Idle time for each Loading-Desk Server

## Example Output (using A2data2.dat)
```
  Simulation Results 
Throughput (passengers processed): 100
Functional Time (last passenger exits): 523

Processing Statistics:
  Average time in system: 139.34
  Average wait in Total Queue: 111.40
  Average wait in Loading Queue: 9.06

Queue Analysis:
  Max Total Queue length: 49
  Max Loading Queue length: 7

Server Efficiency (Idle Time):
  Boarding Server 1: 45
  Boarding Server 2: 42
  Loading-Desk Server 1: 57
  Loading-Desk Server 2: 60

```
## How the Program Works (Simple Explanation)

### Data Reading
- `read_data(path)` reads:
  - first line: `S L`
  - remaining lines: passenger data until `0 0 0`
- Each passenger is stored in a `Passenger` dataclass.

### Stage 1: Boarding (Total Queue)
- Uses FCFS (First Come First Served).
- Each passenger starts boarding when:
  - they have arrived **AND**
  - a boarding server becomes free
- `schedule_fcfs_multi_server()` assigns each passenger to the earliest available server.

### Stage 2: Loading (Loading Queue)
- Passengers can only enter the loading queue after they finish boarding.
- So stage 2 “arrival time” = `end_board`.
- The program sorts passengers by `end_board` time (and `PID` to break ties) to maintain correct FCFS order.

### Queue Length Calculation
- `max_queue_length()` computes the maximum number waiting by tracking:
  - arrivals into the queue
  - starts of service (which remove people from the waiting queue)

### Server Idle Time
- Idle time is counted as:
  - gaps between jobs, plus
  - time from server’s last job end until the overall functional time

## Notes / Assumptions

  - Times are treated as integers.

  - FCFS order is preserved.

  - If multiple events happen at the same time, the queue length calculation updates arrivals and service-starts at the same timestamp to avoid artificial spikes.