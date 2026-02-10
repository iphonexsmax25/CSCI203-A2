import sys
from dataclasses import dataclass
from collections import Counter
from typing import List, Tuple


@dataclass
class Passenger:
    pid: int
    arrival: int
    board: int
    load: int
    start_board: int = 0
    end_board: int = 0
    start_load: int = 0
    end_load: int = 0


def read_data(path: str) -> Tuple[int, int, List[Passenger]]:
    with open(path, "r") as f:
        lines = [ln.strip() for ln in f if ln.strip()]

    s, l = map(int, lines[0].split())
    passengers: List[Passenger] = []

    pid = 1
    for ln in lines[1:]:
        a, b, lo = map(int, ln.split())
        if a == 0 and b == 0 and lo == 0:
            break
        passengers.append(Passenger(pid, a, b, lo))
        pid += 1

    return s, l, passengers


def argmin(values: List[int]) -> int:
    best_i = 0
    best_v = values[0]
    for i, v in enumerate(values):
        if v < best_v:
            best_v = v
            best_i = i
    return best_i


def schedule_fcfs_multi_server(arrivals: List[int], services: List[int], m: int):
    """
    FCFS multi-server schedule.
    Returns start_times, end_times, and per-server idle data (without final trailing idle).
    """
    n = len(arrivals)
    server_free = [0] * m          # when each server becomes free
    server_idle = [0] * m          # accumulated idle gaps between jobs
    start = [0] * n
    end = [0] * n
    used_server = [0] * n

    for i in range(n):
        sid = argmin(server_free)
        st = arrivals[i] if arrivals[i] > server_free[sid] else server_free[sid]

        # idle gap if server was free before this job starts
        server_idle[sid] += st - server_free[sid]

        en = st + services[i]
        server_free[sid] = en

        start[i] = st
        end[i] = en
        used_server[i] = sid

    return start, end, used_server, server_idle, server_free


def max_queue_length(arrival_times: List[int], start_times: List[int]) -> int:
    """
    Queue length = arrivals - service_starts (waiting only, not in service).
    At the same timestamp we apply both together (no fake spikes).
    """
    A = Counter(arrival_times)
    S = Counter(start_times)
    times = sorted(set(A) | set(S))

    q = 0
    max_q = 0
    for t in times:
        q += A.get(t, 0)
        q -= S.get(t, 0)
        if q > max_q:
            max_q = q
    return max_q


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 partB.py <datafile.dat>")
        sys.exit(1)

    path = sys.argv[1]
    S, L, passengers = read_data(path)
    n = len(passengers)

    #  Stage 1 (Total Queue -> Boarding Servers) 
    arrivals1 = [p.arrival for p in passengers]
    services1 = [p.board for p in passengers]
    st1, en1, _, idle1, free1 = schedule_fcfs_multi_server(arrivals1, services1, S)

    for p, st, en in zip(passengers, st1, en1):
        p.start_board = st
        p.end_board = en

    # Stage 2 (Loading Queue -> Loading-Desk Servers) 
    # IMPORTANT: stage-2 “arrivals” happen when boarding ends, so we must process in ready-time order
    order = sorted(range(n), key=lambda i: (passengers[i].end_board, passengers[i].pid))
    arrivals2 = [passengers[i].end_board for i in order]
    services2 = [passengers[i].load for i in order]

    st2, en2, _, idle2, free2 = schedule_fcfs_multi_server(arrivals2, services2, L)

    for idx, st, en in zip(order, st2, en2):
        passengers[idx].start_load = st
        passengers[idx].end_load = en

    #  Stats 
    throughput = n
    functional_time = max(p.end_load for p in passengers) if passengers else 0

    avg_wait_total = sum(p.start_board - p.arrival for p in passengers) / n
    avg_wait_load = sum(p.start_load - p.end_board for p in passengers) / n
    avg_system_time = sum(p.end_load - p.arrival for p in passengers) / n

    max_total_q = max_queue_length([p.arrival for p in passengers], [p.start_board for p in passengers])
    max_load_q = max_queue_length([p.end_board for p in passengers], [p.start_load for p in passengers])

    # add trailing idle from last job end to functional_time
    idle1_total = [idle1[i] + max(0, functional_time - free1[i]) for i in range(S)]
    idle2_total = [idle2[i] + max(0, functional_time - free2[i]) for i in range(L)]

    #  Print results 
    print("Simulation Results ")
    print(f"Throughput (passengers processed): {throughput}")
    print(f"Functional Time (last passenger exits): {functional_time}")
    print()
    print("Processing Statistics:")
    print(f"  Average time in system: {avg_system_time:.2f}")
    print(f"  Average wait in Total Queue: {avg_wait_total:.2f}")
    print(f"  Average wait in Loading Queue: {avg_wait_load:.2f}")
    print()
    print("Queue Analysis:")
    print(f"  Max Total Queue length: {max_total_q}")
    print(f"  Max Loading Queue length: {max_load_q}")
    print()
    print("Server Efficiency (Idle Time):")
    for i, t in enumerate(idle1_total, start=1):
        print(f"  Boarding Server {i}: {t}")
    for i, t in enumerate(idle2_total, start=1):
        print(f"  Loading-Desk Server {i}: {t}")


if __name__ == "__main__":
    main()
