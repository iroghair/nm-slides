function sum = trapezoid(func, x0, x1, N)

x = linspace(x0, x1, N+1);
dx = (x1-x0)/N;
sum = 0;

for i = 1:N
    y = (func(x(i)) + func(x(i+1)) ) / 2;
    sum = sum + dx * y;
end

end
