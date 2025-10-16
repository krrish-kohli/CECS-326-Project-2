# CECS 326 — Group Project 2 Report

- **Program:** `synchronization.py`
- **Group Members:**  
  - Krrish Kohli, 031530055
  - Beau Cordero, 029378347 

---

## 1. Objective

The goal of this program is to implement the **Dining Philosophers Problem** using **threads, locks, and condition variables** in Python.  

- Each philosopher alternates between **thinking** and **eating**, while ensuring that two neighboring philosophers never eat at the same time.  
- This project demonstrates **process synchronization**, **mutual exclusion**, and **avoidance of deadlock** using monitor-like behavior in Python.

---

## 2. Design of the Program

### a) Program structure
The program defines two main classes:

1. **DiningPhilosophers** — Acts as the monitor controlling access to forks.  
2. **Philosopher** — Represents each philosopher running as a separate thread.

There are five philosopher threads (numbered 0–4), each simulating independent thinking and eating cycles.

---

### b) Philosopher states
Each philosopher can be in one of three states:

- **THINKING** — The philosopher is not hungry.  
- **HUNGRY** — The philosopher wants to eat and tries to pick up forks.  
- **EATING** — The philosopher has both forks and is eating.  

The `state` list keeps track of the current state for all philosophers.

---

### c) Synchronization mechanism
Synchronization is achieved using:
- A **mutex lock** (`threading.Lock`) to ensure mutual exclusion.  
- A **condition variable** (`threading.Condition`) for each philosopher to wait until forks are available.  

This allows philosophers to “wait” safely without busy-waiting.

---

### d) Monitor methods

#### `pickup_forks(i)`
- Called when philosopher *i* becomes hungry.  
- Sets the philosopher’s state to **HUNGRY**.  
- Calls `test(i)` to check if the philosopher can start eating.  
- If both neighbors are not eating, the philosopher changes to **EATING** and proceeds.  
- Otherwise, the philosopher waits on its condition variable.

#### `return_forks(i)`
- Called when philosopher *i* finishes eating.  
- Changes its state back to **THINKING**.  
- Calls `test(left(i))` and `test(right(i))` to see if either neighbor can now eat.

---

### e) Helper methods

#### `test(i)`
- Checks whether philosopher *i* can start eating.  
- Conditions:
  - The philosopher must be **HUNGRY**.  
  - Both left and right neighbors must not be **EATING**.  
- If conditions are satisfied, philosopher *i* moves to **EATING** and is notified via its condition variable.

#### `left(i)` and `right(i)`
- Compute the indices of the left and right neighbors using modular arithmetic.

---

### f) Philosopher thread behavior

Each philosopher thread runs the following cycle five times:
1. Thinks for 1–3 seconds (`time.sleep()` with random delay).  
2. Attempts to pick up forks using `pickup_forks(i)`.  
3. Eats for 1–3 seconds.  
4. Puts down forks using `return_forks(i)`.  

This cycle continues until each philosopher has eaten five times.

---

### g) Deadlock prevention

The program prevents deadlock by:
- Allowing a philosopher to eat only when both neighbors are not eating.  
- Using a shared lock to coordinate all state changes.  
- Ensuring condition variables are signaled correctly to wake waiting philosophers.  

This approach guarantees mutual exclusion and ensures that every philosopher eventually gets to eat.

---

### h) Output and execution

The program prints clear messages showing each philosopher’s actions, such as:

```text
Philosopher 0 is thinking...
Philosopher 0 is HUNGRY
Philosopher 0 is EATING
Philosopher 0 finished eating
```

---

### i) Resource management

- The Lock ensures all shared state updates are atomic.
- Each philosopher waits on its own condition variable instead of busy looping, conserving CPU resources.
- Threads terminate automatically once all eating cycles are completed.
