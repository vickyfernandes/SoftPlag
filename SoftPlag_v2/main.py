'''
Created on 25-Apr-2017

@author: Vicky Fernandes
@organization: Don Bosco Institute of Technology, Mumbai
'''

from SoftPlag.SourceCodePreprocessing import Preprocessor
import os
import sys # to get terminal arguments
import threading

# inputdir = "/home/mindcraft/Desktop/vicky/python/SoftPlag_v1/src/input/"
#inputdir = "C:\input/" # not being used
# outputdir = "/home/mindcraft/Desktop/vicky/python/SoftPlag_v1/src/output/"
#outputdir = "C:\output/" # not being used
#filelist = os.listdir(inputdir) # not being used

'''
Current working:
 - pass input dir and output dir as terminal arguments: python3 main.py <input_dir> <output_dir>
'''

if __name__ == '__main__':
    try:
        input_dir = sys.argv[1]
        output_dir = sys.argv[2]
    except IndexError:
        print("[ERROR] Missing parameters...")
        print(" :: python3 main.py <input_dir> <output_dir>")
        exit()

    # enumerate files
    os.chdir(input_dir)
    files = os.listdir()
    
    # create processing threads
    threads = {} # dict of <file>:<thread>
    for file in files:
        threads[file] = Preprocessor(file)
    
    # start threads
    for file in threads:
        threads[file].start()
    
    while True: # This block waits for all the threads to finish (i.e. "blocking")
        finished_thread_count = 0
        for file in threads:
            if threads[file].is_alive() == False:
                finished_thread_count += 1
        if finished_thread_count == len(threads):
            break
        else:
            finished_thread_count = 0

    # Display result ()
    results = {} # dictionary of <file>:<counter_object>
    for file_name in threads:
        results[file_name] = threads[file_name].get_word_count();

    print(results);

    '''for i in filelist:
        with open(os.path.join(inputdir + i), 'r') as f:
            fin = f.read()
            proc = Preprocessor()
            final_string = proc.scpp(fin)
            proc.word_counter(final_string)
            with open(os.path.join(outputdir + i + ".out"), 'w') as file_output:
                file_output = open(os.path.join(outputdir + i + ".out"), 'w')
                file_output.write(final_string)
'''