class Randomiser(object):
    """Builds random levels with pre-made stages"""
    # This fella will do stages_list.pop(random_index) a few times and that's our level

    # Suppose we'll have stages with IDs. Like 1, 2, ... , 99. Here we get a dilemma: 
    # Option A: separate text files for every stage should have the ID in their filename. 
    #           If so, every time we need to load a stage, we read a text file. 
    #           No large data to carry around but needs loading every now and then. 
    # Option B: a major textfile with all stages will have IDs as separators. 
    #           If so, all stages will have to be read from file before the game starts 
    #           and kept in a dict or sth... 
    #           Lots of stuff to carry around, might longer for the game to load. 
    
    # Either way We should provide some classification: 
    #   some stages are suitable for lower levels, others for higher levels.
    #   Using single text file would be less flexible for this since separate text files can be
    #   placed into separate folders like "Level 1-3", "Level 6-7" etc.  

    # Some 



   