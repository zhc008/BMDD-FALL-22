%% the loop that makes most patients happy
function assignment = auction(rating, price, assignment, num_patient)
    epsilon = 1/(num_patient+1); % a weight that terminates the loop faster
    while true
        all_happy = true;
        for patient = 1:num_patient
            % determine which patient is unhappy with current assignment
            [happiness, max_profit_idx] = isHappy(rating, price, assignment, patient, epsilon);
            % if a patient is unhappy, assign a new doctor to make him happy
            if ~happiness
                max_profit_holder = find(assignment == max_profit_idx);
                assignment = swap(patient, max_profit_holder, assignment);
                assigned_doctor = assignment(patient);
                % this patient bidding a new price to get a new assigned
                % doctor
                price(assigned_doctor) = price(assigned_doctor)+ epsilon + 1;
                all_happy = false;
%                 break;
            end
        end
        if all_happy % if everyone is happy, end the loop
            break;
        end
    end
end