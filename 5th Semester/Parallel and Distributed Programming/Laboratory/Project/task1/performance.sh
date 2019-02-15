NT=(1 3 5 10 15 25 50 100 250 500)

echo "Building project..."
cmake .
make

> performance.log

for i in "${NT[@]}"; do
    start=$(gdate +%s.%N);
    echo $i >> performance.log
    echo "Testing with $i threads";
    ./Filters.o image.jpg $i;
    dur=$(echo "$(gdate +%s.%N) - $start" | bc);
    echo $dur >> performance.log
done
