function [err] = fitcrit(k,T,U,U0)
k
[tsim,usim] = ode45(@simpleode, T, U0, [], k);

err = usim - U;
end
