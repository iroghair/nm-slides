% Creates all figures for the LaTeX document for curve fitting
%% Pre-work
close all;
clear;

%% Measurement data
% Generate linear space of control points
N = 100;
x = linspace(0,1,N);
A = [1 1/3 1.5 3.5];

% Generate 'measurement values' with errors following a normal distribution
pd = makedist('normal',0,0.5);
y = A(4)*x.^3 + A(3)*x.^2 + A(2).*x + A(1) + random(pd,1,N);

% Plot the figure and export to TikZ
figure;
p = plot(x,y, 'x');
p(1).MarkerSize = 4;
xlabel('Controlled variable');
ylabel('Measured variable');
matlab2tikz('filename','../tikzplots/scatter1.tikz','width','0.8\textwidth');

% Wite an Excel data file
xldata=[x;y]';
xlswrite('myDataSet.xls', xldata);
save('myDataSet.txt','xldata','-ascii')

%% Fitting a model
X(:,1) = ones(size(x));
X(:,2) = x;
X(:,3) = x.^2;
X(:,4) = x.^3;
Ahat = X\y';

yhat = Ahat(4)*x.^3 + Ahat(3)*x.^2 + Ahat(2)*x + Ahat(1);

figure;
p = plot(x,y,'x',x,yhat,'-');
p(2).LineWidth = 2;
p(1).MarkerSize = 4;
xlabel('Controlled variable');
ylabel('Measured variable');
matlab2tikz('filename','../tikzplots/scatter-model.tikz','width','0.8\columnwidth');

%% Residuals
d = (y - yhat);
figure;
p = stem(x,d);
hold on;
plot([0 1],[ 0 0], '-k');
xlabel('Controlled variable');
ylabel('Absolute deviation');
title(['Mean residual: ' num2str(mean(d))]);
p(1).MarkerSize = 4;
matlab2tikz('filename','../tikzplots/residuals.tikz','width','0.9\textwidth','height','0.3\textheight');

%% Table
% Gather all required data
names = {'N';'SSE';'SST';'SSR';'R^2'};
SSE = sum(d.^2);
SST = sum(yhat.^2);
SSR = sum(y.^2);
R2 = (1 -SSE/SST);
val  = [N; SSE; SST; SSR; R2];
T = table(val,'RowNames',names)

% Write the table in LaTeX format
file = fopen('../tikzplots/table.tex','w');
fprintf(file,'\\begin{tabular}{lc}\n');
fprintf(file,' & Value \\\\ \n');
fprintf(file,'\\hline');
fprintf(file,'$N$   & %i \\\\ \n', N);
fprintf(file,'SSE   & %1.3f \\\\ \n', SSE);
fprintf(file,'SST   & %1.3f \\\\ \n', SST);
fprintf(file,'SSR   & %1.3f \\\\ \n', SSR);
fprintf(file,'$R^2$ & %1.3f \\\\ \n',R2);
fprintf(file,'\\hline');
fprintf(file,'\\end{tabular}\n');
fclose(file);
