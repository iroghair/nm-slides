load('tudataset1.mat');
U0 = 1.00;

k0 = [2 3];
LB = [-Inf -Inf];
UB = [Inf Inf];
options = optimset();

k_final=lsqnonlin(@fitcrit,k0,LB,UB,options,T,U,U0)

[tsim,usim] = ode45(@simpleode, T, U0, [], k_final);
plot(tsim,usim,'-', T,U,'x')
