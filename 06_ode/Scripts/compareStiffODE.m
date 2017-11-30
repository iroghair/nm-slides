subplot(2,1,1)
ode45(@stiff_ode, [0 1], [1 0]);
subplot(2,1,2)
ode15s(@stiff_ode, [0 1], [1 0]);