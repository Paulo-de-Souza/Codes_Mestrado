% Investigacao do EC4 via fmincon <- usado na literatura
% Literatura: RAO ed 4 - Q1.19

Py = 25;
Px = 10;
rho = 0.3;
E = 30e6;
sig0 = 3e4;
L = 50;
alfa_buckling = ((pi^2)*E)/(48*L^2);

% x1 = b; x2 = d
lb = [0.5 0.25];
ub = [4 2];

x0 = [1 0.5];
f0 = obj(x0);

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

f_rao = obj([0.738,0.369])
gv_rao = gcons([0.738,0.369])

function f = obj(x)
rho = 0.3;
L = 50;
f = rho*L*x(1)*x(2);
end

function [c,ceq] = cons(x)
Py = 25;
Px = 10;
E = 30e6;
sig0 = 3e4;
L = 50;
alfa_buckling = ((pi^2)*E)/(48*L^2);

c(1) = x(1) - 2*x(2);
c(2) = Py/(x(1)*x(2)) + (6*Px*L)/(x(1)*x(2)^2) - sig0; 
c(3) = Py/(x(1)*x(2)) + (6*Px*L)/(x(1)*x(2)^2) - alfa_buckling*x(2)^2;
ceq = 0;
end

% para avaliar as restricoes
function g = gcons(x)
Py = 25;
Px = 10;
E = 30e6;
sig0 = 3e4;
L = 50;
alfa_buckling = ((pi^2)*E)/(48*L^2);

g(1) = x(1) - 2*x(2);
g(2) = Py/(x(1)*x(2)) + (6*Px*L)/(x(1)*x(2)^2) - sig0; 
g(3) = Py/(x(1)*x(2)) + (6*Px*L)/(x(1)*x(2)^2) - alfa_buckling*x(2)^2;
end