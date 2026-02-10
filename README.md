# CSCI203 Assignment 2 — Part B (Simulation)

This program simulates passengers going through **two service stages**:

1. **Total Queue → Boarding Servers** (service time = `boarding_time`)
2. **Loading Queue → Loading-Desk Servers** (service time = `loading_time`)

Both stages use **FCFS** (first-come-first-served) and support **multiple servers**.

---

## Requirements
- Python 3 (recommended 3.8+)
- No third‑party libraries (standard library only)

---

## Input file format (`.dat`)
The program reads a text file with this format:

1. **First line:**
   ```
   S L
   ```
   where:
   - `S` = number of **Boarding Servers**
   - `L` = number of **Loading-Desk Servers**

2. **Then one passenger per line:**
   ```
   arrival_time boarding_time loading_time
   ```

3. **End of file marker:**
   ```
   0 0 0
   ```

Example:
```text
2 2
0 4 6
2 3 5
10 2 4
0 0 0
```

---

## How to run
Open a terminal **in the same folder as** `Tree.py` and your `.dat` file.

### macOS / Linux
```bash
python3 Tree.py A2data2.dat
```

### Windows (PowerShell / CMD)
Try one of these:
```powershell
py Tree.py A2data2.dat
```
```powershell
python Tree.py A2data2.dat
```

### Optional: run as an executable (macOS / Linux)
```bash
chmod +x Tree.py
./Tree.py A2data2.dat
```

> Note: The script prints a usage line that says `partB.py` (a name typo). You still run it as `Tree.py`.

---

## What the output means
The program prints:
- **Throughput**: number of passengers processed
- **Functional Time**: time when the **last passenger finishes loading**
- **Processing Statistics** (averages):
  - Average **time in system** = `end_loading - arrival`
  - Average wait in **Total Queue** = `start_boarding - arrival`
  - Average wait in **Loading Queue** = `start_loading - end_boarding`
- **Queue Analysis**:
  - Maximum length of **Total Queue**
  - Maximum length of **Loading Queue**
- **Server Efficiency**:
  - Idle time for each Boarding Server
  - Idle time for each Loading-Desk Server

---

## Troubleshooting
- **“Usage: … <datafile.dat>”**
  You forgot the data file argument. Run:
  ```bash
  python3 Tree.py A2data2.dat
  ```

- **“FileNotFoundError: … .dat”**
  You are not in the correct folder, or the filename is wrong.
  - Check files: `ls` (mac/Linux) or `dir` (Windows)
  - Or run with a full path to the file.

- **“python/python3/py is not recognized”**
  Python is not installed or not on PATH. Install Python 3 and try again.
