package com.company;

import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

public class Main {

    public static void main(String[] args) {
        List<Integer> numbers = Arrays.asList(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16);
        List<Integer> numbers1 = numbers.stream().map(n->n%4 !=0 ).collect(Collectors.toList()).get();
        System.out.println(numbers);

    }
}
