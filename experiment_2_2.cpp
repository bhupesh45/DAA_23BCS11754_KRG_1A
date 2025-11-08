#include <bits/stdc++.h>
using namespace std;

int dp[1001][1001];

bool subsetSum(int index, vector<int>& arr, int target) {
    if (target == 0) return true;
    if (index == 0) return (arr[0] == target);

    if (dp[index][target] != -1) return dp[index][target];

    bool notPick = subsetSum(index - 1, arr, target);
    bool pick = false;
    if (arr[index] <= target)
        pick = subsetSum(index - 1, arr, target - arr[index]);

    return dp[index][target] = (pick || notPick);
}

int main() {
    int n;
    cout << "Enter number of elements: ";
    cin >> n;

    vector<int> arr(n);
    cout << "Enter elements: ";
    for (int i = 0; i < n; i++)
        cin >> arr[i];

    int target;
    cout << "Enter target sum: ";
    cin >> target;

    memset(dp, -1, sizeof(dp));

    if (subsetSum(n - 1, arr, target))
        cout << "YES, subset with sum " << target << " exists.\n";
    else
        cout << "NO, subset with sum " << target << " does not exist.\n";

    return 0;
}
