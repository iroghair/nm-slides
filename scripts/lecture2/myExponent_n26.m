function ex = myExponent_n26(x)
% x:    value to calculate the exponent of

n = 1;              % The counter, increased by 1 each loop
term = 1;           % The term that is added
ex = 0;

% Loop until the new term is small enough
while (n <= 26)
    term = str2double(sprintf('%.4g', term));
    ex = ex + term;
    term = (x^n)/factorial(n);
    n = n + 1;
end

end