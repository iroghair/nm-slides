function sum = traprule(func, x0, x1, N)

xrange = linspace(x0,x1,N+1);
h = (x1-x0)/N;
sum = 0;

for i = 1:N
    y = (func(xrange(i+1)) + func(xrange(i)))/2
    sum = sum + y * h;
end

end