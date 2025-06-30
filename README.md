# MassEnergy: A Mass-Based Energy Conversion Layer for GNU Units

> "Mass is not equivalent to energy. Mass **is** energy."

## Overview

This project introduces a `massenergy.units` file for use with the GNU `units` utility, redefining the speed of light (`c = 1`) and rescaling the second to represent light travel distance (\~299,792 km). These changes allow you to directly convert between mass and energy, effectively treating them as the same unit.

Through this lens, a gram becomes 21 kilotons. A sugar cube is a city-level bomb. And the Sun, in its radiant glory, evaporates 4 million tons of mass every second.

You’ll never see the universe quite the same again.

---

## Features

- 🌍 Redefines core units: `second = 299792 km`, `c = 1`
- 🔁 Enables seamless mass-energy conversions via `E = mc^2`
- 🧠 Makes abstract energy quantities intuitive by expressing them in grams or kilograms
- 📊 Includes real-world examples from physics, history, and geopolitics

---

## Installation

### Step 1: Install GNU Units

- On Linux/macOS:
  ```bash
  sudo apt install units     # Debian/Ubuntu
  brew install units         # macOS (Homebrew)
  ```
- On Windows: Use [Cygwin](https://www.cygwin.com/) or WSL.

### Step 2: Use the File

```bash
units -f "" -f /path/to/massenergy.units
```

For convenience, add an alias in your `.bashrc`:

```bash
alias lightunits='units -vf "" -f /usr/share/units/massenergy.units'
```

---

## What This File Does

- Modifies speed of light to `1`
- Rescales time to be distance-equivalent (`1 second = 299792.458 km`)
- Preserves accuracy and dimensional integrity despite radical re-scaling

By doing so, mass and energy, space and time, are brought into direct, calculable parity.

> "Time and distance are the same thing. Ergo, mass and energy are the same thing."

---

## Usage Examples

### Convert a gram to kilotons:

```bash
You have: 1 g
You want: ton_e
        1 g = 21480.764 ton_e
```

### Compare nuclear yields:

```bash
You have: nagasaki
You want: hiroshima
        nagasaki = 1.76 hiroshima
```

### How much energy is in a sugar cube (\~5 g)?

```bash
You have: 5 g
You want: ton_tnt
        5 g = 107,403.82 ton_tnt
```

### Earth to Sun-scale conversions:

```bash
You have: 384.6 yottawatt * 60 * 60 * 24 * 365.2422 * 4 giga
You want: earthmass
        = 90.414858 earthmass
```

---

## Selected Events in Mass Equivalents

| Event                      | Energy (J)    | Mass Equivalent (g) |
| -------------------------- | ------------- | ------------------- |
| Trinity test (19 kt)       | 7.95 × 10^13  | 0.88 g              |
| Hiroshima (12.5 kt)        | 5.24 × 10^13  | 0.58 g              |
| Castle Bravo (15 Mt)       | 6.3 × 10^16   | 701 g               |
| Solar luminosity (per sec) | 3.828 × 10^26 | 4.25 × 10^9 g       |
| Chicxulub impact           | 4.184 × 10^23 | 4.65 × 10^6 g       |

---

## Philosophy: Why Use Mass as a Unit of Energy?

- **Relatable:** We interact with grams and kilograms daily.
- **Tangible:** Saying "this bomb released 1 gram of energy" is easier to grasp than "63 petajoules".
- **Intuitive Scaling:** Makes cosmic or geopolitical energy use easier to visualize.
- **Physics-Aligned:** Mass and energy are literally interchangeable via `E = mc^2`.

> "A loaf of bread converted entirely to energy could power the Earth for a day."

---

## Advanced Concepts & Warnings

- This file will not help you perform Lorentz transformations or spacetime tensor calculus.
- For spacetime intuition, see *Spacetime Physics* by Edwin Taylor & John Wheeler.
- This project is not affiliated with the GNU Units team.
- Don't mix these unit definitions into unrelated calculations — they are contextually radical.

---
### Summary of World Energy Usage and economics

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
## Global Energy and Economic Relationships

- The abreviation ekg means kg of energy, yes as in the antimatter equivelent kind.
- GDP is gross domestic prodcut.

This data came from the CIA Factbook in 2017.

| Independent (X)                 | Dependent (Y)                   | Correlation | Mean X  | Slope           |
| ------------------------------- | ------------------------------- | ----------- | ------- | --------------- |
| Electric Consumption            | Generating Capacity Fossil Fuel | 0.993       | 29.1    | 1.7 ekg/ekg     |
| Generating Capacity Fossil Fuel | GDP                             | 0.984       | 46.9    | 64.8 ekg/G\$    |
| Electric Production             | GDP                             | 0.982       | 31.5    | 102.0 ekg/G\$   |
| Electric Production             | CO₂ Emissions (Tt)              | 0.977       | 31.5    | 44.3 ekg/TT     |
| Fossil Fuel Gen Capacity        | CO₂ Emissions (Tt)              | 0.969       | 46.9    | 27.8 ekg/TT     |
| Nat Gas Produced                | Nat Gas Consumed                | 0.955       | 102.8   | 0.8 Gcm/Gcm     |
| Oil Reserves                    | Oil % GDP                       | 0.946       | 30974.6 | 0.0 Gbbl/%      |
| GDP                             | CO₂ Emissions (Tt)              | 0.942       | 4090.6  | 0.4 G\$/TT      |
| Electric Consumption            | Renewable Gen Capacity          | 0.934       | 29.1    | 0.4 ekg/ekg     |
| Renewable Gen Capacity          | CO₂ Emissions (Tt)              | 0.932       | 12.9    | 97.9 ekg/TT     |
| Oil Export                      | Oil % GDP                       | 0.927       | 0.9     | 1.3 Mbbl/%      |
| Renewable Gen Capacity          | GDP                             | 0.923       | 12.9    | 222.1 ekg/G\$   |
| Fossil Fuel Gen Capacity        | Renewable Gen Capacity          | 0.921       | 46.9    | 0.3 ekg/ekg     |
| Refined Fuel Consumed           | GDP                             | 0.918       | 3.1     | 1193.9 Mbbl/G\$ |
| Oil Import                      | GDP                             | 0.914       | 1.5     | 2432.9 Mbbl/G\$ |
| Hydro Gen Capacity              | CO₂ Emissions (Tt)              | 0.909       | 11.4    | 101.5 ekg/TT    |
| Fossil Fuel Gen Capacity        | Refined Fuel Consumed           | 0.903       | 46.9    | 0.0 ekg/Mbbl    |
| Refined Export                  | Nat Gas Consumed                | 0.900       | 0.8     | 132.7 Mbbl/Gcm  |
| Electric Consumption            | Refined Fuel Consumed           | 0.895       | 29.1    | 0.1 ekg/Mbbl    |
| Electric Production             | Refined Fuel Consumed           | 0.893       | 31.5    | 0.1 ekg/Mbbl    |
| Refined Fuel Produced           | GDP                             | 0.892       | 2.9     | 1132.5 Mbbl/G\$ |
| Fossil Fuel Gen Capacity        | Oil Import                      | 0.889       | 46.9    | 0.0 ekg/Mbbl    |
| Refined Fuel Produced           | Nat Gas Consumed                | 0.883       | 2.9     | 33.6 Mbbl/Gcm   |
| Oil Export                      | Growth Rate                     | -0.545      | 0.9     | -0.6 Mbbl/%     |

## Brief Relativity Summary

Energy is very difficult for people to comprehend. We understand things we can hold, lift, and see. If you knew that the USA consumed 3,902 terawatt-hours in 2016 it seems incomprehensible. What if I told you that this could be loaded into the back of your truck and would weigh 344.6 lbs. (156.3 kg)?

Time is not a special unit; it is part of space and should be measured in meters—specifically three hundred million meters. Substituting the new value for `s` makes the speed of light a unitless constant equal to one.

When you substitute `s = 300 thousand km` into Newtonian physics, energy and mass become the same thing. A kg is 89.9 PJ or 25 TWh. This might take 186,000 miles to absorb.

Note: In AE's famous "E = mc²", `c²` is just a conversion factor. The speed of light, `c = 1`, and 1 squared is still 1.

Our star radiates 385 yottawatts—about 0.1× the mass of Mt. Everest per hour or 15,000 trillion Nagasakis per hour. *(yotta = trillion trillion)*

How much energy the Earth absorbs and radiates per day seems to be a closely guarded secret. Clearly, absorption and radiation are in equilibrium because the Earth is not getting warmer or cooler within any margin of error we can currently measure.

Note: Mass is not matter; it is an attribute of matter.

Note: The Nagasaki bomb released 1 g of energy. A 21-megaton bomb releases a kg of energy—1000× Nagasaki. Annual world electricity production is about 24,000 TWh or 947 kg (947,000 Nagasaki-sized bombs). I am aware of the rounding error here but am trying to communicate—not get lost in the weeds. One Nagasaki is actually 1.0242 g.

Castle Bravo, the most powerful nuclear test conducted by the United States, released **63 petajoules** of energy—equivalent to **700.97 grams** of mass. The device was nicknamed **SHRIMP**, an acronym for *Staged Hydrogen Radiation IMPlosion*.

This yield defines the custom unit `shrimp` in this project. For quick reference: **1 shrimp = 700 g**.

## Appendix: Contextual Units and Yield Reference

| Name         | Yield (kt / PJ) | Mass-Energy (g) | Date       | Device Name | Design / Fuel                       | Notes                                 |
| ------------ | --------------- | --------------- | ---------- | ----------- | ----------------------------------- | ------------------------------------- |
| Trinity      | 19.0 kt         | 0.8845 g        | 1945-07-16 | Gadget      | Pu-239 implosion                    | First test near White Sands, NM       |
| Hiroshima    | 12.5 kt         | 0.5819 g        | 1945-08-06 | Little Boy  | U-235 gun-type                      | \~118,661 killed                      |
| Nagasaki     | 22.0 kt         | 1.0241 g        | 1945-08-09 | Fat Man     | Pu-239 implosion                    | \~73,884 killed                       |
| Castle Bravo | 15 Mt / 63 PJ   | 700.97 g        | 1954-03-01 | Shrimp      | Pu-239, Li-6, U-238, Tritium staged | Largest U.S. test, Bikini Atoll       |
| Chicxulub    | 4655 years of current human energy use      | \~4.65×10⁶ g    | 66 MYA     | —           | Asteroid kinetic impact             | Cretaceous–Paleogene extinction event |
| Solar (1 s)  | 3.828×10²⁶ J    | 4.25×10⁹ g      | Present    | —           | Hydrogen fusion                     | Current solar luminosity              |
| Nova         | \~1.11×10⁴⁴ J   | \~1.11×10²⁷ g   | —          | —           | Small star thermonuclear explosion  | Contextual astrophysical reference    |

