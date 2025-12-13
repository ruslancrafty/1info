Задание 9: Transfer Learning с предобученной моделью
Задача: использовать предобученную ResNet50 для классификации изображений
растений.
Требования:
Загрузить ResNet50 с весами ImageNet
Заморозить базовые слои
Добавить custom head для 10 классов растений
Fine-tuning с низкой скоростью обучения
Код-заготовка (Python):
import tensorflow as tf
from tensorflow.keras.applications import ResNet50
47
class PlantClassifierTransferLearning:
 def __init__(self, num_classes=10):
 # TODO: Загрузить предобученный ResNet50
 # - include_top=False (для feature extraction)
 # - input_shape=(224, 224, 3)
 # - weights='imagenet'
 self.base_model = None
 self.model = None
 self.num_classes = num_classes

 def freeze_base_model(self):
 # TODO: Заморозить все слои base_model
 # self.base_model.trainable = False
 pass

 def add_custom_head(self):
 # TODO: Добавить custom layers на top of base_model
 # Архитектура custom head:
 # - GlobalAveragePooling2D
 # - Dense(512, activation='relu')
 # - Dropout(0.5)
 # - Dense(256, activation='relu')
 # - Dense(num_classes, activation='softmax')
 pass

 def compile_transfer_learning(self):
 # TODO: Скомпилировать для transfer learning
 # Optimizer: Adam(learning_rate=0.001)
 # Loss: categorical_crossentropy
 pass

 def train_with_frozen_base(self, X_train, y_train, epochs=10):
 # TODO: Обучить только custom head
 # С замороженным base_model
 pass

 def fine_tune(self, num_layers_unfreeze=50):
 # TODO: Разморозить последние num_layers_unfreeze слои
 # self.base_model.trainable = True
 # for layer in self.base_model.layers[:-num_layers_unfreeze]:
 # layer.trainable = False

 # Скомпилировать с низкой скоростью обучения
 # Optimizer: Adam(learning_rate=0.00001)
48
 pass

 def train_fine_tuning(self, X_train, y_train, epochs=20):
 # TODO: Fine-tuning с небольшой скоростью обучения
 pass
# Что нужно дополнить:
# 1. Загрузку ResNet50 с ImageNet весами
# 2. Freeze/unfreeze логику
# 3. Custom head архитектуру
# 4. Две стадии обучения (frozen + fine-tune)
# 5. Сравнение точности от scratch vs transfer learning


Алгоритм работы НС по блокам
Блок 1: Загрузка и подготовка предобученной модели-основы (Backbone)
Цель: Использовать свёрточную сеть, уже обученную на огромном наборе данных (ImageNet), как мощный экстрактор признаков из изображений.

Действия:

Загрузить модель ResNet50 без верхнего классификационного слоя (include_top=False).

Заморозить все её веса (trainable=False), чтобы они не изменялись на первом этапе обучения.

python
# Загрузка предобученной ResNet50 без верхних слоёв
base_model = ResNet50(weights='imagenet', include_top=False, input_shape=(224, 224, 3))
# Заморозка базовых слоёв
base_model.trainable = False
Блок 2: Создание пользовательского классификатора (Custom Head)
Цель: Добавить новые слои, которые научатся интерпретировать извлечённые признаки для решения конкретной задачи (классификации 10 видов растений).

Действия (архитектура head):

Усреднение по картам признаков: GlobalAveragePooling2D() преобразует 3D-тензор в 1D-вектор.

Полносвязный слой с регуляризацией: Dense(512) + Dropout(0.5) для обучения и предотвращения переобучения.

Ещё один полносвязный слой: Dense(256) для дополнительной нелинейности.

Выходной слой: Dense(NUM_CLASSES, activation='softmax') для получения вероятностей по 10 классам.

python
# Добавление custom head
x = base_model.output
x = GlobalAveragePooling2D()(x)
x = Dense(512, activation='relu')(x)
x = Dropout(0.5)(x)
x = Dense(256, activation='relu')(x)
predictions = Dense(NUM_CLASSES, activation='softmax')(x)

model = Model(inputs=base_model.input, outputs=predictions)
Блок 3: Компиляция модели и подготовка данных
Цель: Настроить процесс обучения и подготовить данные.

Действия:

Компиляция: Указать оптимизатор (Adam), функцию потерь и метрику.

Создание синтетических данных: В учебных целях генерируются случайные массивы, имитирующие изображения и метки.

Аугментация данных: Создаётся генератор (ImageDataGenerator) для искусственного увеличения обучающей выборки путём случайных трансформаций.

python
# Компиляция для transfer learning
model.compile(optimizer=Adam(learning_rate=0.001),
              loss='categorical_crossentropy',
              metrics=['accuracy'])

# ... (Генерация синтетических данных и разделение)

# Data augmentation
datagen = ImageDataGenerator(
    rotation_range=20, width_shift_range=0.2,
    height_shift_range=0.2, horizontal_flip=True
)
Блок 4: Этап 1 - Обучение только Custom Head (с замороженной основой)
Цель: Адаптировать только новые, добавленные слои под нашу конкретную задачу, не меняя общие признаки, извлечённые ResNet50.

Действие: Запуск обучения. Градиенты вычисляются и обновляются только для весов слоёв Custom Head.

python
print("\n--- Обучение с замороженными слоями ---")
history_frozen = model.fit(
    datagen.flow(X_train, y_train, batch_size=BATCH_SIZE),
    validation_data=(X_val, y_val),
    epochs=EPOCHS_FROZEN
)
Блок 5: Этап 2 - Разморозка и тонкая настройка (Fine-Tuning)
Цель: Точно подстроить высокоуровневые признаки предобученной модели под нашу задачу для повышения точности.

Действия:

Разморозить часть слоёв основы (здесь — последние 50).

Перекомпилировать модель с очень низкой скоростью обучения, чтобы вносить небольшие, аккуратные изменения в веса ResNet50.

Продолжить обучение уже всей модели (частично размороженная основа + head).

python
# Разморозка последних 50 слоёв для fine-tuning
base_model.trainable = True
for layer in base_model.layers[:-50]:
    layer.trainable = False

# Перекомпиляция с низкой скоростью обучения
model.compile(optimizer=Adam(learning_rate=0.00001),
              loss='categorical_crossentropy',
              metrics=['accuracy'])

# Fine-tuning
print("\n--- Fine-tuning ---")
history_fine = model.fit(...)
Блок 6: Визуализация и вывод результатов
Цель: Оценить процесс и результаты обучения.

Действия:

Построить графики точности (Accuracy) и потерь (Loss) для обоих этапов.

Протестировать модель на примере, чтобы показать итоговый механизм предсказания.

python
# Визуализация метрик (функция plot_history)
# ...

# Пример предсказания
sample_image = np.random.rand(1, 224, 224, 3).astype('float32')
prediction = model.predict(sample_image)
predicted_class = np.argmax(prediction)

<img width="965" height="641" alt="image" src="https://github.com/user-attachments/assets/580426bd-26d3-4a19-9988-0286e610ab91" />
