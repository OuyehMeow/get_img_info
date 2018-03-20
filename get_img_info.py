import os, sys, time

rootdir = r'E:\Hexu Wang\OneDrive\Documents\2018 Spring Special Project\Feb-10-2018 Experiment\Photos'

def get_img_imfo(rootdir):

    old = '+'
    new = '_'

    for root, dirs, filenames in os.walk(rootdir):
        for filename in filenames:
            if old in filename:
                filename = os.path.join(root, filename)
                print (filename)
                os.rename(filename, filename.replace(old,new))
            statinfo = os.stat(filename)
            print str(filename), '\t%04d/%02d/%02d' % (time.localtime(statinfo[8])[0], time.localtime(statinfo[8])[1], time.localtime(statinfo[8])[2]), '\t%02d:%02d:%02d' % (time.localtime(statinfo[8])[3], time.localtime(statinfo[8])[4], time.localtime(statinfo[8])[5])

get_img_imfo(rootdir)
