load('interpolation-dataset');
x_cont = linspace(-1,1,1001);
p4 = polyfit(x3a,y3a,4);
p10 = polyfit(x3b,y3b,10);
y_cont4 = polyval(p4,x_cont);
y_cont10 = polyval(p10,x_cont);
ezplot('1./(x.^2+(1/25))',[-1 1]); hold on;
plot(x3a,y3a,'o',x3b,y3b,'x',x_cont,y_cont4,x_cont,y_cont10)