interact('.draggable')
.draggable({
    inertia: true,
    restrict: {
        endOnly: true,
        elementRect: { top:0, left:0, bottom:1, right:1 },
        restriction:"#container",
    },
    onmove: dragMoveListener,
});
function dragMoveListener (event) {
jsPlumb.repaintEverything();
var target = event.target,
    // keep the dragged position in the data-x/data-y attributes
    x = (parseFloat(target.getAttribute('data-x')) || 0) + event.dx,
    y = (parseFloat(target.getAttribute('data-y')) || 0) + event.dy;


// translate the element
target.style.left = x + 'px';
target.style.top = y + 'px';
// update the position attributes
target.setAttribute('data-x', x);
target.setAttribute('data-y', y);
}
// this is used later in the resizing demo
window.dragMoveListener = dragMoveListener;