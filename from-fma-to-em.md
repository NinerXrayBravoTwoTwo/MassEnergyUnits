# From F = ma to E = m  
## Natural Units, Computational Inertia, and Related Tangents


<p align="center" >
  <img src="images/gadget-color.jpg" width="650" alt="Trinity test — Gadget painting, black and white">
  </br>
  The 'Gadget'</br>—Whats in a gram?—</br>Trinity test, 16 July 1945 (render)
</p>

**“Now for something completely different..." (hat tip to Monty Python)**

---

## 1. The Core Algebraic Claim
Using units in which one second is identified with the distance 
light travels in that second (299 792 458 m), we set  **c = 1**. In these units time and length are dimensionally identical.

Newton’s second law:

$$
F = m a
$$

Acceleration expressed as:

$$
a = \frac{\Delta x}{(\Delta t)^2}
$$

Under the identification:
$$
\Delta t \equiv \Delta x
$$

$$
a = \frac{1}{\Delta x}
$$

Therefore:

$$
F = \frac{m}{\Delta x} \quad \Rightarrow \quad F \cdot \Delta x = m
$$

The left-hand side is mechanical work, which in these units is energy:

$$
E = W = m
$$

Hence:

$$
E = m
$$

The length term cancels, leaving mass and energy dimensionally identical. 
This is the content of **E = mc^2** 


once **c** has been scaled to unity (i.e. **c = 1**)

You can see that nothing more complicated than grade school 
algebra is required to make the identification.

The only subtlety is that the identification is made in a 
particular frame (the light cone) rather than as a property of the mass 
itself. The derivation does not assume **E = mc^2** — it recovers it from the Newtonian work definition and the unit choice.

---

## 2. What the Derivation Actually Does (and Doesn’t)

- It is internally consistent within the chosen units.
- It recovers the rest-energy equivalence 

- E = m  when  v = 0


- It mixes a Newtonian work definition with a relativistic unit choice. The numerical agreement is real; the mixed foundation is the point a referee would flag.
- The substitution is valid along the light cone. Ordinary matter sits inside the cone, so the identification is used as a boundary condition rather than a state the mass itself occupies.

---

## 3. Einstein, Minkowski, and the Missing Shortcut

Einstein’s 1905 derivation did not assume the unit identification. 
It began from the invariance of **\( c \)** (proven, not postulated) 
and a light-emission thought experiment comparing energy and momentum 
in two frames.

$$
\quad Conservation\quad forced\quad \Delta m = E/c^2
$$

Minkowski (1908) made the geometric leap: once spacetime is a single manifold with the metric mixing time and space, \( c = 1 \) becomes the natural coordinate choice rather than a trick. He formalized Einstein’s results; he did not supply a shortcut Einstein overlooked.

---

## 4. The Ruliad and Computational Inertia

Stephen Wolfram’s claim: the invariant speed limit is not primarily a property of photons but of the maximum rate at which one update in the hypergraph can influence another. Light travels at that ceiling because it is the fastest process allowed by the update rule.

**Extension under discussion:**  
Inertia may be the extra computational work required to re-derive a configuration when it is pushed off its current trajectory. Heavier (more complex) states require more substrate steps. From inside that state each step arrives later — observationally indistinguishable from time running slow. This is gravitational time dilation wearing a computational costume.

Gravity itself can then be re-read as regions where the substrate’s bookkeeping runs slower. Trajectories that would be straight in flat compute-time bend toward the slow zone. Einstein’s field equations already contain no force — only geometry. The open question is whether the computational lag is purely local or propagates in a way that yields the inverse-square law.

---

## 5. Mass, Inertia, Entropy, and Measurable Effects

In **c = 1** units, mass and energy are the same quantity. Measuring inertia in grams or in watt-hours is legitimate.

Human entropy production (~100 W of waste heat) is negligible compared with solar flux or planetary heat flow. It does not open a second channel for time dilation beyond the mass/energy channel already accounted for.

Inside an Ares/Apollo-style capsule the external solar load (~1,400 W m⁻²) dominates any internal heat signature.

---

## 6. Mid-Course Corrections and Solar Radiation Pressure

- Solar radiation pressure on the spacecraft’s projected area produces measurable drift over multi-day or multi-month coasts.
- Apollo modeled it as a continuous perturbation; mid-course burns cleaned up the accumulated effect.
- Mars transits (6–9 months) typically plan several correction burns, the last often days before entry interface.
- Jupiter missions (Juno, Galileo) required multiple deep-space maneuvers and trajectory-correction burns over years. Larger target size does not cancel the growth of uncertainty over multi-year coasts.

---

## 7. Historical Side Threads

- SCO Unix (1988–1998), Usenet nodes, USDA hops-system contracts.
- Bedrock patent 5,893,120 (hash table with external chaining and on-the-fly expired-record removal) and its collision with the Linux IPv4 route cache.
- RSA (Rivest–Shamir–Adleman, 1977/78): originally proposed for direct message encryption; in practice used for key exchange inside hybrid schemes (RSA/ECC + AES). Hybrid reduces the attack surface.
- Bayh-Dole Act and the double-payment problem of federally funded research that is later patented.
- Absence of a strong market incentive for secure voting systems.

---

# Closing Note

### The algebraic cancellation that turns **F = ma into E = m** under **c = 1** is real.

Whether the deeper computational reading of inertia and gravity can be made precise inside a ruliad-style model remains an open question — interesting precisely because it sits at the intersection of relativity, information, and the cost of updating state.
