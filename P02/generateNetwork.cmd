rmdir /q /s Files
echo Generates 500 nodes networks csv files
for /l %%x in (1, 1, 10) do (
   python .\redBA.py 3 500  %%x
   python .\redBA.py 4 500  %%x
)

for /l %%x in (1, 1, 10) do (
   python .\redRandom.py 500 0.001 %%x
   python .\redRandom.py 500 0.002 %%x
   python .\redRandom.py 500 0.009 %%x
   python .\redRandom.py 500 0.1 %%x
)


echo Generates 1000 nodes networks csv files
for /l %%x in (1, 1, 10) do (
   python .\redBA.py 3 1000  %%x
   python .\redBA.py 4 1000  %%x
)

for /l %%x in (1, 1, 10) do (
   python .\redRandom.py 1000 0.001 %%x
   python .\redRandom.py 1000 0.002 %%x
   python .\redRandom.py 1000 0.009 %%x
   python .\redRandom.py 1000 0.1 %%x
)


echo Generates 5000 nodes networks csv files
for /l %%x in (1, 1, 10) do (
   python .\redBA.py 3 5000  %%x
   python .\redBA.py 4 5000  %%x
)

for /l %%x in (1, 1, 10) do (
   python .\redRandom.py 5000 0.001 %%x
   python .\redRandom.py 5000 0.002 %%x
   python .\redRandom.py 5000 0.009 %%x
   python .\redRandom.py 5000 0.1 %%x
)