MassEnergy - Units Energy to mass conversion
==============================================================================
Summary
-------
A conversion file for the "units" mathematics utility that modifies core constants setting; second = 299 thousand meters and c = 1.  This  simple change allows the units tool to render mass to energy space to time solutions.  Amazingly changing these fundemental constants does not effect calculation results or the usefulness of Units. If your conversion gives mass instead of energy like you were expecting you may sometimes need to specify that you want joules or watts.

You will never see the universe exactly the same again.

License
-------
Copyright (c) Jillian England, 1995, 2008, 2017, 2018, 2019

GNU License.

About Units
-----------
Units, version 2.14, is a mathematical "Console Unit Converter".

The Units program converts quantities expressed in various scales
to their equivalents in other scales."
See the units homepage; "http://www.gnu.org/software/units/"

Units can be installed with cygwin on a windows systems.  
https://www.cygwin.com/ 

There may be other ways of installing it on windows as well.

This MassEnergy.units file project is *not* related to the Gnu unit's software project.

Units does have several manuals; UnitsWin.pdf, UnitsMKS.pdf, units.pdf 

Usage
-----
units -f '' -f massenergy.units

Can be installed in '/usr/share/units' but this is not required.

##### .bashrc
```
alias lightunits='(units -vf "" -f /usr/share/units/massenergy.units)'
```

Will not help with Spacetime Physics
------------------------------------

This file will NOT help you with your Lorentz transformations or understanding
the geometry of spacetime. To learn that time is really just a 4th dimension
of space and that a second is actually 300 thousand kilometers (186,000 miles) 
you need some spacetime physics. You can take an undergraduate STP class if one is 
available or/and there are many books and videos that are fun and even necessary for continious
immersion in this subject.

An excellent textbook is; "Spacetime Physics, Edwin Taylor and John Archibald Wheeler, Copyright(c)1992".
Both the first and second versions of this book are great.

Annother essential book, a biography of Ted Taylor by John McPhee, will alter the way you see the world;
"The Curve of Binding Energy: a Journey into the Awesome and Alarming world of Theodore B. Taylor, John McPhee, May 22nd 1974".  

Examples
--------
 One gram is equal to about 21,480 tons of TNT or 21 kilotons.
 Trinity and Fatman both liberated about a gram of energy
```
You have: g
You want: ton_e
        g = 21480.764 ton_e

You have: nagasaki
You want: g
        nagasaki = 1.0241721 g
```
The bomb dropped on Nagasaki was 76% more powerful than the bomb dropped on Hiroshima the previous week.
Little boy released 0.58 grams of energy
```
You have: nagasaki
You want: hiroshima
        nagasaki = 1.76 hiroshima
```
A person weighing 170 lbs (77 kg, 12.1 stone) is 1.65 thousand Megatons, or 110 SHRIMP bombs.
OR just 77.11 kg of energy ... mass is energy there is really no need to convert it.
```
You have: 170 lbs
You want: stone
        170 lbs = 12.142857 stone
You want: kg
        170 lbs = 77.110703 kg
You want: Mton_e
        170 lbs = 1656.3968 Mton_e
You want: shrimp
        170 lbs = 110.00578 shrimp
```
 The Castle Bravo shot was most powerful H-bomb tested by the USA. 
 It released 63 peta joule (PJ), appoximately 15 megatons of TNT.
	 The bomb components themselves were nicknamed 'SHRIMP' which may be an acronym, "System for Hydrogen Radiation IMPlosion".
 This bomb was 684 times the energy release of Fatman which was used against Nagasaki. 
```
You have: 63 PJ
You want: Mton_e
        63 PJ = 15.057361 Mton_e

You have: 63 PJ
You want: nagasaki
        63 PJ = 684.42552 nagasaki
```
 An hour is 670 million miles. 
```
You have: hour
You want: kmiles
        1 hour = 670616.63 kmiles

You have: 1 hour
You want: au
        1 hour = 7.2143597 au
```
 A tera watt hour is a whopping amount of energy, equivalent to 40 grams of mass! (thats about 40 fatman bombs)
```
You have: tera watt hours
You want: g
        tera watt hours = 40.055402 g
```
 The following PDF gives lots of numbers to play with.
  http://www.sandia.gov/~jytsao/Solar%20FAQs.pdf

 I find that all the numbers make more sense when I convert Terra watts into grams
 
```
You have: tera watt hour
You want: g
        tera watt hour = 40.055402 g

You have: 15 TW  years
You want: g
        15 TW  years = 5266772.3 g

You have: 15 TW  years
You want: kg
        15 TW  years = 5266.7723 kg
```
 In the 1950's the US built 300 MK-17 and MK-24 bombs, each of which could release 
 approximately 20 Megatons of energy (23 terra watt hours, 0.91 kg) for a total cold war arsenal of 6,000 Megatons. 
 In total these bombs would have released 616 lbs (279 kg) of mass as energy or 6,973 Tera watt hours.
 
 Every one of these bombs could have incinerated a large city while setting fire
 to half a state the size of Washington. True wrath of God type of stuff. These weapons and their counterparts in the Soviet Union are the reason people of the era dug bomb shelters in their back yards.  It was not mass hysteria there really was a world ending man made threat.
 
 All of the American Mark 17 & 24's were removed from service and dismantled in the late 1950's.
```
You have: 20 Mton_e 300
You want: lbs
        20 Mton_e 300 = 615.79446 lbs
    
You have: 20 Mton_e 300
You want: Twatt hours
        20 Mton_e 300 = 6973.3333 Twatt hours

You have: 20 Mton_e 300
You want: Twatt year
        20 Mton_e 300 = 0.79551475 Twatt year
        
You have: 20 Mton_e 300
You want: thousand fatman
        20 Mton_e 300 = 272.72727 thousand fatman
```
An exploding star releases the the mass of 186 earths. If the entire mass of the earth 
was converted into energy it would only be 1/200'th that of an exploding star.
```
You have: nova
You want: earthmass
        nova = 186.24123 earthmass
        nova = (1 / 0.0053693802) earthmass        
```
4H -> He + 24MeV, Which brings up an interesting point. If the sun has been hot for 4 billion years how much mass has it lost in mass to energy conversion?

Lets see; 4 billion years at (todays rate kg/hr conversion) ... oooo this is going to be fun :)

From Old Article

"The sun radiates uniformly in all directions. We can calculate the total amount of energy radiated by measuring the quantity of solar energy/second reaching every square meter of Earth and then multiplying that by the total surface area of a sphere with radius equal to the radius of Earth orbit. We get the astonishingly huge amount of 400 trillion trillion watts."

The exact amount of energy released by the Sun is not as solid a number as I had thought. It turns out values in literature have been as high as 400 yotta watts.  

At the time of this writing I found a value of 
* 382.8 yotta W on wiki and 
* 384.6 yotta W on a nasa fact sheet.

For the best/latest value I suggest you research it looking for "Solar Luminosity".   Note: Luminosity is not the only radiation or energy transfer from the sun.  There are also magnetic, partical, solar wind energy transfers that are not accounted for in luminosity.

* NASA
https://web.archive.org/web/20100715200549/http://nssdc.gsfc.nasa.gov/planetary/factsheet/sunfact.html

* Wikipedia
https://en.wikipedia.org/wiki/Sun

Calculation Of Earth Masses Lost from Hydrogen Fusion over Sun's Lifetime
=

trillion trillion = yotta = 1e+24

Using value of 384.6 yotta W solar luminosity

384.6 yotta watt sec = 384.6 yotta J

which is 91,922 trillion ton_tnt_energy
which (divided by a million) is ~one tenth of a trillion Megaons
or 91.9 Billion Mega tons per second

Which is only 4.7 million tons of mass to energy conversion per second;

work;

384.6 yotta watt seconds = 4.717 million tons (mass/sec)
= 283 million ton (mass/ min)
= 16,981 million ton (mass/hour)
= 407,554 million ton (mass/day)
= 148.9 trillion ton (mass/year)

times 4 billion years

= 0.59 tera tera tons (mass/4 billion years)
= 0.59 yotta tons (mass/4 billion years)

```
You have: 384.6 yotta watt s *60 *60 *24 *365.2422 * 4 giga
You want: yotta ton
        384.6 yotta watt s *60 *60 *24 *365.2422 * 4 giga = 0.59542467 yotta ton
        
You have: 384.6 yotta watt s *60 *60 *24 *365.2422 * 4 giga
You want: earthmass
        384.6 yotta watt s *60 *60 *24 *365.2422 * 4 giga = 90.414858 earthmass
	
You have: 384.6 yotta watt s *60 *60 *24 *365.2422 * 4 giga
You want: solarmass
        384.6 yotta watt s *60 *60 *24 *365.2422 * 4 giga = 0.00027156009 solarmass
	
You have: 384.6 yotta watt s *60 *60 *24 *365.2422 * 4 giga
You want: jupitermass
        384.6 yotta watt s *60 *60 *24 *365.2422 * 4 giga = 0.28441808 jupitermass

You have: 384.6 yotta watt s *60 *60 *24 *365.2422 * 4 giga
You want: nova
        384.6 yotta watt s *60 *60 *24 *365.2422 * 4 giga = 0.48547175 nova
```
**if the earth weighs 6.59+21 ton then; The sun radiated a mass equivelent to 90.41 earths over it's 4 billion year life or .0003 current solar masses or .28 Jupiter masses over it's four billion year life.**

**Interesting; 4 billion years star burn = Half of a Nova?**

This assumes constant solar radiation for four billion years which is certainly incorrect.

That was fun ... what else can I convert to energy ? 

#### CIA Factbook Energy
Not complete, new edit coming soon
Trying to make better sense of the energy requirements of our world is eaiser when converting electrical kW into kg.

The World total production energy is (at the time of this doc edit) 
```
You have: 23.65 trillion kWh
You want: TWh
        23.65 trillion kWh = 23650 TWh
You want: Mton_e
        23.65 trillion kWh = 20348.948 Mton_e
You want: kg
        23.65 trillion kWh = 947.31026 kg
```
Installed generation capacity for world is listed as;

6.386 billion kW (2015 est.)
```
 * Converting capacity to Annual TWh should be TW * year * 24

 * Note; 
	//C# -> $"{Igc.TW * 365.242198781 * 24 *TWh2kg}\t" 
	// 365.242198781 day/year * 24 hr/day *.040055 TWh/kg 
You have: 6.386 TW *year *24 hr/day
Definition: 2242.2405 kg

```


```
TW prd  TW cap  Srpls rtio  country
11.03   40.10   3.64    Italy
10.36   37.18   3.59    Spain
24.55   73.21   2.98    Germany
121.89  342.34  2.81    European Union
12.75   34.08   2.67    United Kingdom
10.49   27.56   2.63    Turkey
39.63   103.90  2.62    Japan
10.91   27.25   2.50    Iran
235.65  580.40  2.46    China
947.31  2242.24 2.37    World
55.52   129.14  2.33    India
22.75   52.95   2.33    Brazil
164.03  381.67  2.33    United States
12.98   29.12   2.24    Saudi Arabia
21.19   45.93   2.17    France
```
##### End of examples
####  Errata
* Freeman’s gift? It’s cosmic. He is able to see more interconnections between more things than almost anybody. He sees the interrelationships, whether it’s in some microscopic physical process or in a big complicated machine like Orion. He has been, from the time he was in his teens, capable of understanding essentially anything that he’s interested in. He’s the most intelligent person I know. — Ted Taylor
* Space has four dimensions.  Time is one of those dimentions measured in meters just like the other three.  A *second* is in reality 300 thousand kilometers. (this means the speed of light is actually 1, without units)
* Mass is NOT equivalent to energy:  **_Mass IS Energy_**
* Matter is not the same thing as mass. Mass is just one attribute of matter. Other attributes of matter are charge, spin, time direction ... _
* **Calculating yields and controversy** There is a well written Wikipedia page that discusses the problems and politics of measuring the energy released by nuclear bombs here; https://en.wikipedia.org/wiki/Nuclear_weapon_yield
