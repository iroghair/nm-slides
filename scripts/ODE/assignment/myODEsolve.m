function [t,x] = myODEsolve(N)
x_init = [0];
tspan = [0 1e-3];
options = odeset('RelTol',1e-4,'AbsTol',[1e-4]);
N
[t,x] = ode45(@myODEfunction,tspan,x_init,options,N);

return
