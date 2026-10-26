from z3 import And, BoolRef, Not, Or, Select


def task_1(a, b, c) -> BoolRef:
    """Устраните ∃x: x >= a+2 ∧ x > b-1 ∧ 2x >= 2c+1 ∧ a+c <= b."""
    raise NotImplementedError()


def task_2(a, b, c, d) -> BoolRef:
    """Устраните ∃x: a < 2x ∧ b <= x ∧ 2x < c ∧ x <= d."""
    raise NotImplementedError()


def task_3(a, b) -> BoolRef:
    """Устраните ∃x: a <= x ∧ x < b ∧ 2 | (x+1) ∧ 3 | (x-a)."""
    raise NotImplementedError()


def task_4(A, B, i, j) -> BoolRef:
    """Уберите A=B из A=B ∧ A[i]=0 ∧ B[i+1]=1 ∧ B[j]=2."""
    raise NotImplementedError()


def task_5(A, B, C, i, j, k) -> BoolRef:
    """Уберите равенства массивов:

    A=B ∧ B=C ∧ A[i]=0 ∧ C[j]=1 ∧ B[k]=A[j] ∧ C[i+1]=B[i].
    """
    raise NotImplementedError()


def task_6(A, B, C, D, i, j, w) -> BoolRef:
    """Уберите равенства и неравенства массивов:

    A=B ∧ C=D ∧ A≠C ∧ B≠D ∧ A[i]=0 ∧ C[i]=0 ∧ B[j]=1 ∧ D[j]=1.
    Используйте переданный w как общий индекс-свидетель неравенств.
    """
    raise NotImplementedError()
