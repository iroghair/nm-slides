function myFittingDemo
data = load('tudataset1.mat');
T = data.T;
U = data.U;

% Initial guesses
k = [1 1];
lb = zeros(size(k));
ub = inf(size(k));

[ke,resnorm,residual,exitflag,output,lambda,jacobian] = ...
    lsqnonlin(@fitcrit, k, lb, ub, [], T, U);
[t_sim,u_sim]  = ode45(@odefun, [0 10], 1, [], ke);

plot(t_sim, u_sim,'r-',T,U,'o');

cflim = nlparci(ke, residual, jacobian);

clc
disp('Fit parameters and confidence bounds')
myTable = table;
myTable.ke = ke';
myTable.lb = cflim(:,1);
myTable.ub = cflim(:,2);

myTable

    function [dudt] = odefun(t,u,k)
        dudt = -k(1) * u + k(2);
    end

    function error = fitcrit(k,T,Ue)
        k
        [t,u]  = ode45(@odefun, T, 1, [], k);
        error = (u-Ue);
    end
end