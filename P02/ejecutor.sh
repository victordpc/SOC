# Red BA analizada con NetworkX
echo Red BA analizada con NetworkX
python generadorRedes.py netX

# Red BA unica
echo Red BA unica
python generadorRedes.py gephi

# Red aleatoria analizada con NetworkX
echo Red aleatoria analizada con NetworkX
python generadorRedes.py random

# Red Unica Aleatoria
echo Red aleatoria única
python random_net.py 500 0.001 A_500_S_
python random_net.py 1000 0.0005 A_1000_S_
python random_net.py 5000 0.0001 A_5000_S_
python random_net.py 500 0.002 A_500_C_
python random_net.py 1000 0.0001 A_1000_C_
python random_net.py 5000 0.00002 A_5000_C_
python random_net.py 500 0.0072 A_500_SC_
python random_net.py 1000 0.00395 A_1000_SC_
python random_net.py 5000 0.00095 A_5000_SC_
python random_net.py 500 0.02 A_500_CO_
python random_net.py 1000 0.01 A_1000_CO_
python random_net.py 5000 0.002 A_5000_CO_

# Fin
echo Fin