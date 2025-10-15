# CECS-326 - Group Project 2: Synchronization

This project demonstrates **thread synchronization using monitors and condition variables** in Python.

Each philosopher is represented by a thread that alternates between **thinking**, **getting hungry**, and **eating**.  
Synchronization ensures that no two adjacent philosophers eat at the same time, avoiding deadlock and starvation.

---

## Requirements

- **OS:** Linux, macOS, or Windows (supports Python threading)
- **Python:** Version 3.8 or newer

---

## How to Run

Run the program directly using Python. No command-line arguments are required.

```bash
python3 synchronization.py
```

## Example Output
```bash
Starting Dining Philosophers problem
----------------------------------------
Philosopher 0 is thinking...
Philosopher 1 is thinking...
Philosopher 0 is HUNGRY
Philosopher 0 is EATING
Philosopher 0 finished eating
Philosopher 0 is thinking...
...
----------------------------------------
Everyone finished eating
```
