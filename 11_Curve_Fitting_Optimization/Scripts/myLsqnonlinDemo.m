% Quick demonstration of the lsqnonlin function, using an ODE as the model
% that is fitted to the data
function myLsqnonlinDemo
clear; clc;

% Load the dataset and assign to variables
data = load('tudataset1.mat');
U = data.U;
T = data.T;

% initial value
U0 = 1.00;

% initial guesses for model parameters
k0 = [1.00 1.00];

% lower and upper bounds for model parameters
LB = [0.00 0.00];
UB = [Inf Inf ];

% Perform nonlinear least squares fit
options = optimset('TolX',1.0E-6,'MaxFunEvals',1000);

[ke,RESNORM,RESIDUAL,EXITFLAG,OUTPUT,LAMBDA,JACOBIAN] = ...
lsqnonlin(@fitcrit,k0,LB,UB,options,T,U,U0);

% Print results to screen
fprintf('Found coefficients: k1 = %f and k2 = %f \n', ke(1), ke(2));

[tf,uef] = ode45(@simpleode,T,U0,[],ke);
plot(tf,uef,'-',T,U,'x');
legend('Model','Data','Location','southeast');
xlabel('t [s]');
ylabel('u [a.u.]');
title('');
matlab2tikz('filename','../tikzplots/lsqnonlinfit.tikz','width','0.8\textwidth');

    % Some nested functions
    function dudt = simpleode(t,u,k);
    dudt = -k(1)*u + k(2);
    end

    function error = fitcrit(ke,T,U,U0)
    [t,ue] = ode45(@simpleode,T,U0,[],ke);
    error = (ue-U);
    end

end
