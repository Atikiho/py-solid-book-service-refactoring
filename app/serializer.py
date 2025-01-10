import json
import xml.etree.ElementTree as ET
from abc import abstractmethod, ABC


class Serializer(ABC):
    def __init__(self, book):
        self.book = book

    @abstractmethod
    def serialize(self):
        pass


class JsonSerializer(Serializer):
    def serialize(self) -> str:
        return json.dumps({"title": self.book.title, "content": self.book.content})


class XmlSerializer(Serializer):
    def serialize(self):
        root = ET.Element("book")
        title = ET.SubElement(root, "title")
        title.text = self.book.title
        content = ET.SubElement(root, "content")
        content.text = self.book.content
        return ET.tostring(root, encoding="unicode")
