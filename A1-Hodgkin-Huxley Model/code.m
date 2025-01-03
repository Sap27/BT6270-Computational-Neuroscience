
%ihist=(1:800)*(0.001);
ihist1=[(1:2)*(0.01) (20:22)*(0.001) (221:229)*(0.0001) (23:61)*(0.001) (611:629)*(0.0001) (63:464)*0.001 (4641:4950)*(0.0001) (496:600)*(0.001) ];
disp(size(ihist1))

%spikes=ones(1,800);
spikes1=zeros(1,889);
gkmax=.36;
vk=-77; 
gnamax=1.20;
vna=50; 
gl=0.003;
vl=-54.387; 
cm=.01; 

dt=0.01;
niter=100000;

for i=(1:889)
    ImpCur=ihist1(i);
    t=(1:niter)*dt;
    iapp=ImpCur*ones(1,niter);
    v=-64.9964;
    m=0.0530;
    h=0.5960;
    n=0.3177;

    gnahist=zeros(1,niter);
    gkhist=zeros(1,niter);
    vhist=zeros(1,niter);
    mhist=zeros(1,niter);
    hhist=zeros(1,niter);
    nhist=zeros(1,niter);
    for iter=1:niter
        gna=gnamax*m^3*h; 
        gk=gkmax*n^4; 
        gtot=gna+gk+gl;
        vinf = ((gna*vna+gk*vk+gl*vl)+ iapp(iter))/gtot;
        tauv = cm/gtot;
        v=vinf+(v-vinf)*exp(-dt/tauv);
        alpham = 0.1*(v+40)/(1-exp(-(v+40)/10));
        betam = 4*exp(-0.0556*(v+65));
        alphan = 0.01*(v+55)/(1-exp(-(v+55)/10));
        betan = 0.125*exp(-(v+65)/80);
        alphah = 0.07*exp(-0.05*(v+65));
        betah = 1/(1+exp(-0.1*(v+35)));
        taum = 1/(alpham+betam);
        tauh = 1/(alphah+betah);
        taun = 1/(alphan+betan);
        minf = alpham*taum;
        hinf = alphah*tauh;
        ninf = alphan*taun;
        m=minf+(m-minf)*exp(-dt/taum);
        h=hinf+(h-hinf)*exp(-dt/tauh);
        n=ninf+(n-ninf)*exp(-dt/taun);
        vhist(iter)=v; mhist(iter)=m; hhist(iter)=h; nhist(iter)=n;
    end
    spikes1(i)=nnz(findpeaks(vhist)>9);
end
plot(ihist1,spikes1)
xlabel('Impulse Current in microampere')
ylabel('Firing Frequency/sec')
title('Impulse Current vs Firing Rate')