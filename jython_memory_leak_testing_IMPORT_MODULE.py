from ij import IJ

ops = None

def memory_leak_test(image_list, test_image=None):
    for i, view in enumerate(image_list):
        # pass
#       Options that I have tested:
        #########################################################################################################################################
        if i == 0: 
            print("Testing view_converted = ops.run('convert.float32', view) \n view = None \n views[i] = view_converted")
        view_converted = ops.run("convert.float32", view) # THIS DOES CAUSES THE MEMORY LEAK 
        view = None # This does not change anything.
        image_list[i] = view_converted
        #########################################################################################################################################
#        view_converted = ops.run("convert.float32", view) # THIS LINE CAUSES THE MEMORY LEAK 
        ##########################################################################################################################################
#        IJ.run(view, "32-bit", "")  # THIS LINE ALSO CAUSES THE MEMORY LEAK    
         ##########################################################################################################################################
#        view.show()
#        view.close()   # THIS DOES NOT CAUSE A MEMORY LEAK
         ##########################################################################################################################################
#        view_converted = ops.run("convert.float32", view)
#        view_converted = None  # THIS ALSO CAUSES THE LEAK
        ##########################################################################################################################################
#        print("Testing IJ.run(test_view, \"32-bit\", \"\")")
#        IJ.run(test_view, "32-bit", "") # THIS DOES NOT CAUSE THE LEAK!
        ##########################################################################################################################################
#        print("Testing view_converted = ops.run(\"convert.float32\", test_view)")
#        view_converted = ops.run("convert.float32", test_view) # THIS DOES CAUSE THE LEAK
        ##########################################################################################################################################
#        if i == 0:
#            print("Testing view_converted = ops.run(\"convert.float32\", test_view) with setting to None")
#        view_converted = ops.run("convert.float32", test_image) # THIS DOES CAUSE THE LEAK
#        view_converted = None
        ##########################################################################################################################################
#        if i == 0: 
#            print("Testing IJ.run(test_view, \"32-bit\", \"\") \n IJ.run(test_view, \"16-bit\", \"\")")
#        IJ.run(test_view, "32-bit", "") # THIS DOES NOT CAUSE THE LEAK!
#        IJ.run(test_view, "16-bit", "") 
        ##########################################################################################################################################
#        if i == 0: 
#            print("Testing test_view = IJ.createImage("BigTestingImage", "16-bit black", 512, 512, 100) \n IJ.run(test_view, \"32-bit\", \"\")")
#        test_view = IJ.createImage("BigTestingImage", "16-bit black", 512, 512, 100)
#        IJ.run(test_view, "32-bit", "") # THIS DOES NOT CAUSE THE LEAK!
##########################################################################################################################################

#    print("Testing out of the loop: test_views_list = [IJ.openImage(path) for path in test_views_paths]")
#    test_views_list = [IJ.openImage(path) for path in range(4)] # THIS DOES NOT CAUSE THE LEAK!

##########################################################################################################################################



    return None