load tudataset1;
% initial value
U0 = 1.00;
% initial guesses for model parameters
k0 = [1.00 1.00];
% lower and upper bounds for model parameters
LB = [0.00 0.00];
UB = [ Inf Inf ];
% Perform nonlinear least squares fit
options = optimset ('TolX' ,1.0E-6, 'MaxFunEvals' ,1000);
[ ke , RESNORM , RESIDUAL , EXITFLAG , OUTPUT , LAMBDA , JACOBIAN ] ...
    = lsqnonlin ( @fitcrit , k0 , LB , UB , options ,T ,U , U0 ) ;

ke
