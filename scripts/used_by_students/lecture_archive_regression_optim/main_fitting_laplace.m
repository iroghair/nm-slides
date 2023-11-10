Nx = 25;
Ny = 35;
Tb = [40 10 40 10];                 % Fixed boundary temperatures
T0 = 0;
T_set = 20;
UB = Inf;
LB = -Inf;

opts = optimoptions('lsqnonlin', 'Display', 'iter');

% T_fit = lsqnonlin(@fitcrit_laplace, T0, LB, UB, opts, Nx, Ny, Tb, T_set)
T_fit = lsqnonlin(@(T) fitcrit_laplace(T,Nx,Ny,Tb,T_set),T0, LB, UB, opts)

T_model = solveLaplaceEq(Nx, Ny, Tb, T_fit);

T_plot = reshape(T_model,[Nx Ny]);       % Reshape x-vec to mat Nx,Ny
[x,y] = meshgrid(1:Ny,1:Nx);             % Get position arrays
surf(x,y,T_plot)                         % Surface plot
mean(T_model)
