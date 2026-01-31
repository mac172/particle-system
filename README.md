
# Build a Game-Style Explosion (Python + Pygame)

---

## What This Is
This is not a course. It is not a textbook.
It is a **sequence of 6 micro-experiments**.

Most tutorials dump 200 lines of code on you and say "figure it out."
Here, we build the engine layer by layer. Each folder adds exactly **one** new physics concept to the system, so you actually understand *why* the explosion looks the way it does.

---


https://github.com/user-attachments/assets/ff0d23af-8c73-4297-9f23-7b15423c76de


##  Repository Structure
The project is divided into 6 independent folders. Each folder contains a standalone `main.py` that runs that specific stage of the simulation.

```text
particle-experiments/
│
├── 01_spawn/       →  Particles & Velocity (The raw motion)
├── 02_gravity/     →  Acceleration & Motion Curves (The arc)
├── 03_friction/    →  Energy Loss & Damping (Air resistance)
├── 04_bounce/      →  Collisions & Restitution (The floor)
├── 05_fade/        →  Lifetime & Alpha Transparency (Cleanup)
└── 06_glow/        →  Additive Blending (The final "Pro" look)

```

---

##  How to Run

**1. Prerequisites**
You need Python installed. You also need the `pygame` library.

```bash
pip install pygame

```

### More Advance 
use the virtual environment like this
```bash
python -m venv particle-system
./particle-system/Scripts/activate 
pip install pygame
```

**2. Running an Experiment**
You do not need to "install" this project. Just enter a folder and run the script.

*To see Stage 1:*

```bash
cd 01_spawn
python main.py

```

*To see the final result:*

```bash
cd 06_glow
python main.py

```

---

##  How to Learn From This

**Do not just run the code.** Break it.

This system is designed for "Tweak-Based Learning."

1. Open `02_gravity/main.py`.
2. Find the `GRAVITY` variable.
3. Change it from `0.25` to `0.05` (Moon gravity) or `1.0` (Jupiter gravity).
4. Run it and see the physics change instantly.

**The Golden Rule:**
If you want to understand how "Friction" works, don't read Wikipedia. Go to folder `03_friction`, change `FRICTION` to `1.01`, and watch the system explode.

---

##  What This Is NOT

* **NOT a Framework:** This is not a library you import. It is raw logic you can steal for your own games.
* **NOT a Video Course:** There are no hours of lectures. The code *is* the lesson.
* **NOT Dependent:** You don't need Folder 01 to run Folder 06. Every folder works on its own.

---

##  Who This Is For
* **Developers** who want to add "juice" (visual flair) to their projects.
* **Beginners** who want a quick win in under 45 minutes.

---

##  Final Note

You are building a system that simulates reality.

* Gravity is just addition.
* Friction is just multiplication.
* Bouncing is just reversing direction.

Start at `01_spawn`.
**Good luck.**

---
