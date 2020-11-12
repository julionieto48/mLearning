clc , clear all , close all ;
%%
archivoUno = 'datosRegLinealUno';
datosUno = xlsread(archivoUno);

%%
% 
x = datosUno(:,1) ; x  = x.' ;
y = datosUno(:,2); y = y.' ;
% scatter(x,y)
%%
% contadro de cantidad de datos ... pregunta como crear mi propia funcion
% length?

n = 0 ;
for j = 1 : length(x)
    n =  j ;
end
%%
xsum = sum(x) ; ysum = sum(y) ;
%%
% columna x * y

xy = [] ; sumXy = 0 ;
for i = 1 : n 
    xy(i) = x(i) * y(i) ;
    sumXy = sumXy + xy(i);
end

%%
% x al cuadrado
sumXCuadrado = 0 ; xCuadrado = [] ;

for i = 1 : n 
    xCuadrado(i) = x(i) ^2 ;
    sumXCuadrado = sumXCuadrado + xCuadrado(i) ;
end
 

% xsum = xsum ^2 no e slo mismo sumar y depsues elevar al cuadrado jeje

%%
% las medias
xMedia = xsum / n ; yMedia = ysum / n ;


%%

m = ( (n * sumXy ) - (xsum + ysum ))    / ( (n *sumXCuadrado ) - ( xsum ^2 )  ) ; %m = 0.849

b = yMedia - ( m * xMedia ) ; %b = 1.504

%%
% graficar
figure ; grid on ;% hold on ;  
x1 = min(x) - 1 :  max(x)+ 1 ;
linea = m .* x1 + b ;
plot(x1,linea); ylim([-1  7]) ; hold on ; grid on ;  scatter(x,y)