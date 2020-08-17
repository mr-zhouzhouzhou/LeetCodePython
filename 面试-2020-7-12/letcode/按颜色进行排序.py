


"""

public void sortColors(int[] nums) {
            int zero = -1, one = 0, two = nums.length;
            while (one < two) { if (nums[one] == 0) {
                    swap(nums, ++zero, one++);
                } else if (nums[one] == 2) {
                    swap(nums, --two, one);
                    } else {
                     ++one;
                     } } }
private void swap(int[] nums, int i, int j) { int t = nums[i]; nums[i] = nums[j]; nums[j] = t; }
"""

def f(nums):
    zero = -1
    one = 0
    two = len(nums)
    while one < two:
        if nums[one] == 0:
            zero += 1
            nums[one], nums[zero] = nums[zero], nums[one]
            one += 1
        elif nums[one] == 2:
            two -= 1
            nums[one], nums[two] = nums[two], nums[one]
            if nums[one] == 0:
                zero += 1
                nums[one], nums[zero] = nums[zero], nums[one]
                one += 1
            one += 1
        else:
            one += 1
