defmodule Solution do

  @spec maximum_product(nums :: [integer]) :: integer

  def maximum_product(nums) do
    sorted = Enum.sort(nums)

    n = length(sorted)

    a = Enum.at(sorted, n - 1)
    b = Enum.at(sorted, n - 2)
    c = Enum.at(sorted, n - 3)

    x = Enum.at(sorted, 0)
    y = Enum.at(sorted, 1)

    max(a * b * c, a * x * y)
  end

end
