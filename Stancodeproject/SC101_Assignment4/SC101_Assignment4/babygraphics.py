"""
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.

YOUR DESCRIPTION HERE
"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index of the current year in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                              with the specified year.
    """
    x_cor = GRAPH_MARGIN_SIZE+year_index*((width-2*GRAPH_MARGIN_SIZE)/len(YEARS))
    return x_cor


def draw_fixed_lines(canvas):
    """
    Erases all existing information on the given canvas and then
    draws the fixed background lines on it.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.

    Returns:
        This function does not return any value.
    """
    canvas.delete('all')  # delete all existing lines from the canvas

    # Write your code below this line
    #################################
    # First, we draw the two lines on the top and the bottom of the canvas
    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, CANVAS_WIDTH-GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE)
    canvas.create_line(GRAPH_MARGIN_SIZE, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, CANVAS_WIDTH-GRAPH_MARGIN_SIZE,
                       CANVAS_HEIGHT-GRAPH_MARGIN_SIZE)
    # Second, we draw several lines to split the canvas coordinate to each year.
    for i in range(len(YEARS)):
        x = get_x_coordinate(CANVAS_WIDTH, i)
        canvas.create_line(x, 0, x, CANVAS_HEIGHT)
        canvas.create_text(x+TEXT_DX, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, text=str(YEARS[i]), anchor=tkinter.NW)


def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)  # draw the fixed background grid
    # Write your code below this line
    #################################
    for name in lookup_names:
        if name in name_data:
            data = name_data[name]  # data is a list containing year, rank of a name.
            # Next, we put all the missing year,rank as '1000.005'
            if '1900' not in data:
                data['1900'] = '1000.0005'
            if '1910' not in data:
                data['1910'] = '1000.0005'
            if '1920' not in data:
                data['1920'] = '1000.0005'
            if '1930' not in data:
                data['1930'] = '1000.0005'
            if '1940' not in data:
                data['1940'] = '1000.0005'
            if '1950' not in data:
                data['1950'] = '1000.0005'
            if '1960' not in data:
                data['1960'] = '1000.0005'
            if '1970' not in data:
                data['1970'] = '1000.0005'
            if '1980' not in data:
                data['1980'] = '1000.0005'
            if '1990' not in data:
                data['1990'] = '1000.0005'
            if '2000' not in data:
                data['2000'] = '1000.0005'
            if '2010' not in data:
                data['2010'] = '1000.0005'
            for key, value in data.items():
                if len(lookup_names) > 4:  # 這個if/else condition 是為了控制顏色
                    index = lookup_names.index(name) % 4
                else:
                    index = lookup_names.index(name)
                if key != '2010':
                    n_key = int(key)
                    n_key1 = n_key+10
                    j = 0
                    for y in YEARS:  # 這個迴圈是為了確認n_key在YEARS中的index位置
                        if n_key == y:
                            break
                        else:
                            j += 1
                    value1 = data[str(n_key1)]
                    x0 = get_x_coordinate(CANVAS_WIDTH, j)
                    # I use float(value) because if the rank is out of 1000, then I give them 1000.0005
                    y0 = GRAPH_MARGIN_SIZE+(((CANVAS_HEIGHT-2*GRAPH_MARGIN_SIZE)/1000)*float(value))
                    x1 = get_x_coordinate(CANVAS_WIDTH, j+1)
                    y1 = GRAPH_MARGIN_SIZE+(((CANVAS_HEIGHT-2*GRAPH_MARGIN_SIZE)/1000)*float(value1))
                    if float(value) > 1000:  # when value == 1000.0005, the text will be '*'
                        canvas.create_text(x0, y0, text=name+' '+'*', anchor=tkinter.SW, fill=COLORS[index])
                        canvas.create_line(x0, y0, x1, y1, width=LINE_WIDTH, fill=COLORS[index])
                    else:
                        canvas.create_text(x0, y0, text=name+' '+value, anchor=tkinter.SW, fill=COLORS[index])
                        canvas.create_line(x0, y0, x1, y1, width=LINE_WIDTH, fill=COLORS[index])
                elif key == '2010':
                    # Don't forget to plus the text of '2010:rank'
                    value_2010 = data['2010']
                    x = get_x_coordinate(CANVAS_WIDTH, 11)
                    y = GRAPH_MARGIN_SIZE + (((CANVAS_HEIGHT-2*GRAPH_MARGIN_SIZE)/1000)*float(value_2010))
                    if float(value) > 1000:
                        canvas.create_text(x, y, text=name+' '+'*', fill=COLORS[index], anchor=tkinter.SW)
                    else:
                        canvas.create_text(x, y, text=name+' '+value_2010, fill=COLORS[index], anchor=tkinter.SW)


# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
