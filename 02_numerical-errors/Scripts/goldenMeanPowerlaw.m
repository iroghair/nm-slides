function [y] = goldenMeanPowerlaw(Ntot)

x = (1 + sqrt(5))/2;

for n = 0:Ntot
    y(n+1) = x^-n;
end

