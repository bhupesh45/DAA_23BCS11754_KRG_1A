class Solution
{
public:
	bool canSplit(vector<int>& nums, int k, long long mid)
	{
		long long current = 0;
		int pieces = 1;

		for(int num : nums)
		{
			if(current + num > mid)
			{
				pieces++;
				current = num;
				if(pieces > k)
					return false;
			}
			else
			{
				current += num;
			}
		}
		return true;
	}

	int splitArray(vector<int>& nums, int k)
	{
		long long low = *max_element(nums.begin(), nums.end());
		long long high = accumulate(nums.begin(), nums.end(), 0LL);
		long long ans = high;

		while(low <= high)
		{
			long long mid = low + (high - low) / 2;

			if(canSplit(nums, k, mid))
			{
				ans = mid;
				high = mid - 1;
			}
			else
			{
				low = mid + 1;
			}
		}

		return ans;
	}
};
