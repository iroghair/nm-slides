function [sum] = leftEndpoint(func, x0, x1, N)

dx = (x1-x0)/N;
x = linspace(x0, x1, N+1);
sum = 0;

for i = 1:N
    y = func(x(i));
    sum = sum + dx*y;
end


end