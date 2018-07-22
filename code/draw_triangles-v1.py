import matplotlib.pyplot as plt

fig, ax = plt.subplots()

ax.set_xlabel('x')
ax.set_ylabel('y')

patch = plt.Polygon([
    (0.2, 0.2),
    (0.2, 0.6),
    (0.4, 0.4)
])

ax.add_patch(patch)

ax.text(0.2, 0.4, '(0.2, 0.4)')
ax.text(0.2, 0.6, '(0.2, 0.6)')
ax.text(0.2, 0.4, '(0.2, 0.4)')

patch = plt.Polygon([
    (0.6, 0.8),
    (0.8, 0.8),
    (0.5, 0.5)
])

ax.add_patch(patch)

ax.text(0.6, 0.8, '(0.6, 0.8)')
ax.text(0.8, 0.8, '(0.8, 0.8)')
ax.text(0.5, 0.5, '(0.5, 0.5)')

patch = plt.Polygon([
    (0.6, 0.1),
    (0.7, 0.3),
    (0.9, 0.2)
])

ax.add_patch(patch)

ax.text(0.6, 0.1, '(0.6, 0.1)')
ax.text(0.7, 0.3, '(0.7, 0.3)')
ax.text(0.9, 0.2, '(0.9, 0.2)')

plt.show()
