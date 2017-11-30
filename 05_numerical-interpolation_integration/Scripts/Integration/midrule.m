function sum = midrule(func, x0, x1, N)

xrange = linspace(x0,x1,N+1);
h = (x1-x0)/N;
sum = 0;

for i = 1:N
    xmid = (xrange(i)+xrange(i+1)) / 2;
    y = func(xmid);
    sum = sum + y * h;
end

end