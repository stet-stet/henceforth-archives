import os
import sys
import shutil

def move(source_folder,range_source,range_target):
    if len(range_source) != len(range_target):
        raise ZeroDivisionError
    for i,j in zip(range_source,range_target):
        wherefrom = source_folder + '/' + '{0:05d}.png'.format(i)
        whereto = "!assembly/{0:05d}.png".format(j)
        shutil.copy(wherefrom,whereto)

if __name__=="__main__":
    if len(sys.argv)<=4:
        print("(source folder) (source begin) (target begin) (number of frames) (repeats/jumps)")
    else:
        if len(sys.argv)==5:
            range_source = [int(sys.argv[2])+i for i in range(int(sys.argv[4]))]
            range_target = [int(sys.argv[3])+i for i in range(int(sys.argv[4]))]
            move(sys.argv[1],range_source,range_target)
        else:
            # repeat each frame how many times?
            # how many jumps after a frame?
            repeats = int(sys.argv[5].split('/')[0])
            jumps = int(sys.argv[5].split('/')[1])
            range_source = [int(sys.argv[2])+(i//repeats)*jumps for i in range(int(sys.argv[4]))]
            range_target = [int(sys.argv[3])+i for i in range(int(sys.argv[4]))]
            print(range_source[:10])
            move(sys.argv[1],range_source,range_target)