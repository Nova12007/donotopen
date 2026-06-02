import json
from tools import get_time, calculator


def run_tool(tool_json):

    data = json.loads(tool_json)

    tool = data.get("tool")
    args = data.get("args", {})

    if tool == "get_time":
        return get_time()

    elif tool == "calculator":
        return calculator(
            args.get("expression")
        )

    return None