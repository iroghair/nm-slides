% Computes the Golden Mean relationship via recurrent and powerlaw
% approaches. First, both methods are initialized, then computation takes
% place. Finally, results are compared in a parity plot.

% Method 1, init array
m1(1) = 1;
m1(2) = 2/(1+sqrt(5));

% Method 2, init array
m2 = m1

for i = 3:50
    m1(i) = m1(i-2) - m1(i-1);
    m2(i) = ((1+sqrt(5))/2)^(-(i-1));
end

% Parity plot
loglog(m1,m2,'+-r',[1e-12 1], [1e-12 1], '-k')



