function [result] = myExponential2(x)

result = 1;
n = 1;
term = x^n/factorial(n);

while (term > 1E-6)
    result = result + term;
    n = n + 1;
    term = x^n/factorial(n);
end
% n
