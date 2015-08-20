<script>
    $(document).ready(function(){
    {% for node in nodes %}{% if node.children.all %}
        {% for child in node.children.all %}
        $("#{{ child.uuid_name }}").hide();
        jsPlumb.hide("{{ child.uuid_name }}", true);
        {% endfor %}
        $("#{{ node.uuid_name }}").dblclick(function(e){
            e.stopPropagation();
            $("#{{ node.uuid_name }}").css('visibility', 'hidden');
            jsPlumb.setTargetEnabled("{{ node.uuid_name }}", false);
            jsPlumb.hide("{{ node.uuid_name }}", true);
        {% for child in node.children.all %}
            $("#{{ child.uuid_name }}").show();
            $("#{{ child.uuid_name }}").css('visibility', 'visible');
            $("#{{ child.uuid_name }}").css('height', '100%');
            $("#{{ child.uuid_name }}").css('width', '100%');
            jsPlumb.show("{{ child.uuid_name }}", 'hide');
            jsPlumb.repaintEverything();
        {% endfor %}
        });
    {% endif %}{% endfor %}
    });
</script>