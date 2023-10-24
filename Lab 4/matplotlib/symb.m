% \section{}
% % Calculate the total uncertainty in the theoretical strain when the 1 kg weight was 
% % applied to the beam. The uncertainty in the weight is 5 g and the uncertainty in the 
% % modulus of elasticity is 1 GPa.

% First propogate the uncertainty in the moment, $M$:
% \begin{align*}
%     M &= mgL \\
%     \implies \delta M &= \sqrt{\left(\frac{\partial M}{\partial m} \delta m\right)^2 +
%     \left(\frac{\partial M}{\partial L} \delta L\right)^2} \\
%     &= \sqrt{(gL)^2 \delta m^2 + (mg)^2 \delta L^2} \\
%     &= \sqrt{(9.81 \times 0.2027)^2 (0.005)^2 + (1 \times 9.81)^2 (0.001)^2} \\
%     &= \boxed{\pm\qty{0.01}{Nm}}
% \end{align*}


% The relevant equations are:
% \begin{align*}
%     M &= mgL \\
%     \sigma &= \frac{Mh}{2I} \\
%     I &= \frac{bh^3}{12} \\
%     \epsilon &= \frac{\sigma}{E}
% \end{align*}

% Combining these equations, we get:
% \begin{align*}
%     \epsilon &= \frac{6mgL}{b h^2 E} \\
% \end{align*}

% Computing the partials,
% \begin{align*}
%     \frac{\partial \epsilon}{\partial m} &= \frac{6gL}{b h^2 E} \\
%     \frac{\partial \epsilon}{\partial L} &= \frac{6mg}{b h^2 E} \\
%     \frac{\partial \epsilon}{\partial b} &= -\frac{6mgL}{b^2 h^2 E} \\
%     \frac{\partial \epsilon}{\partial h} &= -\frac{12mgL}{b h^3 E} \\
%     \frac{\partial \epsilon}{\partial E} &= -\frac{6mgL}{b h^2 E^2} \\
% \end{align*}

% Evaluating the partials times the uncertainty in each variable,
% \begin{align*}
%     \frac{\partial \epsilon}{\partial m} \delta m &= 

clc; clear; close all;
syms m g L b h E  

epsilon = 6*m*g*L/(b*h^2*E)
 
delEdelm = diff(epsilon, m)
delEdelL = diff(epsilon, L)
delEdelb = diff(epsilon, b)
delEdelh = diff(epsilon, h)
delEdelE = diff(epsilon, E)

delEdelm_delta_m = double(subs(delEdelm, [m g L b h E], [1 9.81 0.2027 0.012811 0.0127256 68.9*10^9]) * 0.005)
delEdelL_delta_L = double(subs(delEdelL, [m g L b h E], [1 9.81 0.2027 0.012811 0.0127256 68.9*10^9]) * 1.11654678249935/1000)
delEdelb_delta_b = double(subs(delEdelb, [m g L b h E], [1 9.81 0.2027 0.012811 0.0127256 68.9*10^9]) * 0.00325628602303491/1000)
delEdelh_delta_h = double(subs(delEdelh, [m g L b h E], [1 9.81 0.2027 0.012811 0.0127256 68.9*10^9]) * 0.00378200336150775/1000)
delEdelE_delta_E = double(subs(delEdelE, [m g L b h E], [1 9.81 0.2027 0.012811 0.0127256 68.9*10^9]) * 1*10^9)

delE_delta_E = sqrt(delEdelm_delta_m^2 + delEdelL_delta_L^2 + delEdelb_delta_b^2 + delEdelh_delta_h^2 + delEdelE_delta_E^2)

% delEdelL_delta_L = subs(delEdelL, [m g L b h E], [1 9.81 0.2027 0.012811 0.0127256 68.9]) * 1.11654678249935
% delEdelb_delta_b = subs(delEdelb, [m g L b h E], [1 9.81 0.2027 0.012811 0.0127256 68.9]) * 0.00325628602303491
% delEdelh_delta_h = subs(delEdelh, [m g L b h E], [1 9.81 0.2027 0.012811 0.0127256 68.9]) * 0.00378200336150775
% delEdelE_delta_E = subs(delEdelE, [m g L b h E], [1 9.81 0.2027 0.012811 0.0127256 68.9]) * 1*10^9


