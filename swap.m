%% swap the assignment of doctor
function assignment = swap(current_idx, new_idx, old_assignment)
    temp = old_assignment(current_idx);
    old_assignment(current_idx) = old_assignment(new_idx);
    old_assignment(new_idx) = temp;
    assignment = old_assignment;
end