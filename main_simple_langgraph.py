from langgraph.graph import Graph
# simple graph

def function_1():
    pass

def function_2():
    pass

workflow = Graph()

workflow.add_node("node1", function_1)
workflow.add_node("node2", function_1)

workflow.add_edge("node1", "node2")

workflow.set_entry_point("node1")
workflow.set_finish_point("node2")


app = workflow.compile()


app.invoke("hello world")