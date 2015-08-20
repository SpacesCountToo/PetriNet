function descendTree(node){
    node.css('visibility', 'hidden');
    jsPlumb.setTargetEnabled(node, false);
    jsPlumb.hide(node, true);
    $.cookie(node.attr('id') + "-hidden", true)
    node.children().children().show();
    node.children().children().css('visibility', 'visible');
    node.children().children().css('height', '100%');
    node.children().children().css('width', '100%');
    jsPlumb.show($(node).children($('div div')), 'hide');
    jsPlumb.repaintEverything();
}