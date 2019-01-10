function sum = left_point(func, x0, x1, N)

x = linspace(x0, x1, N+1);
dx = (x1-x0)/N;
sum = 0;

for i = 1:N
    y = func(x(i));
    sum = sum + dx * y;
end

end
