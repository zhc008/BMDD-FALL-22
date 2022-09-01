import numpy as np

## auction algorithm for assignment problem
def auction_algorithm(rating, capacity):
	# get number of patients and number of doctors
	[num_patient, num_doctor] = np.shape(rating)
	# calculate the total capacity of doctors
	total_capacity = np.sum(capacity)
	# create a extended matrix according to the capacity of each doctor
	new_rating = np.zeros([num_patient, total_capacity])
	# keep track of which doctor each spot belongs to
	doctor_index = np.zeros([total_capacity, 1])
	# put in the patient ratings into the new matrix
	for i in range(num_patient):
		current_idx = 0
		for j in range(num_doctor):
			current_capacity = capacity[j] # capacity of the jth doctor
			# replicate the rating for the same doctor
			for k in range(current_capacity):
#                 print('k: ',k);
#                 print('current_idx: ',current_idx);
#                 print('total_capacity: ',total_capacity);
				doctor_index[k+current_idx] = j
				new_rating[i, k+current_idx] = rating[i,j]

			current_idx = current_idx + current_capacity

	price = np.zeros([total_capacity, 1]) # price for each doctor's spot
	assignment = list(range(total_capacity)) # current assignment plan
	temp_output = auction(new_rating, price, assignment, num_patient)
	# change the output into real doctor index
	temp_output = temp_output[:num_patient]
	output = doctor_index[temp_output]
	return output

## the loop that makes most patients happy
def auction(rating, price, assignment, num_patient):
	epsilon = 1/(num_patient+1) # a weight that terminates the loop faster
	while True:
		all_happy = True
		for patient in range(num_patient):
			# determine which patient is unhappy with current assignment
			[happiness, max_profit_idx] = isHappy(rating, price, assignment, patient, epsilon)
			# if a patient is unhappy, assign a new doctor to make him happy
			if (not happiness):
				max_profit_holder = assignment.index(max_profit_idx)
				assignment = swap(patient, max_profit_holder, assignment)
				assigned_doctor = assignment[patient]
				# this patient bidding a new price to get a new assigned
				# doctor
				price[assigned_doctor] = price[assigned_doctor] + epsilon + 1
				all_happy = False
#                 break;
		if all_happy: # if everyone is happy, end the loop
			break
	return assignment

# swap the assignment of doctor
def swap(current_idx, new_idx, old_assignment):
	temp = old_assignment[current_idx]
	old_assignment[current_idx] = old_assignment[new_idx]
	old_assignment[new_idx] = temp
	return old_assignment


## determine whether a certain patient is happy based on profit
def isHappy(rating, price, assignment, patient_idx, epsilon):
	# get the assigne_doctor for current patient
	assigned_doctor = assignment[patient_idx]
	# calculate current profit for this patient
	current_profit = rating[patient_idx, assigned_doctor] - price[assigned_doctor]
	current_rating = rating[patient_idx,:] # rating from this patient
	current_rating = current_rating.ravel()
	profit = current_rating - (price.T).ravel()
	# determine if current profit is maxed
	max_profit = max(profit)
	# this patient is almost happy if his current profit is larger than the
	# largest profit he can make minus the epsilon
	happiness = current_profit >= (max_profit - epsilon)
	max_profit_idx = np.where(profit == max_profit)
	max_profit_idx = max_profit_idx[0]
	return happiness, max_profit_idx

rating = np.array([[3,2,1],[2,1,3],[1,2,3],[2,3,1]])

capacity = [1,2,1]
print(auction_algorithm(rating, capacity))
