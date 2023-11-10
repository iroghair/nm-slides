function [err] = fitcrit_laplace(actuate_T, Nx, Ny, boundary_T, setpoint_T)
% Compute model:
T = solveLaplaceEq(Nx, Ny, boundary_T, actuate_T);

% Compute error (deviation of mean T with desired setpoint T)
err = mean(T,'all') - setpoint_T;

end