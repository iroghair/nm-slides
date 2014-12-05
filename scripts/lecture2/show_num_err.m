a = 0.1;
a_all = [];

for i = 1:30
    a_all = [a_all a];
    a = a * 10 - 0.9
end

semilogy(abs(a_all))