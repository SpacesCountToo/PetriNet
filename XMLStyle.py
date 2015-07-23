## IMPORTS ##

from lxml import etree,html  # Need to process XML

## variables ##

html_text = \
    '''
<!DOCTYPE html>
<html>
    <head>
        <!--link rel='stylesheet' href='styles.css' /-->
    </head>
    <svg viewBox='0 0 1920 1080' height='100%%' width='100%%'>
        %s
    </svg>
</html>
    '''
svg_text = \
    ('<svg height = \'12.5%%\' width = \'12.5%%\' x = \'%s\' y = \'%s\'>\n'
     '    %s\n'
     '    %s\n'
     '</svg>\n')
#print svg_text
xml_file = 'test_net.xml'
tree = etree.parse(xml_file)
## Definitions ##
def attrScanner(parent,svg_format):
    ## WORKING ##
    """
    This scans the id attribute of each object in the XML recursively.
    This returns the list of XPaths to call each element.
    Might be helpful for generating shapes.
    Can use for extraction of x,y relative coordinates.
    """

    tf_scan = '%s/f | %s/t'
    max_length=len(tree.xpath(tf_scan % (parent,parent)))
    svg = ''
    for i in range(max_length):
        child_tag = tree.xpath(tf_scan % (parent,parent))[i].tag
        child_id = tree.xpath(tf_scan % (parent,parent))[i].get('id')
        x_id = tree.xpath(tf_scan % (parent,parent))[i].get('x')
        y_id = tree.xpath(tf_scan % (parent,parent))[i].get('y')
        new_parent = '%s/%s[@id=\'%s\']' % (parent,child_tag,child_id)
        #print shapeChoose(child_tag)
        #print x_id
        #print y_id
        #print new_parent
        #print svg_format % (x_id,y_id,shapeChoose(child_tag),attrScanner(new_parent,svg_format))
        svg += svg_format % (x_id,y_id,shapeChoose(child_tag),attrScanner(new_parent,svg_format))

    return svg

def xmlTemplate():
    pass

def shapeChoose(element):
    if element == 'f':
        svg_text = '<ellipse cx=\'50%\' cy=\'50%\' rx=\'49%\' ry=\'49%\' />'
    elif element == 't':
        svg_text = '<rect x=\'1%\' y=\'1%\' width=\'98%\' height=\'98%\' />'
    #elif element == 'w':
    #    drawWire(element)
    return svg_text

def drawWire(element):
    element

print attrScanner("/petrinet",svg_text)

#full_svg = pretty_svg.prettify()
print '########################################'
print unpretty_svg