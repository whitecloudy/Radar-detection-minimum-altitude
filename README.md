Simple program which can calculate radar's minimum detection altitude based on Distance from radar and Angle.

I assumed that the earth is perfect sphere because the calculation can be too difficult.

I will add the height of radar someday

*********************************************************************************************************

**Calculation Equation**

L -> length from earth center to point of minimum detection altitude
A -> Minimum detection altitude
r -> Earth radius
d -> Earth surface distance
a -> angle of radar(degree)

b = d/2rπ * 360(degree)

    r * cot(a) * sec(b)
L = -------------------
      cot(a) - tan(b)
      
A = L - r
