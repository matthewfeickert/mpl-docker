axd = plt.figure(constrained_layout=True).subplot_mosaic(
  [["Top", "Top", "Edge"],
   ["Left", ".",  "Edge"]]
)
for k, ax in axd.items():
    ax.text(0.5, 0.5, k,
            ha='center', va='center', fontsize=36,
            color='darkgrey')