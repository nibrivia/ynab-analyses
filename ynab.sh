# token file should define $token and $budget_id
source token

# Gets the budget IDs
# curl -H "Authorization: Bearer $token" https://api.youneedabudget.com/v1/budgets
curl -H "Authorization: Bearer $token" https://api.youneedabudget.com/v1/budgets/$budget_id/transactions
