

#  Stage 1: The Big Bang (Spawning & Velocity)

> **"Before gravity exists, everything flies in straight lines."**

---

##  The Mission
In this first experiment, we are building the **engine core**.
We are ignoring gravity, friction, and walls. We only care about one thing:
**Converting an Angle and Speed into X and Y movement.**

---

##  The Logic: Vector Math (Simplified)
Computers don't understand "move 45 degrees." They only understand "move 3 pixels Right (X) and 3 pixels Down (Y)."

We use **Trigonometry** to convert the random angle into X and Y steps:
* `math.cos(angle)` gives us the **Horizontal (X)** step.
* `math.sin(angle)` gives us the **Vertical (Y)** step.

```python
self.dx = math.cos(angle) * speed
self.dy = math.sin(angle) * speed

```

---

##  Controls

* **Run the script:** `python main.py`
* **Hold Left Click:** Particles spawn from your mouse cursor.
* **Observe:** Notice they fly outward in a perfect circle and never stop.

---

##  Experiments (Try These!)

1. **The "Laser Beam":**
* Change `angle = random.uniform(0, 2 * math.pi)` to `angle = 0`.
* *Result:* All particles will shoot exactly to the right.


2. **The "Slow Motion":**
* Change `speed = random.uniform(2, 9)` to `speed = 1`.
* *Result:* Particles will crawl slowly.



---

*Proceed to Folder 02 to add Gravity.*


***

### 2. Questions (The "Test")
Includes these questions in a separate text file named `CHALLENGES.txt` inside the folder, or just append them to the bottom of the README.

These are designed to make the user look at specific lines of code.

**Q1: The Infinity Problem**
> Run the code and spawn particles for 10 seconds. Notice the particle count (in the top corner) keeps going up and never comes down.
> **Question:** Why doesn't the computer lag immediately?
> **Answer:** Python is fast, but eventually, it *will* crash. We are creating objects but never deleting them. We will fix this in **Stage 05**.

**Q2: The Circle of Life**
> Look at this line: `angle = random.uniform(0, 2 * math.pi)`
> **Question:** Why do we multiply by `2`? What happens if you change it to `0.5 * math.pi`?
> **hint:** `2 * pi` is 360 degrees (a full circle). `0.5 * pi` is 90 degrees. Try it!

**Q3: The "Teleport" Glitch**
> Look at the `move(self)` function:
> ```python
> self.x += self.dx
> self.y += self.dy
> ```
> **Question:** If you wanted the particles to move *twice as fast* without changing the `speed` variable, how would you change this math?
> **Challenge:** Try changing it to `self.x += self.dx * 5`. It's warp speed!

**Q4: Color Theory**
> Look at the `COLORS` list at the top.
> **Challenge:** Add a Blue color `(0, 0, 255)` to the list. Do blue particles appear now? Why?

