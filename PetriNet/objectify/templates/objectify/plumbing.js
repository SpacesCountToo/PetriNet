<script>
    jsPlumb.ready(function(){
        jsPlumb.setContainer("container");
        jsPlumb.importDefaults({
            Anchor:"Continuous",
            Connector: ["Flowchart", {cornerRadius: 5}],
            Overlays: [
                ["Arrow", {width:9, foldback:.7, location:.1}],
                ["Arrow", {width:9, foldback:.7, location:.5}],
                ["Arrow", {width:9, foldback:.7, location:.9}]],
            PaintStyle: { lineWidth:2, strokeStyle: "#800000" },
            MaxConnections:20,
        });

        {% for wire in wires %}
        jsPlumb.connect({
            source:"{{ wire.source.uuid_name }}",
            target:"{{ wire.destination.uuid_name }}"
        });
        {% endfor %}

        {% for node in nodes %}
        jsPlumb.makeTarget("{{ node.uuid_name }}",{
            {% if node.shape == "O" %}
            scope:"L",
            anchor:["Perimeter", {shape:"Ellipse"}],
            {% elif node.shape == "L" %}
            scope:"O",
            anchor:["Perimeter", {shape:"Rectangle"}],
            {% endif %}
        });
        jsPlumb.makeSource("{{ node.uuid_name }}",{
            {% if node.shape == "O" %}
            scope:"O",
            anchor:["Perimeter", {shape:"Ellipse"}],
            {% elif node.shape == "L" %}
            scope:"L",
            anchor:["Perimeter", {shape:"Rectangle"}],
            {% endif %}
        });
        jsPlumb.toggleSourceEnabled("{{ node.uuid_name }}");
        {% endfor %}
        if ($.cookie('connect-toggled') == 'connect-mode'){
            console.log($('#toggle_connect').html())
            $('#toggle_connect').html("/")
            {% for node in nodes %}
            jsPlumb.toggleSourceEnabled("{{ node.uuid_name }}");
            {% endfor %}
        }

        jsPlumb.on($('#toggle_connect'),'click',function(e){
        console.log($.cookie('connect-toggled'))
        if ($.cookie('connect-toggled') == 'connect-mode'){
            $(this).html("D");
            $.cookie('connect-toggled', 'drag-mode',{ expires:1 });
        }
        else if ($.cookie('connect-toggled') == 'drag-mode'){
            $(this).html("/");
            $.cookie('connect-toggled', 'connect-mode',{ expires:1 });
        }
        else if (!$.cookie('connect-toggled')){
            $(this).html("/");
            $.cookie('connect-toggled','connect-mode',{ expires:1 })
        }
            {% for node in nodes %}
            jsPlumb.toggleSourceEnabled("{{ node.uuid_name }}");
            {% endfor %}
            jsPlumbUtil.consume(e);
        });

        jsPlumb.repaintEverything();

    });
</script>