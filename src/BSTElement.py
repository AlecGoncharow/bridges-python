from BinTreeElement import *
#
#  *  @brief The BSTElement class is the building block for creating binary search trees.
#  *
#  *	The BSTElement class is the building block for creating binary search tree structures.
#  *  It contains two children (viz., left, right), and a search key, to be used
#  *  in search operations .
#  *
#  *  BSTElement contains a visualizer (ElementVisualizer) object for setting visual
#  *  attributes (color, shape, opacity, size), necessary for displaying them in a
#  *  web browser.
#  *
#  *  BST Elements also have a LinkVisualizer object, that is used when they are linked to
#  *  another element, appropriate for setting link attributes, for instance, between
#  *  the current element and its left or right child
#  *
#  *	@param E he generic parameter object that is part of this element, representing
#  *      application specific data.
#  *	@param K is the search key parameter in the BST node; K must be orderable, such
#  *		as integer, float, string, etc., on which relational operators work.
#  *
#  *	@author Kalpathi Subramanian, Mihai Mehedint
#  *
#  *	@date 6/22/16, 1/7/17, 5/17/17
#  *
#  *	@brief This class extends the BinTreeElement class by adding a 'key' value
#  *	for use in a binary search tree implementations.
#  *
#  *	\sa Example tutorial using BSTElement at  <br>
#  *		http://bridgesuncc.github.io/Hello_World_Tutorials/BST.html
#  *
#
class BSTElement(BinTreeElement):
    key = object()

    # this is the BSTElement key
    #
    # 	 *
    # 	 * 	Construct an empty BSTElement with no key assigned and left and
    # 	 *	right pointers set to null.
    # 	 *
    #
    def __init__(self, key = None, e = None, left = None, right = None):
        if key is not None:
            self.set_key(key)
        if e is not None:
            super(BSTElement, self).__init__(key, e)
        if left is not None and right is not None:
            super(BSTElement, self).__init__(left, right)
        elif left is not None and right is None:
            super(BSTElement, self).__init__(left)
        elif right is not None and left is None:
            super(BSTElement, self).__init__(right)
        else:
            super(BSTElement, self).__init__()



    #
    # 	 *	This method gets the data structure type
    # 	 *
    # 	 *	@return  The date structure type as a string
    #
    def get_data_structure_type(self):
        return "BinarySearchTree"


    #
    # 	 *	Return the key of the BSTElement
    # 	 *
    # 	 * 	@return the key of this BSTElement
    # 	 *
    #
    def get_key(self):
        return self.key

    #
    # 	 *
    # 	 *	Set the key of the BSTElement to key
    # 	 * 	@param key the key to set
    #
    def set_key(self, key):
        self.key = key
        #  add this to the element's properties

    # 	 * @see edu.uncc.cs.bridgesV2.base.TreeElement#getLeft()
    #
    def get_left(self):
        return super(BSTElement, self).get_left()

    # 	 * @see edu.uncc.cs.bridgesV2.base.TreeElement#getRight()
    #
    def get_right(self):
        return super(BSTElement, self).get_right()

    #  (non-Javadoc)
    # 	 * @see edu.uncc.cs.bridgesV2.base.Element#getRepresentation()
    #
    #
    # 		@Override
    # 		public String getRepresentation() {
    # 			String locx = "0.0", locy = "0.0";
    # 			String json = "{";
    # 			for (Entry<String, String> entry : super.getVisualizer().properties.entrySet()) {
    # 				if (entry.getKey() == "locationX")
    # 					locx = entry.getValue();
    # 				else if (entry.getKey() == "locationY")
    # 					locy = entry.getValue();
    # 	            else
    # 					json += String.format("\"%s\": \"%s\", ", entry.getKey(),
    # 										entry.getValue());
    # 			}
    # 			json += String.format("\"location\": [ %s , %s ], ", locx, locy);
    # 			json += String.format("\"name\": \"%s\", ", super.getLabel());
    #  must check type
    # 			String s = ((Object) this.getKey()).__class__.__name__;
    # 			if ( (s == "java.lang.Integer") || (s == "java.lang.Long") )
    # 				json += String.format("\"key\": \"%d\"", this.getKey());
    # 			else if ( (s == "java.lang.Float") || (s == "java.lang.Double") )
    # 				json += String.format("\"key\": \"%f\"", this.getKey());
    # 			else if ( (s == "java.lang.String") )
    # 				json += String.format("\"key\": \"%s\"", this.getKey());
    # 			return json + "}";
    # 		}
    #
