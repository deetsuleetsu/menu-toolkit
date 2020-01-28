from psutil import virtual_memory

mem = virtual_memory().available
ram = mem / 1000000000

mem2 = virtual_memory()
ramtotal = mem2.total / 1000000000
