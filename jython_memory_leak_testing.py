# @ File(label='Specify a directory containing the scripts', style='directory') scripts_dir
# @ Integer dummy_variable
#@ OpService ops

import sys
from ij import IJ

from java.lang import Runtime
sys.path.append(scripts_dir.getAbsolutePath()) 
import jython_memory_leak_testing_IMPORT_MODULE as jython_memory_leak_testing_IMPORT_MODULE
jython_memory_leak_testing_IMPORT_MODULE.ops = ops

print("#################################################################################\n		Starting testing memory leak.\n#################################################################################")

IJ.run("Collect Garbage", "")
initial_mem_usage = (Runtime.getRuntime().totalMemory() - Runtime.getRuntime().freeMemory()) / 1024 / 1024
used_mem_last = initial_mem_usage


for i in range(8):
    print("Testing iteration: %s" % i)
    IJ.run("Collect Garbage", "")
    print("Collected garbage")
    
    test_image_list = [IJ.createImage("BigTestingImage", "16-bit black", 512, 512, 100) for i in range(4)]
    test_image = IJ.createImage("BigTestingImage", "16-bit black", 512, 512, 100)

    used_mem = (Runtime.getRuntime().totalMemory() - Runtime.getRuntime().freeMemory()) / 1024 / 1024
    print("Used memory growth per iteration: %s Mb" % (used_mem - used_mem_last))
    print("Used memory growth total: %s Mb" % (used_mem - initial_mem_usage))
    used_mem_last = used_mem
    
    tmp_img = jython_memory_leak_testing_IMPORT_MODULE.memory_leak_test(test_image_list, test_image)
    
    for view in test_image_list:
        view = None # This does not change anything.
IJ.run("Collect Garbage", "")
print("Used memory growth total (after final GC): %s Mb" % ((Runtime.getRuntime().totalMemory() - Runtime.getRuntime().freeMemory()) / 1024 / 1024 - initial_mem_usage))