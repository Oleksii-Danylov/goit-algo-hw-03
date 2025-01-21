#!/usr/bin/python3
'''
Завдання 2:
1. Код виконується. Програма візуалізує фрактал «сніжинка Коха».
2. Користувач має можливість вказати рівень рекурсії.
'''
import turtle

def koch_curve(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        size /= 3
        koch_curve(t, order - 1, size)
        t.left(60)
        koch_curve(t, order - 1, size)
        t.right(120)
        koch_curve(t, order - 1, size)
        t.left(60)
        koch_curve(t, order - 1, size)

def draw_snowflake(order, size):
    window = turtle.Screen()
    window.title("Сніжинка Коха")
    window.bgcolor("white")
    
    # Створення об'єкта
    t = turtle.Turtle()
    t.speed(0)  # Швидкість малювання
    t.penup()
    t.goto(-size / 2, size / 3)  # Встановлення початкової позиції
    t.pendown()
    
    # Малювання трьох сторін сніжинки
    for _ in range(3):
        koch_curve(t, order, size)
        t.right(120)
    
    window.mainloop()


try:
    order = int(input("Введіть рівень рекурсії : "))
    if order < 0:
        raise ValueError("Вкажіть невід'ємне число.")
except ValueError as e:
    print(f"Помилка вводу: {e}. рівень за замовчуванням: 3.")
    order = 3

# Довжина сторони
size = 250

draw_snowflake(order, size)
