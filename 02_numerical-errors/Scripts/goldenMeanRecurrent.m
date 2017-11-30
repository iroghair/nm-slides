function [y] = goldenMeanRecurrent(Ntot)

y(1) = 1;
y(2) = 2 / (1+sqrt(5));

for n = 2:Ntot
    y(n+1) = y(n-1) - y(n);
end

end
