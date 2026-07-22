# The Ultimate Reframe

**Just two lines of code that change how you see reality.**

```plaintext
s         2.99792458e8 m
c         1
```

### That’s it

With those two lines, **time becomes distance** and mass becomes energy.

* A second is now ~300,000 km.
* The speed of light is exactly 1.

**E = mc²** turns energy into something you can actually touch, or carry.

---

## Backstory: the whole project is two lines

There was a time — for years — when it seemed possible to get away with a units file of only those two lines.

And in an important sense, that was never wrong. Those two lines still *are* the package. Everything else is commentary, context, and convenience so other people can land in the same place without already knowing the punchline.

| Layer | Role |
| ----- | ---- |
| **Core** | Time as distance → mass **is** energy |
| **Named yields, TNT scale, solar / Earth units** | “Show me Nagasaki in grams,” “show me a data center vs sunshine” |
| **Topic notes** | Data centers, solar radiance, Earth absorption — scale for current arguments |
| **minkowski_entropy, twin paradox, finance** | Same exponential map, other stories |
| **README, CONTRIBUTING, license** | Packaging so the insight can travel without the author in the room |

The file got longer. The center of mass did not move.

For a long time the two lines were enough because *one person* already knew what they meant. The expanded repo is what happens when that knowledge has to travel: strangers, students, campaign notes, late-night rabbit holes — people who need the ladder, not just the rooftop.

> **The whole project is two lines. Everything else is so you don’t have to already believe them.**

You still can’t get away with *only* two lines if you want others to use the idea. You also never abandoned them. Open `massenergy.units` and the first real definitions are still the same move: measure the second as light-travel distance, set \(c = 1\), and watch mass and energy stop pretending to be different things.

---

## The mind-blower

Global electricity consumption in 2023: **27.047 trillion kWh** (27.047 PWh).

Converted to mass-equivalent: ≈ **1,083 kg**

That’s roughly the payload of a single large pickup truck.

All the power plants on Earth — coal, gas, nuclear, hydro, wind, solar — 
running full tilt for an entire year amount to about one ton of mass converted into energy.

Now hold that against the Sun blasting energy onto Earth every second.
Or the planet’s total energy gradient.

Even the entire peak Cold War nuclear stockpile (including the massive Mark 17 & 24 H-bombs) would have been just a 
momentary sparkle against that abyss — noticeable for a few hours at most, then gone.

Note that the 1950s Cold War arsenal of about 250 Shrimp-design bombs was dwarfed by the world’s 2023 annual electric consumption.

``` text
You have: 1083 kg
You want: shrimp
        1083 kg = 1550.9112 shrimp
```

We are not energy titans. We are a thin, vibrant film living on an overwhelmingly abundant gradient.

This project is a tiny key that unlocks a much larger perspective. The universe runs on scales and flows that make our total activity look modest. Our real challenge is not scarcity or fragility, but courage: the courage to use the gradient wisely instead of fearing it.

Load the file. Play with the numbers. Let the math smile back at you.

```bash
# From the MassEnergyUnits repo (system units + this file)
units -f /usr/share/units/definitions.units -f ./massenergy.units
```

### Keep exploring

| Next | What you get |
| ---- | ------------ |
| [massenergy.units](massenergy.units) | The two lines, plus the aliases that make them easy to use |
| [README.md](README.md) | Install, examples, full index |
| [datacenter-power.md](datacenter-power.md) | Waste heat vs Earth solar absorption |
| [solarradiance-earthabsorption.md](solarradiance-earthabsorption.md) | Daily sunshine at planetary scale |
| [minkowski_entropy/](minkowski_entropy/) | Growth/decay, entropy-like measures along timelike intervals |

---

### A note from the author

If you ever wondered what software engineers do for fun:

We fly airplanes,

— Jillian England

See **[Bio.md](bio.md)** for an extrapolation :grinning: