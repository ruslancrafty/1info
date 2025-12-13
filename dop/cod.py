import numpy as np
import tensorflow as tf
from tensorflow.keras.applications import ResNet50
from tensorflow.keras.layers import Dense, GlobalAveragePooling2D, Dropout
from tensorflow.keras.models import Model
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import matplotlib.pyplot as plt

# Константы
IMG_SIZE = (224, 224)
BATCH_SIZE = 32
NUM_CLASSES = 10
EPOCHS_FROZEN = 10
EPOCHS_FINE_TUNE = 20

# Загрузка предобученной ResNet50 без верхних слоёв
base_model = ResNet50(weights='imagenet', include_top=False, input_shape=(224, 224, 3))

# Заморозка базовых слоёв
base_model.trainable = False

# Добавление custom head
x = base_model.output
x = GlobalAveragePooling2D()(x)
x = Dense(512, activation='relu')(x)
x = Dropout(0.5)(x)
x = Dense(256, activation='relu')(x)
predictions = Dense(NUM_CLASSES, activation='softmax')(x)

model = Model(inputs=base_model.input, outputs=predictions)

# Компиляция для transfer learning
model.compile(optimizer=Adam(learning_rate=0.001),
              loss='categorical_crossentropy',
              metrics=['accuracy'])

# Вывод структуры модели
model.summary()

# Генерация синтетических данных (для примера, вместо реальных изображений растений)
# В реальном задании нужно загрузить реальный датасет
num_samples = 1000
train_images = np.random.rand(num_samples, 224, 224, 3).astype('float32')
train_labels = np.random.randint(0, NUM_CLASSES, size=(num_samples,))
train_labels = tf.keras.utils.to_categorical(train_labels, NUM_CLASSES)

# Разделение на обучающую и валидационную выборки
split = int(0.8 * num_samples)
X_train, X_val = train_images[:split], train_images[split:]
y_train, y_val = train_labels[:split], train_labels[split:]

# Data augmentation
datagen = ImageDataGenerator(
    rotation_range=20,
    width_shift_range=0.2,
    height_shift_range=0.2,
    horizontal_flip=True
)

# Обучение с замороженной базой
print("\n--- Обучение с замороженными слоями ---")
history_frozen = model.fit(
    datagen.flow(X_train, y_train, batch_size=BATCH_SIZE),
    validation_data=(X_val, y_val),
    epochs=EPOCHS_FROZEN
)

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
history_fine = model.fit(
    datagen.flow(X_train, y_train, batch_size=BATCH_SIZE),
    validation_data=(X_val, y_val),
    epochs=EPOCHS_FINE_TUNE
)

# Визуализация метрик
def plot_history(history_frozen, history_fine):
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    
    # Accuracy
    axes[0, 0].plot(history_frozen.history['accuracy'], label='Train (frozen)')
    axes[0, 0].plot(history_frozen.history['val_accuracy'], label='Val (frozen)')
    axes[0, 0].set_title('Accuracy (Frozen Base)')
    axes[0, 0].legend()
    
    axes[0, 1].plot(history_fine.history['accuracy'], label='Train (fine-tune)')
    axes[0, 1].plot(history_fine.history['val_accuracy'], label='Val (fine-tune)')
    axes[0, 1].set_title('Accuracy (Fine-tuning)')
    axes[0, 1].legend()
    
    # Loss
    axes[1, 0].plot(history_frozen.history['loss'], label='Train (frozen)')
    axes[1, 0].plot(history_frozen.history['val_loss'], label='Val (frozen)')
    axes[1, 0].set_title('Loss (Frozen Base)')
    axes[1, 0].legend()
    
    axes[1, 1].plot(history_fine.history['loss'], label='Train (fine-tune)')
    axes[1, 1].plot(history_fine.history['val_loss'], label='Val (fine-tune)')
    axes[1, 1].set_title('Loss (Fine-tuning)')
    axes[1, 1].legend()
    
    plt.tight_layout()
    plt.show()

plot_history(history_frozen, history_fine)

# Пример предсказания
print("\n--- Пример предсказания ---")
sample_image = np.random.rand(1, 224, 224, 3).astype('float32')
prediction = model.predict(sample_image)
predicted_class = np.argmax(prediction)
print(f"Предсказанный класс: {predicted_class}, Вероятности: {prediction[0]}")
