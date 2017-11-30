% Generate random data set
x=0:25;
y = rand(size(x));
% Interpolant on a fine mesh
xc = linspace(0,25,1001);
yc = interp1(x,y,xc,'spline');
plot(x,y,'o',xc,yc,'-r')