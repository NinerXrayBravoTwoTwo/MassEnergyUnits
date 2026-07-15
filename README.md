# MassEnergy: A Mass-Based Energy Conversion Layer for GNU Units

> "Mass is not simply equivalent to energy — Mass **is** energy."

## Overview

This project provides a small `massenergy.units` file for [GNU Units](https://www.gnu.org/software/units/). It redefines the second as the distance light travels in one second and sets the speed of light `c = 1`. Mass and energy then convert directly via \(E = mc^2\).

Through this lens, a gram is about 21 kilotons of TNT. A sugar cube is city-scale. The Sun radiates roughly four million tons of mass every second.

You’ll never see the universe quite the same again.

---

## Features

- Redefines core units: `second ≈ 299792 km`, `c = 1`
- Mass ↔ energy conversions without extra factors
- Named references for familiar nuclear yields and large-scale events
- Real-world examples from physics, history, and energy economics

---

## Requirements

- [GNU Units](https://www.gnu.org/software/units/) 2.x (tested with 2.23)
- A Unix-like shell (Linux, macOS, WSL, or Cygwin)

---

## Installation

### 1. Install GNU Units

```bash
# Debian / Ubuntu / WSL
sudo apt install units

# Fedora / RHEL
sudo dnf install units

# macOS (Homebrew)
brew install units
```

On Windows, use [WSL](https://learn.microsoft.com/en-us/windows/wsl/) or [Cygwin](https://www.cygwin.com/) and install `units` inside that environment.

### 2. Get this file

```bash
git clone https://github.com/NinerXrayBravoTwoTwo/MassEnergyUnits.git
cd MassEnergyUnits
```

Or download `massenergy.units` alone from the repository.

### 3. Run it (no system install required)

Load the **system** units database first, then this file (so `m`, `J`, `g`, etc. still exist):

```bash
units -f /usr/share/units/definitions.units -f ./massenergy.units
```

Homebrew on macOS often uses:

```bash
units -f "$(brew --prefix)/share/units/definitions.units" -f ./massenergy.units
```

### 4. Optional: permanent setup

**Personal units file** (recommended for multi-user machines — each person configures their own home directory):

```bash
# Use the absolute path to your clone
echo "!include $PWD/massenergy.units" >> ~/.units
```

Then any normal `units` session picks up the definitions.

**Shell alias** (repo-local, no install into `/usr`):

```bash
# Linux / WSL
alias lightunits='units -f /usr/share/units/definitions.units -f /path/to/MassEnergyUnits/massenergy.units'

# macOS Homebrew
alias lightunits='units -f "$(brew --prefix)/share/units/definitions.units" -f /path/to/MassEnergyUnits/massenergy.units'
```

Add the alias to `~/.bashrc` or `~/.zshrc` as you prefer.

**Shared install** (optional; needs admin rights):

```bash
sudo cp massenergy.units /usr/share/units/
```

---

## What This File Does

| Definition | Meaning |
| ---------- | ------- |
| `s = 2.99792458e8 m` | One second is the distance light travels in one second |
| `c = 1` | Speed of light is unitless |
| `ton_tnt = 4.184e9 J` | Standard thermochemical ton of TNT |

Mass and energy, space and time, are brought into direct calculable parity.

> "Time and distance are the same thing. Ergo, mass and energy are the same thing."

---

## Quick examples

Interactive session (`You have:` / `You want:` prompts):

### Gram → kilotons of TNT

```text
You have: 1 g
You want: kton
        * 21.480764
        / 0.046553278
```

### Nuclear yield comparison

```text
You have: nagasaki
You want: hiroshima
        * 1.4
        / 0.71428571
```

### Sugar cube (~5 g) in tons of TNT

```text
You have: 5 g
You want: ton_tnt
        * 107403.82
        / 9.3106556e-06
```

### Nagasaki in grams of mass-energy

```text
You have: nagasaki
You want: g
        * 0.97761885
        / 1.0228935
```

### One-shot command line

```bash
units -f /usr/share/units/definitions.units -f ./massenergy.units '1 g' 'kton'
units -f /usr/share/units/definitions.units -f ./massenergy.units 'castlebravo' 'g'
units -f /usr/share/units/definitions.units -f ./massenergy.units '1 s' 'km'
```

### Built-in names

| Name | Definition |
| ---- | ---------- |
| `s`, `c` | Second as light-travel distance; speed of light = 1 |
| `ton_tnt`, `ton_e`, `ton_tnt_energy` | 1 ton TNT = 4.184 GJ |
| `kton`/`kt`, `Mton`/`Mt` | 10³ and 10⁶ tons TNT |
| `trinity`, `gadget` | 19 kt |
| `hiroshima`, `littleboy` | 15 kt |
| `nagasaki`, `fatman` | 21 kt |
| `castlebravo`, `shrimp` | 15 Mt |
| `chicxulub`, `dinokill` | K–Pg impact energy (~4.184×10²³ J) |
| `solarluminosity`, `sunpower` | Solar power (382.8 yotta W) |
| `nova` | Order-of-magnitude supernova (~10⁴⁴ J) |
| `everestmass` | Mass of Mt. Everest (approx.) |

Yields are common public figures; historical estimates have ranges. Device and convenience names alias the primary units so mass-energy stays consistent when `c = 1`.

---

## Selected events in mass equivalents

| Event | Energy (J) | Mass equivalent (g) |
| ----- | ---------- | ------------------- |
| Trinity test (19 kt) | ~8.0 × 10¹³ | ~0.88 g |
| Hiroshima (~15 kt) | ~6.3 × 10¹³ | ~0.70 g |
| Nagasaki (~21 kt) | ~8.8 × 10¹³ | ~0.98 g |
| Castle Bravo (15 Mt) | ~6.3 × 10¹⁶ | ~700 g |
| Solar luminosity (per sec) | 3.828 × 10²⁶ | ~4.25 × 10⁹ g |
| Chicxulub impact | 4.184 × 10²³ | ~4.65 × 10⁶ g |

---

## Philosophy: why mass as energy?

- **Relatable:** Grams and kilograms are everyday units.
- **Tangible:** “This release was about one gram” is easier than “42 petajoules.”
- **Intuitive scaling:** Cosmic and industrial energy use become comparable.
- **Physics-aligned:** Mass and energy are interchangeable via \(E = mc^2\).

> "A loaf of bread converted entirely to energy could power the Earth for a day."

---

## Notes and warnings

- This file is for intuition and conversion, not Lorentz transforms or tensor calculus.
- For spacetime intuition, see *Spacetime Physics* (Taylor & Wheeler).
- Not affiliated with the GNU Units project.
- Do not mix these redefinitions into unrelated unit work without understanding that `s` and `c` have been changed.
- Historical nuclear yields are estimates; modern analyses sometimes revise them.

---

### Summary of world energy usage and economics (CIA Factbook ~2016)

ElecProd ekg|Qx ekg/G$|Qx ekg/TT|CapFF ekg|Qx ekg/G$|Qx ekg/TT|EmissionTT TT|GDP G$|Country
---:|---:|---:|---:|---:|---:|---:|---:|----:
947.3|-28.154|17.312|1412.612|-32.698|11.967|33620.0|127800.0|World
235.6|0.739|-2.564|359.847|0.085|-3.455|11670.0|23210.0|China
164.0|-2.494|4.201|267.166|-1.970|4.601|5242.0|19490.0|United States
121.9|-7.598|3.995|150.630|-9.990|1.506|3475.0|20850.0|European Union
55.5|-3.440|0.157|91.690|-3.184|0.356|2383.0|9474.0|India
41.3|0.176|-0.038|58.472|-0.206|-0.458|1847.0|4016.0|Russia
39.6|-1.265|1.012|73.766|-0.599|1.646|1268.0|5443.0|Japan
26.0|0.793|1.063|11.589|-0.922|-0.666|640.6|1774.0|Canada
24.5|-1.530|0.497|30.015|-2.030|-0.025|847.6|4199.0|Germany
22.7|-0.838|1.025|9.001|-2.400|-0.551|513.8|3248.0|Brazil
21.2|-0.627|1.241|7.807|-2.116|-0.259|341.2|2856.0|France

---

## Global energy and economic relationships

- **ekg** means kilograms of mass-energy (the antimatter-equivalent sense).
- **GDP** is gross domestic product.

Data from the CIA World Factbook (circa 2016–2017).

| Independent (X) | Dependent (Y) | Correlation | Mean X | Slope |
| --------------- | ------------- | ----------- | ------ | ----- |
| Electric Consumption | Generating Capacity Fossil Fuel | 0.993 | 29.1 | 1.7 ekg/ekg |
| Generating Capacity Fossil Fuel | GDP | 0.984 | 46.9 | 64.8 ekg/G$ |
| Electric Production | GDP | 0.982 | 31.5 | 102.0 ekg/G$ |
| Electric Production | CO₂ Emissions (Tt) | 0.977 | 31.5 | 44.3 ekg/TT |
| Fossil Fuel Gen Capacity | CO₂ Emissions (Tt) | 0.969 | 46.9 | 27.8 ekg/TT |
| Nat Gas Produced | Nat Gas Consumed | 0.955 | 102.8 | 0.8 Gcm/Gcm |
| Oil Reserves | Oil % GDP | 0.946 | 30974.6 | 0.0 Gbbl/% |
| GDP | CO₂ Emissions (Tt) | 0.942 | 4090.6 | 0.4 G$/TT |
| Electric Consumption | Renewable Gen Capacity | 0.934 | 29.1 | 0.4 ekg/ekg |
| Renewable Gen Capacity | CO₂ Emissions (Tt) | 0.932 | 12.9 | 97.9 ekg/TT |
| Oil Export | Oil % GDP | 0.927 | 0.9 | 1.3 Mbbl/% |
| Renewable Gen Capacity | GDP | 0.923 | 12.9 | 222.1 ekg/G$ |
| Fossil Fuel Gen Capacity | Renewable Gen Capacity | 0.921 | 46.9 | 0.3 ekg/ekg |
| Refined Fuel Consumed | GDP | 0.918 | 3.1 | 1193.9 Mbbl/G$ |
| Oil Import | GDP | 0.914 | 1.5 | 2432.9 Mbbl/G$ |
| Hydro Gen Capacity | CO₂ Emissions (Tt) | 0.909 | 11.4 | 101.5 ekg/TT |
| Fossil Fuel Gen Capacity | Refined Fuel Consumed | 0.903 | 46.9 | 0.0 ekg/Mbbl |
| Refined Export | Nat Gas Consumed | 0.900 | 0.8 | 132.7 Mbbl/Gcm |
| Electric Consumption | Refined Fuel Consumed | 0.895 | 29.1 | 0.1 ekg/Mbbl |
| Electric Production | Refined Fuel Consumed | 0.893 | 31.5 | 0.1 ekg/Mbbl |
| Refined Fuel Produced | GDP | 0.892 | 2.9 | 1132.5 Mbbl/G$ |
| Fossil Fuel Gen Capacity | Oil Import | 0.889 | 46.9 | 0.0 ekg/Mbbl |
| Refined Fuel Produced | Nat Gas Consumed | 0.883 | 2.9 | 33.6 Mbbl/Gcm |
| Oil Export | Growth Rate | -0.545 | 0.9 | -0.6 Mbbl/% |

## Brief relativity summary

Energy is hard to grasp in abstract SI form. U.S. electricity use of about 3,900 TWh in 2016 is hard to picture — until you notice that as pure mass-energy it is only a few hundred pounds.

Time is not a special dimension separate from space; measuring the second as ~300,000 km makes `c = 1`. Substituting that into everyday energy formulas makes mass and energy the same unit. One kilogram is about 89.9 PJ or 25 TWh.

In the equation E = mc^2^,  c^2^ is actually just a conversion factor and not very interesting :grinning:

The Sun radiates ~385 yottawatts — on the order of 0.1× the mass of Mt. Everest per hour. Annual world electricity production is roughly a tonne of mass-energy (order of magnitude: hundreds of kilograms). One Nagasaki-class yield is about one gram.

Castle Bravo released on the order of **63 petajoules** — about **700 grams**. That yield is the custom unit `shrimp` in this file (`shrimp` = `castlebravo`).

## Appendix: contextual units and yield reference

| Name | Yield | Mass-energy | Date | Device | Notes |
| ---- | ----- | ----------- | ---- | ------ | ----- |
| Trinity | 19 kt | ~0.88 g | 1945-07-16 | Gadget | First test, White Sands, NM |
| Hiroshima | ~15 kt | ~0.70 g | 1945-08-06 | Little Boy | U-235 gun-type |
| Nagasaki | ~21 kt | ~0.98 g | 1945-08-09 | Fat Man | Pu-239 implosion |
| Castle Bravo | 15 Mt / ~63 PJ | ~701 g | 1954-03-01 | Shrimp | Largest U.S. test |
| Chicxulub | 4.184×10²³ J | ~4.65×10⁶ g | 66 Ma | — | K–Pg extinction impact |
| Solar (1 s) | 3.828×10²⁶ J | ~4.25×10⁹ g | Present | — | Solar luminosity |
| Nova | ~10⁴⁴ J | ~10²⁷ g | — | — | Order-of-magnitude |

## Contributing / sharing

- The core deliverable is `massenergy.units` — keep it small and commented.
- Historical yield numbers may be updated when better public estimates appear; keep device aliases (`gadget`, `littleboy`, …) linked to the yield names.
- Longer essay material and exercise ideas live in `README-original.md` and `Projects.md`.

## License

[MIT](LICENSE) — Copyright (c) 1995, 2008, 2017, 2026 Jillian England.
