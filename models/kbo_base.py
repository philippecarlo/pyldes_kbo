from typing import List

class KboBase:

    def to_dict(self):
        result = {}
        for key in self.__dict__:
            item = self.__dict__[key]
            if isinstance(item,  List):
                mapped_list = []
                for list_item in item:
                    if issubclass(type(list_item), KboBase):
                        mapped_list.append(list_item.to_dict())
                    else:
                        mapped_list.append(list_item)
                result[key] = mapped_list
            elif issubclass(type(item), KboBase):
                result[key] = item.to_dict()
            else:
                result[key] = item
        return result
