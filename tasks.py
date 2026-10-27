from z3 import And, BoolRef, Not, Or, Select


def task_1(a, b, c) -> BoolRef:
    """Устраните ∃x: x >= a+2 ∧ x > b-1 ∧ 2x >= 2c+1 ∧ a+c <= b."""
    # x > a+1, x > b-1, x > c + 1
    # ч:= max(a+1, b-1, c+1) + 1 - вот, нашли
    return a + c <= b


def task_2(a, b, c, d) -> BoolRef:
    """Устраните ∃x: a < 2x ∧ b <= x ∧ 2x < c ∧ x <= d."""
    # low: b <= x 2b <= 2x, a < 2x
    # high: 2x < c, x <= d  2x <= 2d
    

    # 2b <= 2x <= 2d => b <= d
    # 2b <= 2x < c => 2b < c
    # a < 2x <= 2d => a < 2d
    # a < 2x < c - чётное число между a,c 
    return And(
        b <= d,
        2 * b < c,
        a < 2 * d,
        Or(c - a > 2, And(c - a == 2, a % 2 == 1)),
    )


def task_3(a, b) -> BoolRef:
    """Устраните ∃x: a <= x ∧ x < b ∧ 2 | (x+1) ∧ 3 | (x-a)."""
    # x >= a, x < b
    # 2 | (x+1) => x нечетное
    # 3 | (x-a) => x = a + 3k
    return Or(
        And(a % 2 == 1, a < b),
        And(a % 2 == 0, a + 3 < b),
    )


def task_4(A, B, i, j) -> BoolRef:
    """Уберите A=B из A=B ∧ A[i]=0 ∧ B[i+1]=1 ∧ B[j]=2."""
    # заменяем A=B на равенства значений по всем индксам
    return And(
        A[i] == B[i],
        A[i + 1] == B[i + 1],
        A[j] == B[j],
        A[i] == 0,
        B[i + 1] == 1,
        B[j] == 2,
    )


def task_5(A, B, C, i, j, k) -> BoolRef:
    """Уберите равенства массивов:

    A=B ∧ B=C ∧ A[i]=0 ∧ C[j]=1 ∧ B[k]=A[j] ∧ C[i+1]=B[i].
    """
    # аналогично
    return And(
        A[i] == B[i],
        B[i] == C[i],
        A[i + 1] == B[i + 1],
        B[i + 1] == C[i + 1],
        A[j] == B[j],
        B[j] == C[j],
        A[k] == B[k],
        B[k] == C[k],
        A[i] == 0,
        C[j] == 1,
        B[k] == A[j],
        C[i + 1] == B[i],
    )


def task_6(A, B, C, D, i, j, w) -> BoolRef:
    """Уберите равенства и неравенства массивов:

    A=B ∧ C=D ∧ A≠C ∧ B≠D ∧ A[i]=0 ∧ C[i]=0 ∧ B[j]=1 ∧ D[j]=1.
    Используйте переданный w как общий индекс-свидетель неравенств.
    """
    # аналогично, но используем w для как бы отличающихся элементов
    return And(
        A[i] == B[i],
        C[i] == D[i],
        A[j] == B[j],
        C[j] == D[j],
        A[w] == B[w],
        C[w] == D[w],
        A[w] != C[w],
        B[w] != D[w],
        A[i] == 0,
        C[i] == 0,
        B[j] == 1,
        D[j] == 1,
    )