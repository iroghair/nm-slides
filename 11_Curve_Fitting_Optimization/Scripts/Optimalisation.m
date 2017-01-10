% Creates all figures for the LaTeX document for optimalisation
%% Pre-work
close all;
clear;
limits = [0 20,0,20];
C = get(groot,'DefaultAxesColorOrder');

%% Initial optimalisation problem
% Plot the constraints
figure; 
e1 = ezplot('5*x_1 + 2*x_2 = 60',limits);
hold on;
e2 = ezplot('2*x_1 + 8*x_2 = 60',limits);
x = [0 10 12 0];
y = [7.5 5 0 0];
f1 = fill(x,y,'r');

f1.FaceColor = C(5,:)
% f1.FaceAlpha = 0.8;
% f1.EdgeAlpha = 0;
e1.LineColor = C(1,:);
e2.LineColor = C(2,:);

legend('5x_1 + 2x_2 = 60', '2x_1 + 8x_2 = 60', 'Feasible solutions');
xlabel('x_1');
ylabel('x_2');
title('');
matlab2tikz('filename','../tikzplots/optim1.tikz','width','0.8\textwidth');


%% Helper lines in plot
z1 = 0;
e3 = ezplot('40*x_1 + 88*x_2=200', limits);
e3.LineStyle = '--';
e3.LineColor = 'k';

e3 = ezplot('40*x_1 + 88*x_2=500', limits);
e3.LineStyle = '--';
e3.LineColor = 'k';

e3 = ezplot('40*x_1 + 88*x_2=840', limits);
e3.LineStyle = '--';
e3.LineColor = 'k';

text(2,2,'z=200');
text(5,4,'z=500');
text(10,6,'z=840');
legend off
title('');

matlab2tikz('filename','../tikzplots/optim2.tikz','width','0.8\textwidth');
