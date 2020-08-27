clc , clear all , close all ;
%%
archivoUno = 'desvMuestral';
datosUno = xlsread(archivoUno);

%%
% machos
tasaMetaMachos = datosUno(:,1) ; tasaMetaMachos  = tasaMetaMachos.' ; tasaMetaMachos  = tasaMetaMachos (1,1: length(tasaMetaMachos ) ) ;
tasaMetaHembras = datosUno(:,3); tasaMetaHembras = tasaMetaHembras.' ; tasaMetaHembras = tasaMetaHembras(1,1: length(tasaMetaHembras) );

for i = 1 : length(tasaMetaHembras)
    if isnan(tasaMetaHembras(i))
        tasaMetaHembras(i) = 0 ;
    end
end

%%
% calculo de media

sumMachos = 0 ; NMachos = length(tasaMetaMachos) ;
for i = 1 : length(tasaMetaMachos) 
    sumMachos = sumMachos + tasaMetaMachos(i) ;
end
mediaMachos = sumMachos / NMachos ;
 
sumHembras = 0 ; NHembras = length(tasaMetaMachos) ;
i = 1; 
while i < NHembras + 1
    sumHembras = sumHembras + tasaMetaHembras(i);
    i = i + 1 ;
end
mediaHembras = sumHembras / NHembras ;

%%
% sumatoriaDiferencias con la media de cada dato jaja olvide que se elevaba

sumDifMacho = 0 ; restasMachos = [] ;
for i = 1 : length(tasaMetaMachos)
    restasMachos(i) =  (tasaMetaMachos(i) - mediaMachos)^ 2;
    sumDifMacho = sumDifMacho + restasMachos(i) ;
end

sumDifHembra = 0 ; restasHembras = [] ;
for i = 1 : length(tasaMetaMachos)
    restasHembras(i) =  (tasaMetaHembras(i) - mediaHembras)^2;
    sumDifHembra = sumDifHembra + restasHembras(i) ;
end
%%
% desviacion muestral
desvMacho = sumDifMacho / (NMachos - 1)
desvHembra = sumDifHembra / (NHembras - 1 ) 


%%
% referencia
% https://es.mathworks.com/help/matlab/math/reshaping-and-rearranging-arrays.html
% https://es.mathworks.com/help/matlab/learn_matlab/array-indexing.html
% https://es.wikipedia.org/wiki/Desviaci%C3%B3n_t%C3%ADpica
% https://es.wikipedia.org/wiki/Medidas_de_dispersi%C3%B3n