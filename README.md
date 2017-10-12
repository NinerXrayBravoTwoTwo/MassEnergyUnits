[MassEnergy - Units](http://www.hyperfaceted.com/) - Energy to mass and back was never this easy
================================================================================================
Summary
-------
An extension for the Unix units conversion files that changes 
energy to mass and seconds to meters.  Will never see the universe exactly the same again.

License
-------
Copyright (c) Jillian England, 1995, 2008, 2017. 


Can be installed in '/usr/share/units' but you don't have to.
GNU License. CopyLeft if that is still in vogue 

Usage
-----
units -f '' -f massenergy.units

Bash alias

alias lightunits=
'(units -vf "" -usr/share/units/massenergy.units)'

Will not help with Spacetime physics
------------------------------------

This file will NOT help you doing Lorentz transformations or understanding
the geometry of spacetime.  

I recommend "Spacetime Physics, Edwin Taylor and John Archibald Wheeler, Copyright(c)1992"

Examples
--------

On gram is equal to about 21,480 tons of TNT or 21 kilotons
Trinity and Fatman both liberated about a gram of energy

You have: g
You want: ton_e
        g = 21480.764 ton_e

You have: nagasaki
You want: g
        nagasaki = 1.0241721 g

---------
An hour is a very long distance. 
It is 670 thousand miles 

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
---------
 Are a year and a light year the same thing?  Depends on politics ;)
You have: year
You want: ly
        year = 0.99997864 ly


 A tera watt hour is a whopping amount of energy!
 equivalent to 40 grams of mass! (thats about 40 fatman bombs)

You have: tera watt hours
You want: g
        tera watt hours = 40.055402 g

 The following PDF gives lots of numbers to play with.
  http://www.sandia.gov/~jytsao/Solar%20FAQs.pdf

 I find that all the numbers make more sense when I convert Terra watts into grams

You have: tera watt hour
You want: g
        tera watt hour = 40.055402 g

You have: 15 TW  years
You want: g
        15 TW  years = 5266772.3 g

You have: 15 TW  years
You want: kg
        15 TW  years = 5266.7723 kg
--------
 In the 1950's the US built 300 MK-17 and MK-24 bombs, each of which could release 
 about ~20 Mega ton's of energy for a total cold war arsenal of about 6,000 Mega tons 
 in this one weapon system. This was equal to 616 lbs of matter-energy conversion or ~7,000 
 Terra watt hours. Each of these bombs could have incinerated a large city and set fire
 to half a state the size of Washington

You have: 20 Mton_e 300
You want: lbs
        20 Mton_e 300 = 615.79446 lbs
You have: 20 Mton_e 300
You want: Twatt hours
        20 Mton_e 300 = 6973.3333 Twatt hours

You have: 20 Mton_e 300
You want: Twatt year
        20 Mton_e 300 = 0.79551475 Twatt year

End of examples
