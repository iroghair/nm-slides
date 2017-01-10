%% Set up parameters
t_end = 2;  % End time
h = 0.1;    % Time step
k = 1;      % Reaction rate constant
c0 = 10;    % Initial concentration

%% Initialization
tspan = 0:h:t_end;  % The time vector
c = c0;              % Store initial concentration in output

%% First-order Euler Time loop
for t = 2:length(tspan)
    f    = -k*c(t-1);           % dc/dt
    c(t) = c(t-1) + h*f;        % Euler time step
end

%% Output: numerical and analytical solutions
tspan_ana = 0:h/100:t_end;
plot(tspan,c,'-*',tspan_ana,c0*exp(-k*tspan_ana));
legend('First-order Euler','Analytical')