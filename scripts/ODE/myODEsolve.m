x_init = [0 1];
tspan = [0 10];
options = odeset('RelTol',1e-4,'AbsTol',[1e-4 1e-4]);

[t,x] = ode45(@myODEfunction,tspan,x_init,options);