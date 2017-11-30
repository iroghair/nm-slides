tic
Nx = 100;           % Nx grid points
Nt = 40000;         % Nt time steps
D = 1e-8;           % m/s
c_L = 1.0; c_R = 0; % mol/m3
t_end = 5000.0;     % s
x_end = 5e-3;       % m

% Time step and grid size
dt = t_end/Nt; 
dx = x_end/Nx;

% Fourier number
Fo=D*dt/dx/dx

% Initial matrices for solutions (Nx times Nt)
c = zeros(Nt+1,Nx+1);  % All concentrations are zero
c(:,1)  = c_L;     % Concentration at left side
c(:,Nx+1) = c_R;     % Concentration at right side

% Grid node and time step positions
x = linspace(0,x_end,Nx+1);

for n = 1:Nt-1 % time loop
    for i = 2:Nx % Nested loop for grid nodes
        c(n+1,i) = Fo*c(n,i-1) + (1-2*Fo)*c(n,i) + Fo*c(n,i+1);
    end
end

toc

% Plot at a number of different time steps
outtimes = fix(linspace(1,Nt,min(Nt,250)));
plot(x,c(outtimes,:))
