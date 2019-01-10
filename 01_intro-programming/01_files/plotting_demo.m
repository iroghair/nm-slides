x = -5:0.1:5
y = x.^2 -4*x + 3;
y2 = y + (2-4*(rand(size(y))));

subplot(2,1,1)
plot(x,y,x,y2,'.');

subplot(2,1,2)
plot(x,y-y2,'r-');
