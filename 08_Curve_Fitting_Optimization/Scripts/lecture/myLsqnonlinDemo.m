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

% Perform fitting
[ke,RESNORM,RESIDUAL,EXITFLAG,OUTPUT,LAMBDA,JACOBIAN] = ...
lsqnonlin(@fitcrit,k0,LB,UB,options,T,U,U0);

% Get confidence intervals
cflim = nlparci(ke, RESIDUAL, JACOBIAN);

% Print results to screen
clc
disp('model parameters and confidence limits');
myTable = table;
myTable.ke = ke';
myTable.LowerCI = cflim(:,1);
myTable.UpperCI = cflim(:,2)

% Compute results with fitted value and plot
[T_final,U_final] = ode45(@simpleode,T,U0,[],ke);
plot(T_final,U_final,T,U,'o');
xlabel('Time [s]'); ylabel('U [-]');


    % Some nested functions
    function dudt = simpleode(t,u,k);
    dudt = -k(1)*u + k(2);
    end

    function error = fitcrit(ke,T,U,U0)
    [t,ue] = ode45(@simpleode,T,U0,[],ke);
    error = (ue-U);
    end

end
