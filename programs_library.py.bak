"""programs_library.py - 40 programs, each in Python AND C.
Used by main.py:
    import programs_library as pl
    hit = pl.find("prime number program in c")
    # hit = {"text": ..., "files": [(path, code), ...]} or None
Add your own: copy a P(...) entry at the bottom of PROGRAMS.
"""
import os
import re
from textwrap import dedent

ORDINALS = {"first", "second", "third", "fourth", "fifth", "sixth",
            "seventh", "eighth", "ninth", "tenth"}


def P(title, keywords, py, c):
    return {"title": title, "kws": keywords,
            "py": dedent(py).strip("\n"), "c": dedent(c).strip("\n")}


PROGRAMS = [
    P("Hello World", ["hello world", "hello world program", "print hello"],
      r"""
        print('Hello, world!')
      """,
      r"""
        #include <stdio.h>
        int main(void) {
            printf("Hello, world!\n");
            return 0;
        }
      """),

    P("Add two numbers",
      ["add two numbers", "sum of two numbers", "add numbers",
       "addition of two numbers"],
      r"""
        a = float(input('First number: '))
        b = float(input('Second number: '))
        print('Sum =', a + b)
      """,
      r"""
        #include <stdio.h>
        int main(void) {
            float a, b;
            printf("First number: ");
            scanf("%f", &a);
            printf("Second number: ");
            scanf("%f", &b);
            printf("Sum = %.2f\n", a + b);
            return 0;
        }
      """),

    P("Simple calculator", ["calculator", "simple calculator"],
      r"""
        a = float(input('First: '))
        op = input('Operator (+ - * /): ')
        b = float(input('Second: '))
        if op == '+':
            print(a + b)
        elif op == '-':
            print(a - b)
        elif op == '*':
            print(a * b)
        elif op == '/':
            print(a / b if b else 'Cannot divide by 0')
        else:
            print('Unknown operator')
      """,
      r"""
        #include <stdio.h>
        int main(void) {
            float a, b;
            char op;
            printf("Enter: number op number\n");
            scanf("%f %c %f", &a, &op, &b);
            switch (op) {
                case '+': printf("%.2f\n", a + b); break;
                case '-': printf("%.2f\n", a - b); break;
                case '*': printf("%.2f\n", a * b); break;
                case '/':
                    if (b == 0) printf("Cannot divide by 0\n");
                    else printf("%.2f\n", a / b);
                    break;
                default: printf("Unknown operator\n");
            }
            return 0;
        }
      """),

    P("Even or odd", ["even or odd", "even odd", "odd even", "odd or even"],
      r"""
        n = int(input('Number: '))
        if n % 2 == 0:
            print('Even')
        else:
            print('Odd')
      """,
      r"""
        #include <stdio.h>
        int main(void) {
            int n;
            printf("Number: ");
            scanf("%d", &n);
            if (n % 2 == 0) printf("Even\n");
            else printf("Odd\n");
            return 0;
        }
      """),

    P("Largest of three numbers",
      ["largest of three", "biggest of three", "maximum of three",
       "greatest of three", "largest three"],
      r"""
        a = int(input('First: '))
        b = int(input('Second: '))
        c = int(input('Third: '))
        print('Largest =', max(a, b, c))
      """,
      r"""
        #include <stdio.h>
        int main(void) {
            int a, b, c, m;
            printf("Enter three numbers: ");
            scanf("%d %d %d", &a, &b, &c);
            m = a;
            if (b > m) m = b;
            if (c > m) m = c;
            printf("Largest = %d\n", m);
            return 0;
        }
      """),

    P("Swap two numbers", ["swap", "swap two numbers", "interchange"],
      r"""
        a = int(input('a: '))
        b = int(input('b: '))
        a, b = b, a
        print('a =', a, 'b =', b)
      """,
      r"""
        #include <stdio.h>
        int main(void) {
            int a, b, t;
            printf("Enter a and b: ");
            scanf("%d %d", &a, &b);
            t = a;
            a = b;
            b = t;
            printf("a = %d, b = %d\n", a, b);
            return 0;
        }
      """),

    P("Factorial", ["factorial"],
      r"""
        n = int(input('Number: '))
        f = 1
        for i in range(2, n + 1):
            f *= i
        print(n, '! =', f)
      """,
      r"""
        #include <stdio.h>
        int main(void) {
            int n;
            unsigned long long f = 1;  // up to 20!
            printf("Number: ");
            scanf("%d", &n);
            for (int i = 2; i <= n; i++)
                f *= i;
            printf("%d! = %llu\n", n, f);
            return 0;
        }
      """),

    P("Fibonacci series", ["fibonacci", "fibonacci series"],
      r"""
        n = int(input('How many terms: '))
        a, b = 0, 1
        for _ in range(n):
            print(a, end=' ')
            a, b = b, a + b
        print()
      """,
      r"""
        #include <stdio.h>
        int main(void) {
            int n, a = 0, b = 1, next;
            printf("How many terms: ");
            scanf("%d", &n);
            for (int i = 0; i < n; i++) {
                printf("%d ", a);
                next = a + b;
                a = b;
                b = next;
            }
            printf("\n");
            return 0;
        }
      """),

    P("Prime number check",
      ["prime", "prime number", "prime check", "check prime"],
      r"""
        n = int(input('Number: '))
        prime = n > 1
        i = 2
        while i * i <= n:
            if n % i == 0:
                prime = False
                break
            i += 1
        print('Prime' if prime else 'Not prime')
      """,
      r"""
        #include <stdio.h>
        int main(void) {
            int n, prime = 1;
            printf("Number: ");
            scanf("%d", &n);
            if (n < 2) prime = 0;
            for (int i = 2; i * i <= n; i++) {
                if (n % i == 0) {
                    prime = 0;
                    break;
                }
            }
            printf(prime ? "Prime\n" : "Not prime\n");
            return 0;
        }
      """),

    P("Prime numbers in a range",
      ["prime number in range", "prime in range", "prime range",
       "list prime", "prime series"],
      r"""
        lo = int(input('From: '))
        hi = int(input('To: '))
        for n in range(max(lo, 2), hi + 1):
            if all(n % i for i in range(2, int(n ** 0.5) + 1)):
                print(n, end=' ')
        print()
      """,
      r"""
        #include <stdio.h>
        int main(void) {
            int lo, hi;
            printf("From and to: ");
            scanf("%d %d", &lo, &hi);
            for (int n = (lo < 2 ? 2 : lo); n <= hi; n++) {
                int prime = 1;
                for (int i = 2; i * i <= n; i++)
                    if (n % i == 0) { prime = 0; break; }
                if (prime) printf("%d ", n);
            }
            printf("\n");
            return 0;
        }
      """),

    P("Palindrome check",
      ["palindrome", "palindrome string", "palindrome check"],
      r"""
        w = input('Word: ').lower()
        if w == w[::-1]:
            print('Palindrome')
        else:
            print('Not a palindrome')
      """,
      r"""
        #include <stdio.h>
        #include <string.h>
        int main(void) {
            char w[100];
            printf("Word (lowercase): ");
            scanf("%99s", w);
            int n = strlen(w), ok = 1;
            for (int i = 0; i < n / 2; i++)
                if (w[i] != w[n - 1 - i]) ok = 0;
            printf(ok ? "Palindrome\n" : "Not a palindrome\n");
            return 0;
        }
      """),

    P("Reverse a number",
      ["reverse number", "reverse digits", "reverse integer"],
      r"""
        n = int(input('Number: '))
        rev = 0
        while n > 0:
            rev = rev * 10 + n % 10
            n //= 10
        print('Reversed =', rev)
      """,
      r"""
        #include <stdio.h>
        int main(void) {
            int n, rev = 0;
            printf("Number: ");
            scanf("%d", &n);
            while (n > 0) {
                rev = rev * 10 + n % 10;
                n /= 10;
            }
            printf("Reversed = %d\n", rev);
            return 0;
        }
      """),

    P("Reverse a string",
      ["reverse string", "reverse word", "reverse text"],
      r"""
        s = input('Text: ')
        print(s[::-1])
      """,
      r"""
        #include <stdio.h>
        #include <string.h>
        int main(void) {
            char s[100];
            printf("Word: ");
            scanf("%99s", s);
            for (int i = strlen(s) - 1; i >= 0; i--)
                putchar(s[i]);
            printf("\n");
            return 0;
        }
      """),

    P("Armstrong number", ["armstrong"],
      r"""
        n = int(input('Number: '))
        d = str(n)
        total = sum(int(x) ** len(d) for x in d)
        print('Armstrong' if total == n else 'Not Armstrong')
      """,
      r"""
        // compile: clang file.c -o out -lm
        #include <stdio.h>
        #include <math.h>
        int main(void) {
            int n, t, d = 0, sum = 0;
            printf("Number: ");
            scanf("%d", &n);
            for (t = n; t > 0; t /= 10) d++;
            for (t = n; t > 0; t /= 10)
                sum += (int)(pow(t % 10, d) + 0.5);
            printf(sum == n ? "Armstrong\n" : "Not Armstrong\n");
            return 0;
        }
      """),

    P("Sum of digits", ["sum of digits", "digit sum", "digits sum"],
      r"""
        n = int(input('Number: '))
        s = 0
        while n > 0:
            s += n % 10
            n //= 10
        print('Sum of digits =', s)
      """,
      r"""
        #include <stdio.h>
        int main(void) {
            int n, s = 0;
            printf("Number: ");
            scanf("%d", &n);
            while (n > 0) {
                s += n % 10;
                n /= 10;
            }
            printf("Sum of digits = %d\n", s);
            return 0;
        }
      """),

    P("Multiplication table",
      ["multiplication table", "table of", "times table", "print table"],
      r"""
        n = int(input('Table of: '))
        for i in range(1, 11):
            print(n, 'x', i, '=', n * i)
      """,
      r"""
        #include <stdio.h>
        int main(void) {
            int n;
            printf("Table of: ");
            scanf("%d", &n);
            for (int i = 1; i <= 10; i++)
                printf("%d x %d = %d\n", n, i, n * i);
            return 0;
        }
      """),

    P("Leap year", ["leap year", "leap"],
      r"""
        y = int(input('Year: '))
        if (y % 4 == 0 and y % 100 != 0) or y % 400 == 0:
            print('Leap year')
        else:
            print('Not a leap year')
      """,
      r"""
        #include <stdio.h>
        int main(void) {
            int y;
            printf("Year: ");
            scanf("%d", &y);
            if ((y % 4 == 0 && y % 100 != 0) || y % 400 == 0)
                printf("Leap year\n");
            else
                printf("Not a leap year\n");
            return 0;
        }
      """),

    P("Count vowels", ["count vowels", "vowels", "vowel count"],
      r"""
        s = input('Text: ').lower()
        count = sum(1 for ch in s if ch in 'aeiou')
        print('Vowels =', count)
      """,
      r"""
        #include <stdio.h>
        #include <ctype.h>
        int main(void) {
            char s[200];
            int count = 0;
            printf("Text: ");
            fgets(s, sizeof s, stdin);
            for (int i = 0; s[i]; i++) {
                char ch = tolower(s[i]);
                if (ch == 'a' || ch == 'e' || ch == 'i' ||
                    ch == 'o' || ch == 'u')
                    count++;
            }
            printf("Vowels = %d\n", count);
            return 0;
        }
      """),

    P("Simple interest", ["simple interest", "interest"],
      r"""
        p = float(input('Principal: '))
        r = float(input('Rate % per year: '))
        t = float(input('Years: '))
        print('Simple interest =', p * r * t / 100)
      """,
      r"""
        #include <stdio.h>
        int main(void) {
            float p, r, t;
            printf("Principal, rate %%, years: ");
            scanf("%f %f %f", &p, &r, &t);
            printf("Simple interest = %.2f\n", p * r * t / 100);
            return 0;
        }
      """),

    P("Area of a circle", ["area of circle", "circle area", "area circle"],
      r"""
        import math
        r = float(input('Radius: '))
        print('Area =', round(math.pi * r * r, 2))
      """,
      r"""
        #include <stdio.h>
        int main(void) {
            float r;
            const float pi = 3.14159265f;
            printf("Radius: ");
            scanf("%f", &r);
            printf("Area = %.2f\n", pi * r * r);
            return 0;
        }
      """),

    P("Celsius to Fahrenheit",
      ["celsius to fahrenheit", "temperature conversion", "celsius",
       "fahrenheit"],
      r"""
        c = float(input('Celsius: '))
        print('Fahrenheit =', c * 9 / 5 + 32)
      """,
      r"""
        #include <stdio.h>
        int main(void) {
            float c;
            printf("Celsius: ");
            scanf("%f", &c);
            printf("Fahrenheit = %.1f\n", c * 9 / 5 + 32);
            return 0;
        }
      """),

    P("Grade checker",
      ["grade checker", "grade calculator", "marks grade", "grade"],
      r"""
        marks = float(input('Marks (0-100): '))
        if marks >= 90:
            grade = 'A'
        elif marks >= 75:
            grade = 'B'
        elif marks >= 60:
            grade = 'C'
        elif marks >= 40:
            grade = 'D'
        else:
            grade = 'F'
        print('Grade:', grade)
      """,
      r"""
        #include <stdio.h>
        int main(void) {
            float marks;
            char grade;
            printf("Marks (0-100): ");
            scanf("%f", &marks);
            if (marks >= 90) grade = 'A';
            else if (marks >= 75) grade = 'B';
            else if (marks >= 60) grade = 'C';
            else if (marks >= 40) grade = 'D';
            else grade = 'F';
            printf("Grade: %c\n", grade);
            return 0;
        }
      """),

    P("GCD and LCM", ["gcd", "lcm", "hcf", "gcd and lcm"],
      r"""
        import math
        a = int(input('First: '))
        b = int(input('Second: '))
        g = math.gcd(a, b)
        print('GCD =', g, 'LCM =', a * b // g)
      """,
      r"""
        #include <stdio.h>
        int main(void) {
            int a, b, x, y;
            printf("Two numbers: ");
            scanf("%d %d", &a, &b);
            x = a;
            y = b;
            while (y != 0) {
                int t = y;
                y = x % y;
                x = t;
            }
            printf("GCD = %d, LCM = %d\n", x, a / x * b);
            return 0;
        }
      """),

    P("Power of a number",
      ["power of a number", "power of number", "exponent", "power"],
      r"""
        base = float(input('Base: '))
        exp = int(input('Exponent: '))
        print(base ** exp)
      """,
      r"""
        #include <stdio.h>
        int main(void) {
            double base, result = 1;
            int exp;
            printf("Base and exponent (>= 0): ");
            scanf("%lf %d", &base, &exp);
            for (int i = 0; i < exp; i++)
                result *= base;
            printf("Result = %g\n", result);
            return 0;
        }
      """),

    P("Sum of natural numbers",
      ["sum of natural numbers", "natural numbers", "sum of n numbers",
       "sum 1 to n"],
      r"""
        n = int(input('n: '))
        total = 0
        for i in range(1, n + 1):
            total += i
        print('Sum =', total)
      """,
      r"""
        #include <stdio.h>
        int main(void) {
            int n;
            long total = 0;
            printf("n: ");
            scanf("%d", &n);
            for (int i = 1; i <= n; i++)
                total += i;
            printf("Sum = %ld\n", total);
            return 0;
        }
      """),

    P("Largest number in an array",
      ["largest in array", "largest element", "max in array",
       "largest number in list", "largest array", "largest list"],
      r"""
        nums = list(map(int, input('Numbers: ').split()))
        print('Largest =', max(nums))
      """,
      r"""
        #include <stdio.h>
        int main(void) {
            int n, a[100];  // up to 100 numbers
            printf("How many: ");
            scanf("%d", &n);
            printf("Enter %d numbers: ", n);
            for (int i = 0; i < n; i++)
                scanf("%d", &a[i]);
            int max = a[0];
            for (int i = 1; i < n; i++)
                if (a[i] > max) max = a[i];
            printf("Largest = %d\n", max);
            return 0;
        }
      """),

    P("Sum and average of an array",
      ["sum and average", "array sum", "average of array", "average",
       "sum of array", "sum of list"],
      r"""
        nums = list(map(int, input('Numbers: ').split()))
        print('Sum =', sum(nums))
        print('Average =', sum(nums) / len(nums))
      """,
      r"""
        #include <stdio.h>
        int main(void) {
            int n, a[100], sum = 0;  // up to 100
            printf("How many: ");
            scanf("%d", &n);
            printf("Enter %d numbers: ", n);
            for (int i = 0; i < n; i++) {
                scanf("%d", &a[i]);
                sum += a[i];
            }
            printf("Sum = %d\n", sum);
            printf("Average = %.2f\n", (float)sum / n);
            return 0;
        }
      """),

    P("Bubble sort",
      ["bubble sort", "sort array", "sorting program", "sort numbers",
       "sort list", "sorting"],
      r"""
        a = list(map(int, input('Numbers: ').split()))
        n = len(a)
        for i in range(n):
            for j in range(n - i - 1):
                if a[j] > a[j + 1]:
                    a[j], a[j + 1] = a[j + 1], a[j]
        print('Sorted:', a)
      """,
      r"""
        #include <stdio.h>
        int main(void) {
            int n, a[100];  // up to 100
            printf("How many: ");
            scanf("%d", &n);
            printf("Enter %d numbers: ", n);
            for (int i = 0; i < n; i++)
                scanf("%d", &a[i]);
            for (int i = 0; i < n - 1; i++)
                for (int j = 0; j < n - i - 1; j++)
                    if (a[j] > a[j + 1]) {
                        int t = a[j];
                        a[j] = a[j + 1];
                        a[j + 1] = t;
                    }
            printf("Sorted: ");
            for (int i = 0; i < n; i++)
                printf("%d ", a[i]);
            printf("\n");
            return 0;
        }
      """),

    P("Linear search", ["linear search", "search array", "search element"],
      r"""
        a = list(map(int, input('Numbers: ').split()))
        x = int(input('Find: '))
        if x in a:
            print('Found at index', a.index(x))
        else:
            print('Not found')
      """,
      r"""
        #include <stdio.h>
        int main(void) {
            int n, x, a[100], pos = -1;
            printf("How many: ");
            scanf("%d", &n);
            printf("Enter %d numbers: ", n);
            for (int i = 0; i < n; i++)
                scanf("%d", &a[i]);
            printf("Find: ");
            scanf("%d", &x);
            for (int i = 0; i < n; i++)
                if (a[i] == x) { pos = i; break; }
            if (pos >= 0) printf("Found at index %d\n", pos);
            else printf("Not found\n");
            return 0;
        }
      """),

    P("Binary search", ["binary search"],
      r"""
        a = sorted(map(int, input('Numbers: ').split()))
        x = int(input('Find: '))
        lo, hi, pos = 0, len(a) - 1, -1
        while lo <= hi:
            mid = (lo + hi) // 2
            if a[mid] == x:
                pos = mid
                break
            elif a[mid] < x:
                lo = mid + 1
            else:
                hi = mid - 1
        if pos >= 0:
            print('Found at index', pos)
        else:
            print('Not found')
      """,
      r"""
        #include <stdio.h>
        int main(void) {
            int n, x, a[100], lo, hi, pos = -1;
            printf("How many: ");
            scanf("%d", &n);
            printf("Enter %d SORTED numbers: ", n);
            for (int i = 0; i < n; i++)
                scanf("%d", &a[i]);
            printf("Find: ");
            scanf("%d", &x);
            lo = 0;
            hi = n - 1;
            while (lo <= hi) {
                int mid = (lo + hi) / 2;
                if (a[mid] == x) { pos = mid; break; }
                else if (a[mid] < x) lo = mid + 1;
                else hi = mid - 1;
            }
            if (pos >= 0) printf("Found at index %d\n", pos);
            else printf("Not found\n");
            return 0;
        }
      """),

    P("Matrix addition (2x2)",
      ["matrix addition", "add matrices", "matrix sum", "matrix"],
      r"""
        def read(name):
            print('Matrix', name, '- 2 rows of 2 numbers')
            return [list(map(int, input().split()))
                    for _ in range(2)]

        a = read('A')
        b = read('B')
        for i in range(2):
            print([a[i][j] + b[i][j] for j in range(2)])
      """,
      r"""
        #include <stdio.h>
        int main(void) {
            int a[2][2], b[2][2];
            printf("Matrix A (4 numbers): ");
            for (int i = 0; i < 2; i++)
                for (int j = 0; j < 2; j++)
                    scanf("%d", &a[i][j]);
            printf("Matrix B (4 numbers): ");
            for (int i = 0; i < 2; i++)
                for (int j = 0; j < 2; j++)
                    scanf("%d", &b[i][j]);
            printf("Sum:\n");
            for (int i = 0; i < 2; i++) {
                for (int j = 0; j < 2; j++)
                    printf("%d ", a[i][j] + b[i][j]);
                printf("\n");
            }
            return 0;
        }
      """),

    P("Star triangle pattern",
      ["star triangle", "triangle pattern", "star pattern",
       "right triangle", "triangle", "pattern"],
      r"""
        n = int(input('Rows: '))
        for i in range(1, n + 1):
            print('*' * i)
      """,
      r"""
        #include <stdio.h>
        int main(void) {
            int n;
            printf("Rows: ");
            scanf("%d", &n);
            for (int i = 1; i <= n; i++) {
                for (int j = 0; j < i; j++)
                    printf("*");
                printf("\n");
            }
            return 0;
        }
      """),

    P("Pyramid pattern", ["pyramid", "pyramid pattern", "star pyramid"],
      r"""
        n = int(input('Rows: '))
        for i in range(1, n + 1):
            print(' ' * (n - i) + '*' * (2 * i - 1))
      """,
      r"""
        #include <stdio.h>
        int main(void) {
            int n;
            printf("Rows: ");
            scanf("%d", &n);
            for (int i = 1; i <= n; i++) {
                for (int s = 0; s < n - i; s++)
                    printf(" ");
                for (int k = 0; k < 2 * i - 1; k++)
                    printf("*");
                printf("\n");
            }
            return 0;
        }
      """),

    P("Number guessing game",
      ["guessing game", "guess game", "number guessing",
       "guess the number"],
      r"""
        import random
        secret = random.randint(1, 20)
        while True:
            g = int(input('Guess 1-20: '))
            if g < secret:
                print('Higher')
            elif g > secret:
                print('Lower')
            else:
                print('Correct!')
                break
      """,
      r"""
        #include <stdio.h>
        #include <stdlib.h>
        #include <time.h>
        int main(void) {
            srand(time(NULL));
            int secret = rand() % 20 + 1, guess;
            do {
                printf("Guess 1-20: ");
                if (scanf("%d", &guess) != 1) return 1;
                if (guess < secret) printf("Higher\n");
                else if (guess > secret) printf("Lower\n");
            } while (guess != secret);
            printf("Correct!\n");
            return 0;
        }
      """),

    P("ASCII value of a character",
      ["ascii", "ascii value", "character code"],
      r"""
        ch = input('Character: ')[0]
        print('ASCII value =', ord(ch))
      """,
      r"""
        #include <stdio.h>
        int main(void) {
            char ch;
            printf("Character: ");
            scanf(" %c", &ch);
            printf("ASCII value = %d\n", ch);
            return 0;
        }
      """),

    P("Decimal to binary",
      ["decimal to binary", "binary conversion", "convert to binary"],
      r"""
        n = int(input('Decimal number: '))
        print('Binary =', bin(n)[2:])
      """,
      r"""
        #include <stdio.h>
        int main(void) {
            int n, bits[32], i = 0;
            printf("Decimal number: ");
            scanf("%d", &n);
            if (n == 0) bits[i++] = 0;
            while (n > 0) {
                bits[i++] = n % 2;
                n /= 2;
            }
            printf("Binary = ");
            while (i > 0)
                printf("%d", bits[--i]);
            printf("\n");
            return 0;
        }
      """),

    P("File write and read",
      ["file handling", "file write", "file read", "read file",
       "write file", "file program"],
      r"""
        with open('notes.txt', 'w') as f:
            f.write('Hello file\n')
        with open('notes.txt') as f:
            print(f.read())
      """,
      r"""
        #include <stdio.h>
        int main(void) {
            char line[100];
            FILE *f = fopen("notes.txt", "w");
            if (!f) return 1;
            fprintf(f, "Hello file\n");
            fclose(f);
            f = fopen("notes.txt", "r");
            if (!f) return 1;
            while (fgets(line, sizeof line, f))
                printf("%s", line);
            fclose(f);
            return 0;
        }
      """),

    P("Student record (class / struct)",
      ["student record", "student structure", "struct", "structure",
       "student class", "class example"],
      r"""
        class Student:
            def __init__(self, name, marks):
                self.name = name
                self.marks = marks

            def show(self):
                print(self.name, 'scored', self.marks)

        name = input('Name: ')
        marks = int(input('Marks: '))
        Student(name, marks).show()
      """,
      r"""
        #include <stdio.h>
        struct Student {
            char name[50];
            int marks;
        };
        int main(void) {
            struct Student s;
            printf("Name: ");
            scanf("%49s", s.name);
            printf("Marks: ");
            scanf("%d", &s.marks);
            printf("%s scored %d\n", s.name, s.marks);
            return 0;
        }
      """),

    P("Password strength checker",
      ["password strength", "password checker", "check password strength",
       "password strength checker"],
      r"""
        import getpass
        pw = getpass.getpass('Password: ')
        score = 0
        if len(pw) >= 12:
            score += 1
        if any(c.isdigit() for c in pw):
            score += 1
        if any(c.isupper() for c in pw):
            score += 1
        if any(c.islower() for c in pw):
            score += 1
        if any(not c.isalnum() for c in pw):
            score += 1
        print('Strength:', score, '/ 5')
      """,
      r"""
        #include <stdio.h>
        #include <string.h>
        #include <ctype.h>
        int main(void) {
            char pw[100];
            int up = 0, low = 0, dig = 0, sym = 0;
            printf("Password: ");  // visible in C
            scanf("%99s", pw);
            for (int i = 0; pw[i]; i++) {
                if (isupper(pw[i])) up = 1;
                else if (islower(pw[i])) low = 1;
                else if (isdigit(pw[i])) dig = 1;
                else sym = 1;
            }
            int score = up + low + dig + sym;
            if (strlen(pw) >= 12) score++;
            printf("Strength: %d / 5\n", score);
            return 0;
        }
      """),

    P("Caesar cipher (encrypt)",
      ["caesar cipher", "caesar", "shift cipher", "cipher"],
      r"""
        text = input('Text: ')
        shift = int(input('Shift: '))
        out = ''
        for ch in text:
            if ch.isalpha():
                base = ord('A') if ch.isupper() else ord('a')
                out += chr((ord(ch) - base + shift) % 26 + base)
            else:
                out += ch
        print(out)
      """,
      r"""
        #include <stdio.h>
        #include <ctype.h>
        int main(void) {
            char text[200];
            int shift;
            printf("Text: ");
            fgets(text, sizeof text, stdin);
            printf("Shift: ");
            scanf("%d", &shift);
            for (int i = 0; text[i]; i++) {
                char ch = text[i];
                if (isalpha(ch)) {
                    char base = isupper(ch) ? 'A' : 'a';
                    ch = (ch - base + shift % 26 + 26) % 26 + base;
                }
                putchar(ch);
            }
            return 0;
        }
      """),
]


# ----------------------------------------------------------- helpers
def _norm(text):
    """Lowercase words with a light plural strip (primes -> prime)."""
    words = re.findall(r"[a-z0-9]+", text.lower())
    return [w[:-1] if len(w) > 3 and w.endswith("s")
            and not w.endswith("ss") else w for w in words]


def _slug(title):
    return re.sub(r"[^a-z0-9]+", "_", title.lower()).strip("_")


def _indent(code):
    return "\n".join("  " + ln if ln else ln for ln in code.split("\n"))


def _files_for(i, langs):
    p = PROGRAMS[i]
    out = []
    for lang in langs:
        code = p["py"] if lang == "python" else p["c"]
        ext = "py" if lang == "python" else "c"
        out.append((f"{lang}/{i + 1:02d}_{_slug(p['title'])}.{ext}", code))
    return out


def _listing(langs):
    lines = []
    for lang in langs:
        label = "Python" if lang == "python" else "C"
        lines.append(f"{label} programs ({len(PROGRAMS)}):")
        for i, p in enumerate(PROGRAMS, 1):
            lines.append(f"{i}. {p['title']}")
        lines.append("")
    lines.append("Ask like: prime number in c / python factorial / "
                 "c program 7")
    lines.append("Type 'save all' to create every program as files "
                 "in the programs folder.")
    return "\n".join(lines)


def _render(i, langs, default_lang):
    p = PROGRAMS[i]
    parts = []
    for lang in langs:
        label = "Python" if lang == "python" else "C"
        code = p["py"] if lang == "python" else p["c"]
        parts.append(f"{i + 1}. {p['title']} ({label})")
        parts.append(_indent(code))
        parts.append("")
    if default_lang:
        parts.append("Add 'in c' to get the C version.")
    parts.append("Type 'save' to store it as a file.")
    return {"text": "\n".join(parts), "files": _files_for(i, langs)}


# -------------------------------------------------------------- API
def find(question):
    """Return {'text', 'files'} for a program request, else None."""
    words = _norm(question)
    wset = set(words)
    if wset & ORDINALS:                 # 'first code' etc. handled elsewhere
        return None
    wants_c = "c" in wset
    wants_py = "python" in wset or "py" in wset
    if wants_c and wants_py:
        langs = ["python", "c"]
    elif wants_c:
        langs = ["c"]
    else:
        langs = ["python"]
    default_lang = not (wants_c or wants_py)

    best, best_score = None, 0
    for i, p in enumerate(PROGRAMS):
        for kw in p["kws"]:
            k = _norm(kw)
            if k and all(w in wset for w in k) and len(k) > best_score:
                best, best_score = i, len(k)

    if best is None:
        has_prog = "program" in wset
        nums = [int(w) for w in words if w.isdigit()]
        if has_prog and nums and 1 <= nums[0] <= len(PROGRAMS):
            best = nums[0] - 1
        elif has_prog and (wants_c or wants_py):
            return {"text": _listing(langs), "files": []}
        else:
            return None
    return _render(best, langs, default_lang)


def save_files(files, base="programs"):
    paths = []
    for rel, code in files:
        path = os.path.join(base, rel)
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w") as f:
            f.write(code + "\n")
        paths.append(path)
    return paths


def save_all(base="programs"):
    files = []
    for i in range(len(PROGRAMS)):
        files += _files_for(i, ["python", "c"])
    return len(save_files(files, base))


if __name__ == "__main__":
    while True:
        q = input("\nAsk: ").strip()
        if q in ("quit", "exit"):
            break
        hit = find(q)
        print(hit["text"] if hit else "No program found.")
