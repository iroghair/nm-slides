function [p] = broyden(func, x, tol_x, tol_f)
  ITMAX = 100;
  error = 2*tol_f;
  it = 0;
  f = feval(func,x);  
  b = eye(2); % create identity matrix
  while (((error>tol_f) || (max(abs(dx))>tol_x)) && (it<ITMAX))
    it = it + 1;
    dx = b\(-f);
    x = x + dx;
    f0 = f;
    f = func(x);
    df = f - f0;
    b = b + ((df - b*dx)*dx.')/(dx.'*dx); % Broyden's updating
    error = max(abs(f));
    disp(sprintf('iteration %d: x[1] = %e, x[2] = %e with f[1] = %e, f[2] = %e', [it,x(1),x(2),f(1),f(2)]));     
  end;  
  if it<=ITMAX 
    disp(sprintf('\nRoot found in %d iterations at x[1] = %e, x[2] = %e with f[1] = %e; f[2] = %e\n', [it,x(1),x(2),f(1),f(2)])); 
  else
    disp(sprintf('\nNo root found after %d iterations!\n', [it]));   
  end;
end