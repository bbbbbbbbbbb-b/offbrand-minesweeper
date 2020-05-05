import tkinter as tk
import random
root = tk.Tk()

columns = 20
rows = 20
mineNo = 50


class box():
    def __init__(self,pos,hasMine,ref):
        self.pos = pos
        self.hasMine = hasMine
        self.ref = ref
        self.adjMineCount = 0
        self.revealed = False
        self.marked = False
    

def mineDist(x,y,no):
    output = set()
    while len(output) < no:
        output.add((random.randint(0,x-1),random.randint(0,y-1)))
    return output



    

grid = []

def adj(pos):
    return {(pos[0]-1,pos[1]-1),(pos[0],pos[1]-1),(pos[0]+1,pos[1]-1),(pos[0]-1,pos[1]),(pos[0]+1,pos[1]),(pos[0]-1,pos[1]+1),(pos[0],pos[1]+1),(pos[0]+1,pos[1]+1)}

def click(event):
    global boxRef,grid,columns,rows
    for i in boxRef:
        if event.widget == i[0]:
            clickedBox = i[1]
    if clickedBox.hasMine and not clickedBox.marked:
        event.widget["background"] = "red"
    else:
        reveal(clickedBox)

def mark(event):
    global boxRef,grid,columns,rows
    for i in boxRef:
        if event.widget == i[0]:
            clickedBox = i[1]
    if not clickedBox.revealed:
        if not clickedBox.marked:
            event.widget["background"] = "gray"
            clickedBox.marked = True
        else:
            event.widget["background"] = "light gray"
            clickedBox.marked = False
def reveal(box):
    global boxRef,grid,columns,rows
    if (not box.hasMine) and (not box.marked):
        box.revealed = True
        if box.adjMineCount > 0:
            box.ref.create_text(18,18,font="10",text=str(box.adjMineCount))
        box.ref["background"] = "white"
        if box.adjMineCount == 0:
            for k in adj(box.pos):
                if k[0] < columns and k[1] < rows and not grid[k[1]][k[0]].revealed:
                    reveal(grid[k[1]][k[0]])
                    if grid[k[1]][k[0]].adjMineCount > 0:
                        grid[k[1]][k[0]].ref.create_text(18,18,font="10",text=str(grid[k[1]][k[0]].adjMineCount))
                    grid[k[1]][k[0]].ref["background"] = "white"




if __name__ == "__main__":

    minesPos = mineDist(columns,rows,mineNo)


    for r in range(columns):
        temp = []
        for c in range(rows):
            temp2 = tk.Canvas(root,width=30,height=30,background='light gray',borderwidth=1)
            temp2.grid(row=r,column=c)
            temp2.bind("<Button-1>",click)
            temp2.bind("<Button-3>",mark)
            if (c,r) in minesPos:
                temp.append(box((c,r),True,temp2))
            else:
                temp.append(box((c,r),False,temp2))
        grid.append(temp)


    boxRef = []
    for i in grid:
        for j in i:
            boxRef.append((j.ref,j))
    
    for i in grid:
        for j in i:
            for k in adj(j.pos):
                if k[0] < columns and k[1] < rows:
                    if grid[k[1]][k[0]].hasMine:
                        j.adjMineCount += 1



    root.mainloop()