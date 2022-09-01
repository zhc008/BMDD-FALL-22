%% auction algorithm for assignment problem
function output = acution_algorithm(rating, capacity)
    % get number of patients and number of doctors
    [num_patient, num_doctor] = size(rating);
    % calculate the total capacity of doctors
    total_capacity = sum(capacity);
    % create a extended matrix according to the capacity of each doctor
    new_rating = zeros(num_patient, total_capacity);
    % keep track of which doctor each spot belongs to
    doctor_index = zeros(total_capacity,1);
    % put in the patient ratings into the new matrix
    for i = 1:num_patient
        current_idx = 0;
    	for j = 1:num_doctor
    	    current_capacity = capacity(j); % capacity of the jth doctor
    	    % replicate the rating for the same doctor
    	    for k = 1:current_capacity
%                 print('k: ',k);
%                 print('current_idx: ',current_idx);
%                 print('total_capacity: ',total_capacity);
                doctor_index(k+current_idx) = j;
                new_rating(i, k+current_idx) = rating(i,j);
            end
            current_idx = current_idx + current_capacity;
        end
    
        
    end
    price = zeros(total_capacity, 1); % price for each doctor's spot
    assignment = 1:total_capacity; % current assignment plan
    temp_output = auction(new_rating,price, assignment, num_patient);
    % change the output into real doctor index
    temp_output = temp_output(1:num_patient);
    output = doctor_index(temp_output);
    
end

