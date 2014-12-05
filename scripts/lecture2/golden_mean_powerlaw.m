% initialise
x = (1 + sqrt(5))/2;
y2(1) = x^0; % n = 1

for n = 0:39
    y2(n+1) = x^-n
end
