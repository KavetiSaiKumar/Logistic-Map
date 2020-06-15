import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

colors =  {
            'lightest':"#eeeeee",
            'lighter':"#e5e5e5",
            'lomid':"#4f98ca",
            'dark' :"#272727",
            'darker' :"#23374d",
            'blue': "#235789",
            'cobweb': "#89BBFE"
            }

def logistic(r, x):
    return r * x * (1 - x)

def plot_update(ax1=None, passed_rate=3.1):

    #Clear the previous drawn plot to remove duplicates
    ax1.cla()
    plt.sca(ax1)
    plot_settings(ax = ax1, growth_rate=passed_rate)

    new_rate = np.linspace(2.5, passed_rate, n)
    new_x = 1e-5 * np.ones(n)

    for i in range(iterations):
        new_x = logistic(new_rate, new_x)

        # We display the bifurcation diagram.
        if i >= (iterations - last):
            ax1.plot(new_rate, new_x, ',k', alpha=0.25, c = colors['lomid'])

def plot_settings(ax =None, growth_rate=2.5):
    ax.set_axisbelow(True)

    # hide all axis spines
    #for spine in ax.spines.values():
    #    spine.set_visible(False)

    # Hide the right and top spines
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)

    plt.setp(ax.spines.values(), color= colors['lighter'])
            
    # hide top and right ticks
    ax.xaxis.tick_bottom()
    ax.yaxis.tick_left()

    # lighten ticks and labels
    ax.tick_params(colors='gray', direction='out')
    for tick in ax.get_xticklabels():
        tick.set_color('white')
    for tick in ax.get_yticklabels():
        tick.set_color('white')

    #plt.grid(color='w', linestyle='solid', linewidth= 0.0)  #Draw solid white grid lines
    plt.title("Bifurcation diagram, growth rate: {:4.2f}".format(growth_rate), color= colors['lighter'], size= 15)
    plt.ylabel("(Equilibrium Population) Xn+1", color= colors['lighter'])
    plt.xlabel("(Rate) r", color= colors['lighter'])

#################start of code ######################
initial_val = 2.5
n = 10000
r = np.linspace(2.5, 3.6, n) #set to stop value to 4.0 to get full plot
iterations = 1000
last = 100

x = 1e-5 * np.ones(n)
#lyapunov = np.zeros(n)

fig, ax = plt.subplots(figsize=(10,6), facecolor=colors['dark']) #Changes plot frame color 
ax.set_facecolor(colors['dark'])           #changes plot back color
plot_settings(ax = ax, growth_rate= 2.5)

for i in range(iterations):
    x = logistic(r, x)

    # We display the bifurcation diagram.
    if i >= (iterations - last):
        ax.plot(r, x, ',k', alpha=0.25, c= colors['lomid'])#, marker= 'o',markerfacecolor='#03CEA4', markersize=1)

ax.set_xlim(2.5, 4)

#code for Slider

axamp = plt.axes([0.25, 0.02, 0.50, 0.02]) #position of slider. values in list are of 4 required positional arguments: 'x0', 'y0', 'width', and 'height'.

samp = Slider(axamp, 'Rate',valmin= 2.5, valmax= 4, valinit=initial_val)

def update(val):
    # amp is the current value of the slider
    cur_growth_rate = samp.val
    
    # update curve by calling update function
    plot_update(passed_rate= cur_growth_rate, ax1= ax) #update the function here

    # redraw canvas while idle
    fig.canvas.draw_idle()

# call update function on slider value change
samp.on_changed(update)

plt.show()









