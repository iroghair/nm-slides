close all
clear
n = 1;
mySum = 1/(pi^2 * n^2);
Nmax = 90

for n = 2:Nmax
    term = 1/(pi^2 * n^2);
    mySum(n) = mySum(n-1) + term;
end

mySum(end)

subplot(2,1,1); plot(1:Nmax, mySum)
subplot(2,1,2); semilogy(1:Nmax, mySum - (1/6))
