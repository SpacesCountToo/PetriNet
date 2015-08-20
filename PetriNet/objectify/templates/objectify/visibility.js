<script>
    $(document).ready(function(){
    {% for node in nodes %}{% if node.children.all %}
        $("#{{ node.uuid_name }}").children().children().hide();
        jsPlumb.hide($("#{{ node.uuid_name }}").children().children(), true);
        $("#{{ node.uuid_name }}").dblclick(function(e){
            e.stopPropagation();
            descendTree($(this));
        });
    {% endif %}{% endfor %}

    });
</script>