#  Step 05: Fading (Life & Death)

> **"Particles must die so the system can live."**

---

##  What Changed in This Step
In Steps 01–04, every particle you clicked stayed in memory forever.
Even if they fell off the screen or stopped moving, the computer was still calculating their physics.
If you ran the simulation for 10 minutes, your computer would crash.

In Step 05, we gave every particle a **Lifetime**.
* They start opaque (255 alpha).
* They fade out slowly.
* When they disappear, **we delete them from memory.**

---

##  Why This Matters
This step teaches **Garbage Collection**.
In visual effects, you are creating thousands of objects per second. You *must* destroy them when they are no longer useful.

If you watch the **Particles** counter in the top-left corner, it will now stabilize instead of growing to infinity.

---

##  The One Line That Does the Magic
This line removes the particle from the list if it's dead:

```python
if p.lifetime <= 0: particles.remove(p)

```

**Also:**
We use `pygame.Surface((size, size), pygame.SRCALPHA)` to create a transparent texture for each particle, which allows us to fade it out visually using the `lifetime` value.

---

##  What to Experiment With

Change `LIFETIME_DECAY` in the configuration.

**1. The "Smoke" Effect**

* Set `LIFETIME_DECAY = 8`
* *Result:* Particles vanish very quickly, like thin smoke or steam.

**2. The "Embers" Effect**

* Set `LIFETIME_DECAY = 1`
* *Result:* Particles stay on screen for a long time, glowing on the floor.

---

##  What Breaks If You Push It Too Far

* **Negative Decay (-1):** The particles will become *more* opaque over time (which is impossible since max is 255) and never die. Memory usage will explode.
* **Very High Decay (100):** Particles will disappear instantly before you can even see them spawn.

---

##  Before Moving On

Can you answer these two questions?

1. **Why do we write `for p in particles[:]:` instead of `for p in particles:`?**
*(Hint: You cannot remove items from a list while you are actively looping through it. `[:]` creates a safe copy.)*
2. **Why do the particles turn invisible *before* they are deleted?**
*(Hint: Visual fade usually happens before the logic delete to make it look smooth.)*

