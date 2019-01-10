Nx = 100; % Number of grid points
Nt = 4000;
D =1e-8;
c_L = 1.0;
c_R = 0;
t_end = 5000.0;
x_end = 5e-3;

dt = t_end/Nt;
dx = x_end/Nx;
Fo = D*dt/dx/dx;

c = zeros(Nt+1,Nx+1);
c(:,1) = c_L;
c(:,Nx+1) = c_R;

% A = sparse(Nx+1,Nx+1);
% for i=2:Nx
%     A(i,i-1) = -Fo;
%     A(i,i) = (1+2*Fo);
%     A(i,i+1) = -Fo;
% end
e = ones(Nx+1,1);
A = spdiags([-e*Fo,e*(1+2*Fo),-e*Fo],[-1,0,1],Nx+1,Nx+1);
A(1,2) = 0;
A(1,1) = 1;
A(Nx+1,Nx) = 0;
A(Nx+1,Nx+1) = 1;

x = linspace(0,x_end,Nx+1);
for n = 1:Nt
  b = c(n,:)';
  c(n+1,:) = A\b;
end

% Plot at a number of different time steps
outtimes = fix(linspace(1,Nt,50));
plot(x,c(outtimes,:))
