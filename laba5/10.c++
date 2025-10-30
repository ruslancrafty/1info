#include <iostream>
#include <vector>
using namespace std;

int interpolationSearch(const vector<int>& arr, int target) {
    int low = 0;
    int high = arr.size() - 1;

    while (low <= high && target >= arr[low] && target <= arr[high]) {
        // Предполагаемая позиция
        int pos = low + ((double)(high - low) * (target - arr[low])) / (arr[high] - arr[low]);

        // проверка на выход за границы
        if (pos < low || pos > high)
            break;

        if (arr[pos] == target)
            return pos;  // нашли
        else if (arr[pos] < target)
            low = pos + 1;   // ищем справа
        else
            high = pos - 1;  // ищем слева
    }
    return -1; // не найдено
}

int main() {
    vector<int> array = {10, 22, 35, 40, 50, 80, 82, 85, 90, 100};
    int target = 85;
    int index = interpolationSearch(array, target);
    if (index != -1)
        cout << "Элемент " << target << " найден на позиции: " << index << endl;
    else
        cout << "Элемент не найден" << endl;
    return 0;
}