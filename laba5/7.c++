#include <iostream>
#include <vector>

// функция позиций для heapify
void heapify(std::vector<int>& arr, int n, int i) {
    int largest = i;           // корень
    int left = 2 * i + 1;      // левый ребёнок
    int right = 2 * i + 2;     // правый ребёнок

    // если левый ребёнок больше корня
    if (left < n && arr[left] > arr[largest])
        largest = left;

    // если правый ребёнок больше текущего максимума
    if (right < n && arr[right] > arr[largest])
        largest = right;

    // если есть необходимость — меняем местами и рекурсивно heapify поддерево
    if (largest != i) {
        std::swap(arr[i], arr[largest]);
        heapify(arr, n, largest);
    }
}

void heapSort(std::vector<int>& arr) {
    int n = arr.size();

    // Построение max-heap
    for (int i = n / 2 - 1; i >= 0; --i)
        heapify(arr, n, i);

    // извлекаем элементы один за другим
    for (int i = n - 1; i > 0; --i) {
        // переносим корень в конец массива
        std::swap(arr[0], arr[i]);
        // вызываем heapify для уменьшенного массива
        heapify(arr, i, 0);
    }
}

int main() {
    std::vector<int> array = {12, 11, 13, 5, 6, 7};
    heapSort(array);
    std::cout << "Отсортированный массив: ";
    for (int num : array) {
        std::cout << num << " ";
    }
    return 0;
}