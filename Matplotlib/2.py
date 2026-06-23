import matplotlib.pyplot as plt

# x=[1,2,3,4]
x=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
y=[10,20,15,25,32,23,45]

plt.plot(x,y,color='red',linestyle='-',linewidth=1,marker='o',label='2025 sales data')

# plt.plot(x,y,color='red',linestyle='-',linewidth=1,marker='marker',label='label_name')
# plt.title("Bakery Products sell in a week!")
# plt.xlabel('Days')
# plt.ylabel('Cakes Sold')
plt.legend()
# plt.legend(loc='upper left/lower right',fontsize=12)
# plt.grid()
plt.grid(color='gray',linestyle=':',linewidth=1)
# plt.xlim(1,4)
# plt.ylim(10,40)
plt.xticks([1,2,3,4,5,6,7],['D1','D2','D3','D4','D5','D6','D7'])
plt.show()
