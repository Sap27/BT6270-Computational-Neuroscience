% Initialising the variables and starting condition
dt=0.01;
t=0:0.01:100;
V=zeros(size(t));
W=zeros(size(t));
a=0.5;
b=0.0;
r=0.8;
Im=0.0;
vt=0.0;
wt=0;
% for perturbing P1
V(1)=0.01;
W(1)=0.01;
% % for perturbing p2
V(1)=0.49;
V(1)=0.51;
% % 
% % W(1)=0.01;
% % % For perturbinng p3
V(1)=1.01;
% W(1)=0.01;
% Euler integration carried out to obtain the V and W values at a given
% time instant
for i=1:10000
    V(i+1)=(V(i)*(a-V(i))*(V(i)-1)-W(i)+Im)*dt+V(i);
    W(i+1)=(b*V(i)-r*W(i))*dt+W(i);
end
% Plots for V(t) vs t and W(t) vs t
figure;
plot(t,V);
xlabel('time')
ylabel('V')
plot(t,W);
xlabel('time')
ylabel('W')
% Plotting the Phase plane, trajectory and quiver plot to understand limit
% cycle behavior
v1=-0.5:0.005:1.5;
w1=-0.5:0.005:1.5;
[v,w] = meshgrid(-0.5:0.005:1.5);
dvdt=zeros(size(v1));
dwdt=zeros(size(v1));
disp(size(v1));
for i=1:401
    dvdt(i)=v1(i)*(a-v1(i))*(v1(i)-1)+Im;
    dwdt(i)=b*v1(i)-r*(w1(i));
end

plot(v1,(b/r)*v1,v1,dvdt)
hold on

%plot(V(1:7863),W(1:7863))
plot(V,W,color='black')
hold on
quiver(v,w,v*(a-v)*(v-1)-w+Im,b*v-r*w,'LineWidth',1,'AutoScaleFactor',0.955)
hold off
hold on
%plot(V(7864:10001),W(7864:10001),Color='black')
hold off 
 xlabel('V')
 ylabel('W')
%legend('W nullcline','V nullcline','Trajectory','Quiverplot','Limit Cycle')
legend('W nullcline','V nullcline','Trajectory','Quiverplot')
%legend('W nullcline','V nullcline')
hold off 


