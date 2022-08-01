import dis

from examples import naive_sum, python_sum


print("naive")
dis.dis(naive_sum)

print("\npython")
dis.dis(python_sum)
