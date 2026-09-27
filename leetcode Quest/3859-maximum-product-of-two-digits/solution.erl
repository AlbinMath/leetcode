-spec max_product(N :: integer()) -> integer().

max_product(N) ->
    Digits = [D - $0 || D <- integer_to_list(N)],
    Sorted = lists:sort(Digits),
    Len = length(Sorted),
    lists:nth(Len, Sorted) * lists:nth(Len - 1, Sorted).
