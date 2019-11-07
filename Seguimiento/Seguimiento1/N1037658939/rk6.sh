arr=(10 100 1000 10000)

g++ -o rk.out rk6.cpp

for n in "${arr[@]}"
do
./rk.out <<<$n > data$n.txt
done

python3 rk6_plot.py 
