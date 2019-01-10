Nx = 100; % Number of grid points
Nt = 40000;
D =1e-8;
c_L = 1.0;
c_R = 0;
t_end = 250.0;
x_end = 5e-3;

dt = t_end/Nt;
dx = x_end/Nx;
Fo = D*dt/dx/dx;

c = zeros(Nt+1,Nx+1);
c(:,1) = c_L;
c(:,Nx+1) = c_R;

x = linspace(0,x_end,Nx+1);
for n = 1:Nt
    for i = 2:Nx
        c(n+1,i) = Fo*c(n,i-1) + (1-2*Fo)*c(n,i) + Fo*c(n,i+1);
    end
end

% Plot at a number of different time steps
outtimes = fix(linspace(1,Nt,50));
plot(x,c(outtimes,:))
