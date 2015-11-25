% Create x vector
x = -5:0.1:5;
% Compute quadratic function y(x)
y = x.^2-4*x+3;
% Get some random noise around y for demonstration purposes
y2 = y + (2-4*rand(size(y)));

% First subplot
subplot(2,1,1); 
plot(x,y,'-',x,y2,'r.'); % Plot discrete data as markers
xlabel('X'); 
ylabel('Y'); 
title('Graph and scatter data');

% Second subplot
subplot(2,1,2); 
plot(x,abs(y-y2),'r-');
xlabel('X'); 
ylabel('Y'); 
title('Absolute error');
