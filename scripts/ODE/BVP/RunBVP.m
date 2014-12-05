function x_end = RunBVP(N)
[z,x] = ode45(@BVPODE,[0 1e-3],[0.2 0], [], N);
x_end = x(end,1) - 0;
% plotyy(x,cq(:,1),x,cq(:,2));
return;
