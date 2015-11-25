% Linear interpolation
c_sim_new = interp1(t_sim,c_sim,t_exp,'linear');
diff = abs(c_exp-c_sim_new);
% Plot the solution
subplot(2,1,1); 
plot(t_exp,c_exp,'b-x',t_exp,c_sim_new,'r-o');
subplot(2,1,2);
stem(t_exp,diff);
% Compute the L2-norm
norm(diff)