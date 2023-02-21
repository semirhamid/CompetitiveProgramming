class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        dic = {}
        result = []
        for path in paths:
            files = path.split()
            directory = files[0]
            files = files[1:]
            for file in files:
                file_content = file[file.find("(") + 1:-1]
                file_path = directory + "/" + file[:file.find("(")]
                if file_content in dic:
                    dic[file_content] = dic[file_content] + " " + file_path
                else:
                    dic[file_content] = file_path
        for path in dic:
            splitted = dic[path].split()
            if len(splitted) >= 2:
                result.append(splitted)

        return result