#  Step 02: Gravity (Acceleration)

> **"Acceleration changes velocity over time."**

---

##  What Changed in This Step
In Step 01, we had **Velocity** (speed in a direction). The particles moved at a constant speed forever.
In Step 02, we added **Acceleration**.

We introduced a new constant `GRAVITY = 0.25`. Now, the vertical speed of the particle changes every single frame.

---

##  Why This Matters
If you only use velocity, everything looks like it is in deep space.
To make things feel "real" or "heavy," you need gravity.

Gravity creates **Parabolic Motion** (curves). It pulls the particle down a little bit more every millisecond, transforming a boring straight line into a beautiful arc.

---

##  The One Line That Does the Magic
This is the single line inside the `move()` method that creates the curve:

```python
self.dy += GRAVITY

```

**What this does:**
It takes the current vertical speed (`self.dy`) and adds `0.25` to it.

* Frame 1: Speed is -5 (Moving up)
* Frame 10: Speed is 0 (Hanging at the top)
* Frame 20: Speed is +5 (Falling down)

---

##  What to Experiment With

Open `main.py` and look for the **CONFIGURATION** section. Change the numeric values to see physics break.

**1. Moon Gravity**

* Set `GRAVITY = 0.05`
* *Result:* Particles float lazily. The arc becomes huge.

**2. Jupiter Gravity**

* Set `GRAVITY = 1.0`
* *Result:* Particles feel incredibly heavy. They barely go up before smashing down.

---

##  What Breaks If You Push It Too Far

* **Too Low (0.0):** The particles revert to Step 01 behavior (flying straight).
* **Too High (20.0):** The arc disappears. The particles teleport to the bottom of the screen instantly because the acceleration is faster than the frame rate.

---

##  Before Moving On

Can you answer these two questions?

1. **Why does the motion curve?**
*(Hint: The horizontal speed `dx` stays the same, but the vertical speed `dy` keeps changing.)*
2. **Why does the particle fall faster at the bottom than at the top?**
*(Hint: Gravity adds up. The longer it falls, the faster it gets.)*

*Once you get this, go to Folder 03.*
