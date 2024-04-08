#include <iostream>
#include <iostream>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <chrono>
#include <vector>

void bubbleSort(std::vector<int>& arr);
bool checkVectorSorted(const std::vector<int>& arr);
bool checkArraySorted(const int arr[], int size);


int main() {
    //Seed generation for rand
    srand(time(nullptr));

    //Size of array and vector
    int n = 1;

    //Instantiates an array of size n with numbers up to 1000000
    int array[n];
    for (int i = 0; i < n; i++) {
        array[i] = rand() % 1000000;
    }
    //Calculates start and end time for the array sort
    auto start = std::chrono::steady_clock::now();
    std::sort(array, array + n);
    auto end = std::chrono::steady_clock::now();
    std::chrono::duration<double> DiffInSeconds = end - start;
    std::cout << "The time for the array sorting is: " << DiffInSeconds.count() << std::endl;

    //Instantiates a vector of size n with numbers up to 1000000
    std::vector<int> vector;
    for (int i = 0; i < n; i++) {
        vector.push_back(rand() % 1000000);
    }
    //Calculates start and end time for the vector bubble sort
    start = std::chrono::steady_clock::now();
    bubbleSort(vector);
    end = std::chrono::steady_clock::now();
    DiffInSeconds = end - start;
    std::cout << "The time for the vector sorting is: " << DiffInSeconds.count() << std::endl;

    std::cout << "Array Sorted: " << checkArraySorted(array,n) << std::endl;
    std::cout << "Vector Sorted: " << checkVectorSorted(vector) << std::endl;

    return 0;
}

//Bubble sort method of array
void bubbleSort(std::vector<int>& arr) {
    int n = arr.size();
    bool swapped;
    for (int i=0; i<n-1; i++) {
        swapped = false;
        for (int j=0; j<n-i-1; j++) {
            if (arr[j] > arr[j+1]) {
                int temp = arr[j];
                arr[j] = arr[j+1];
                arr[j+1] = temp;
                swapped = true;
            }
        }
        if (!swapped)
            break;
    }
}

//Methods to check if the output is properly sorted
bool checkVectorSorted(const std::vector<int>& arr) {
    for (int i=1; i<arr.size(); ++i) {
        if (arr[i] < arr[i-1]) {
            return false;
        }
    }
    return true;
}

bool checkArraySorted(const int arr[], int size) {
    for (int i = 1; i < size; ++i) {
        if (arr[i] < arr[i-1]) {
            return false;
        }
    }
    return true;
}