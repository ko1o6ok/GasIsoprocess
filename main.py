import matplotlib.pyplot as plt
plt.style.use('ggplot')
R_CONST = 9.81
scale= 1.05
def draw_graphs(P,V,mole):
    T = []
    for p,v in zip(P,V):
        T.append(p*v/(mole*R_CONST))
    fig2, axs = plt.subplots(nrows=1, ncols=2)
    ax = axs[0]

    ax.quiver(T[:n - 1], P[:n - 1], [T[i + 1] - T[i] for i in range(n - 1)], [P[i + 1] - P[i] for i in range(n - 1)],
              angles='xy', scale_units='xy', scale=1, color='#E24A33')

    ax.set_xlim([min(T) / scale, max(T) * scale])
    ax.set_ylim([min(P) / scale, max(P) * scale])
    ax.set_title('P от T')
    ax.set_xlabel('T')
    ax.set_ylabel('P')
    ax = axs[1]

    ax.quiver(T[:n - 1], V[:n - 1], [T[i + 1] - T[i] for i in range(n - 1)], [V[i + 1] - V[i] for i in range(n - 1)],
              angles='xy', scale_units='xy', scale=1, color='#E24A33')

    ax.set_xlim([min(T) / scale, max(T) * scale])
    ax.set_ylim([min(V) / scale, max(V) * scale])
    ax.set_title('V от T')
    ax.set_xlabel('T')
    ax.set_ylabel('V')
    fig2.suptitle('Полученные зависимости',y=0.997)
    plt.tight_layout()
    plt.show()
mole = float(input("Введите количество вещества газа: "))
n = int(input("Введите количество точек: "))
P = []
V = []
for i in range(n):
    print("Точка {}".format(i+1))
    V.append(float(input("V: ")))
    P.append(float(input("P: ")))
plt.figure()
ax = plt.gca()
ax.quiver(V[:n-1],P[:n-1],[V[i+1] - V[i] for i in range(n-1)],[P[i+1] - P[i] for i in range(n-1)],
          angles='xy', scale_units='xy', scale=1,color='#E24A33')
ax.set_xlim([min(V)/scale,max(V)*scale])
ax.set_ylim([min(P)/scale,max(P)*scale])
plt.xlabel('V')
plt.ylabel('P')
plt.title('Введенная зависимость')
plt.show()
draw_graphs(P,V,mole)

