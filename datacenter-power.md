# Data Centers -- A *hot* topic :wink:
<p align="center">
  <img src="images/data-center-1.jpg" width="650" alt="Data Center - Grok generate">
  <h3 align="center">Data Center Power and Waste Heat Comparison</h3>
</p>

---

### Data centers are being built all over the world in sizes up to 1 megawatt power consumption.

To power these **production** centers we are building matching power plants.

All this energy is eventually converted to heat and must be radiated away from the servers.

---

## Gas-Fired Power Plant + 500 MW Data Center

| Component                                 | Power (MW)        | Notes                                    |
| ----------------------------------------- | ----------------- | ---------------------------------------- |
| Fuel burned at power plant                | 1,000 – 1,250     | Natural gas input                        |
| Waste heat from power plant               | 500 – 750         | Dumped locally (cooling towers, exhaust) |
| Electricity delivered to data center      | 500               | Usable output from plant                 |
| Waste heat from data center               | 500               | All electricity becomes heat             |
| **Total waste heat added to environment** | **1,000 – 1,250** | Combined from plant + data center        |

A natural-gas-powered 500 MW data center (the largest being considered) would add heat to the
environment of about **1/97,600,000** of our current daily sunshine.

:sun_with_face:

``` plaintext
You have: 1250 MW
You want: earthsolarabsorbed (ESA)
        1250 MW = 1.0245902e-08 ESA
        1250 MW = (1 / 97,600,000) ESA
```

---

## Nuclear Power Plant + 500 MW Data Center

| Component                                 | Power (MW) | Notes                             |
| ----------------------------------------- | ---------- | --------------------------------- |
| Fuel burned at power plant (thermal)      | ~550       | Nuclear fission heat input        |
| Waste heat from power plant               | ~50        | Dumped via cooling towers         |
| Electricity delivered to data center      | 500        | Usable output from plant          |
| Waste heat from data center               | 500        | All electricity becomes heat      |
| **Total waste heat added to environment** | **~550**   | Combined from plant + data center |

**Key takeaway:** Nuclear is far more efficient with much less waste heat. Even the gas case is orders of magnitude below exaggerated claims like 10 GW per data center.

:sun_with_face:

A nuclear-powered 500 MW data center has considerably less waste heat when powered by nuclear instead of gas, equivalent to about **1/222,000,000** of daily sunlight.

``` plaintext
You want: ESA
        550 MW = 4.5081967e-09 ESA
        550 MW = (1 / 221,818,181) ESA
```
---
