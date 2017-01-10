function [p] = newton1D(func, grad, x, tol_x, tol_f)
  ITMAX = 100;
  error = 2*tol_f;
  it = 0;
  f = func(x);  
  while (((error>tol_f) || (dx>tol_x)) && (it<ITMAX))
    it = it + 1;
    g = grad(x);
    dx = -f/g;
    x = x + dx;
    f = func(x);
    error = abs(f);
  end;  
  if it<=ITMAX 
    disp(sprintf('Root found in %d iterations at x = %e\n (function value = %e)', [it,x,f])); 
  else
    disp(sprintf('No root found after %d iterations!', [it]));   
  end;
end