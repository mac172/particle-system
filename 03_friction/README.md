#  Step 03: Friction (Air Resistance)

> **"Nothing moves forever. Energy is always lost."**

---

##  What Changed in This Step
In Step 02, particles moved in an arc, but they accelerated constantly and never lost energy sideways. If the screen were infinite, they would travel sideways forever.

In Step 03, we introduced **Damping**.
We added `FRICTION = 0.99`. Every single frame, the particle loses **1%** of its speed.

---

##  Why This Matters
Real explosions happen in air, not a vacuum. Air particles hit the object and slow it down.

Without friction, simulations look "slippery" or "floaty." Adding just a tiny bit of drag makes the movement feel physical and grounded.

---

##  The One Line That Does the Magic
This logic sits right inside the `move()` loop:

```python
self.dx *= FRICTION

```

**What this does:**
It multiplies the current speed by `0.99`.

* Frame 1: Speed is 10.
* Frame 2: Speed is 9.9.
* Frame 50: Speed is ~6.0.
* Frame 200: Speed is ~1.3.

It never *fully* reaches zero (mathematically), but it gets slow enough to look stopped.

---

##  What to Experiment With

Go to the **CONFIGURATION** section in `main.py` and tweak `FRICTION`.

**1. The "Thick Mud" Experiment**

* Set `FRICTION = 0.85`
* *Result:* The particles look like they are exploding underwater or in thick oil. They stop almost instantly.

**2. The "Vacuum" Experiment**

* Set `FRICTION = 1.0`
* *Result:* No energy is lost. They fly sideways much further. This is how space looks.

---

##  What Breaks If You Push It Too Far

* **Too Low (0.5):** The particles look like they hit a glass wall instantly.
* **Above 1.0 (1.01):** **DANGER.** This adds energy instead of removing it. The particles will accelerate faster and faster until they fly off the screen at warp speed.

---

##  Before Moving On

Can you answer these two questions?

1. **Why do we multiply (`*=`) instead of subtract (`-=`)?**
*(Hint: Drag depends on speed. Fast objects lose more speed than slow objects.)*
2. **Why does the explosion look "tighter" now?**
*(Hint: The particles at the outer edge lose the most speed.)*

*Once you understand energy loss, go to Folder 04.*
