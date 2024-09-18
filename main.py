import random
import os
import json
from prettytable import PrettyTable
from datetime import datetime

# Sample math questions
questions = [
    {
        "id": 1,
        "question": "What is the value of x in the equation 2x - 3 = 7?",
        "answer": "5",
        "explanation": "Add 3 to both sides to get 2x = 10. Then divide by 2 to find x = 5.",
        "level": "easy"
    },
    {
        "id": 3,
        "question": "What is the area of a triangle with a base of 5 and a height of 8?",
        "answer": "20",
        "explanation": "Use the formula for the area of a triangle: (base * height) / 2. So, (5 * 8) / 2 = 40 / 2 = 20.",
        "level": "easy"
    },
    {
        "id": 4,
        "question": "What is the value of 3^2 - 2 * 4?",
        "answer": "1",
        "explanation": "Calculate 3^2 to get 9. Then 2 * 4 is 8. So, 9 - 8 = 1.",
        "level": "easy"
    },
    {
        "id": 5,
        "question": "If 3x + 4 = 19, what is x?",
        "answer": "5",
        "explanation": "Subtract 4 from both sides to get 3x = 15. Then divide by 3 to find x = 5.",
        "level": "easy"
    },
    {
        "id": 8,
        "question": "What is the value of 4! (4 factorial)?",
        "answer": "24",
        "explanation": "Calculate 4! as 4 * 3 * 2 * 1 = 24.",
        "level": "easy"
    },
    {
        "id": 9,
        "question": "If a rectangle has a length of 10 and a width of 4, what is its perimeter?",
        "answer": "28",
        "explanation": "The perimeter of a rectangle is 2(length + width). So, 2(10 + 4) = 2 * 14 = 28.",
        "level": "easy"
    },
    {
        "id": 12,
        "question": "If a triangle has angles A, B, and C such that A = 30° and B = 45°, what is angle C?",
        "answer": "105",
        "explanation": "The sum of the angles in a triangle is 180°. So, C = 180° - A - B = 180° - 30° - 45° = 105°.",
        "level": "easy"
    },
    {
        "id": 10,
        "question": "If 5x - 2 = 3x + 4, what is x?",
        "answer": "3",
        "explanation": "Subtract 3x from both sides to get 2x - 2 = 4. Add 2 to both sides to get 2x = 6. Then divide by 2 to find x = 3.",
        "level": "medium"
    },
    {
        "id": 6,
        "question": "Solve for x: 2(x - 3) = 8.",
        "answer": "7",
        "explanation": "Distribute the 2 to get 2x - 6 = 8. Add 6 to both sides to get 2x = 14. Then divide by 2 to find x = 7.",
        "level": "medium"
    },
    {
        "id": 7,
        "question": "What is the slope of the line passing through the points (2, 3) and (4, 7)?",
        "answer": "2",
        "explanation": "Use the slope formula: (y2 - y1) / (x2 - x1). Here, (7 - 3) / (4 - 2) = 4 / 2 = 2.",
        "level": "medium"
    },
    {
        "id": 2,
        "question": "If f(x) = 2x^2 - 3x + 4, what is f(2)?",
        "answer": "10",
        "explanation": "Substitute x = 2 into the function: f(2) = 2(2)^2 - 3(2) + 4 = 8 - 6 + 4 = 6.",
        "level": "medium"
    },    
    {
        "id": 11,
        "question": "What is the quadratic formula used to solve ax^2 + bx + c = 0?",
        "answer": "x = (-b ± √(b^2 - 4ac)) / 2a",
        "explanation": "The quadratic formula is used to find the values of x in a quadratic equation. It solves for x by using the coefficients a, b, and c.",
        "level": "hard"
    },
    {
        "id": 13,
        "question": "Simplify: (3x^2 - 4x) - (2x^2 - x).",
        "answer": "x^2 - 3x",
        "explanation": "Distribute the minus sign and combine like terms: 3x^2 - 4x - 2x^2 + x = x^2 - 3x.",
        "level": "medium"
    },
    {
        "id": 15,
        "question": "Find the median of the following set of numbers: 2, 5, 7, 10, 12.",
        "answer": "7",
        "explanation": "To find the median, list the numbers in ascending order and identify the middle number. Here, the middle number is 7.",
        "level": "easy"
    },
    {
        "id": 16,
        "question": "If 2x + 3y = 12 and x = 3, what is y?",
        "answer": "3",
        "explanation": "Substitute x = 3 into the equation: 2(3) + 3y = 12. Simplify to get 6 + 3y = 12. Then, subtract 6 from both sides to get 3y = 6, so y = 2.",
        "level": "medium"
    },
    {
        "id": 17,
        "question": "What is the result of (5^2 + 3) * 2?",
        "answer": "32",
        "explanation": "First calculate 5^2 = 25. Then, 25 + 3 = 28. Finally, 28 * 2 = 56.",
        "level": "medium"
    },
    {
        "id": 18,
        "question": "A circle has a radius of 3. What is its area?",
        "answer": "28.27",
        "explanation": "Use the formula for the area of a circle: π * r^2. So, π * 3^2 = 9π ≈ 28.27.",
        "level": "medium"
    },
    {
        "id": 19,
        "question": "If the probability of an event is 0.25, what are the odds of the event occurring?",
        "answer": "1:3",
        "explanation": "Probability is expressed as a fraction of favorable outcomes over possible outcomes. Here, odds are the ratio of success to failure: 0.25 = 1/4, so odds are 1:3.",
        "level": "hard"
    },
    {
        "id": 20,
        "question": "What is the x-intercept of the line represented by the equation 2x + 3y = 6?",
        "answer": "3",
        "explanation": "To find the x-intercept, set y = 0 in the equation: 2x + 3(0) = 6. Solve for x to get x = 3.",
        "level": "medium"
    },
    {
        "id": 21,
        "question": "Simplify the expression: 4(x - 2) + 3x.",
        "answer": "7x - 8",
        "explanation": "Distribute 4 to get 4x - 8. Add 3x to get 4x - 8 + 3x = 7x - 8.",
        "level": "medium"
    },
    {
        "id": 22,
        "question": "What is the value of log10(100)?",
        "answer": "2",
        "explanation": "log10(100) means finding the power to which 10 must be raised to get 100. 10^2 = 100, so log10(100) = 2.",
        "level": "hard"
    },
    {
        "id": 23,
        "question": "What is the length of the hypotenuse of a right triangle with legs of lengths 3 and 4?",
        "answer": "5",
        "explanation": "Use the Pythagorean theorem: a^2 + b^2 = c^2. Here, 3^2 + 4^2 = 9 + 16 = 25, so c = √25 = 5.",
        "level": "easy"
    },
    {
        "id": 24,
        "question": "What is the sum of the first 5 positive integers?",
        "answer": "15",
        "explanation": "Sum = 1 + 2 + 3 + 4 + 5 = 15.",
        "level": "easy"
    },
    {
        "id": 25,
        "question": "Solve for y in the equation 4y - 7 = 5y + 2.",
        "answer": "-9",
        "explanation": "Subtract 4y from both sides to get -7 = y + 2. Subtract 2 from both sides to get y = -9.",
        "level": "medium"
    },
    {
        "id": 26,
        "question": "Find the value of x in the equation 3x/4 = 9.",
        "answer": "12",
        "explanation": "Multiply both sides by 4 to get 3x = 36. Then divide by 3 to find x = 12.",
        "level": "easy"
    },
    {
        "id": 27,
        "question": "If the sum of two numbers is 20 and their difference is 4, what are the numbers?",
        "answer": "[12, 8]",
        "explanation": "Let the numbers be x and y. Then, x + y = 20 and x - y = 4. Solve these equations to get x = 12 and y = 8.",
        "level": "medium"
    },
    {
        "id": 28,
        "question": "What is the median of the following set: 8, 12, 15, 22, 30, 35?",
        "answer": "18.5",
        "explanation": "List the numbers in ascending order: 8, 12, 15, 22, 30, 35. With an even number of data points, the median is the average of the middle two numbers: (15 + 22) / 2 = 18.5.",
        "level": "medium"
    },
    {
        "id": 29,
        "question": "Calculate the value of 2^(3 + 2).",
        "answer": "32",
        "explanation": "First, solve the exponent: 3 + 2 = 5. Then calculate 2^5 = 32.",
        "level": "easy"
    },
    {
        "id": 30,
        "question": "If a rectangle's length is doubled and width remains the same, how does the area change?",
        "answer": "The area doubles.",
        "explanation": "If the length is doubled, the new area will be twice the original area, assuming the width stays the same.",
        "level": "medium"
    },
    {
        "id": 31,
        "question": "Solve for x in the inequality 2x - 5 > 7.",
        "answer": "6",
        "explanation": "Add 5 to both sides to get 2x > 12. Then divide by 2 to find x > 6.",
        "level": "medium"
    },
    {
        "id": 32,
        "question": "What is the value of the expression (2 + 3)^2 - 4?",
        "answer": "21",
        "explanation": "First calculate (2 + 3)^2 = 5^2 = 25. Then subtract 4 to get 25 - 4 = 21.",
        "level": "easy"
    },
    {
        "id": 33,
        "question": "A car travels 60 miles in 1 hour. How far will it travel in 3.5 hours at the same speed?",
        "answer": "210",
        "explanation": "If the car travels 60 miles in 1 hour, then in 3.5 hours it will travel 60 * 3.5 = 210 miles.",
        "level": "easy"
    },
    {
        "id": 34,
        "question": "Find the y-intercept of the line given by 2x - 5y = 10.",
        "answer": "-2",
        "explanation": "To find the y-intercept, set x = 0 in the equation: 2(0) - 5y = 10. Solving for y gives y = -2.",
        "level": "medium"
    },
    {
        "id": 35,
        "question": "Simplify the expression: (3a + 2b) - (a - b).",
        "answer": "2a + 3b",
        "explanation": "Distribute the negative sign: (3a + 2b) - a + b = 2a + 3b.",
        "level": "medium"
    },
    {
        "id": 36,
        "question": "What is the value of √(81)?",
        "answer": "9",
        "explanation": "√(81) means finding the square root of 81, which is 9.",
        "level": "easy"
    },
    {
        "id": 37,
        "question": "If a number is doubled and then increased by 3, the result is 19. What is the number?",
        "answer": "8",
        "explanation": "Let the number be x. Then 2x + 3 = 19. Subtract 3 to get 2x = 16, then divide by 2 to find x = 8.",
        "level": "medium"
    },
    {
        "id": 38,
        "question": "What is the value of 5 + 6 * (2 - 3)?",
        "answer": "-1",
        "explanation": "First solve inside the parentheses: 2 - 3 = -1. Then multiply 6 * -1 = -6. Finally, 5 + (-6) = -1.",
        "level": "medium"
    },
    {
        "id": 39,
        "question": "If a number is increased by 5 and then divided by 3, the result is 7. What is the number?",
        "answer": "16",
        "explanation": "Let the number be x. Then (x + 5) / 3 = 7. Multiply both sides by 3 to get x + 5 = 21. Subtract 5 to get x = 16.",
        "level": "medium"
    },
    {
        "id": 40,
        "question": "What is the sum of the angles in a hexagon?",
        "answer": "720",
        "explanation": "The sum of the interior angles of a polygon is given by (n - 2) * 180°, where n is the number of sides. For a hexagon, n = 6, so (6 - 2) * 180° = 720°.",
        "level": "medium"
    },
    {
        "id": 41,
        "question": "If 3a + 2b = 12 and a = 2, what is b?",
        "answer": "3",
        "explanation": "Substitute a = 2 into the equation: 3(2) + 2b = 12. Simplify to get 6 + 2b = 12. Then subtract 6 to get 2b = 6, so b = 3.",
        "level": "medium"
    },
    {
        "id": 42,
        "question": "Find the area of a circle with a diameter of 10.",
        "answer": "78.54",
        "explanation": "The radius is half the diameter, so r = 5. The area is π * r^2 = π * 5^2 = 25π ≈ 78.54.",
        "level": "medium"
    },
    {
        "id": 43,
        "question": "What is the solution to the system of equations: x + y = 10 and x - y = 2?",
        "answer": "[6, 4]",
        "explanation": "Add the equations to eliminate y: (x + y) + (x - y) = 10 + 2, so 2x = 12, hence x = 6. Substitute x = 6 into the first equation: 6 + y = 10, so y = 4.",
        "level": "hard"
    },
    {
        "id": 44,
        "question": "Simplify: 2(3x - 4) - 5x.",
        "answer": "x - 8",
        "explanation": "Distribute 2: 2(3x - 4) = 6x - 8. Then subtract 5x to get 6x - 8 - 5x = x - 8.",
        "level": "medium"
    },
    {
        "id": 45,
        "question": "What is the value of (x^2 - 4) / (x - 2) when x = 3?",
        "answer": "5",
        "explanation": "First, factor x^2 - 4 as (x + 2)(x - 2). Then (x^2 - 4) / (x - 2) simplifies to x + 2. Substitute x = 3 to get 3 + 2 = 5.",
        "level": "hard"
    },
    {
        "id": 46,
        "question": "What is the x-value that makes the function f(x) = x^2 - 4x + 3 equal to zero?",
        "answer": "[1, 3]",
        "explanation": "Factor the quadratic function: x^2 - 4x + 3 = (x - 1)(x - 3). So, x = 1 and x = 3.",
        "level": "medium"
    },
    {
        "id": 47,
        "question": "If a polygon has 8 sides, how many diagonals does it have?",
        "answer": "20",
        "explanation": "The number of diagonals in a polygon with n sides is given by n(n - 3) / 2. For an 8-sided polygon, it’s 8(8 - 3) / 2 = 40 / 2 = 20.",
        "level": "hard"
    },
    {
        "id": 48,
        "question": "What is the value of 3x if x = -2?",
        "answer": "-6",
        "explanation": "Substitute x = -2 into 3x: 3(-2) = -6.",
        "level": "easy"
    },
    {
        "id": 49,
        "question": "If the length of one side of a square is 7, what is its area?",
        "answer": "49",
        "explanation": "The area of a square is side^2. So, 7^2 = 49.",
        "level": "easy"
    },
    {
        "id": 50,
        "question": "Solve for x: 5(x - 1) = 3x + 7.",
        "answer": "3",
        "explanation": "Distribute 5: 5x - 5 = 3x + 7. Subtract 3x from both sides: 2x - 5 = 7. Add 5 to both sides: 2x = 12. Divide by 2 to get x = 6.",
        "level": "medium"
    },
    {
        "id": 51,
        "question": "What is the sum of the first 10 positive integers?",
        "answer": 55,
        "explanation": "Sum = 1 + 2 + 3 + ... + 10. Use the formula n(n + 1) / 2, where n = 10. So, 10(11) / 2 = 55.",
        "level": "easy"
    },
    {
        "id": 52,
        "question": "Find the y-intercept of the line 3x - 2y = 6.",
        "answer": "-3",
        "explanation": "Set x = 0 in the equation: 3(0) - 2y = 6. Solve for y: -2y = 6, so y = -3.",
        "level": "medium"
    },
    {
        "id": 53,
        "question": "What is the value of 2^3 * 3^2?",
        "answer": "72",
        "explanation": "Calculate each part: 2^3 = 8 and 3^2 = 9. Then multiply: 8 * 9 = 72.",
        "level": "medium"
    },
    {
        "id": 54,
        "question": "What is the value of the expression 7 - 2 * 3^2?",
        "answer": "-5",
        "explanation": "First calculate 3^2 = 9. Then multiply: 2 * 9 = 18. Finally, 7 - 18 = -11.",
        "level": "medium"
    },
    {
        "id": 55,
        "question": "Solve the inequality 4x - 3 < 9.",
        "answer": 3,
        "explanation": "Add 3 to both sides: 4x < 12. Then divide by 4: x < 3.",
        "level": "medium"
    },
    {
        "id": 56,
        "question": "Find the perimeter of a triangle with side lengths of 6, 8, and 10.",
        "answer": 24,
        "explanation": "Add the side lengths: 6 + 8 + 10 = 24.",
        "level": "easy"
    },
    {
        "id": 57,
        "question": "What is the value of the expression (x + 5)^2 when x = 2?",
        "answer": 49,
        "explanation": "Substitute x = 2 into the expression: (2 + 5)^2 = 7^2 = 49.",
        "level": "medium"
    },
    {
        "id": 58,
        "question": "If the mean of a set of numbers is 8 and there are 5 numbers, what is their total sum?",
        "answer": 40,
        "explanation": "The mean is the total sum divided by the number of values. So, Total sum = Mean * Number of values = 8 * 5 = 40.",
        "level": "easy"
    },
    {
        "id": 59,
        "question": "What is the next number in the sequence: 2, 4, 8, 16, ...?",
        "answer": 32,
        "explanation": "The sequence doubles each time. So, the next number after 16 is 16 * 2 = 32.",
        "level": "easy"
    },
    {
        "id": 60,
        "question": "Solve for x: 2x + 7 = 3x - 4.",
        "answer": 11,
        "explanation": "Subtract 2x from both sides: 7 = x - 4. Then add 4 to both sides to get x = 11.",
        "level": "easy"
    },
    {
        "id": 61,
        "question": "What is the value of 9/3 + 4?",
        "answer": 7,
        "explanation": "First, calculate 9/3 = 3. Then add 4: 3 + 4 = 7.",
        "level": "easy"
    },
    {
        "id": 62,
        "question": "If a triangle has side lengths 7, 24, and 25, is it a right triangle?",
        "answer": "Yes",
        "explanation": "Check using the Pythagorean theorem: 7^2 + 24^2 = 49 + 576 = 625. Since 25^2 = 625, it is a right triangle.",
        "level": "hard"
    },
    {
        "id": 63,
        "question": "What is the value of (4x + 2) / 2 when x = 3?",
        "answer": 7,
        "explanation": "Substitute x = 3: (4(3) + 2) / 2 = (12 + 2) / 2 = 14 / 2 = 7.",
        "level": "easy"
    },
    {
        "id": 64,
        "question": "Find the distance between the points (1, 2) and (4, 6).",
        "answer": 5,
        "explanation": "Use the distance formula: √((x2 - x1)^2 + (y2 - y1)^2). Here, √((4 - 1)^2 + (6 - 2)^2) = √(3^2 + 4^2) = √9 + 16 = √25 = 5.",
        "level": "medium"
    },
    {
        "id": 65,
        "question": "What is the area of a parallelogram with a base of 8 and a height of 5?",
        "answer": 40,
        "explanation": "Use the formula for the area of a parallelogram: base * height. So, 8 * 5 = 40.",
        "level": "easy"
    },
    {
        "id": 66,
        "question": "What is the value of 8 - 2 * (3 + 1)?",
        "answer": 0,
        "explanation": "First solve inside the parentheses: 3 + 1 = 4. Then multiply: 2 * 4 = 8. Finally, 8 - 8 = 0.",
        "level": "easy"
    },
    {
        "id": 67,
        "question": "Find the circumference of a circle with a radius of 7.",
        "answer": 43.98,
        "explanation": "Use the formula for circumference: 2πr. So, 2 * π * 7 ≈ 43.98.",
        "level": "medium"
    },
    {
        "id": 68,
        "question": "What is the value of 3 * (5 + 2) - 4?",
        "answer": 23,
        "explanation": "First solve inside the parentheses: 5 + 2 = 7. Then multiply: 3 * 7 = 21. Finally, 21 - 4 = 23.",
        "level": "easy"
    },
    {
        "id": 69,
        "question": "If a number is decreased by 6 and then tripled, the result is 24. What is the number?",
        "answer": 10,
        "explanation": "Let the number be x. Then 3(x - 6) = 24. Divide both sides by 3 to get x - 6 = 8. Add 6 to both sides to get x = 14.",
        "level": "medium"
    },
    {
        "id": 70,
        "question": "What is the value of 2^4 + 3^2?",
        "answer": 19,
        "explanation": "Calculate each part: 2^4 = 16 and 3^2 = 9. Then add: 16 + 9 = 25.",
        "level": "easy"
    }
]

log_file = 'practice_log.txt'

# ... (keep the questions list as is) ...

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def load_questions(file_path):
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: Question file '{file_path}' not found.")
        return []
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON format in '{file_path}'.")
        return []
     
def print_menu_screen():
    
    while True:
        clear_screen()
    
        print("=" * 80)
        print("Chương Trình Thực Hành Câu Hỏi Trắc Nghiệm - Màn Hình Chính".center(80))
        print("=" * 80)
        print("\n" + "Hãy chọn 1 phương án:")
        print("1. Giải Câu Hỏi")
        print("2. Xem Toàn Bộ Câu Hỏi")
        print("3. Xem Lịch Sử Giải Bài")
        print("4. Thoát Chương Trình")
        print("\n")

        choice = input("Lựa Chọn Của Bạn Là (1-4): ")

        if choice == '1':
            print_practice_screen()
        elif choice == '2':
            print_all_questions_screen()
        elif choice == '3':
            print_practice_log_screen()
        elif choice == '4':
            clear_screen()
            print("\nCác Ơn Bạn Đã Sử Dụng Chương Trình! Chào Tạm Biệt")
            break
        else:
            print("\nLựa Chọn Không Hợp Lệ. Vui Lòng Chọn Lại.")

def print_practice_screen():
    session_log = []
    total_questions = 0
    correct_answers = 0

    for question in questions:      

        total_questions += 1

        clear_screen()
    
        print("=" * 80)
        print("Trả Lời Câu Hỏi".center(80))
        print("=" * 80)

        print()
        print(f"Câu Hỏi {total_questions} / {len(questions)} :")
        print()
        print(question["question"])
        print()
        print("-" * 80)
        user_answer = input("Đáp Án Của Bạn Là: ")
        
        is_correct = False;
        if user_answer == question["answer"]:
            result = "✓ Đúng!"
            correct_answers += 1
            is_correct = True
        else:
            result = f"✗ Sai. \nĐáp Án Là {question['answer']}."
        
        session_log.append({
            'question': question['question'],
            'user_answer': user_answer,
            'correct_answer': question['answer'],
            'is_correct': is_correct
        })
        
        print("\n" + result)
        print("\nGiải Thích:")
        print(question["explanation"])
        print("\n")

        user_input = input("Bạn Có Muốn Tới Câu Hỏi Kế Tiếp? (y/n): ").lower()
        if user_input != 'y' or total_questions >= len(questions):
            if total_questions >= len(questions):
                print(f"\nBạn Đã Trả Lời Hết Tất Cả Câu Hỏi")
            print(f"Điểm Của Bạn Là: {correct_answers}/{total_questions}")
            input("Hãy nhấn ENTER để quay lại màn hình chính...")
            break

    log_practice_session(session_log, correct_answers, total_questions)


def print_all_questions_screen():
    clear_screen()
    
    print("=" * 80)
    print("Danh Sách Câu Hỏi".center(80))
    print("=" * 80)

    table = PrettyTable()
    table.field_names = ["#", "Question"]
    table.align["Question"] = "l"
    
    for question in questions:
        table.add_row([question["id"], question["question"]])
        table.add_row(["", ""])
    
    print(table)
    input("\nHãy nhấn ENTER để quay lại màn hình chính...")

def log_practice_session(session_log, correct_answers, total_questions):
    
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
    with open(log_file, 'a') as file:
        file.write(f"Session started at: {timestamp}\n")
        for entry in session_log:
            file.write(f"Question: {entry['question']}\n")
            file.write(f"User Answer: {entry['user_answer']}\n")
            file.write(f"Correct Answer: {entry['correct_answer']}\n")
            file.write(f"Result: {'Correct' if entry['is_correct'] else 'Incorrect'}\n")
        file.write(f"Total Questions: {total_questions}\n")
        file.write(f"Correct Answers: {correct_answers}\n")
        file.write(f"Accuracy: {correct_answers / total_questions * 100:.2f}%\n")
        file.write("-" * 50 + "\n\n")


def print_practice_log_screen():
    clear_screen()
    
    print("=" * 80)
    print("Math Practice Program - Practice Log".center(80))
    print("=" * 80)

    try:
        with open(log_file, 'r') as file:
            log_entries = file.read().split('-' * 50)
        
        if log_entries:
            for session in log_entries:
                if session.strip():
                    lines = session.strip().split('\n')
                    timestamp = lines[0].split(': ')[1]
                    
                    table = PrettyTable()
                    table.field_names = ["Question", "User Answer", "Correct Answer", "Result"]
                    table.align = "l"  # Left-align all columns
                    
                    for i in range(1, len(lines), 4):
                        if i + 3 < len(lines):
                            question = lines[i].split(': ', 1)[1]
                            user_answer = lines[i+1].split(': ', 1)[1]
                            correct_answer = lines[i+2].split(': ', 1)[1]
                            result = lines[i+3].split(': ', 1)[1]
                            table.add_row([question, user_answer, correct_answer, result])
                    
                    total_questions = lines[len(lines) - 3].split(': ', 1)[1]
                    correct_answers = lines[len(lines) - 2].split(': ', 1)[1]
                    accuracy = lines[len(lines) - 1].split(': ', 1)[1]
                    
                    print(f"\nSession started at: {timestamp}")
                    print(table)
                    print(f"Total Questions: {total_questions}")
                    print(f"Correct Answers: {correct_answers}")
                    print(f"Accuracy: {accuracy}")
                    print("\n" + "-" * 80 + "\n")
        else:
            print("\nNo practice sessions logged yet.")
    except FileNotFoundError:
        print("\nNo practice log found.")

    input("\nPress Enter to return to the main menu...")

if __name__ == "__main__":
    # Load questions at the start of the program
    #questions = load_questions('questions.json')
    if not questions:
        print("No questions found. Exiting program.")
    else:
        print_menu_screen()