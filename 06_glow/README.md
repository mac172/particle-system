
#  Step 06: Glow (Additive Blending)

> **"Paint covers. Light combines."**

---

##  What Changed in This Step
In Steps 01–05, when two particles overlapped, the top one simply covered the bottom one. This is how paint works.

In Step 06, we changed the **Blending Mode**.
We switched from "Normal" blending to "Additive" blending.
Now, when two red particles overlap, the pixel values are added together.
* **Red (100) + Red (100) = Bright Red (200)**
* **Bright Red (200) + Bright Red (100) = MAX White (255)**

---

##  Why This Matters
This is the secret sauce of game feel.
Fire, lasers, magic spells, and explosions are not solid objects. They are light.

By using **Additive Blending**, the center of your explosion (where many particles overlap) naturally turns white-hot, while the edges remain cool and colorful.

---

##  The One Line That Does the Magic
We added a special flag to the `blit` (draw) function:

```python
surface.blit(target_surface, position, special_flags=pygame.BLEND_ADD)

```

**What this does:**
It tells the graphics card: "Don't replace the pixel that is already there. ADD my color to it."

---

##  What to Experiment With

This step is all about color theory. Open `main.py` and change the `COLORS` list.

**1. The "Matrix" Code**

* Change `COLORS` to `[(0, 50, 0), (0, 150, 0)]`.
* *Result:* A spooky digital rain effect. Notice how overlapping greens become bright neon.

**2. The "Blue Flame"**

* Change `COLORS` to `[(50, 50, 255), (0, 200, 255)]`.
* *Result:* Looks like a gas stove or a sci-fi thruster.

---

##  What Breaks If You Push It Too Far

* **White Background:** If you change `BG_COLOR` to `(255, 255, 255)`, your particles will become invisible.
* *Why?* You cannot add light to something that is already maximum white.


* **Too Many Particles:** If you spawn 1,000 particles in one spot, it will just look like a solid white blob.

---

##  Final Victory Lap

You have built a complete system.

1. **Motion** (Step 1)
2. **Gravity** (Step 2)
3. **Friction** (Step 3)
4. **Bouncing** (Step 4)
5. **Life Cycle** (Step 5)
6. **Visual Polish** (Step 6)

**Challenge:** Go back to `01_spawn` and compare it to this. Look how far you have come in just 6 files.

*Congratulations, You Finally Build It.*
