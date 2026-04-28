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


