# Python Standard Library
import sys

# Third-Party
import numpy as np
from scipy.integrate import solve_ivp
import spark
import matplotlib.pyplot as plt
import typer

WEEK = 7
YEAR = 365

N = 100
beta = 1 / (WEEK)
gamma = 1 / (2 * WEEK)
omega = 1 / YEAR

S0, I0 = 99.0, 1.0
R0 = N - S0 - I0
t_span = [0.0, 5 * YEAR]


def dSIR(t, SIR):
    S, I, R = SIR
    dS = omega * R - beta * I * S / N
    dI = beta * I * S / N - gamma * I
    dR = gamma * I - omega * R
    return (dS, dI, dR)




def main(
    sparklines: bool = typer.Option(False, help="Output sparklines"),
    beta: float = typer.Option(beta, help="Contagion rate")):

    globals()["beta"] = beta
    results = solve_ivp(dSIR, t_span=t_span, y0=(S0, I0, R0), dense_output=True)
    sol = results["sol"]
    t = np.arange(0, 1 * YEAR)
    S, I, R = sol(t)

    if sparklines:
        spark.spark_print(I)
    else:
        output = " ".join(f"{v:.2f}" for v in I)
        typer.echo(output)


if __name__ == "__main__":
    typer.run(main)
