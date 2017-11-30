function [result] = myExponential1(x)

result = 1;
for n = 1:2000
    term = x^n/factorial(n);
    result = result + term;
    if (term < 1E-6)
        n
        break;
    end
end

