% Investigacao do EC1 via fmincon <- usado na literatura
% Literatura: RAO ed 4 - Q1.32

lb = [0.04 0.06];
ub = [0.12 0.20];

x0 = [0.05 0.15];
f0 = obj(x0);
g0 = gcons(x0);

[xv,fval] = fmincon(@obj,x0,[],[],[],[],lb,ub,@cons);
gv = gcons(xv);

format long
clc
fprintf('Ponto Otimo')
xv
fprintf('\nFobj:')
disp(fval)
fprintf('\nRestricoes')
gv

function f = obj(x)
f = 76500*x(1)*x(2);
end

function [c,ceq] = cons(x)
%c(1) = 0.9/(x(1)*x(2)^2) - 220;     %equacao correta 
c(1) = 0.00403409/(x(1)*x(2)^2) - 1; %equacao do solucionario
c(2) = 875.604*1e-9 / (x(1)*x(2)^3) - 0.02;
c(3) = x(1) - x(2);
ceq = 0;
end

% para avaliar as restricoes
function g = gcons(x)
g(1) = 0.9/(x(1)*x(2)^2) - 220;    %equacao correta 
g(2) = 875.604*1e-9 / (x(1)*x(2)^3) - 0.02;
g(3) = x(1) - x(2);
end