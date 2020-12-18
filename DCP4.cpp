// This problem was asked by Stripe.

// Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

// For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

// You can modify the input array in-place.
// C++ program for the above approach 

#include <iostream>

using namespace std;
 
// Function for finding the first missing positive number
 
int firstMissingPositive(int arr[], int n)
{
    int ptr = 0;
 
    for (int i = 0; i < n; i++) {
        if (arr[i] == 1) {
            ptr = 1;
            break;
        }
    }
 
    if (ptr == 0)
        return 1;

    for (int i = 0; i < n; i++)
        if (arr[i] <= 0 || arr[i] > n)
            arr[i] = 1;
 

    for (int i = 0; i < n; i++)
        arr[(arr[i] - 1) % n] += n;
 

    for (int i = 0; i < n; i++)
        if (arr[i] <= n)
            return i + 1;
 

    return n + 1;
}
 

int main()
{
    int arr[] = {3,4,-1,1};
    int n = sizeof(arr) / sizeof(arr[0]);
 
    int ans = firstMissingPositive(arr, n);
 
    cout << ans;
 
    return 0;
}