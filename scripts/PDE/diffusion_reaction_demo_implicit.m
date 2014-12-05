tic
Nx = 100;           % Nc grid points
Nt = 1600;          % Nt time steps
D = 1e-8;           % m/s
kR = 0.01;           % s-1
c_L = 1.0;          % mol/m3
c_R = 1.0;          % mol/m3
t_end = 5000.0;     % s
x_end = 5e-3;       % m

% Time step and grid size
dt = t_end/Nt; 
dx = x_end/Nx;

% Fourier number
Fo=D*dt/dx/dx

% Grid node and time step positions
x = linspace(0,x_end,Nx+1);

% Bands in matrix (internal cells)
A = sparse(Nx+1,Nx+1);
for i=2:Nx
    A(i,i-1) = -Fo;
    A(i,i ) = (1+2*Fo+kR*dt);
    A(i,i+1) = -Fo;
end

% Set boundary cells, independent on neighbors:
A(1 ,1 ) = 1;       % Left
A(Nx+1,Nx+1) = 1;   % Right

% Initial matrices for solutions (Nx times Nt)
c = zeros(Nt+1,Nx+1);  % All concentrations are zero
c(:,1)    = c_L;       % Concentration at left side (all time steps)
c(:,Nx+1) = c_R;       % Concentration at left side (all time steps)

for n = 1:Nt-1 % time loop 
    b = c(n,:)';   % Set right hand side
    solX = A\b;                 % Solve linear system
    c(n+1,:) = solX;            % Store solution each time step
end
toc

plotconc = c(fix(linspace(1,Nt,25)),:);
plot(x,plotconc)
p = [x; plotconc]';
save diff_implicit.dat p -ascii
