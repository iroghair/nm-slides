function [p] = newton(func, jac, x, tol_x, tol_f)
  ITMAX = 100;
  error = 2*tol_f;
  it = 0;
  f = feval(func,x);  
  while (((error>tol_f) || (max(abs(dx))>tol_x)) && (it<ITMAX))
    it = it + 1;
    j = feval(jac,x);
    dx = j\(-f);
    x = x + dx;
    f = func(x);
    error = max(abs(f));
    disp(sprintf('iteration %d: x[1] = %e, x[2] = %e with f[1] = %e, f[2] = %e', [it,x(1),x(2),f(1),f(2)]));     
  end;  
  if it<=ITMAX 
    disp(sprintf('\nRoot found in %d iterations at x[1] = %e, x[2] = %e with f[1] = %e; f[2] = %e\n', [it,x(1),x(2),f(1),f(2)])); 
  else
    disp(sprintf('\nNo root found after %d iterations!\n', [it]));   
  end;
end