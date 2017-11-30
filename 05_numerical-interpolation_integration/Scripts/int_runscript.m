Nrange = [10 20 40 80 160 320 640 1280];

I_exact = 1.029166666666667e+02;
c = 1;

for N = Nrange
    IL(c) = leftEndpoint(@myfunction, 0, 5, N);
    IR(c) = rightEndpoint(@myfunction, 0, 5, N);
    IM(c) = midpoint(@myfunction, 0, 5, N);
    IT(c) = trapezoidrule(@myfunction, 0, 5, N);

    c = c + 1;
end

IL = abs(IL - I_exact);
IR = abs(IR - I_exact);
IM = abs(IM - I_exact);
IT = abs(IT - I_exact);

loglog(Nrange, IL, Nrange, IR, Nrange, IM, Nrange, IT);
xlabel('N'); ylabel('Error');