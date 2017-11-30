function [dcdt] = stiff_ode(t,c)
dcdt = zeros(2,1);
dcdt(1) =  998 * c(1) + 1998*c(2);
dcdt(2) = -999 * c(1) - 1999*c(2);
return
