### List of errors

* Readme is unfinished
* Book referances need to be corrected to standard format, include ISDN's if possible.
* The hyperlink on the readme page point's to a web site I don't have hosted at the moment
* Readme should be less personal and more professional.  Phrases such as "I like" etc should be removed.
* Could just reduce the examples to a few key examples and create a seperate Examples.md document to 
include a larger list.
* Group the examples by topic and add topic sub header
* Missing example for Tritium / Mol  fusion reaction energy.  Should be able to estimate yeild from fusion by 4H -> He + 24MeV and subsequent estimate of secondary minimum construction weight.  I did this calculation once 30 years ago and a new example could be interesting.

### List of possible projects

* Missing a simple explanation of Spacetime.  A spacetime diagram might help or confuse ...
* Pictures?  If so which ones would help.  Should be referenced from a public Wiki I believe.
* A tool that draw's good spacetime diagrams with hyperbolic graph lines that can be used to
create diagrams for powerpoints and other presentations.  Could this use povray for some diagrams?
* A seperate file for this that includes all the shot designations, type, estimated yeild, aliases.
* Should all shot designations be resolved to Peta Joules instead of tons_tnt?
* A lorenz transformation is just a conversion from one spacetime world line to another.  There may be a way to teach units to do
lorenz transforms with simple definitions.  I may have already achived it to some degree with this definition set but I believe more needs to be done.  I'll play with it.
* I have a simple program that displays a time countdown expressd in ly, au, miles instead of hours min sec which is kind of neat (and simple)
```
var ly = interval.TotalDays / 365.25;
var au = interval.TotalDays * 173.14463;
var mi = interval.TotalDays * 16.094799;

Console.WriteLine($"{interval.TotalDays:N5} days");
Console.WriteLine("");

Console.WriteLine($"{ly:N8} ly");
Console.WriteLine($"{au:N3} au");
Console.WriteLine(mi > 100 ? $"{mi:N4} billion miles" : $"{mi * 1000:N1} million miles");
```
