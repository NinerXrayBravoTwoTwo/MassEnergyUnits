[MassEnergy - Units](http://www.hyperfaceted.com/) - Energy to mass conversion
==============================================================================
Summary
-------

An extension for the Unix units conversion files that changes 
energy to mass and seconds to meters.  
    You will never see the universe exactly the same again.

License
-------
Copyright (c) Jillian England, 1995, 2008, 2017. 

GNU License.
    CopyLeft if that is still in vogue 

About Units
-----------
Units, version 2.14, is a mathematical "Console Unit Converter".

The Units program converts quantities expressed in various scales
to their equivalents in other scales."
See the units homepage; "http://www.gnu.org/software/units/"

Units can be installed with cygwin on a windows systems.  
https://www.cygwin.com/ 

There may be other ways of installing it on windows as well.

Units is one of my favorite programs.  Especially since I taught it that one second is 300 thousand kilometers 
and speed of light is one.

Usage
-----
units -f '' -f massenergy.units

Can be installed in '/usr/share/units' but this is not required.

##### .bashrc
```
alias lightunits = '(units -vf "" -f /usr/share/units/massenergy.units)'
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
 On gram is equal to about 21,480 tons of TNT or 21 kilotons.
 Trinity and Fatman both liberated about a gram of energy
```
You have: g
You want: ton_e
        g = 21480.764 ton_e

You have: nagasaki
You want: g
        nagasaki = 1.0241721 g
```
A person weighing 170 lbs (77 kg, 12.1 stone) is 1.65 thousand Megatons, or 110 SHRIMP bombs.
OR just 77.11 kg of energy ... mass is energy there is really no need to convert it.
```
~ Extra 'You have:' lines have been removed from this result for brevity ...
You have: 170 lbs
You want: stone
        170 lbs = 12.142857 stone
You want: kg
        170 lbs = 77.110703 kg
You want: stone
        170 lbs = 12.142857 stone
You want: Mton_e
        170 lbs = 1656.3968 Mton_e
You want: shrimp
        170 lbs = 110.00578 shrimp
```
The bomb dropped on Nagasaki was almost twice as powerful as the bomb dropped on Hiroshima the previous week.
Little boy released 0.58 grams of energy and fatman released 1.02.
```
You have: nagasaki
You want: hiroshima
        nagasaki = 1.76 hiroshima
```
 The Castle Bravo shot was most powerful H-bomb tested by the USA. 
 It released 63 peta joule (PJ), appoximately 15) Megatons.
	 The bomb components themselves were nicknamed 'SHRIMP' which may be an acronym.
 This bomb was 684 times the energy release of Fatman which was used against Nagasaki. 
```
You have: 63 PJ
You want: Mton_e
        63 PJ = 15.057361 Mton_e

You have: 63 PJ
You want: nagasaki
        63 PJ = 684.42552 nagasaki
```
 An hour is 670 thousand miles. 
```
You have: 1 hour
You want:
        Definition: 1.0792528e+12 m

You have: hour
You want: kmiles
        1 hour = 670616.63 kmiles

You have: 1 hour
You want: au
        1 hour = 7.2143597 au

You have: au
You want:
        Definition: astronomicalunit = 149597870700 m = 1.4959787e+11 m
```
 Are a year and a light year the same thing?  Depends on politics ;)
```
You have: year
You want: ly
        year = 0.99997864 ly
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
 about ~20 Megatons of energy for a total cold war arsenal of about 6,000 Megatons 
 in this one weapon system. This was equal to 616 lbs of matter-energy conversion or ~7,000 
 Terra watt hours. Each of these bombs could have incinerated a large city and set fire
 to half a state the size of Washington.
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

##### End of examples
####  Errata
* Freeman’s gift? It’s cosmic. He is able to see more interconnections between more things than almost anybody. He sees the interrelationships, whether it’s in some microscopic physical process or in a big complicated machine like Orion. He has been, from the time he was in his teens, capable of understanding essentially anything that he’s interested in. He’s the most intelligent person I know. — Ted Taylor
* Space has four dimensions.  Time is one of those dimentions measured in meters just like the other three.  A *second* is in reality 300 thousand kilometers. (this of course means the speed of light is actually 1, without units)
* Mass is NOT equivalent to energy:  **_Mass IS Energy_**
* Matter is not the same thing as mass either. Mass is just one attribute of matter. Other attributes of matter are charge, spin, time direction ... 
* It seems that the mass attribute of matter can be seperated from matter's other attributes at the 'event horizon of a black hole leaving the remaining part of matter, it's 'information' components, behind while the energy/mass component becomes part of the singularity. 	_I will not pretend that I actually understand this._
