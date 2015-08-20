<script>
    function saveUnitSubmit(){
        {% for node in nodes %}
        document.getElementById('{{ node.uuid_name }}-x_val').childNodes[1]['value'] =
            document.getElementById('{{ node.uuid_name }}').style.left.slice(0,-2);

        document.getElementById('{{ node.uuid_name }}-y_val').childNodes[1]['value'] =
            document.getElementById('{{ node.uuid_name }}').style.top.slice(0,-2);

        {% endfor %}
        return true;
    }
    jsPlumb.bind("connection", function(info,originalEvent) {
        if (originalEvent){
        $("#id_source").val(info.sourceId);
        $("#id_destination").val(info.targetId);
        $("#save_conn_form").submit()
        }
    });

</script>