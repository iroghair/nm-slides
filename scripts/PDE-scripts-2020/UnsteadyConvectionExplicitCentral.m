Nx = 1000;
Nt = 10000;
u = 0.0001;
cin = 1;
tend = 100;
length = 0.1;

dt = tend/Nt;
dx = length/Nx;

Co = u*dt/dx;

x = linspace(0, length, Nx+1);

c = zeros(Nt+1,Nx+1);
c(:,1) = cin;

for n=1:Nt
    for i=2:Nx
        c(n+1,i) = c(n,i) - Co*(c(n,i+1) - c(n,i-1))/2;
    end
    c(n+1,Nx+1) = c(n+1,Nx);
end

out = [10 20 30 60 100];
outdt = fix(out/dt);
plot(x,c(outdt,:))