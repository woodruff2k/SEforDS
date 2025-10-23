import matplotlib.pyplot as plt


def plot_big_o(save_path):
    n = np.linspace(1, 10, 1000)
    line_names = ["Constant", "Linear", "Quadratic", "Exponential", "Logarithmic"]
    big_o = [np.ones(n.shape), n, n**2, 2**n, np.log(n)]

    fig, ax = plt.subplots()
    fig.set_facecolor("white")

    ax.set_lim(0, 50)
    for i in range(len(big_o)):
        ax.plot(n, big_o[i], label=line_names[i])
    ax.set_ylabel("Relative Runtime")
    ax.set_xlabel("Input Size")
    ax.legend()

    fig.savefig(save_path, bbox_inches="tight")
