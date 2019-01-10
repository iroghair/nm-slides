function [f] = myfunc(x)

% f = 1./(x.^2 + 25*x + 5);
% f = exp(-x);

% f = x.^3 - 2*x.^2 + 2*x + 1;

f = x.^2 - 4*x + 6 + sin(5*x);

end