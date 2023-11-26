data = xlsread('myDataSet.xls');
x = data(:,1);
y = data(:,2);
N = length(x);
X(:,1) = ones(N,1);
X(:,2) = x;
X(:,3) = x.^2;
X(:,4) = x.^3;
A = X\y
yfit = A(4)*x.^3 + A(3)*x.^2 + A(2).*x + A(1);

figure;
subplot(2,1,1)
p = plot(x,y, 'x');
hold on
plot(x,yfit,'-r')
xlabel('Controlled variable');
ylabel('Measured variable');
subplot(2,1,2)
stem(x,y-yfit)
xlabel('Controlled variable');
ylabel('Absolute error');
title(['Mean residual: ' num2str(mean(y-yfit))]);