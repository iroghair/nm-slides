function [dxdt] = myODEFunction(t,x)
dxdt(1) = -1*x(1) - 1*x(2);
dxdt(2) = x(1) - 2*x(2);
dxdt=dxdt';
return