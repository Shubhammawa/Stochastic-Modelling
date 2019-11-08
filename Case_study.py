import numpy as np
#from pydtmc import MarkovChain as mc

pi = np.array([0.033, 1.584/1000, 1.4256/10000, 2.35224/100000, 4.9867488/1000000, 1.431196906/1000000, 
				4.708637819/10000000])

#print(pi*0.9385100507)

p_stat = np.array([0.9385100507, 3.09708317e-02, 1.48659992e-03, 1.33793993e-04, 2.20760088e-05, 4.68011387e-06
			, 1.34319268e-06, 4.41910392e-07, 0.02887])
#print(p_stat*100)
p = [0.033, 0.048, 0.090, 0.165, 0.212, 0.287, 0.329]

q = np.array([0.030, 0.021, 0.037, 0.052, 0.075, 0.135, 0.182])

b = np.array([1243.78, 2090.33, 2615.16, 3073.13, 3502.99, 3905.77, 4280.26])

bankruptcy_loss = 0
bankruptcy_losses = []
termination_losses_SPI = []
termination_losses = []
for m in range(1,8):
	bankruptcy_loss = 0
	termination_loss_SPI = 0
	termination_loss = 0
	for k in range(0,m):
		#print(k)
		bankruptcy_loss += p_stat[k]*q[k]*b[k]
	bankruptcy_losses.append(bankruptcy_loss)

	# With SPI (Factor of 0.25)
	termination_loss_SPI = p_stat[m-1]*p[m-1]*0.25*b[m-1]
	termination_losses_SPI.append(termination_loss_SPI)
	
	# Without SPI
	termination_loss = p_stat[m-1]*p[m-1]*b[m-1]
	termination_losses.append(termination_loss)
#print(loss)
n_cust = 14*10**6
#print(loss*n_cust)
#print(bankruptcy_losses)
#print(termination_losses)
total = (np.add(bankruptcy_losses,termination_losses))
Total_loss = np.add(total,50000/n_cust)

#print(total)


#### Problem 5

p_new = [0.033, 0.048, 0.090, 0.165, 0.212, 0.287, 0.25]

pi_new = np.array([1, 0.033, 1.584/1000, 1.4256/10000, 2.35224/100000, 4.9867488/1000000, 1.431196906/1000000, 
				3.57799015/10000000, 0.03076171899])
p_stat_new = pi_new * 0.9385101503
#print(p_stat_new)
call_cost = 1
bankruptcy_loss = 0
for k in range(0,7):
	#print(k)
	bankruptcy_loss += p_stat_new[k]*q[k]*b[k]
termination_loss = p_stat[6]*p_new[6]*b[6]
#print(bankruptcy_loss)
#print(termination_loss+bankruptcy_loss+p_stat_new[6])


### Problem 6
q_6 = np.array([0.030, 0.021, 0.037, 0.052, 0.075, 0.135, 0.182])*1.5
print(q_6)

pi_6 = np.array([1, 0.033, 1.584/1000, 1.4256/10000, 2.35224/100000, 4.9867488/1000000, 1.431196906/1000000, 
				4.708637819/10000000, 0.03076171899])

p_stat_6 = pi_6 * 0.925155349

bankruptcy_loss = 0
bankruptcy_losses = []
termination_losses_SPI = []
termination_losses = []
for m in range(1,8):
	bankruptcy_loss = 0
	termination_loss_SPI = 0
	termination_loss = 0
	for k in range(0,m):
		#print(k)
		bankruptcy_loss += p_stat_6[k]*q_6[k]*b[k]
	bankruptcy_losses.append(bankruptcy_loss)

	# With SPI (Factor of 0.25)
	termination_loss_SPI = p_stat_6[m-1]*p[m-1]*0.25*b[m-1]
	termination_losses_SPI.append(termination_loss_SPI)

	termination_loss = p_stat_6[m-1]*p[m-1]*b[m-1]
	termination_losses.append(termination_loss)

# print(bankruptcy_losses)
# print(termination_losses_SPI)
# total = (np.add(bankruptcy_losses,termination_losses_SPI))
# Total_loss = np.add(total,50000/n_cust)
# print(Total_loss)
# print(np.argmin(Total_loss))

# print(np.add(bankruptcy_losses, termination_losses))



### Problem 7

bankruptcy_loss = 0
bankruptcy_losses = []
termination_losses_SPI = []
termination_losses = []
for m in range(1,8):
	bankruptcy_loss = 0
	termination_loss_SPI = 0
	termination_loss = 0
	for k in range(0,m):
		#print(k)
		bankruptcy_loss += p_stat[k]*q[k]*b[k]
	bankruptcy_losses.append(bankruptcy_loss)

	# With SPI (Factor of 0.4)
	termination_loss_SPI = p_stat[m-1]*p[m-1]*0.4*b[m-1]
	termination_losses_SPI.append(termination_loss_SPI)

print(bankruptcy_losses)
print(termination_losses_SPI)
total = (np.add(bankruptcy_losses,termination_losses_SPI))
Total_loss = total
print(Total_loss)
print(np.argmin(Total_loss))
