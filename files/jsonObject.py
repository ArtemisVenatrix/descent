import json

class JsonObject:
    def jsonify(self):
        toDump = {}
        for x in self.__dict__:
            if isinstance(self.__dict__[x], JsonObject):
                toDump[x] = self.__dict__[x].jsonify()
            elif isinstance(self.__dict__[x], list):
                print("list detected")
                toDump[x] = json.decode(self.jsonifyList(self.__dict__[x]))
            else:
                toDump[x] = self.__dict__[x]
        #print(toDump)
        return json.dumps(toDump)

    def jsonifyList(self, array):
        output = []
        for x in array:
            if isinstance(x, list):
                output.append(self.jsonifyList(x))
            elif isinstance(x, JsonObject):
                output.append(x.jsonify())
            else:
                output.append(x)
        return output

    def checkIfContains(self, array, target):
        if isinstance(array[0], list):
            return self.checkIfContains(array[0], target)
        elif isinstance(array[0], target):
            return True
        else:
            return False
