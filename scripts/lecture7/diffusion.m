function diffusion ()

tspan= [0 100];
% Setting differentiation options
options = odeset('RelTol',1e-4,'AbsTol',[1e-8 1e-8],'Stats','on'); 

%ODE solver
[t,Ye]=ode15s(@Model,q.tspan,q.inits,[],q);

end

function diff_ODE


end