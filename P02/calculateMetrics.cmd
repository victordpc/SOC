rmdir /q /s Result

echo 500 nodes ba 
for /l %%x in (1, 1, 10) do (
    python .\metricas.py BA Files/BA_NODOS_M3_T500_%%x.csv        Files/BA_ARISTAS_M3_T500_%%x.csv  3
    python .\metricas.py BA Files/BA_NODOS_M4_T500_%%x.csv        Files/BA_ARISTAS_M4_T500_%%x.csv  4
)
 
echo 500 nodes random 
for /l %%x in (1, 1, 10) do (
    python .\metricas.py Random Files/Random_NODOS_N500_T0.001_%%x.csv Files/Random_ARISTAS_N500_T0.001_%%x.csv 0.001
    python .\metricas.py Random Files/Random_NODOS_N500_T0.002_%%x.csv Files/Random_ARISTAS_N500_T0.002_%%x.csv 0.002
    python .\metricas.py Random Files/Random_NODOS_N500_T0.009_%%x.csv Files/Random_ARISTAS_N500_T0.009_%%x.csv 0.009
    python .\metricas.py Random Files/Random_NODOS_N500_T0.1_%%x.csv   Files/Random_ARISTAS_N500_T0.1_%%x.csv   0.1
)

echo 1000 nodes BA
for /l %%x in (1, 1, 10) do (
    python .\metricas.py BA Files/BA_NODOS_M3_T1000_%%x.csv       Files/BA_ARISTAS_M3_T1000_%%x.csv 3
    python .\metricas.py BA Files/BA_NODOS_M4_T1000_%%x.csv       Files/BA_ARISTAS_M4_T1000_%%x.csv 4
)

echo 1000 nodes random 
for /l %%x in (1, 1, 10) do (
    python .\metricas.py Random Files/Random_NODOS_N1000_T0.001_%%x.csv   Files/Random_ARISTAS_N1000_T0.001_%%x.csv 0.001
    python .\metricas.py Random Files/Random_NODOS_N1000_T0.002_%%x.csv   Files/Random_ARISTAS_N1000_T0.002_%%x.csv 0.002
    python .\metricas.py Random Files/Random_NODOS_N1000_T0.009_%%x.csv   Files/Random_ARISTAS_N1000_T0.009_%%x.csv 0.009
    python .\metricas.py Random Files/Random_NODOS_N1000_T0.1_%%x.csv     Files/Random_ARISTAS_N1000_T0.1_%%x.csv   0.1
)

echo 5000 nodes BA
for /l %%x in (1, 1, 10) do (
    python .\metricas.py BA Files/BA_NODOS_M3_T5000_%%x.csv       Files/BA_ARISTAS_M3_T5000_%%x.csv 3
    python .\metricas.py BA Files/BA_NODOS_M4_T5000_%%x.csv       Files/BA_ARISTAS_M4_T5000_%%x.csv 4
)

echo 5000 nodes random 
for /l %%x in (1, 1, 10) do (
    python .\metricas.py Random Files/Random_NODOS_N5000_T0.001_%%x.csv   Files/Random_ARISTAS_N5000_T0.001_%%x.csv 0.001
    python .\metricas.py Random Files/Random_NODOS_N5000_T0.002_%%x.csv   Files/Random_ARISTAS_N5000_T0.002_%%x.csv 0.002
    python .\metricas.py Random Files/Random_NODOS_N5000_T0.009_%%x.csv   Files/Random_ARISTAS_N5000_T0.009_%%x.csv 0.009
    python .\metricas.py Random Files/Random_NODOS_N5000_T0.1_%%x.csv     Files/Random_ARISTAS_N5000_T0.1_%%x.csv   0.1
)
