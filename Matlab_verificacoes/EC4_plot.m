%% -------------------------------
%  1. Defina os limites das variáveis
% Evite zero para não dar divisão por zero
x1 = linspace(0.1, 2, 200);
x2 = linspace(0.1, 2, 200);

% Cria malha 2D
[X1, X2] = meshgrid(x1, x2);

%% -------------------------------
% 2. Parâmetros do problema
Py = 25;           % Exemplo
Px = 10;            % Exemplo
E = 30e6;
L  = 50;              % Comprimento
rho = 0.3;
sig0 = 3e4;
alfa_buckling = ((pi^2)*E)/(48*L^2); % Fator buckling

%% -------------------------------
% 3. Calcule a inequação
C1 = X1 - 2*X2;
C2 = Py ./ (X1 .* X2) + (6 * Px * L) ./ (X1 .* X2.^2) - sig0;
C3 = Py ./ (X1 .* X2) + (6 * Px * L) ./ (X1 .* X2.^2) - alfa_buckling .* X2.^2;
C4 = 0.5 - X1;
Z = rho*L.*(X1).*(X2);

%% -------------------------------
% 4. Plote as curvas de nível
figure; hold on; grid on; box on;

% % Contornos C1=0
%  contour(X1, X2, C1, [0 0], 'r', 'LineWidth', 2);
% % Contornos C2=0
%  contour(X1, X2, C2, [0 0], 'b', 'LineWidth', 2);
% % % Contornos C3=0
  contour(X1, X2, C3, [0 0], 'g', 'LineWidth', 2);
% % % Contornos C4=0
%  contour(X1, X2, C4, [0 0], 'k', 'LineWidth', 2);

%% -------------------------------
% 5. Regiões viáveis
% (Opcional: com transparência)
% % Região viável de C1
%  contourf(X1, X2, C1 <= 0, [1 1], 'FaceColor','r', 'FaceAlpha',0.1, 'LineStyle','none');
% % Região viável de C2
%  contourf(X1, X2, C2 <= 0, [1 1], 'FaceColor','b', 'FaceAlpha',0.1, 'LineStyle','none');
% % % Região viável de C3
  contourf(X1, X2, C3 <= 0, [1 1], 'FaceColor','g', 'FaceAlpha',0.1, 'LineStyle','none');
% % % Região viável de C4
%  contourf(X1, X2, C4 <= 0, [1 1], 'FaceColor','k', 'FaceAlpha',0.1, 'LineStyle','none');
% % 
% % Máscara da região viável TOTAL
%  AllFeasible = (C1 <= 0) & (C2 <= 0) & (C3 <= 0) & (C4 <= 0);
% % % Pinte a região viável final em verde escuro, mais opaca
%  contourf(X1, X2, AllFeasible, [1 1], 'FaceColor', [0 0 0.6], 'FaceAlpha', 0.4, 'LineStyle', 'none');
% 
% % Funcao objetivo
[CF, hF] = contour(X1, X2, Z, 30, 'LineStyle', '--', 'LineColor', [0.2 0.2 0.2]);
% Adiciona os rótulos
clabel(CF, hF, 'FontSize', 8, 'Color', 'k', 'FontWeight','bold');
% 
% % Ponto otimo
% x1_opt = 0.500000283564746;
% x2_opt = 1.252001422330915;
% plot(x1_opt, x2_opt, 'kp', 'MarkerSize', 12, ...
%     'MarkerFaceColor', 'y', 'DisplayName', 'Ótimo');
% 
% x1_rao = 0.738;
% x2_rao = 0.369;
% plot(x1_rao, x2_rao, 'ko', 'MarkerSize', 12, ...
%     'MarkerFaceColor', 'r');

%% -------------------------------
% 6. Ajustes do gráfico
xlabel('x_1');
ylabel('x_2');
% title('Curvas de nível das 4 restrições e regiões viáveis');
% legend({
%     'C1=0','C2=0','C3=0','C4=0',...
%     'Região Viável Total'
% }, 'Location','northeastoutside');

xlim([min(x1) max(x1)]);
ylim([min(x2) max(x2)]);

hold off;
