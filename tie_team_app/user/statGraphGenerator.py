# Libraries
import matplotlib.pyplot as plt
import pandas as pd
from math import pi
 


def statgraphGenerate(username,ability=[],interest=[]):
        # Set data
        df = pd.DataFrame({
        'group': ['Current Self-evaluated Ability'],
        'Mesh_ip': [ability[0]],
        'Mesh': [ability[1]],
        'Gas': [ability[2]],
        'Water': [ability[3]],
        'DA': [ability[4]],
        'PLX':[ability[5]],
        'SQL':[ability[6]]
        })

        # Set data
        interest = pd.DataFrame({
        'group': ['Interest'],
        'Mesh_ip': [interest[0]],
        'Mesh': [interest[1]],
        'Gas': [interest[2]],
        'Water': [interest[3]],
        'DA': [interest[4]],
        'PLX':[interest[5]],
        'SQL':[interest[6]]
        })
        
        
        
        # ------- PART 1: Create background
        
        # number of variable
        categories=list(df)[1:]
        N = len(categories)
        
        # What will be the angle of each axis in the plot? (we divide the plot / number of variable)
        angles = [n / float(N) * 2 * pi for n in range(N)]
        angles += angles[:1]
        
        # Initialise the spider plot
        ax = plt.subplot(111, polar=True)
        
        # If you want the first axis to be on top:
        ax.set_theta_offset(pi / 2)
        ax.set_theta_direction(-1)
        
        # Draw one axe per variable + add labels labels yet
        plt.xticks(angles[:-1], categories,fontsize =15)
        
        # Draw ylabels
        ax.set_rlabel_position(0)
        plt.yticks([20,40,60,80], ["20","40","60","80"], color="grey", size=7)
        plt.ylim(0,100)
        
        
        # # ------- PART 2: Add plots
        
        # # Plot each individual = each line of the data
        # # I don't do a loop, because plotting more than 3 groups makes the chart unreadable
        
        # Ind1
        values=df.loc[0].drop('group').values.flatten().tolist()
        values += values[:1]
        ax.plot(angles, values, linewidth=1, linestyle='solid', label="Current Ability")
        ax.fill(angles, values, 'b', alpha=0.1)
        
        # # Ind2
        values=interest.loc[0].drop('group').values.flatten().tolist()
        values += values[:1]
        ax.plot(angles, values, linewidth=1, linestyle='solid', label="Interest")
        ax.fill(angles, values, 'r', alpha=0.1)
        
        # Add legend
        plt.legend( bbox_to_anchor=(1.3, 0.1))
        # plt.show()
        savedir='static/graph/'+username+'_stat.svg'
        plt.savefig(savedir,bbox_inches = 'tight',
            pad_inches = 0)