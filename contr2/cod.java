java
import java.util.Scanner;

public class ScheduleOptimizer {
    
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        // Ввод данных
        System.out.println("=== Оптимизация расписания задач ===");
        
        // Ввод количества задач
        System.out.print("Введите количество задач (n): ");
        int n = scanner.nextInt();
        
        // Ввод длительностей задач
        int[] durations = new int[n];
        System.out.println("Введите длительности задач:");
        for (int i = 0; i < n; i++) {
            System.out.print("Задача " + (i + 1) + ": ");
            durations[i] = scanner.nextInt();
        }
        
        // Ввод количества машин
        System.out.print("Введите количество машин (m): ");
        int m = scanner.nextInt();
        
        // Ввод максимального числа итераций
        System.out.print("Введите максимальное число итераций: ");
        int maxIter = scanner.nextInt();
        
        scanner.close();
        
        // Запуск алгоритма
        System.out.println("\nЗапуск алгоритма локального поиска...");
        int[] assignment = localSearchSchedule(durations, m, maxIter);
        
        // Вывод результатов
        printResults(durations, m, assignment);
    }
    
    public static int[] localSearchSchedule(int[] durations, int m, int maxIter) {
        int n = durations.length;
        int[] assignment = new int[n]; // машина для каждой задачи
        int[] load = new int[m];
        
        // Инициализация случайного распределения
        for (int i = 0; i < n; i++) {
            assignment[i] = (int) (Math.random() * m);
            load[assignment[i]] += durations[i];
        }
        
        System.out.println("Начальное распределение:");
        printLoadInfo(load);
        
        for (int iter = 0; iter < maxIter; iter++) {
            // Выбираем случайную задачу
            int taskIdx = (int) (Math.random() * n);
            int currentMachine = assignment[taskIdx];
            int taskDuration = durations[taskIdx];
            
            // Вычисляем текущий makespan
            int currentMakespan = getMakespan(load);
            
            // Пробуем переложить задачу на каждую другую машину
            for (int newMachine = 0; newMachine < m; newMachine++) {
                if (newMachine == currentMachine) continue;
                
                // Временно вычисляем новую загрузку
                int[] newLoad = load.clone();
                newLoad[currentMachine] -= taskDuration;
                newLoad[newMachine] += taskDuration;
                
                // Вычисляем новый makespan
                int newMakespan = getMakespan(newLoad);
                
                // Если улучшили makespan, принимаем изменение
                if (newMakespan < currentMakespan) {
                    // Обновляем распределение и загрузку
                    assignment[taskIdx] = newMachine;
                    load[currentMachine] -= taskDuration;
                    load[newMachine] += taskDuration;
                    
                    System.out.println("Итерация " + (iter + 1) + ": " +
                            "Задача " + (taskIdx + 1) + " перенесена с машины " + 
                            (currentMachine + 1) + " на машину " + (newMachine + 1) +
                            " | Makespan: " + currentMakespan + " -> " + newMakespan);
                    break;
                }
            }
        }
        return assignment;
    }
    
    // Вспомогательный метод для вычисления makespan (максимальной загрузки)
    private static int getMakespan(int[] load) {
        int max = 0;
        for (int l : load) {
            if (l > max) max = l;
        }
        return max;
    }
    
    // Метод для вывода информации о загрузке машин
    private static void printLoadInfo(int[] load) {
        for (int i = 0; i < load.length; i++) {
            System.out.println("Машина " + (i + 1) + ": загрузка = " + load[i]);
        }
        System.out.println("Текущий makespan: " + getMakespan(load));
        System.out.println();
    }
    
    // Метод для вывода финальных результатов
    private static void printResults(int[] durations, int m, int[] assignment) {
        int[] finalLoad = new int[m];
        
        System.out.println("\n=== РЕЗУЛЬТАТЫ ===");
        System.out.println("Финальное распределение задач:");
        
        // Собираем информацию о загрузке и выводим распределение
        for (int i = 0; i < assignment.length; i++) {
            finalLoad[assignment[i]] += durations[i];
            System.out.println("Задача " + (i + 1) + " (длительность " + durations[i] + 
                    ") -> Машина " + (assignment[i] + 1));
        }
        
        System.out.println("\nФинальная загрузка машин:");
        for (int i = 0; i < m; i++) {
            System.out.println("Машина " + (i + 1) + ": общая загрузка = " + finalLoad[i]);
        }
        
        System.out.println("\nФинальный makespan: " + getMakespan(finalLoad));
    }
}
