%% determine whether a certain patient is happy based on profit
function [happiness, max_profit_idx] = isHappy(rating, price, assignment, patient_idx, epsilon)
    % get the assigne_doctor for current patient
    assigned_doctor = assignment(patient_idx);
    % calculate current profit for this patient
    current_profit = rating(patient_idx, assigned_doctor) - price(assigned_doctor);
    profit = rating(patient_idx,1:end) - price';
    % determine if current profit is maxed
    max_profit = max(profit);
    % this patient is almost happy if his current profit is larger than the
    % largest profit he can make minus the epsilon
    happiness = current_profit >= max_profit - epsilon;
    max_profit_idx = find(profit == max_profit);
    max_profit_idx = max_profit_idx(1);
end