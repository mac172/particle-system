
#  Step 04: Bouncing (Collision & Restitution)

> **"For every action, there is an equal (but slightly weaker) reaction."**

---

##  What Changed in This Step
In Steps 01–03, the particles fell forever into the infinite void at the bottom of the screen.
In Step 04, we installed a **Floor**.

We added `BOUNCE_FACTOR = 0.7`.
Now, when a particle hits `SCREEN_HEIGHT`, it doesn't disappear. It reverses its direction but loses 30% of its energy in the impact.

---

##  Why This Matters
Without collisions, your particles are ghosts. They don't interact with the world.
Adding a floor creates **Restitution**—the physics term for "bounciness."

This is the difference between dropping a bowling ball (thud) and a rubber ball (boing).

---

##  The One Line That Does the Magic
This simple math trick handles the entire collision:

```python
self.dy *= -BOUNCE_FACTOR

```

**What this does:**

1. **Inverts Direction:** The negative sign (`-`) flips the speed from "Down" (+10) to "Up" (-10).
2. **Reduces Energy:** The `0.7` reduces the speed to 7.
* *Result:* It goes up, but not as high as it started. This is why bounces get smaller and smaller.



---

##  What to Experiment With

Change `BOUNCE_FACTOR` in the configuration.

**1. The "Superball"**

* Set `BOUNCE_FACTOR = 0.95`
* *Result:* The particles keep bouncing for a long time, retaining almost all their energy.

**2. The "Brick"**

* Set `BOUNCE_FACTOR = 0.1`
* *Result:* The particles hit the floor and stick immediately. No bounce.

---

##  What Breaks If You Push It Too Far

* **Greater than 1.0 (1.2):** **Flubber Mode.** The particle gains energy with every bounce. It will bounce higher and higher until it breaks the sound barrier.
* **Negative Numbers (-0.5):** The particle will glitch through the floor and accelerate downwards forever.

---

##  Before Moving On

Can you answer these two questions?

1. **Why do we also add `self.dx *= 0.9` inside the collision check?**
*(Hint: The floor isn't ice. Friction is higher when you scrape against the ground.)*
2. **Why do we set `self.y = SCREEN_HEIGHT - self.radius`?**
*(Hint: If we don't force it out of the floor, it might get stuck inside and vibrate endlessly.)*

*Once you master the bounce, go to Folder 05.*
