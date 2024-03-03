def power(n, m):

  n_pow = 1
  m_pow = 1
  for i in range(m):
    n_pow *= n
  for i in range(n):
    m_pow *= m
  return n_pow, m_pow

n = int(input("Enter the value of n: "))
m = int(input("Enter the value of m: "))
n_pow, m_pow = power(n, m)
print(n_pow, m_pow)