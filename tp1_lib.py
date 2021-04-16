import numpy as np


def Uinit(X, J):
    return (-1 / 4 <= X) * (X <= 1 / 4) * 256 * ((X - 1 / 4) ** 2) * ((X + 1 / 4) ** 2)


def schema1(U0, J, alpha):
    U1 = np.empty(J)
    U1[0] = U0[0] - alpha * (U0[0] - U0[J - 1])
    U1[1:J] = U0[1:J] - alpha * (U0[1:J] - U0[0 : J - 1])
    return U1


def schema2(U0, J, alpha):
    U1 = np.empty(J)
    U1[0] = (
        U0[0]
        - alpha / 2 * (U0[1] - U0[J - 1])
        + (alpha ** 2) / 2 * (U0[1] - 2 * U0[0] + U0[J - 1])
    )
    U1[1 : J - 1] = (
        U0[1 : J - 1]
        - alpha / 2 * (U0[2:J] - U0[0 : J - 2])
        + (alpha ** 2) / 2 * (U0[2:J] - 2 * U0[1 : J - 1] + U0[0 : J - 2])
    )
    U1[J - 1] = (
        U0[J - 1]
        - alpha / 2 * (U0[0] - U0[J - 2])
        + (alpha ** 2) / 2 * (U0[0] - 2 * U0[J - 1] + U0[J - 2])
    )
    return U1


def schema3(U0, J, alpha):
    U1 = np.empty(J)
    U1[0] = (
        U0[0]
        - alpha * (U0[0] - U0[J - 1])
        - alpha * (1 - alpha) / 4 * (U0[1] - U0[0] - U0[J - 1] + U0[J - 2])
    )
    U1[1] = (
        U0[1]
        - alpha * (U0[1] - U0[0])
        - alpha * (1 - alpha) / 4 * (U0[2] - U0[1] - U0[0] + U0[J - 1])
    )
    U1[2 : J - 1] = (
        U0[2 : J - 1]
        - alpha * (U0[2 : J - 1] - U0[1 : J - 2])
        - alpha
        * (1 - alpha)
        / 4
        * (U0[3:J] - U0[2 : J - 1] - U0[1 : J - 2] + U0[0 : J - 3])
    )
    U1[J - 1] = (
        U0[J - 1]
        - alpha * (U0[J - 1] - U0[J - 2])
        - alpha * (1 - alpha) / 4 * (U0[0] - U0[J - 1] - U0[J - 2] + U0[J - 3])
    )
    return U1
