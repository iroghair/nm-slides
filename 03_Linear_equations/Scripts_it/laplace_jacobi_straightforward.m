% Set grid resolution
nx = 40;
ny = 40;

% Set old solution array
T = zeros(nx,ny);

% Set boundary conditions
T(1,:) = 40; % Left
T(nx,:) = 60; % Right
T(:,1) = 20; % Bottom
T(:,ny) = 30;
T(20:25,20:25) = 100;

% Set new solution array (including boundary conditions)
Tnew = T;

Tfix=zeros(nx,ny);
Tfix(20:25,20:25) = 1;

% Required for plotting
[x y] = meshgrid(1:nx, 1:ny);

for iter = 1:1000
    for i = 2:nx-1
        for j = 2:ny-1
            if (Tfix(i,j) ~= 1)
                Tnew(i,j) = (T(i-1,j)+T(i+1,j)+T(i,j-1)+T(i,j+1))/4.0;
            end
        end
    end
    surf(x,y,T);
    title(['Iteration: ' num2str(iter)]);
    drawnow
    T = Tnew;
end
