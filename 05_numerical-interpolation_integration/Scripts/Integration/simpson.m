function [sum] = simpson(func, x0, x1, N)

x = linspace(x0, x1, N+1);
dx = x(2)-x(1);

sum = func(x0) + func(x1);

for i = 2:2:N
    y1 = func( x(i));
    y2 = func( x(i+1));
    sum = sum + 4*y1 + 2*y2;
end
if (i == N)
    sum = sum - 2*y2;
end

sum = sum * dx/3;

end