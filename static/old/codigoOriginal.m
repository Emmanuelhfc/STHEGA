%% Projeto do trocador de calor casco e tubo

clc
clear
close all
%% Dados iniciais
Resultados(1,:)={'L','Dic','Npt','Nt','Is','Nº de Chicanas',...
        'At','At2','tip_f','Ft','d',...
        'Re_t','v','hi','h_io','Re_s','ji','hideal','jc','delta_sb',...
        'delta_tb','jl','jb','jr','js','hs','Área de Projeto',...
        'Area necessária','EA','Ud1','Ud pela área','Uc','Ud real',...
        'P.C. tubo','P.C.cruzado','P.C. janelas',...
        'P.C. entrada/saída','P.C. Casco','Outros valores','Diam. Casco',...
        'diâmetro interno tubo','Ii','Io','Diam do Bocal','Isi','Iso'...
        'Ic','Diam do feixe','Área do escomaento','at','Gt','p','pn','pp',...
        'Sm','delta_sb','Ssb','delta_tb','Stb','Nº fileira t cruzados(Nc)',...
        'Nº de pares de tiras selantes','tw'};

%Matriz com dados iniciais do excel
d_ini=num2cell(readmatrix('base_dados.xlsx','Sheet','dados','Range','C5'));
[N,d,L,Ud,T1,T2,wq,t1,t2,wf,~,At,Col,Ft,Npt,tip_f,At2,t_mat]=d_ini{:};

pol=0.0254; % ----> Fator de conversão pol--> m
%L,N,Dic,At,Npt,Ft,d ----> não precisará pegar da tabela
T1=T1+273.15;
T2=T2+273.15;
t1=t1+273.15;
t2=t2+273.15;
Dic_inter =[(L/pol)/5,(L/pol)/10]; % intervalo de valores de Dic [pol]
di = d-2*0.065; % BWG 16---[pol]

if Dic_inter(2)<8.071
    Dic=8.071;
else
    Dic_tab=tab_tubos((tab_tubos(:,1)>=Dic_inter(2) & tab_tubos(:,1)<=...
        Dic_inter(1)),1);
    
    Dic=max(Dic_tab); %adotado por enquanto
end

Dc=Dic+2; % Diâmetro do casco apenas por enquanto  [m]
class_p=150;    % Apenas por enquanto-- classe de pressão [psi]

%constantes
tab_constantes=readmatrix('base_dados.xlsx','Sheet','constantes',...
        'Range','A1');

%% Proprieades Físicas da Tabela

p_quente=num2cell(readmatrix('base_dados.xlsx','Sheet','dados','Range', ...
    'G5:G10').');
%Matriz com propriedades do fluído frio (EXCEL)
p_frio=num2cell(readmatrix('base_dados.xlsx','Sheet','dados','Range', ...
    'G11:G16').');

[cpq,hq,vq,uq,pq,k_q]=p_quente{:};
[cpf,hf,vf,uf,pf,k_f]=p_frio{:};
%% Passo 1: Balanço de energia
filename = 'base_dados.xlsx'; 
% Condições para verificar qual variável está faltando e determina-la
if isnan(T1) || isnan(T2) || isnan(wq)
    q = wf*cpf*(t2-t1);
    if isnan(T1)  %---> isnan = é vazio
        T1=(q/(wq*cpq))+T2;
        %writematrix ---> add um valor no excel, no range especificado
        writematrix(T1,filename,'Sheet','dados','Range','C9');
    elseif isnan(T2)
        T2=(-q/(wq*cpq))+T1;
        writematrix(T2,filename,'Sheet','dados','Range','C10');
    else
        wq=q/(cpq*(T1-T2));
        writematrix(wq,filename','Sheet','dados','Range','C11');
    end
elseif isnan(t1) || isnan(t2) || isnan(wf)
    q = wq*cpq*(T1-T2);
    if isnan(t1)
        t1=(-q/(wf*cpf))+t2;
        writematrix(t1,filename,'Sheet','dados','Range','C12');
    elseif isnan(t2)
        t2=(q/(wq*cpf))+t1;
        writematrix(t2,filename,'Sheet','dados','Range','C13');
    else
        wf=q/(cpf*(t2-t1));
        writematrix(wf,filename,'Sheet','dados','Range','C14');
    end
else % Caso não esteja faltando nenhuma variável
    q = wq*cpq*(T1-T2);
end
writematrix(q,filename,'Sheet','dados','Range','K5');
%% Passo 2: Diferença de temperartura no trocador

mldt = ((T1-t2)-(T2-t1))/log((T1-t2)/(T2-t1)); %Diferença logaritimica
%Admensionais para cálculo do fator de  (F)
R = (T1-T2)/(t2-t1);
S = (t2-t1)/(T1-t1);

%A equação para cálculo de F depende da quantidade de passagens no casco
%A quantidade de passos nos tubo afeta muito pouco em F (<1/%), então para
%um trocador 1-2 e 1-4 a equação é a mesma
if N == 1 && R ~= 1 %Para 1 passagem no casco
    num = ((R^2+1)^0.5)*log((1-(S*R))/(1-S));
    a = (2-S*(R+1-(R^2+1)^0.5));
    b = (2-S*(R+1+(R^2+1)^0.5));
    den = (1-R)*log(a/b);
    F = num/den;
elseif N > 1 && R~=1 %Mais de uma passagem no casco
    S=(((1-S*R)/(1-S))^(1/N)-1)/(((1-S*R)/(1-S))^(1/N)-R);
    num = S*2^0.5;
    a = (2-S*(2-2^0.5));
    b = (2-S*(2+2^0.5));
    F = num/((1-S)*log(a/b));
else % Para R=1
    S=S/(S-S*N+N);
    num = S*2^0.5;
    a = (2-S*(2-2^0.5));
    b = (2-S*(2+2^0.5));
    F = num/((1-S)*log(a/b));
end

%delta_t corrigido
delta_t = F*mldt;
writematrix(delta_t,filename,'Sheet','dados','Range','K9');
writematrix(F,filename,'Sheet','dados','Range','K8');
writematrix(mldt,filename,'Sheet','dados','Range','K7');

%% Passo 3: Temperaturas médias ou calórica
Ud1=Ud;
%Adotar um valor para Ud à partir de Kern,p.840-> tabela 8
A1 = q/(Ud1*(delta_t)); % área à partir do Ud inicial da tabela
Nt1 = A1/(pi*d*0.0254*L); % número de tubos calculado REVER
writematrix(Nt1,filename,'Sheet','dados','Range','K12');
writematrix(A1,filename,'Sheet','dados','Range','K11');

%% Laço com iterações
arranjo = [3 1
           2 2
           2 3];
colors=["r" "g" "b" "c" "m" "y" "k"];
estilo={'--', '-', ':'};
num_p=[1 2 4];
num_r=[15 26 28 29 34 38];
titulos={'Espaçamento das Chicanas  X Coef. Trans. de calor do tubo',...
    'Espaçamento das Chicanas  X Coef. Trans. de calor do casco',...
    'Espaçamento das Chicanas  X Área necessária',...
    'Espaçamento das Chicanas  X Excesso de área',...
    'Espaçamento das Chicanas  X Perda de Carga no Tubo',...
    'Espaçamento das Chicanas  X Perda de Carga do Casco'};
titulos_y={'Coeficiente de Transferência de Calor [W/m^2*K]',...
    'Coeficiente de Transferência de Calor [W/m^2*K]',...
    'Área necessária [m^2]',...
    'Excesso de Área [%]',...
    'Perda de Carga no tubo [Pa]',...
    'Perda de Carga no casco [Pa]'};

for t=1:6
    figure
    for y=1:2
        Npt=num_p(y);
        if Npt==1
            Col=5;
        elseif Npt==2
            Col=6;
        elseif Npt==4
            Col=7;
        end
        for k=1:3
            At=arranjo(k,1);
            At2=arranjo(k,2);
         
            i=1;
            saida=1;
            x=[0.06,2];
            %%%%%%%%%%%%%%%%%%%%%%%%%%% PARTE DO PASSO 3%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
            for j=x(1):0.035:x(end)
                
                L=2.5;
            
                tab_tubos=readmatrix('base_dados.xlsx','Sheet','contagem_tubos','Range', ...
                    'A3');
                Dic_inter =[(L/pol)/5,(L/pol)/10]; % intervalo de valores de Dic [pol]
            
                if max(Dic_inter)<8.071
                    Dic_inter=[8.071 8.071];
                end     
                        
                Dic_tab=tab_tubos((tab_tubos(:,1)>=Dic_inter(2) & tab_tubos(:,1)<=...
                    Dic_inter(1)),1);
                
                Dic=Dic_tab(1);
                
               
                Dc=Dic+2;
            
                   
                %%%%%%%%%%%%%%%%%%%%%%%%%%% CHICANAS %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%    
                % Espaç. min. ---> NÃO menor que 1/5 diam do casco ou 2 pol
                % Depois chicanas virarão um vetor tbm
                % Usar o trecho abaixo para cria um vetor depois
                % Ii e Io da tabela
                Ii=tab_constantes((tab_constantes(:,17)==class_p) & ...
                    tab_constantes(:,18)<Dc & tab_constantes(:,19)>=Dc ,20);
                Io=tab_constantes((tab_constantes(:,17)==class_p) & ...
                    tab_constantes(:,18)<Dc & tab_constantes(:,19)>=Dc ,21);
                
                %Diâmetro do bocal [pol]
                d_b=tab_constantes((tab_constantes(:,13)<Dc) & ...
                    (tab_constantes(:,14)>=Dc),15);
                d_b=d_b(1);
                
                Isi=(Ii+d_b)*pol;  % Espaçamento da primeira chicana [m]
                Iso=(Io+d_b)*pol;  % Espaçamento da última chicana   [m]
                
             
                Is=j;
                
                Nb=((L-Isi-Iso)/Is)+1;  % número de chicanas
                Nb=Nb+(1-rem(Nb,1));
                
                %Ic --- Corte da chicana
                %Ic/Dic --- 25% valor típico
                Ic= 0.25*Dic; %----> [pol]
                
                dados_chicana={Nb,Is,Ii,Io,Isi,Iso,Ic};
            
                %%%%%%%%%%%%%%%%%%%%%%%%%Passo 3%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
                A1 = q/(Ud1*(delta_t)); % área à partir do Ud inicial da tabela
                Nt1 = A1/(pi*d*0.0254*L); % número de tubos calculado REVER
                
                 if At == 4 || At == 5
                    d=1;
                    di = d-2*0.065;
                 else
                    d=0.75;
                    di = d-2*0.065;
                 end
                 
                verif = [Dic,d,At]; % Os valores para entrar na tabela
        
                %Verificação na tabela para pegar o nº de tubos
                Nt=tab_tubos((tab_tubos(:,1)==verif(1) & tab_tubos(:,3)==verif(2)...
                    & tab_tubos(:,4)==verif(3)),Col);
                
                
                Df=tab_tubos(tab_tubos(:,1)==Dic,2);
                Df=Df(1);
                
                A = Nt*(pi*d*0.0254*L); %área de projeto
                Ud = q/(A*delta_t);
                
                %%%%%%%%%%%%Aplicando função passso 4%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
                dados_trocador={L,Dic,Npt,At,At2,tip_f,Ft,d,Df,di,pol,Nt};
                
                [R4_tubo,R4_casco]=passo4(tab_constantes,dados_trocador,dados_chicana,...
                    p_frio,p_quente,d_ini); %% Chamando função do passo 4
                
                [at,a_t,Gt,mi,ro,cp,Re_t,v,hi,h_io]=R4_tubo{:};
                
                [p,pn,pp,Sm,Re_s,a1,a2,a3,a4,a,ji,hideal,Fc,jc,delta_sb,Ssb,...
                        delta_tb,Stb,alpha,jl,Nc,Fbp,Nss,jb,jr,js,hs,jl1] = R4_casco{:};
                
                %%%%%%%%%%% Cálculo da Temperatura da parede %%%%%%%%%%%%%%%%%%%%%%%%%
                
                tc=(t1+t2)/2;
                Tc=(T1+T2)/2;
                if Ft==1
                    tw=tc+(hs/(h_io+hs))*(Tc-tc);
                else
                    tw=tc+(h_io/(h_io+hs))*(Tc-tc);
                end
                phit=1; %---> apenas por enquanto
                
                %%%%%%%%%%% Cálculo do fator de incrustação e excesso de área de troca
                
                Uc=(h_io*hs)/(h_io+hs); %% Coeficiente Global Limpo
                
                Rdt=1.7*10^-5;
                Rds=2*10^-5;
                Ud2=1/(Rdt+Rds+1/Uc);
                An=q/(Ud2*delta_t);
                
                EA=(A-An)/An*100;
                
                %%%%%%%%%%%%%%%%%%%%%%% Passo 5: Lado do Tubo %%%%%%%%%%%%%%%%%%%%%%%%%
            
                if Ft==1  % fluído frio no tubo
                    rho=pf; %rho ---->densidade do fluido no tubo
                else
                    rho=pq;
                end
                
                f= (1.58*log(Re_t)-3.28)^(-2); % Fator de atrito de Filoneno
                delta_Pt =(4*f*(Gt^2)*L*Npt)/(di*pol*2*rho*phit);
                
                % Perda de carga de retorno (entre passagens)
                delta_Pr = (4*Npt*rho*v^2)/2;
                % Perda de carga total no lado tubo
                delta_PT= delta_Pt+delta_Pr;
            
                %%%%%%%%%%%%%%%%%%%% Passo 5: Lado do Casco %%%%%%%%%%%%%%%%%%%%%%%%%%
                
                if Ft==1 %fluído frio do lado do casco
                    W=wq;
                    rho=pq;
                    mi=uq;
                else
                    W=wf;
                    rho=pf;
                    mi=uf;
                end
                
                b_1=tab_constantes((tab_constantes(:,28)==At2 & tab_constantes(:,29)...
                    >=Re_s & tab_constantes(:,30)<Re_s),31);
                b_2=tab_constantes((tab_constantes(:,28)==At2 & tab_constantes(:,29)...
                    >=Re_s & tab_constantes(:,30)<Re_s),32);
                b_3=tab_constantes((tab_constantes(:,28)==At2 & tab_constantes(:,29)...
                    >=Re_s & tab_constantes(:,30)<Re_s),33);
                b_4=tab_constantes((tab_constantes(:,28)==At2 & tab_constantes(:,29)...
                    >=Re_s & tab_constantes(:,30)<Re_s),34);
                
                % I perda de carga na seção de escoamento cruzado (dp_c)
                 
                b= b_3/(1+0.14*(Re_s)^b_4); %c=b (variável b já utilizada)
                f_i= b_1*((1.33/(p/d))^b)*((Re_s)^b_2);
                
                dp_bi= ((4*f_i*W^2*Nc)/(rho*Sm^2))*phit; 
                m=0.15*(1+(Ssb/(Stb+Ssb)))+0.8;
                R_11=-1.33*(1+(Ssb/(Stb+Ssb)))*(((Stb+Ssb)/Sm)^m);
                R_1= exp(R_11);
                
                if Re_s > 100
                    C_bp=3.7;
                else %para Res <= 100
                    C_bp=4.5;
                end
                R_b1=-C_bp*Fbp*(1-((2*Nss/Nc)^(1/3)));
                R_b= exp(R_b1);
                dp_c=dp_bi*(Nb-1)*R_b*R_1;
                
                % II perda de carga nas janelas (dp_w)
                 
                N_cw= (0.8*Ic)/pp;
                S_wg= (((Dic*pol)^2)/4)*(acos(1-(2*Ic/Dic))-(1-2*Ic/Dic)*...
                    ((1-(1-2*Ic/Dic)^2)^1/2));
                S_wt= (Nt/8)*(1-Fc)*pi*(d*pol)^2;
                S_w= S_wg-S_wt;
                
                teta_b= 2*acos(1-2*Ic/Dic);
                D_w= (4*S_w)/((pi/2)*Nt*(1-Fc)*(d*pol)+Dic*pol*teta_b);
                
                
                if Re_s >= 100
                    dp_wi= (W^2*(2+0.6*N_cw))/(2*Sm*S_w*rho);
                else 
                    dp_wi1=((26*mi*W)/(((Sm*S_w)^(1/2))*rho));
                
                    dp_wi=((dp_wi1)*((N_cw/(p*pol-d*pol))+(Is/(D_w^2)))+((2*W^2)/(2*Sm*S_w*rho)));
                end
                 
                dp_w= Nb*dp_wi*R_1;
                
                
                % III perda de carga nas regiões de entrada e de saída do casco (dp_e) 
                if Re_s>100
                    n1= 0.2;
                else
                    n1=1;
                end
                 
                R_s= 1/2*(((Isi/pol)^(n1-2))+((Iso/pol)^(n1-2)));
                dp_e= 2*dp_bi*(1+(N_cw/Nc))*R_b*R_s;
                
                %Perda de carga total lado do casco
                delta_ps=dp_c+dp_w+dp_e;
            
                Resultados(i+1,:)={L,Dic,Npt,Nt,Is,Nb,At,At2,tip_f,Ft,d,Re_t,v,hi,h_io,...
                    Re_s,ji,hideal,jc,delta_sb,delta_tb,jl,jb,jr,js,hs,A,An,EA,Ud1,Ud,...
                    Uc,Ud2,delta_PT,dp_c,dp_w,dp_e,delta_ps,'########',Dc,di,Ii,...
                    Io,d_b,Isi,Iso,Ic,Df,at,a_t,Gt,p,pn,pp,Sm,delta_sb,...
                    Ssb,delta_tb,Stb,Nc,Nss,tw};
                i=i+1;
            end
            
            
            %{
            plot(cell2mat(Resultados(2:end,1)),cell2mat(Resultados(2:end,27)),'Color', ...
                colors(k),'LineWidth',1.0,'LineStyle','-')
            title('Comprimento do Casco (L) X Área de projeto (A)')
            ylabel('Área de projeto [m^2]')
            grid on
            xlabel('Comprimento do casco [m]')
            
            hold on
            %}
            
            
            plot(cell2mat(Resultados(2:end,5)),cell2mat(Resultados(2:end,num_r(t))),...
                'LineWidth',1,'LineStyle',estilo(y),'Color',colors(k))
    
            title(titulos(t))
            ylabel(titulos_y(t))
            xlabel('Espaçamento das Chicanas (Is) [m]')
            grid on
            hold on
            
            
        end
    end
        legend('Triângular - Passo 1" - Tubo 3/4" - 1 Passe',...
            'Quadrado - Passo 1" - Tubo 3/4" - 1 Passe', ...
            'Rodado - Passo 1" - Tubo 3/4" - 1 Passe',...
            'Triângular - Passo 1" - Tubo 3/4" - 2 Passes',...
            'Quadrado - Passo 1" - Tubo 3/4" - 2 Passes',...
            'Rodado - Passo 1" - Tubo 3/4" - 2 Passes')
        
end
        
        

%% Funções do passo 4
function [R4_tubo,R4_casco]=passo4(tab_constantes,dados_trocador,...
    dados_chicana,p_frio,p_quente,d_ini) 
    
    [~,~,~,~,T1,T2,wq,t1,t2,wf,~,~,~,~,~,~,~,~]=d_ini{:};
    [L,Dic,Npt,At,At2,tip_f,Ft,d,Df,di,pol,Nt] = dados_trocador{:};
    [cpq,~,~,uq,pq,k_q] = p_quente{:};
    [cpf,~,~,uf,pf,k_f] = p_frio{:};
    [Nb,Is,~,~,Isi,Iso,Ic]=dados_chicana{:};

    %%%%%%%%%%%%%%%% LADO DO TUBO %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    % Sendo a_t a área de escoamento de um tubo (pi*di^2)/4; Npt é o número
    a_t=(pi*(di*pol)^2)/4;   
    at =(Nt*a_t)/Npt;
    
    
    % w é a vazão mássica do fluido do lado do tubo, depende do fluido no tubo
    if Ft == 1
        Gt = wf/at;   % vazão mássica por uni. de área  
        mi = uf;      % viscosidade dinâmica que será usada
        ro=pf;        % densidade que será usada
        t=(t2-t1)/2;  % t médio que será usado
        cp=cpf;       % capacidade calorífica
        k=k_f;
    else
        Gt = wq/at;
        mi = uq;
        ro=pq;
        t=(T1-T2)/2;
        cp=cpq;
        k=k_q;
    end   
    
    Re_t = (Gt*di*0.0254)/mi;   % NÚMERO DE REYNOLDS tubo
    
    v=Gt/ro;   % VELOCIDADE DE ESCOAMENTO
    
    % Como o fluido é água utilizar a seguinte equação:Como a água é um...
    %fluido normalmente incrustante não se utilizam velocidades de escoamento...
    %inferiores a 1 m/s. Sugere-se ler a parte referente a "Trocadores...
    % usando água", p. 115, do Kern.
    
    if tip_f == 1 % Para água
        hi = 1055*(1.352+(0.0198*t))*(v^0.8)/((di*0.0254)^0.2);%(3.24b, ARAU.)    
                            % t é a temperartura média da água (°C)
                            % v é a velocidade de escoamento (m/s)
    elseif Re_t>10000 % Turbulento
        % no ínicio considera (mi/miw)^0.14 = 1
        Nu = 0.027*(((di*0.0254)*Gt/mi)^0.8)*((cp*mi/k)^(1/3))*1; %(3.25, Araújo) 
        hi=k*Nu/(di*0.0254);  % Definição do nº de Nu 
    
    elseif Re_t<2100 % Laminar
        hi= 3.66*k/(di*0.0254); % (3.27, ARAÚJO)
    else % Transição
         Nu = 0.1*((((di*0.0254)*Gt/mi)^(2/3))-125)*((cp*mi/k)^0.495)*...
             (exp(-0.0225*(log(cp*mi/k))^2))*((1+((di*0.0254)/(L*Npt)))^...
             (2/3))*1;        % (3.28, ARAÚJO)
         hi=k*Nu/(di*0.0254); % No início considere o termo ((Mi/Miw)^0.14)...
                              % igual a 1. 
    end
    
    h_io = (hi*di)/d; % (3.29, ARAÚJO)
    
    % Resultados
    R4_tubo={at,a_t,Gt,mi,ro,cp,Re_t,v,hi,h_io};

    %%%%%%%%%%%%%%%%%%%%%%%%Lado do Casco%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    if Ft==1             % Fluído no tubo frio e no casco quente
        w=wq;
        cp=cpq;
        mi=uq;
        k=k_q;
    else
        w=wf;
        cp=cpf;
        mi=uf;
        k=k_f;
    end
    
    %Passos
    tab_passos=readmatrix('base_dados.xlsx','Sheet','passos','Range','A1');
    p=tab_passos((tab_passos(:,1)==d & tab_passos(:,3)==At2),2);  % [pol]
    pn=tab_passos((tab_passos(:,1)==d & tab_passos(:,3)==At2),5); % [pol]
    pp=tab_passos((tab_passos(:,1)==d & tab_passos(:,3)==At2),4); % [pol]
    
    %I
    if At==2  
        Sm=Is*((Dic*0.0254)-(Df*0.0254)+(((Df*0.0254)-(d*0.0254))/...
            (pn*0.0254))*((p-d)*0.0254)); % [m]
    elseif At == 4
        Sm=Is*((Dic*0.0254)-(Df*0.0254)+(((Df*0.0254)-(d*0.0254))/...
            (pn*0.0254))*((p-d)*0.0254)); % [m]
    else
        Sm=Is*((Dic*0.0254)-(Df*0.0254)+(((Df*0.0254)-(d*0.0254))/...
            (p*0.0254))*((p-d)*0.0254)); % [m]
    end
 
    Re_s=(d*0.0254*w)/(mi*Sm);
    
    a1=tab_constantes((tab_constantes(:,1)==At2 & tab_constantes(:,2)>=Re_s...
        & tab_constantes(:,3)<Re_s),4);
    a2=tab_constantes((tab_constantes(:,1)==At2 & tab_constantes(:,2)>=Re_s...
        & tab_constantes(:,3)<Re_s),5);
    a3=tab_constantes((tab_constantes(:,1)==At2 & tab_constantes(:,2)>=Re_s...
        & tab_constantes(:,3)<Re_s),6);
    a4=tab_constantes((tab_constantes(:,1)==At2 & tab_constantes(:,2)>=Re_s...
        & tab_constantes(:,3)<Re_s),7);
    
    a=a3/(1+0.14*(Re_s^a4));     % (3.33)
    ji=a1*((1.33/(p*0.0254/(d*0.0254)))^a)*((Re_s)^a2);   %(3.32)
    hideal=ji*cp*(w/Sm)*(k/(cp*mi))^(2/3)*1; %(3.31, ARAÚJO)-feixe de tubos id.
    
    %II- efeitos da configuração da chicana
   
    Fc1=((Dic*0.0254)-2*(Ic*0.0254))/(Df*0.0254);
    Fc=(1/pi)*(pi+2*Fc1*sin(acos(Fc1))-2*acos(Fc1));
    jc=Fc+0.54*(1-Fc)^0.345;
    
    %III- efeitos dos vazmentos
    
    delta_sb=tab_constantes((tab_constantes(:,9)<=Dic & ...
        tab_constantes(:,10)>Dic),11); % Folga diametral casco chicana [m]
    
    Ssb1=1-(2*Ic/Dic);
    Ssb=(Dic*pol*delta_sb/2)*(pi-acos(Ssb1)); % [m]
    
    delta_tb=7.938*10^-4; % Folga diametral tubo chicana - TEMA classe R
    Stb=pi*d*pol*delta_tb*Nt*(Fc+1)/4;
    alpha =0.44*(1-(Ssb/(Ssb+Stb)));
    
    jl1 = -2.2*(Stb+Ssb)/Sm;
    jl=alpha+(1-alpha)*exp(jl1);
    
    %IV- correção para efeitos de contorno do feixe
    if Re_s<=100
        Cbh=1.35;
    else
        Cbh=1.25;
    end
    
    Nc=Dic*0.0254*(1-2*(Ic/Dic))/(pp*0.0254); % nº de fileiras de tubos cruzados
    Nc=Nc-rem(Nc,1);  % número inteiro
    
    Fbp=0.0254*(Dic-Df)*Is/Sm;
    
    cond=((Dic-Df)>0.5 & (Ssb/(Sm- Ssb))>0.1);
    if (Dic-Df)>1.5 || cond
        Nss=Nc/5; % nº de pares de tiras selante
    else
        Nss=0;
    end
    
    if (Nss/Nc)>=0.5
        jb=1;
    else
        jb1=1-(2*Nss/Nc)^(1/3);
        jb2=-Cbh*Fbp*jb1;
        jb=exp(jb2);
    end
    
    % V Fator de correção para o gradiente adverso de temperatura
    if Re_s >100
        jr=1;
    elseif Re_s <=20
        jr=1.51/(Nc^0.18);
    else
        jr1=1.51/(Nc^0.18);
        jr=jr1+((20-Re_s)/80)*(jr1-1);
    end
    
    %IV- fator de correção devido ao espaçamento desigual
    if Re_s >100
        n=0.6;
    else
        n=1/3;
    end
    
    Isi1= Isi/Is;
    Iso1= Iso/Is;
    
    
    js1 = (Nb-1)+(Isi1)^(1-n)+(Iso1)^(1-n);
    js2 = (Nb-1)+(Isi1)+(Iso1);
    js=js1/js2;
    
    %Cálculo coeficiente do lado do casco
    hs=hideal*jc*jl*jb*jr*js;

    %Resultados
    R4_casco={p,pn,pp,Sm,Re_s,a1,a2,a3,a4,a,ji,hideal,Fc,jc,delta_sb,Ssb...
        delta_tb,Stb,alpha,jl,Nc,Fbp,Nss,jb,jr,js,hs,jl1};

end
