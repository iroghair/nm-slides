Nx = 100;          % Nc grid points
Nt = 1000;         % Nt time steps
u = 0.0008;          % m/s
c_in = 1.0;         % mol/m3
t_end = 100.0;      % s
x_end = 0.1;        % m

% Time step and grid size
dt = t_end/Nt; dx = x_end/Nx;

% Courant number
Co=u*dt/dx

% Initial matrices for solutions (Nx times Nt)
c1 = zeros(Nt+1,Nx+1);  % All concentrations are zero
c1(:,1) = c_in;     % Concentration at inlet (all time steps)
an = c1; c2 = c1;   % Analytical and upwind solution

% Grid node and time step positions
x = linspace(0,x_end,Nx+1);
t = linspace(0,t_end,Nt+1);

for n = 1:Nt % time loop
    for i = 2:Nx % Nested loop for grid nodes
        % Central difference
        c1(n+1,i) = c1(n,i) - u*((c1(n,i+1) - c1(n,i-1))/(2*dx))*dt;
        % Upwind
        c2(n+1,i) = c2(n,i) - u*((c2(n,i) - c2(n,i-1))/(dx))*dt;
        % Analytical
        an(n+1,i) = (x(i) < u*t(n+1))*c_in;
    end
end

% Plot at a number of different time steps
outtimes = fix(linspace(1,Nt,min(Nt,25)));

plot(x,c2(outtimes,:))

% Store certain time steps
cendiff = [x; c1([1 1000 2000 4000 6000 8000],:)]';
upwind  = [x; c2([1 1000 2000 4000 6000 8000],:)]';
exact   = [x; an([1 1000 2000 4000 6000 8000],:)]';
save conv_cendiff.dat cendiff -ascii;
save conv_upwind.dat upwind -ascii;
save conv_ex.dat exact -ascii;