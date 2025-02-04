from numpy import sqrt
from mysqrt import sqrt2
small=1.0e-14
x_values=[0,2,100,10000,0.0001,1e8]
for x in x_values:
	s=sqrt2(x)
	s_numpy=sqrt(x)
	print(f"for x={x},s={s} and s_numpy={s_numpy}")
	assert (s-s_numpy)<small, f"square roo disagrees with numpy sqrt for x={x}"

