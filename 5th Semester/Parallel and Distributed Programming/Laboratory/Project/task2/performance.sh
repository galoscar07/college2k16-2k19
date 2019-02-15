NT=(localhost localhost,localhost localhost,localhost,localhost localhost,localhost,localhost,localhost)

echo "Building project..."
cmake .
make

> performance.log

for i in "${NT[@]}"; do
    start=$(gdate +%s.%N);
    echo $i >> performance.log
    echo "Testing with $i hosts";
    mpirun --host $i ./Filters.o image.jpg
    dur=$(echo "$(gdate +%s.%N) - $start" | bc);
    echo $dur >> performance.log
done
