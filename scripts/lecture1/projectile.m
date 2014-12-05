function [pos,tim] = projectile(v0,M)

% Initialise parameters
t_end = 2;                  % End time
deltat = 0.1;              % Time step
x0 = 1;                     % Initial position

nsteps = fix(t_end/deltat); % Number of time steps
pos = zeros(nsteps,1);      % Position vector
vel = zeros(nsteps,1);      % Velocity vector
tim = zeros(nsteps,1);      % Time vector

% Default values for mass and velocity
if (nargin < 2)
    M = 10;
    if (nargin < 1)
        v0 = 1;
    end
end

pos(1) = x0;                % Store initial position
vel(1) = v0;                % Store initial velocity

% The time loop
for n = 1:nsteps-1
    pos(n+1) = position(pos(n),vel(n),deltat);
    vel(n+1) = velocity(vel(n),M,deltat);
    tim(n+1) = tim(n) + deltat;
end

% Plot results
figure; plot(tim,pos, 'o');

% Compare to analytical solution
compareToExact(x0,v0,tim,pos);

end

function F = force(M)
% M:    mass of particle
g = -9.81;
F = M * g;
end

function v = velocity(vt,mass,dt)
% vt:   velocity at previous time
% mass: mass of particle
% dt:   time step size
v = vt + force(mass)/mass * dt;
end

function x = position(xt,vel,dt)
% xt:   position at current time step
% vel:  velocity at current time step
% dt:   time step size
x = xt + vel * dt;
end

function compareToExact(x0,v0,tim,pos)
% Exact solution
pos_ex = x0 + v0 * tim + ( 0.5 * -9.81 * tim .* tim );

% Draw comparative figure
figure;
subplot(2,1,1)
plot(tim,pos, 'o');
hold on;
plot(tim,pos_ex,'r-')
subplot(2,1,2)
stem(tim,pos_ex-pos,'r-')
end
