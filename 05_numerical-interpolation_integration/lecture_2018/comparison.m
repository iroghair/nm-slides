clear;
Nx = [10 20 40 80 160 500 1000 2000 5000 1e4 50000 1e5 1e6];

x0 = 0;
x1 = 10;
Iexact = integral(@myfunc, x0, x1);

for i = 1:length(Nx)
    N = Nx(i);
    
    IL(i) = left_point(@myfunc, x0, x1, N);
    IR(i) = right_point(@myfunc, x0, x1, N);
    IM(i) = mid_point(@myfunc, x0, x1, N);
    IT(i) = trapezoid(@myfunc, x0, x1, N);
end

IL = abs(IL - Iexact);
IR = abs(IR - Iexact);
IM = abs(IM - Iexact);
IT = abs(IT - Iexact);

loglog(Nx, IL, Nx, IR, Nx, IM, Nx, IT);
legend('Left','Right','Mid','Trapezoid')

