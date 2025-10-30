#include <iostream>
#include <vector>

// функция слияния двух отсортированных массивов
void merge(std::vector<int>& arr, int left, int mid, int right) {
    int n1 = mid - left + 1;
    int n2 = right - mid;

    // создаем временные массивы
    std::vector<int> L(n1), R(n2);
    for (int i = 0; i < n1; i++)
        L[i] = arr[left + i];
    for (int i = 0; i < n2; i++)
        R[i] = arr[mid + 1 + i];

    // сливаем массивы обратно в arr
    int i = 0, j = 0, k = left;
    while (i < n1 && j < n2) {
        if (L[i] <= R[j]) {
            arr[k] = L[i];
            i++;
        } else {
            arr[k] = R[j];
            j++;
        }
        k++;
    }

    // копируем оставшиеся элементы, если есть
    while (i < n1) {
        arr[k] = L[i];
        i++;
        k++;
    }
    while (j < n2) {
        arr[k] = R[j];
        j++;
        k++;
    }
}

// функция сортировки слиянием
void mergeSort(std::vector<int>& arr, int left, int right) {
    if (left < right) {
        int mid = left + (right - left) / 2;

        // сортируем левую и правую части
        mergeSort(arr, left, mid);
        mergeSort(arr, mid + 1, right);

        // сливаем отсортированные половины
        merge(arr, left, mid, right);
    }
}

int main() {
    std::vector<int> array = {38, 27, 43, 3, 9, 82, 10};
    mergeSort(array, 0, array.size() - 1);
    std::cout << "Отсортированный массив: ";
    for (int num : array)
        std::cout << num << ' ';
    return 0;
}