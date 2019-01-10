clear
load sim_exp_dataset.mat

c_sim_int = interp1(t_sim, c_sim, t_exp, 'linear');
c_err = abs(c_exp - c_sim_int);

subplot(2,1,1);
plot(t_exp, c_exp, '-o', t_sim, c_sim, '-o');
subplot(2,1,2);
stem(t_exp,c_err)