class HTMLNode():

    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        result = ""
        if self.props is not None:
            for prop in self.props:
                result += f'{prop}="{self.props[prop]}", '
        return result
    
    def __repr__(self):
        report = f"HTMLNode({self.tag}, {self.value}"
        if self.children is not None:
            report += ", children=["
            for child in self.children:
                report += child.value + ", "
            report += "]"
        if self.props is not None:
            report += f", props=[{self.props_to_html()}]"
        report += ")"
        return report
    
class LeafNode(HTMLNode):

    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("All leaf nodes must have a value")
        if self.tag is None:
            return self.value
        return (
            "<" + self.tag + ">" +
            self.value +
            "</" + self.tag + ">" 
        )
    
    def __repr__(self):
        report = f"LeafNode({self.tag}, {self.value}"
        if self.props is not None:
            report += f", props=[{self.props_to_html()}]"
        report += ")"
        return report




