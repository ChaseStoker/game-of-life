class Settings:
    screen_width = 1000
    screen_height = 1000
    block_size = 10
    rows = screen_height//block_size
    cols = screen_width//block_size

    tick_rate = 10

    sim_ind_loc = (block_size, block_size)
    sim_ind_color = 'green'

    alive_color = 'white'