import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
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

def plot_system(rate, x0, n, t, ax1=None):
    
    #Clear the previous drawn plot to remove duplicates
    ax1.cla()
    plt.sca(ax1)
    ax1.plot(t, logistic(rate, t), lw=2, color='#235789')#, marker= 'o', markerfacecolor='#03CEA4', markersize=10)
    plot_updates(ax1=ax1, growth_rate= rate)

    # Recursively apply y=f(x) and plot two lines: (x, x) -> (x, y) & (x, y) -> (y, y)
    x = x0

    for i in range(n):
        y = logistic(rate, x)
        # Plot the two lines.
        ax1.plot([x, x], [x, y], 'k', lw=1, color= colors['cobweb'])
        ax1.plot([x, y], [y, y], 'k', lw=1, color= colors['cobweb']) 
    
        # Plot the positions with increasing opacity.
        ax1.plot([x], [y], 'ok', alpha=(i + 1) / n,  marker= 'o', markerfacecolor='#BFD7EA', markersize=6)
        x = y



def plot_updates(ax1=None, growth_rate=2.5):
    ax.plot([0, 1], [0, 1], 'k', lw=1, color= colors['lighter'])                #Tangent line
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
    plt.title("Population vs Time, growth rate: {:4.2f}".format(growth_rate), color= colors['lighter'], size= 15)
    plt.ylabel("(Population Next)Xn+1", color= colors['lighter'])
    plt.xlabel("(Population)Xn", color= colors['lighter'])


############ start of code ############### 

sample_size = 1
growth_rate = 2.5
initial_amp = 1.0
time = np.linspace(0, 1)
n = 30

fig, ax = plt.subplots(figsize=(10,6), facecolor=colors['dark'])                #Changes plot frame color 
ax.set_facecolor(colors['dark'])                                                #changes plot back color
ax.plot(time, logistic(growth_rate, time), lw=2, color= colors['blue'])
plot_updates(ax1=ax, growth_rate= growth_rate)

x = 0.1

for i in range(n):
    y = logistic(growth_rate, x)
    # Plot the two tracking lines.
    ax.plot([x, x], [x, y], 'k', lw=1, color= colors['cobweb'])
    ax.plot([x, y], [y, y], 'k', lw=1, color= colors['cobweb'])

# Plot the positions with increasing opacity.
    ax.plot([x], [y], 'ok', alpha=(i + 1) / n,  marker= 'o', markerfacecolor='#BFD7EA', markersize=6)
    x = y

plt.axis([0,1,0,1]) # list contains xmin, xmax, ymin, ymax
axamp = plt.axes([0.25, 0.02, 0.50, 0.02]) #position of slider. values in list are of 4 required positional arguments: 'x0', 'y0', 'width', and 'height'.

# Slider
samp = Slider(axamp, 'Rate',valmin= 0, valmax= 3.99, valinit=initial_amp)


def update(val):
    # amp is the current value of the slider
    cur_growth_rate = samp.val
    
    # update curve by calling update function
    plot_system(rate= cur_growth_rate, x0= 0.1, n= 40, t=time, ax1= ax) #update the function here

    # redraw canvas while idle
    fig.canvas.draw_idle()

# call update function on slider value change
samp.on_changed(update)

plt.show()
