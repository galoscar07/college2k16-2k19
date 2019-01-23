NR % 2 == 1 {
    s1 = s1 + $1
    s2 = s2 + $2
}

NR % 2 == 0 {
    s1 = s1 + $2
    s2 = s2 + $1
}

END {
    print s1, s2
}
