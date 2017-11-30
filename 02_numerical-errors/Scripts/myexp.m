function [ex, n] = myexp(x)
% x:    value to calculate the exponent of

format long
% Some pre-work
ex = ones(size(x)); % The result, starting at 1

% Loop over all elements of x
term = 1;           % The term that is added
n=1;
% Loop until the new term is small enough
while (abs(term) > 1e-6) % Note: use abs!
    term = (x.^n)./factorial(n);
    term = str2double(sprintf('%1.4g',term));
    ex = ex + term;
    n=n+1;
end
end