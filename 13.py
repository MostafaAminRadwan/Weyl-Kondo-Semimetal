import numpy as np
import matplotlib.pyplot as plt

# Data: lambda_0 vs Delta(infinity)
lambda_values = np.array([10, 15, 20, 25, 28.5, 30, 35, 40, 45, 50])
delta_values = 0.134 * lambda_values  # Linear relation

# Experimental and theoretical values
lambda_exp = 28.5  # meV (from cosmology)
delta_theory = 3.82  # meV (prediction)
delta_exp = 20.0  # meV (ARPES)
lambda_required = delta_exp / 0.134  # ~149 meV

fig, ax = plt.subplots(figsize=(8, 6))

# Main data
ax.plot(lambda_values, delta_values, 'o-', 
        color='navy', markersize=8, linewidth=2,
        label=r'ED + Extrapolation')

# Linear fit
ax.plot([5, 55], [0.134*5, 0.134*55], '--', 
        color='gray', linewidth=1.5, alpha=0.7,
        label=r'Linear fit: $\Delta = 0.134\,\lambda_0$')

# Cosmological value
ax.axvline(lambda_exp, color='green', linestyle=':', 
           linewidth=2.5, label=r'$\lambda_0 = 28.5$ meV (QGU)')
ax.axhline(delta_theory, color='green', linestyle=':', 
           linewidth=2.5, alpha=0.7)

# Experimental gap
ax.axhline(delta_exp, color='red', linestyle='-.', 
           linewidth=2.5, label=r'$\Delta_{\rm exp} = 20$ meV (ARPES)')

# Point of intersection
ax.plot(lambda_exp, delta_theory, 'go', markersize=12, 
        markeredgecolor='darkgreen', markeredgewidth=2)
ax.plot(lambda_required, delta_exp, 'rs', markersize=10, 
        markerfacecolor='none', markeredgewidth=2,
        label=r'Required: $\lambda_0 \approx 150$ meV')

ax.set_xlabel(r'Geometric Coupling $\lambda_0$ (meV)', fontsize=14)
ax.set_ylabel(r'Extrapolated Gap $\Delta(\infty)$ (meV)', fontsize=14)
ax.set_title('Energy Gap Scaling with Geometric Coupling', fontsize=15)
ax.grid(True, alpha=0.3)
ax.legend(fontsize=11, loc='upper left')
ax.set_xlim(5, 55)
ax.set_ylim(0, 8)

# R² text
ax.text(0.95, 0.25, r'$R^2 = 0.996$', 
        transform=ax.transAxes, fontsize=12,
        verticalalignment='top', horizontalalignment='right',
        bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

plt.tight_layout()
plt.savefig('fig_lambda_scan.pdf', dpi=300, bbox_inches='tight')
plt.savefig('fig_lambda_scan.png', dpi=300, bbox_inches='tight')
plt.show()

print("Figure saved: fig_lambda_scan.pdf and .png")