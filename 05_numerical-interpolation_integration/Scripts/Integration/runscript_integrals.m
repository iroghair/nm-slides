% Set up parameters
x0 = 0;
x1 = 3;
Nrange = [5 10 20 40 80 160 320 640 1280];

% Exact solution
I = integral(@myfunc, x0, x1);

counter = 1;
for N = Nrange
    % Compute integral: right end point method
    IR(counter) = rightrule(@myfunc, x0, x1, N);

    % Compute integral: left end point method
    IL(counter) = leftrule(@myfunc, x0, x1, N);

    % Compute integral: mid point method
    IM(counter) = midrule(@myfunc, x0, x1, N);

    % Compute integral: trapezoid method
    IT(counter) = traprule(@myfunc, x0, x1, N);

    counter = counter + 1;
end

errR = abs(IR-I);
errL = abs(IL-I);
errM = abs(IM-I);
errT = abs(IT-I);
loglog(Nrange, errR, Nrange, errL, Nrange, errM, Nrange, errT)