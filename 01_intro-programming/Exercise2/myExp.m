function [result] = myExp(x)

result = 1;

for n = 1:500
    term = x^n/factorial(n);
    result = result + term;
    if (term < 1E-12)
        n
        break;
    end
end
