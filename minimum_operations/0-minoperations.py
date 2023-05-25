def minOperations(n):
  """
  Calculates the fewest number of operations needed to result in exactly n H characters in the file.

  Args:
    n: The number of H characters to be in the file.

  Returns:
    The fewest number of operations needed.

  Raises:
    Exception: If n is impossible to achieve.
  """

  # Check if n is possible to achieve.
  if n <= 0:
    raise Exception("n must be positive")

  # Initialize the dp table.
  dp = [0] * (n + 1)

  # Fill in the dp table.
  for i in range(1, n + 1):
    # The minimum number of operations to get i H characters is the minimum of the following:
    #   * The minimum number of operations to get i - 1 H characters, plus 1 operation to insert a new H character.
    #   * The minimum number of operations to get i / 2 H characters, plus 1 operation to copy all the characters and paste them again.
    dp[i] = min(dp[i - 1] + 1, dp[i // 2] + 1)

  # Return the minimum number of operations.
  return dp[n]
