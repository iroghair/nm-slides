%% Generate linear space of control points
N = 100;                % Number of data points
x = linspace(0,1,N);    % Points (independent variable)
A = [1 1/3 1.5 3.5];    % Coefficients of polynomial

%% Generate 'measurement values' with errors following a normal distribution
% Initialize randomizer
pd = makedist('normal',0,0.5);
% Add scatter data to the polynomial
y = A(4)*x.^3 + A(3)*x.^2 + A(2).*x + A(1) + random(pd,1,N);

%% Plot the generated data
plot(x,y,'x');

%% Fit using backslash division
% Generate coefficient matrix 
X(:,1) = ones(N,1) ;
X(:,2) = x;
X(:,3) = x.^2;
X(:,4) = x.^3;
% Solve and print coefficients
A=X\y'
